use std::collections::BTreeMap;
use std::fs::File;
use std::io::{self, Cursor, Read, Write};
use std::path::Path;
use byteorder::{BigEndian, ReadBytesExt, WriteBytesExt};
use serde::{Deserialize, Serialize};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AdminError {
    #[error(transparent)]
    Io(#[from] io::Error),
    #[error("Invalid stream magic: {0:#06x}, expected 0xACED")]
    InvalidMagic(u16),
    #[error("Invalid stream version: {0:#06x}, expected 0x0005")]
    InvalidVersion(u16),
    #[error("Malformed Java serialization stream: {0}")]
    MalformedStream(String),
}

/// 12 Managed LN Studio Component Extensions (plus aliases .que and .fun)
pub const MANAGED_EXTENSIONS: &[&str] = &[
    ".tbl", ".ses", ".lib", ".dmn", ".lbl", ".mnu",
    ".rpt", ".msg", ".qst", ".que", ".add", ".fnc",
    ".fun", ".bus", ".cha",
];

/// Standalone script extensions that must NEVER be stored in .admin
pub const EXCLUDED_EXTENSIONS: &[&str] = &[
    ".src", ".4gl", ".dal", ".clnsrc", ".rptdsrc",
];

/// Single AdministrationComponent entry corresponding to
/// com.infor.ln.studio.common.core.cm.administration.AdministrationComponent (serialVersionUID = 2L).
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct AdministrationComponent {
    pub is_checked_out: bool,
    pub is_created: bool,
    pub is_ever_checked_in: bool,
    pub is_expired: bool,
    pub is_dirty: bool,
    pub is_vsc_happy: bool,
    pub path: String,
}

impl AdministrationComponent {
    pub fn new(path: impl Into<String>) -> Self {
        Self {
            is_checked_out: false,
            is_created: false,
            is_ever_checked_in: false,
            is_expired: false,
            is_dirty: false,
            is_vsc_happy: true,
            path: normalize_admin_path(&path.into()),
        }
    }
}

/// Normalizes relative paths to project-relative paths without leading slash or :<activity>/ prefix.
pub fn normalize_admin_path(path: &str) -> String {
    let mut p = path.replace('\\', "/").trim().to_string();
    while p.starts_with('/') {
        p.remove(0);
    }
    if p.starts_with(':') {
        if let Some(slash_idx) = p.find('/') {
            p = p[slash_idx + 1..].to_string();
        } else {
            p.remove(0);
        }
    }
    while p.starts_with('/') {
        p.remove(0);
    }
    p
}

/// Checks if an extension is managed by .admin
pub fn is_managed_extension(ext_or_path: &str) -> bool {
    let lower = ext_or_path.to_ascii_lowercase();
    MANAGED_EXTENSIONS.iter().any(|ext| lower.ends_with(ext))
}

/// Checks if an extension is an excluded standalone script file
pub fn is_excluded_extension(ext_or_path: &str) -> bool {
    let lower = ext_or_path.to_ascii_lowercase();
    EXCLUDED_EXTENSIONS.iter().any(|ext| lower.ends_with(ext))
}

/// In-memory representation of an Eclipse Activity .admin file.
#[derive(Debug, Default, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct AdminFile {
    /// Normalized project-relative path -> AdministrationComponent
    pub entries: BTreeMap<String, AdministrationComponent>,
}

impl AdminFile {
    pub fn new() -> Self {
        Self {
            entries: BTreeMap::new(),
        }
    }

    pub fn load_from_path(path: &Path) -> Result<Self, AdminError> {
        if !path.exists() {
            return Ok(Self::new());
        }
        let mut file = File::open(path)?;
        let mut buf = Vec::new();
        file.read_to_end(&mut buf)?;
        Self::deserialize(&buf)
    }

    pub fn save_to_path(&self, path: &Path) -> Result<(), AdminError> {
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent)?;
        }
        let bytes = self.serialize()?;
        std::fs::write(path, bytes)?;
        Ok(())
    }

    pub fn get(&self, path: &str) -> Option<&AdministrationComponent> {
        let norm = normalize_admin_path(path);
        self.entries.get(&norm)
    }

    pub fn get_mut(&mut self, path: &str) -> Option<&mut AdministrationComponent> {
        let norm = normalize_admin_path(path);
        self.entries.get_mut(&norm)
    }

    /// Helper to add or update an entry with path normalization
    pub fn insert(&mut self, comp: AdministrationComponent) {
        let norm = normalize_admin_path(&comp.path);
        if is_excluded_extension(&norm) {
            return;
        }
        self.entries.insert(norm.clone(), AdministrationComponent {
            path: norm,
            ..comp
        });
    }

    pub fn remove(&mut self, path: &str) -> Option<AdministrationComponent> {
        let norm = normalize_admin_path(path);
        self.entries.remove(&norm)
    }

    /// CMStudio state transition: after_get
    /// isCreated=false, isCheckedout=false, isEvercheckedIn=false, isExpired=false, m_isDirty=false, m_isVSCHappy=true
    pub fn after_get(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if is_excluded_extension(&norm) {
            return;
        }
        let comp = self.entries.entry(norm.clone()).or_insert_with(|| AdministrationComponent::new(&norm));
        comp.path = norm;
        comp.is_created = false;
        comp.is_checked_out = false;
        comp.is_ever_checked_in = false;
        comp.is_expired = false;
        comp.is_dirty = false;
        comp.is_vsc_happy = true;
    }

    /// CMStudio state transition: after_create
    /// isCreated=true, isCheckedout=true, isEvercheckedIn=false, isExpired=false, m_isDirty=true, m_isVSCHappy=false
    pub fn after_create(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if is_excluded_extension(&norm) {
            return;
        }
        let comp = self.entries.entry(norm.clone()).or_insert_with(|| AdministrationComponent::new(&norm));
        comp.path = norm;
        comp.is_created = true;
        comp.is_checked_out = true;
        comp.is_ever_checked_in = false;
        comp.is_expired = false;
        comp.is_dirty = true;
        comp.is_vsc_happy = false;
    }

    /// CMStudio state transition: after_checkout
    /// isCreated=false, isCheckedout=true, isEvercheckedIn=false, isExpired=false, m_isDirty=false, m_isVSCHappy=true
    pub fn after_checkout(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if is_excluded_extension(&norm) {
            return;
        }
        let comp = self.entries.entry(norm.clone()).or_insert_with(|| AdministrationComponent::new(&norm));
        comp.path = norm;
        comp.is_created = false;
        comp.is_checked_out = true;
        comp.is_ever_checked_in = false;
        comp.is_expired = false;
        comp.is_dirty = false;
        comp.is_vsc_happy = true;
    }

    /// CMStudio state transition: after_put
    /// isCheckedout=true, m_isDirty=false (retaining isCreated, isEvercheckedIn, isExpired, m_isVSCHappy)
    pub fn after_put(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if is_excluded_extension(&norm) {
            return;
        }
        let comp = self.entries.entry(norm.clone()).or_insert_with(|| AdministrationComponent::new(&norm));
        comp.path = norm;
        comp.is_checked_out = true;
        comp.is_dirty = false;
    }

    /// CMStudio state transition: after_checkin
    /// isCreated=false, isCheckedout=false, isEvercheckedIn=true, isExpired=false, m_isDirty=false, m_isVSCHappy=true
    pub fn after_checkin(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if is_excluded_extension(&norm) {
            return;
        }
        let comp = self.entries.entry(norm.clone()).or_insert_with(|| AdministrationComponent::new(&norm));
        comp.path = norm;
        comp.is_created = false;
        comp.is_checked_out = false;
        comp.is_ever_checked_in = true;
        comp.is_expired = false;
        comp.is_dirty = false;
        comp.is_vsc_happy = true;
    }

    /// CMStudio state transition: after_uncheckout
    /// if isCreated && !isEvercheckedIn, remove entry from .admin;
    /// otherwise set isCreated=false, isCheckedout=false, m_isDirty=false, m_isVSCHappy=true.
    pub fn after_uncheckout(&mut self, path: &str) {
        let norm = normalize_admin_path(path);
        if let Some(comp) = self.entries.get(&norm) {
            if comp.is_created && !comp.is_ever_checked_in {
                self.entries.remove(&norm);
                return;
            }
        }
        if let Some(comp) = self.entries.get_mut(&norm) {
            comp.is_created = false;
            comp.is_checked_out = false;
            comp.is_dirty = false;
            comp.is_vsc_happy = true;
        }
    }

    /// Sets m_isVSCHappy flag
    pub fn set_vsc_happy(&mut self, path: &str, happy: bool) {
        let norm = normalize_admin_path(path);
        if let Some(comp) = self.entries.get_mut(&norm) {
            comp.is_vsc_happy = happy;
        }
    }

    /// Repairs an existing .admin file by pruning standalone script files (.src, .4gl, etc.)
    /// and ensuring all keys and m_path values are properly normalized.
    pub fn repair(&mut self) -> usize {
        let mut pruned = 0;
        let mut new_entries = BTreeMap::new();
        for (k, mut v) in std::mem::take(&mut self.entries) {
            let norm_k = normalize_admin_path(&k);
            if is_excluded_extension(&norm_k) {
                pruned += 1;
                continue;
            }
            v.path = normalize_admin_path(&v.path);
            new_entries.insert(norm_k, v);
        }
        self.entries = new_entries;
        pruned
    }

    /// Serializes the AdminFile into byte-exact Java Object Serialization (0xACED0005) format.
    pub fn serialize(&self) -> Result<Vec<u8>, AdminError> {
        let mut w = Cursor::new(Vec::new());

        // Header: STREAM_MAGIC (0xACED), STREAM_VERSION (0x0005)
        w.write_u16::<BigEndian>(0xACED)?;
        w.write_u16::<BigEndian>(0x0005)?;

        // TC_OBJECT (0x73): java.util.HashMap
        w.write_u8(0x73)?;

        // TC_CLASSDESC (0x72) -> Handle 0x007E0000: java.util.HashMap class descriptor
        w.write_u8(0x72)?;
        write_utf(&mut w, "java.util.HashMap")?;
        w.write_i64::<BigEndian>(362498820763181265_i64)?; // serialVersionUID = 0x0507DAC1C31660D1
        w.write_u8(0x03)?; // flags = SC_WRITE_METHOD | SC_SERIALIZABLE
        w.write_u16::<BigEndian>(2)?; // numFields = 2
        // Field 1: 'F', "loadFactor"
        w.write_u8(b'F')?;
        write_utf(&mut w, "loadFactor")?;
        // Field 2: 'I', "threshold"
        w.write_u8(b'I')?;
        write_utf(&mut w, "threshold")?;
        w.write_u8(0x78)?; // TC_ENDBLOCKDATA
        w.write_u8(0x70)?; // TC_NULL (super classdesc)
        // Object(HashMap) -> Handle 0x007E0001

        // HashMap values:
        // loadFactor = 0.75f (0x3F400000)
        w.write_u32::<BigEndian>(0x3F400000)?;

        let count = self.entries.len();
        // buckets: next power of 2 >= 16
        let mut buckets: u32 = 16;
        while (buckets as usize) < count * 2 {
            buckets *= 2;
        }
        let threshold = (buckets as f32 * 0.75) as i32;
        w.write_i32::<BigEndian>(threshold)?;

        // Block data containing buckets and size:
        w.write_u8(0x77)?; // TC_BLOCKDATA
        w.write_u8(0x08)?; // length = 8
        w.write_u32::<BigEndian>(buckets)?;
        w.write_u32::<BigEndian>(count as u32)?;

        let mut class_desc_written = false;
        let mut class_desc_handle: u32 = 0x007E0003;

        // Current next handle counter per JVM ObjectOutputStream rules:
        // 0x007E0000: ClassDesc(HashMap)
        // 0x007E0001: Object(HashMap)
        let mut next_handle: u32 = 0x007E0002;

        for (key, comp) in &self.entries {
            // Key string: TC_STRING
            w.write_u8(0x74)?;
            write_utf(&mut w, key)?;
            let key_handle = next_handle;
            next_handle += 1;

            // Value: TC_OBJECT
            w.write_u8(0x73)?;

            if !class_desc_written {
                // First occurrence: TC_CLASSDESC
                w.write_u8(0x72)?;
                write_utf(&mut w, "com.infor.ln.studio.common.core.cm.administration.AdministrationComponent")?;
                w.write_i64::<BigEndian>(2_i64)?; // serialVersionUID = 2L
                w.write_u8(0x02)?; // flags = SC_SERIALIZABLE
                w.write_u16::<BigEndian>(7)?; // numFields = 7

                // Per JVM ObjectOutputStream spec, ClassDesc gets its handle BEFORE field descriptors
                class_desc_handle = next_handle; // 0x007E0003 for entry 0
                next_handle += 1;

                // 7 fields in exact JVM canonical order:
                // 1. 'Z' "isCheckedout"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "isCheckedout")?;
                // 2. 'Z' "isCreated"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "isCreated")?;
                // 3. 'Z' "isEvercheckedIn"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "isEvercheckedIn")?;
                // 4. 'Z' "isExpired"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "isExpired")?;
                // 5. 'Z' "m_isDirty"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "m_isDirty")?;
                // 6. 'Z' "m_isVSCHappy"
                w.write_u8(b'Z')?;
                write_utf(&mut w, "m_isVSCHappy")?;
                // 7. 'L' "m_path" -> TC_STRING "Ljava/lang/String;"
                w.write_u8(b'L')?;
                write_utf(&mut w, "m_path")?;
                w.write_u8(0x74)?; // TC_STRING
                write_utf(&mut w, "Ljava/lang/String;")?;
                next_handle += 1; // 0x007E0004: String("Ljava/lang/String;")

                w.write_u8(0x78)?; // TC_ENDBLOCKDATA
                w.write_u8(0x70)?; // TC_NULL (super classdesc)

                class_desc_written = true;
            } else {
                // Subsequent occurrences: TC_REFERENCE to class descriptor
                w.write_u8(0x71)?;
                w.write_u32::<BigEndian>(class_desc_handle)?;
            }

            // Object(AdministrationComponent) gets its handle AFTER classDesc and BEFORE classdata[]
            next_handle += 1; // 0x007E0005 for entry 0

            // Field values in order:
            w.write_u8(if comp.is_checked_out { 1 } else { 0 })?;
            w.write_u8(if comp.is_created { 1 } else { 0 })?;
            w.write_u8(if comp.is_ever_checked_in { 1 } else { 0 })?;
            w.write_u8(if comp.is_expired { 1 } else { 0 })?;
            w.write_u8(if comp.is_dirty { 1 } else { 0 })?;
            w.write_u8(if comp.is_vsc_happy { 1 } else { 0 })?;

            // m_path: TC_REFERENCE to key_handle when equal, else distinct TC_STRING
            if comp.path == *key {
                w.write_u8(0x71)?; // TC_REFERENCE
                w.write_u32::<BigEndian>(key_handle)?;
            } else {
                w.write_u8(0x74)?; // TC_STRING
                write_utf(&mut w, &comp.path)?;
                next_handle += 1;
            }
        }

        // Terminating TC_ENDBLOCKDATA
        w.write_u8(0x78)?;

        Ok(w.into_inner())
    }

    /// Deserializes an AdminFile from arbitrary valid Java serialization stream.
    pub fn deserialize(bytes: &[u8]) -> Result<Self, AdminError> {
        let mut r = Cursor::new(bytes);
        if bytes.len() < 4 {
            return Err(AdminError::MalformedStream("Stream too short for header".into()));
        }
        let magic = r.read_u16::<BigEndian>()?;
        if magic != 0xACED {
            return Err(AdminError::InvalidMagic(magic));
        }
        let version = r.read_u16::<BigEndian>()?;
        if version != 0x0005 {
            return Err(AdminError::InvalidVersion(version));
        }

        let mut parser = JavaStreamParser::new(r);
        parser.parse_admin()
    }
}

fn write_utf<W: Write>(w: &mut W, s: &str) -> io::Result<()> {
    let bytes = s.as_bytes();
    if bytes.len() > 65535 {
        return Err(io::Error::new(io::ErrorKind::InvalidInput, "String too long for UTF"));
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

/// Java Serialization stream parser supporting HashMap<String, AdministrationComponent>
struct JavaStreamParser<'a> {
    r: Cursor<&'a [u8]>,
    handles: Vec<HandleValue>,
}

#[derive(Clone, Debug)]
enum HandleValue {
    Object,
    ClassDesc(ClassDescriptor),
    StringVal(String),
}

#[derive(Clone, Debug)]
struct ClassDescriptor {
    name: String,
    fields: Vec<FieldDesc>,
}

#[derive(Clone, Debug)]
#[allow(dead_code)]
struct FieldDesc {
    type_code: u8,
    name: String,
    class_name: Option<String>,
}

impl<'a> JavaStreamParser<'a> {
    fn new(r: Cursor<&'a [u8]>) -> Self {
        Self {
            r,
            handles: Vec::new(),
        }
    }

    fn record_handle(&mut self, val: HandleValue) -> u32 {
        let h = 0x007E0000 + self.handles.len() as u32;
        self.handles.push(val);
        h
    }

    fn resolve_handle(&self, handle: u32) -> Result<&HandleValue, AdminError> {
        let idx = (handle.wrapping_sub(0x007E0000)) as usize;
        self.handles.get(idx).ok_or_else(|| {
            AdminError::MalformedStream(format!("Invalid handle reference: {handle:#010x}"))
        })
    }

    fn parse_admin(&mut self) -> Result<AdminFile, AdminError> {
        let mut admin = AdminFile::new();

        // Expect TC_OBJECT (0x73) for HashMap: read classDesc first, then record object handle
        let tag = self.r.read_u8()?;
        if tag != 0x73 {
            return Err(AdminError::MalformedStream(format!("Expected TC_OBJECT (0x73), found {tag:#04x}")));
        }
        let class_desc = self.read_class_desc()?;
        self.record_handle(HandleValue::Object); // HashMap handle (0x007E0001)
        if !class_desc.name.contains("HashMap") {
            return Err(AdminError::MalformedStream(format!("Expected HashMap class, got {}", class_desc.name)));
        }

        // Read HashMap fields: loadFactor (f32) + threshold (i32)
        let _load_factor = self.r.read_f32::<BigEndian>()?;
        let _threshold = self.r.read_i32::<BigEndian>()?;

        // Read block data or entries
        loop {
            let tc = match self.r.read_u8() {
                Ok(b) => b,
                Err(e) if e.kind() == io::ErrorKind::UnexpectedEof => break,
                Err(e) => return Err(e.into()),
            };

            match tc {
                0x77 => { // TC_BLOCKDATA
                    let len = self.r.read_u8()? as usize;
                    if len >= 8 {
                        let _buckets = self.r.read_i32::<BigEndian>()?;
                        let size = self.r.read_i32::<BigEndian>()? as usize;
                        let rem = len - 8;
                        if rem > 0 {
                            let mut skip = vec![0u8; rem];
                            self.r.read_exact(&mut skip)?;
                        }

                        // Read `size` key/value pairs
                        for _ in 0..size {
                            let key = self.read_string_or_ref()?;
                            let comp = self.read_admin_component(&key)?;
                            admin.entries.insert(normalize_admin_path(&key), comp);
                        }
                    } else {
                        let mut skip = vec![0u8; len];
                        self.r.read_exact(&mut skip)?;
                    }
                }
                0x78 => { // TC_ENDBLOCKDATA
                    // End of HashMap object
                    break;
                }
                other => {
                    return Err(AdminError::MalformedStream(format!("Unexpected tag in HashMap body: {other:#04x}")));
                }
            }
        }

        Ok(admin)
    }

    fn read_class_desc(&mut self) -> Result<ClassDescriptor, AdminError> {
        let tag = self.r.read_u8()?;
        match tag {
            0x72 => { // TC_CLASSDESC
                let name = read_utf(&mut self.r)?;
                let _serial_version_uid = self.r.read_i64::<BigEndian>()?;
                let _flags = self.r.read_u8()?;

                // JVM ObjectInputStream assigns the ClassDesc handle BEFORE reading field descriptors!
                let handle_idx = self.handles.len();
                self.handles.push(HandleValue::ClassDesc(ClassDescriptor {
                    name: name.clone(),
                    fields: Vec::new(),
                }));

                let num_fields = self.r.read_u16::<BigEndian>()? as usize;
                let mut fields = Vec::with_capacity(num_fields);

                for _ in 0..num_fields {
                    let type_code = self.r.read_u8()?;
                    let field_name = read_utf(&mut self.r)?;
                    let class_name = if type_code == b'[' || type_code == b'L' {
                        Some(self.read_string_or_ref()?)
                    } else {
                        None
                    };
                    fields.push(FieldDesc {
                        type_code,
                        name: field_name,
                        class_name,
                    });
                }

                // class annotations terminated by TC_ENDBLOCKDATA (0x78)
                let mut end = self.r.read_u8()?;
                while end != 0x78 {
                    end = self.r.read_u8()?;
                }

                // super class desc: TC_NULL (0x70) or another classdesc
                let _super_desc = self.read_class_desc()?;

                let desc = ClassDescriptor { name, fields };
                self.handles[handle_idx] = HandleValue::ClassDesc(desc.clone());
                Ok(desc)
            }
            0x71 => { // TC_REFERENCE
                let handle = self.r.read_u32::<BigEndian>()?;
                match self.resolve_handle(handle)? {
                    HandleValue::ClassDesc(d) => Ok(d.clone()),
                    _ => Err(AdminError::MalformedStream(format!("Handle {handle:#010x} is not a ClassDescriptor"))),
                }
            }
            0x70 => { // TC_NULL
                Ok(ClassDescriptor {
                    name: String::new(),
                    fields: Vec::new(),
                })
            }
            other => Err(AdminError::MalformedStream(format!("Expected TC_CLASSDESC or TC_REFERENCE, found {other:#04x}"))),
        }
    }

    fn read_string_or_ref(&mut self) -> Result<String, AdminError> {
        let tag = self.r.read_u8()?;
        match tag {
            0x74 => { // TC_STRING
                let s = read_utf(&mut self.r)?;
                self.record_handle(HandleValue::StringVal(s.clone()));
                Ok(s)
            }
            0x71 => { // TC_REFERENCE
                let handle = self.r.read_u32::<BigEndian>()?;
                match self.resolve_handle(handle)? {
                    HandleValue::StringVal(s) => Ok(s.clone()),
                    _ => Err(AdminError::MalformedStream(format!("Handle {handle:#010x} is not a String"))),
                }
            }
            0x70 => Ok(String::new()), // TC_NULL
            other => Err(AdminError::MalformedStream(format!("Expected TC_STRING or TC_REFERENCE, found {other:#04x}"))),
        }
    }

    fn read_admin_component(&mut self, fallback_key: &str) -> Result<AdministrationComponent, AdminError> {
        let tag = self.r.read_u8()?;
        if tag != 0x73 {
            return Err(AdminError::MalformedStream(format!("Expected TC_OBJECT (0x73) for component, found {tag:#04x}")));
        }
        // Per JVM ObjectInputStream: read classDesc first, then record object handle
        let class_desc = self.read_class_desc()?;
        self.record_handle(HandleValue::Object); // Component object handle
        let mut is_checked_out = false;
        let mut is_created = false;
        let mut is_ever_checked_in = false;
        let mut is_expired = false;
        let mut is_dirty = false;
        let mut is_vsc_happy = true;
        let mut path = fallback_key.to_string();

        for f in &class_desc.fields {
            match f.name.as_str() {
                "isCheckedout" => is_checked_out = self.r.read_u8()? != 0,
                "isCreated" => is_created = self.r.read_u8()? != 0,
                "isEvercheckedIn" => is_ever_checked_in = self.r.read_u8()? != 0,
                "isExpired" => is_expired = self.r.read_u8()? != 0,
                "m_isDirty" => is_dirty = self.r.read_u8()? != 0,
                "m_isVSCHappy" => is_vsc_happy = self.r.read_u8()? != 0,
                "m_path" => {
                    path = self.read_string_or_ref()?;
                }
                _ => {
                    // Skip unknown primitive or object
                    match f.type_code {
                        b'Z' | b'B' => { self.r.read_u8()?; }
                        b'C' | b'S' => { self.r.read_u16::<BigEndian>()?; }
                        b'I' | b'F' => { self.r.read_u32::<BigEndian>()?; }
                        b'J' | b'D' => { self.r.read_u64::<BigEndian>()?; }
                        b'[' | b'L' => {
                            let _ = self.read_string_or_ref();
                        }
                        _ => {}
                    }
                }
            }
        }

        Ok(AdministrationComponent {
            is_checked_out,
            is_created,
            is_ever_checked_in,
            is_expired,
            is_dirty,
            is_vsc_happy,
            path: normalize_admin_path(&path),
        })
    }
}
