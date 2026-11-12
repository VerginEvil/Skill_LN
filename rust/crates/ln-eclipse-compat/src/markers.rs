use std::collections::HashMap;
use std::fs::File;
use std::io::{self, Cursor, Read, Write};
use std::path::Path;
use byteorder::{BigEndian, ReadBytesExt, WriteBytesExt};
use serde::{Deserialize, Serialize};
use thiserror::Error;

pub const VERSION: u32 = 3;

#[derive(Error, Debug)]
pub enum MarkerError {
    #[error(transparent)]
    Io(#[from] io::Error),
    #[error("Unsupported .markers version: {0}, expected 3")]
    UnsupportedVersion(u32),
    #[error("Malformed .markers stream: {0}")]
    MalformedStream(String),
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub enum MarkerSeverity {
    Info,
    Warning,
    Error,
    Unknown(i32),
}

impl MarkerSeverity {
    pub fn from_code(code: i32) -> Self {
        match code {
            0 => Self::Info,
            1 => Self::Warning,
            2 => Self::Error,
            other => Self::Unknown(other),
        }
    }

    pub fn to_code(&self) -> i32 {
        match self {
            Self::Info => 0,
            Self::Warning => 1,
            Self::Error => 2,
            Self::Unknown(c) => *c,
        }
    }

    pub fn as_str(&self) -> &str {
        match self {
            Self::Info => "INFO",
            Self::Warning => "WARNING",
            Self::Error => "ERROR",
            Self::Unknown(_) => "UNKNOWN",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub enum AttributeValue {
    Bool(bool),
    Int(i32),
    String(String),
}

/// A decoded problem marker from Eclipse `.markers` (MarkerReader_3 v3).
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct ProblemMarker {
    pub id: u64,
    pub marker_type: String,
    pub resource_path: String,
    pub file: String,
    pub line_number: i32,
    pub severity: MarkerSeverity,
    pub message: String,
    pub is_script_problem: bool,
    pub creation_time: u64,
    pub attributes: HashMap<String, AttributeValue>,
}

/// In-memory representation of an Eclipse `.markers` file.
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
pub struct MarkersFile {
    pub version: u32,
    pub markers: Vec<ProblemMarker>,
}

impl MarkersFile {
    pub fn new() -> Self {
        Self {
            version: VERSION,
            markers: Vec::new(),
        }
    }

    pub fn load_from_path(path: &Path) -> Result<Self, MarkerError> {
        if !path.exists() {
            return Ok(Self::new());
        }
        let mut file = File::open(path)?;
        let mut buf = Vec::new();
        file.read_to_end(&mut buf)?;
        Self::deserialize(&buf)
    }

    pub fn save_to_path(&self, path: &Path) -> Result<(), MarkerError> {
        if let Some(parent) = path.parent() {
            std::fs::create_dir_all(parent)?;
        }
        let bytes = self.serialize()?;
        std::fs::write(path, bytes)?;
        Ok(())
    }

    /// Serializes to the exact MarkerReader_3 v3 binary format.
    pub fn serialize(&self) -> Result<Vec<u8>, MarkerError> {
        let mut w = Cursor::new(Vec::new());

        // Header: u32 version = 3
        w.write_u32::<BigEndian>(self.version)?;

        // Group markers by resource_path
        let mut grouped: HashMap<String, Vec<&ProblemMarker>> = HashMap::new();
        for m in &self.markers {
            grouped.entry(m.resource_path.clone()).or_default().push(m);
        }

        let mut types_table: Vec<String> = Vec::new();

        for (res_path, markers) in grouped {
            write_utf(&mut w, &res_path)?;
            w.write_u32::<BigEndian>(markers.len() as u32)?;

            for m in markers {
                w.write_u64::<BigEndian>(m.id)?;

                if let Some(pos) = types_table.iter().position(|t| t == &m.marker_type) {
                    w.write_u8(1)?; // TAG_INDEX
                    w.write_u32::<BigEndian>(pos as u32)?;
                } else {
                    w.write_u8(2)?; // TAG_QNAME
                    write_utf(&mut w, &m.marker_type)?;
                    types_table.push(m.marker_type.clone());
                }

                w.write_i16::<BigEndian>(m.attributes.len() as i16)?;

                for (k, val) in &m.attributes {
                    write_utf(&mut w, k)?;
                    match val {
                        AttributeValue::Bool(b) => {
                            w.write_u8(1)?;
                            w.write_u8(if *b { 1 } else { 0 })?;
                        }
                        AttributeValue::Int(i) => {
                            w.write_u8(2)?;
                            w.write_i32::<BigEndian>(*i)?;
                        }
                        AttributeValue::String(s) => {
                            w.write_u8(3)?;
                            write_utf(&mut w, s)?;
                        }
                    }
                }

                w.write_u64::<BigEndian>(m.creation_time)?;
            }
        }

        Ok(w.into_inner())
    }

    /// Deserializes from the exact MarkerReader_3 v3 binary format.
    pub fn deserialize(bytes: &[u8]) -> Result<Self, MarkerError> {
        if bytes.len() < 4 {
            return Ok(Self::new());
        }

        let mut r = Cursor::new(bytes);
        let version = r.read_u32::<BigEndian>()?;
        if version != VERSION {
            return Err(MarkerError::UnsupportedVersion(version));
        }

        let mut types_table: Vec<String> = Vec::new();
        let mut markers: Vec<ProblemMarker> = Vec::new();

        while (r.position() as usize) < bytes.len() {
            let res_path = match read_utf(&mut r) {
                Ok(s) => s,
                Err(e) if e.kind() == io::ErrorKind::UnexpectedEof => break,
                Err(e) => return Err(e.into()),
            };

            if (r.position() as usize) + 4 > bytes.len() {
                break;
            }

            let marker_count = r.read_u32::<BigEndian>()? as usize;

            for _ in 0..marker_count {
                if (r.position() as usize) >= bytes.len() {
                    break;
                }

                let marker_id = r.read_u64::<BigEndian>()?;
                let type_flag = r.read_u8()?;

                let marker_type = match type_flag {
                    1 => {
                        let type_idx = r.read_u32::<BigEndian>()? as usize;
                        types_table.get(type_idx).cloned().unwrap_or_else(|| "unknown".to_string())
                    }
                    2 => {
                        let t = read_utf(&mut r)?;
                        types_table.push(t.clone());
                        t
                    }
                    _ => "unknown".to_string(),
                };

                let attr_count = r.read_i16::<BigEndian>()?;
                let mut attributes = HashMap::new();
                let mut line_number = 0;
                let mut severity_code = 1;
                let mut message = String::new();
                let mut is_script_problem = false;

                if attr_count > 0 {
                    for _ in 0..attr_count {
                        let key = read_utf(&mut r)?;
                        let val_type = r.read_u8()?;
                        let val = match val_type {
                            1 => {
                                let b = r.read_u8()? != 0;
                                if key == "isScriptProblem" {
                                    is_script_problem = b;
                                }
                                AttributeValue::Bool(b)
                            }
                            2 => {
                                let i = r.read_i32::<BigEndian>()?;
                                if key == "lineNumber" {
                                    line_number = i;
                                } else if key == "severity" {
                                    severity_code = i;
                                }
                                AttributeValue::Int(i)
                            }
                            3 => {
                                let s = read_utf(&mut r)?;
                                if key == "message" {
                                    message = s.clone();
                                }
                                AttributeValue::String(s)
                            }
                            _ => {
                                AttributeValue::String(String::new())
                            }
                        };
                        attributes.insert(key, val);
                    }
                }

                let creation_time = if (r.position() as usize) + 8 <= bytes.len() {
                    r.read_u64::<BigEndian>()?
                } else {
                    0
                };

                let clean_res = res_path.trim_start_matches('/').to_string();
                let file = if let Some(slash) = clean_res.find('/') {
                    clean_res[slash + 1..].to_string()
                } else {
                    clean_res.clone()
                };

                markers.push(ProblemMarker {
                    id: marker_id,
                    marker_type,
                    resource_path: res_path.clone(),
                    file,
                    line_number,
                    severity: MarkerSeverity::from_code(severity_code),
                    message,
                    is_script_problem,
                    creation_time,
                    attributes,
                });
            }
        }

        Ok(Self {
            version,
            markers,
        })
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
    let len = match r.read_u16::<BigEndian>() {
        Ok(l) => l as usize,
        Err(e) => return Err(e),
    };
    let mut buf = vec![0u8; len];
    r.read_exact(&mut buf)?;
    Ok(String::from_utf8_lossy(&buf).to_string())
}
