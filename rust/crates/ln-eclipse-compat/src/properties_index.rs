use std::collections::{BTreeMap, HashMap};
use std::fs::File;
use std::io::{self, Cursor, Read, Write};
use std::path::Path;
use byteorder::{BigEndian, ReadBytesExt, WriteBytesExt};
use serde::{Deserialize, Serialize};
use thiserror::Error;

pub const VERSION: u8 = 1;
pub const TAG_INDEX: u8 = 1;
pub const TAG_QNAME: u8 = 2;

#[derive(Error, Debug)]
pub enum PropertyBucketError {
    #[error(transparent)]
    Io(#[from] io::Error),
    #[error("Unsupported PropertyBucket version: {0}, expected 1")]
    UnsupportedVersion(u8),
    #[error("Malformed PropertyBucket stream: {0}")]
    MalformedStream(String),
}

/// In-memory representation of an Eclipse PropertyBucket (`properties.index`).
/// Maintains properties per resource path (e.g. `""` for the project root).
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct PropertyBucket {
    pub version: u8,
    /// resource_path -> (qualifier, local_name) -> value
    pub entries: BTreeMap<String, BTreeMap<(String, String), String>>,
}

impl Default for PropertyBucket {
    fn default() -> Self {
        Self::new()
    }
}

impl PropertyBucket {
    pub fn new() -> Self {
        Self {
            version: VERSION,
            entries: BTreeMap::new(),
        }
    }

    pub fn load_from_path(path: &Path) -> Result<Self, PropertyBucketError> {
        if !path.exists() {
            return Ok(Self::new());
        }
        let mut file = File::open(path)?;
        let mut buf = Vec::new();
        file.read_to_end(&mut buf)?;
        Self::deserialize(&buf)
    }

    pub fn save_to_path(&self, path: &Path) -> Result<(), PropertyBucketError> {
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent)?;
        }
        let bytes = self.serialize()?;
        std::fs::write(path, bytes)?;
        Ok(())
    }

    pub fn get_property(&self, local_name: &str, qualifier: &str, resource_path: &str) -> Option<&str> {
        let res_map = self.entries.get(resource_path)?;
        res_map.get(&(qualifier.to_string(), local_name.to_string())).map(|s| s.as_str())
    }

    pub fn set_property(&mut self, local_name: &str, value: &str, qualifier: &str, resource_path: &str) {
        let res_map = self.entries.entry(resource_path.to_string()).or_default();
        res_map.insert((qualifier.to_string(), local_name.to_string()), value.to_string());
    }

    pub fn delete_property(&mut self, local_name: &str, qualifier: &str, resource_path: &str) -> bool {
        if let Some(res_map) = self.entries.get_mut(resource_path) {
            let removed = res_map.remove(&(qualifier.to_string(), local_name.to_string())).is_some();
            if res_map.is_empty() {
                self.entries.remove(resource_path);
            }
            removed
        } else {
            false
        }
    }

    pub fn get_properties_for_resource(&self, resource_path: &str) -> BTreeMap<(String, String), String> {
        self.entries.get(resource_path).cloned().unwrap_or_default()
    }

    /// Serializes to the exact Eclipse PropertyBucket binary format v1.
    pub fn serialize(&self) -> Result<Vec<u8>, PropertyBucketError> {
        let mut w = Cursor::new(Vec::new());

        // Header: byte version
        w.write_u8(self.version)?;

        // int entryCount (number of resource paths)
        w.write_u32::<BigEndian>(self.entries.len() as u32)?;

        let mut qualifier_indices: HashMap<String, i32> = HashMap::new();
        let mut next_qualifier_idx: i32 = 0;

        for (res_path, props) in &self.entries {
            // UTF resource_path ("" for project root)
            write_utf(&mut w, res_path)?;

            // unsignedShort propCount
            w.write_u16::<BigEndian>(props.len() as u16)?;

            for ((qualifier, local_name), value) in props {
                if let Some(&idx) = qualifier_indices.get(qualifier) {
                    // Tag: 1 (TAG_INDEX) + int index
                    w.write_u8(TAG_INDEX)?;
                    w.write_i32::<BigEndian>(idx)?;
                } else {
                    // Tag: 2 (TAG_QNAME) + UTF qualifier
                    w.write_u8(TAG_QNAME)?;
                    write_utf(&mut w, qualifier)?;
                    qualifier_indices.insert(qualifier.clone(), next_qualifier_idx);
                    next_qualifier_idx += 1;
                }

                // UTF localName + UTF value
                write_utf(&mut w, local_name)?;
                write_utf(&mut w, value)?;
            }
        }

        Ok(w.into_inner())
    }

    /// Deserializes from the exact Eclipse PropertyBucket binary format v1.
    pub fn deserialize(bytes: &[u8]) -> Result<Self, PropertyBucketError> {
        let mut r = Cursor::new(bytes);
        if bytes.is_empty() {
            return Ok(Self::new());
        }

        let version = r.read_u8()?;
        if version != VERSION {
            return Err(PropertyBucketError::UnsupportedVersion(version));
        }

        let entry_count = r.read_u32::<BigEndian>()? as usize;
        let mut bucket = Self::new();
        bucket.version = version;

        let mut qualifiers_table: Vec<String> = Vec::new();

        for _ in 0..entry_count {
            let res_path = read_utf(&mut r)?;
            let prop_count = r.read_u16::<BigEndian>()? as usize;

            for _ in 0..prop_count {
                let tag = r.read_u8()?;
                let qualifier = match tag {
                    TAG_QNAME => {
                        let q = read_utf(&mut r)?;
                        qualifiers_table.push(q.clone());
                        q
                    }
                    TAG_INDEX => {
                        let idx = r.read_i32::<BigEndian>()? as usize;
                        qualifiers_table.get(idx).cloned().ok_or_else(|| {
                            PropertyBucketError::MalformedStream(format!(
                                "Qualifier index {idx} out of bounds (len: {})",
                                qualifiers_table.len()
                            ))
                        })?
                    }
                    other => {
                        return Err(PropertyBucketError::MalformedStream(format!(
                            "Invalid property qualifier tag: {other}"
                        )));
                    }
                };

                let local_name = read_utf(&mut r)?;
                let value = read_utf(&mut r)?;

                bucket.set_property(&local_name, &value, &qualifier, &res_path);
            }
        }

        Ok(bucket)
    }
}

fn write_utf<W: Write>(w: &mut W, s: &str) -> io::Result<()> {
    let bytes = s.as_bytes();
    if bytes.len() > 65535 {
        return Err(io::Error::new(io::ErrorKind::InvalidInput, "String exceeds 65535 bytes"));
    }
    w.write_u16::<BigEndian>(bytes.len() as u16)?;
    w.write_all(bytes)?;
    Ok(())
}

fn read_utf<R: Read>(r: &mut R) -> io::Result<String> {
    let len = r.read_u16::<BigEndian>()? as usize;
    let mut buf = vec![0u8; len];
    r.read_exact(&mut buf)?;
    String::from_utf8(buf).map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))
}

/// ProjectProperties helper (qualifier="") with all standard LN Studio keys.
#[derive(Debug, Clone, Default)]
pub struct ProjectProperties {
    pub application_release: Option<String>,
    pub customer: Option<String>,
    pub description: Option<String>,
    pub environment: Option<String>,
    pub label: Option<String>,
    pub label_uuid: Option<String>,
    pub language: Option<String>,
    pub package: Option<String>,
    pub package_combination: Option<String>,
    pub package_vrc: Option<String>,
    pub project_server: Option<String>,
    pub server_user: Option<String>,
    pub solution: Option<String>,
    pub task_version_id: Option<String>,
    pub use_proxy: Option<String>,
    pub user: Option<String>,
    pub version: Option<String>,
    pub vrc: Option<String>,
    pub workspace_root: Option<String>,
}

impl ProjectProperties {
    pub fn from_bucket(bucket: &PropertyBucket, resource_path: &str) -> Self {
        let get = |k: &str| bucket.get_property(k, "", resource_path).map(|s| s.to_string());
        Self {
            application_release: get("ApplicationRelease"),
            customer: get("Customer"),
            description: get("Description"),
            environment: get("Environment"),
            label: get("Label"),
            label_uuid: get("labelUUID"),
            language: get("Language"),
            package: get("Package"),
            package_combination: get("PackageCombination"),
            package_vrc: get("PackageVRC"),
            project_server: get("ProjectServer"),
            server_user: get("ServerUser"),
            solution: get("Solution"),
            task_version_id: get("TaskVersionID"),
            use_proxy: get("UseProxy"),
            user: get("User"),
            version: get("Version"),
            vrc: get("VRC"),
            workspace_root: get("workspace_root"),
        }
    }

    pub fn apply_to_bucket(&self, bucket: &mut PropertyBucket, resource_path: &str) {
        let mut set = |k: &str, opt: &Option<String>| {
            if let Some(v) = opt {
                bucket.set_property(k, v, "", resource_path);
            }
        };
        set("ApplicationRelease", &self.application_release);
        set("Customer", &self.customer);
        set("Description", &self.description);
        set("Environment", &self.environment);
        set("Label", &self.label);
        set("labelUUID", &self.label_uuid);
        set("Language", &self.language);
        set("Package", &self.package);
        set("PackageCombination", &self.package_combination);
        set("PackageVRC", &self.package_vrc);
        set("ProjectServer", &self.project_server);
        set("ServerUser", &self.server_user);
        set("Solution", &self.solution);
        set("TaskVersionID", &self.task_version_id);
        set("UseProxy", &self.use_proxy);
        set("User", &self.user);
        set("Version", &self.version);
        set("VRC", &self.vrc);
        set("workspace_root", &self.workspace_root);
    }
}

/// StudioProjectSettings helper (qualifier="IStudio_Core")
#[derive(Debug, Clone, Default)]
pub struct StudioProjectSettings {
    pub generate_component_source_files: Option<bool>,
    pub generate_form_source_files: Option<bool>,
    pub generate_menu_source_files: Option<bool>,
    pub generate_report_source_files: Option<bool>,
}

impl StudioProjectSettings {
    pub const QUALIFIER: &'static str = "IStudio_Core";

    pub fn from_bucket(bucket: &PropertyBucket, resource_path: &str) -> Self {
        let get_bool = |k: &str| {
            bucket.get_property(k, Self::QUALIFIER, resource_path)
                .map(|s| s.eq_ignore_ascii_case("true"))
        };
        Self {
            generate_component_source_files: get_bool("generateComponentSourceFiles"),
            generate_form_source_files: get_bool("generateFormSourceFiles"),
            generate_menu_source_files: get_bool("generateMenuSourceFiles"),
            generate_report_source_files: get_bool("generateReportSourceFiles"),
        }
    }

    pub fn apply_to_bucket(&self, bucket: &mut PropertyBucket, resource_path: &str) {
        let mut set_bool = |k: &str, opt: Option<bool>| {
            if let Some(b) = opt {
                bucket.set_property(k, if b { "true" } else { "false" }, Self::QUALIFIER, resource_path);
            }
        };
        set_bool("generateComponentSourceFiles", self.generate_component_source_files);
        set_bool("generateFormSourceFiles", self.generate_form_source_files);
        set_bool("generateMenuSourceFiles", self.generate_menu_source_files);
        set_bool("generateReportSourceFiles", self.generate_report_source_files);
    }
}
