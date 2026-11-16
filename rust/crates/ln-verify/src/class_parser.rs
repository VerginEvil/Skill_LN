use std::io::{Cursor, Read};
use byteorder::{BigEndian, ReadBytesExt};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct FieldInfo {
    pub name: String,
    pub descriptor: String,
    pub is_public: bool,
    pub is_protected: bool,
    pub is_static: bool,
    pub is_final: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ParsedClass {
    pub class_name: String,
    pub super_class_name: Option<String>,
    pub serial_version_uid: Option<i64>,
    pub sha256: String,
    pub field_count: usize,
    pub fields: Vec<FieldInfo>,
}

impl ParsedClass {
    /// Counts declared public/protected non-static fields representing TDE XML elements.
    pub fn declared_model_fields_count(&self) -> usize {
        self.fields.iter().filter(|f| {
            (f.is_public || (f.is_protected && self.class_name.contains("additional")))
                && !f.is_static
                && !f.name.ends_with("_EDEFAULT")
                && f.name != "eFlags"
        }).count()
    }
}

#[allow(dead_code)]
#[derive(Debug, Clone)]
enum CpEntry {
    Utf8(String),
    Integer(i32),
    Float(f32),
    Long(i64),
    Double(f64),
    Class(u16),
    String(u16),
    Fieldref { class_index: u16, name_and_type_index: u16 },
    Methodref { class_index: u16, name_and_type_index: u16 },
    InterfaceMethodref { class_index: u16, name_and_type_index: u16 },
    NameAndType { name_index: u16, descriptor_index: u16 },
    MethodHandle { reference_kind: u8, reference_index: u16 },
    MethodType(u16),
    Dynamic { bootstrap_method_attr_index: u16, name_and_type_index: u16 },
    InvokeDynamic { bootstrap_method_attr_index: u16, name_and_type_index: u16 },
    Module(u16),
    Package(u16),
    Unusable,
}

pub fn parse_class_bytes(bytes: &[u8]) -> Result<ParsedClass, String> {
    let mut cur = Cursor::new(bytes);

    let magic = cur.read_u32::<BigEndian>().map_err(|e| format!("IO error: {e}"))?;
    if magic != 0xCAFEBABE {
        return Err(format!("Invalid JVM class magic: {magic:#010X}, expected 0xCAFEBABE"));
    }

    let _minor = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
    let _major = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;

    let cp_count = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())? as usize;
    let mut cp: Vec<CpEntry> = Vec::with_capacity(cp_count);
    cp.push(CpEntry::Unusable); // 1-based indexing in JVM constant pool

    let mut i = 1;
    while i < cp_count {
        let tag = cur.read_u8().map_err(|e| e.to_string())?;
        match tag {
            1 => {
                let len = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())? as usize;
                let mut buf = vec![0u8; len];
                cur.read_exact(&mut buf).map_err(|e| e.to_string())?;
                let s = String::from_utf8_lossy(&buf).to_string();
                cp.push(CpEntry::Utf8(s));
                i += 1;
            }
            3 => {
                let val = cur.read_i32::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Integer(val));
                i += 1;
            }
            4 => {
                let val = cur.read_f32::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Float(val));
                i += 1;
            }
            5 => {
                let val = cur.read_i64::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Long(val));
                cp.push(CpEntry::Unusable); // 8-byte constants take two entries
                i += 2;
            }
            6 => {
                let val = cur.read_f64::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Double(val));
                cp.push(CpEntry::Unusable); // 8-byte constants take two entries
                i += 2;
            }
            7 => {
                let name_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Class(name_idx));
                i += 1;
            }
            8 => {
                let str_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::String(str_idx));
                i += 1;
            }
            9 => {
                let c_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let nt_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Fieldref { class_index: c_idx, name_and_type_index: nt_idx });
                i += 1;
            }
            10 => {
                let c_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let nt_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Methodref { class_index: c_idx, name_and_type_index: nt_idx });
                i += 1;
            }
            11 => {
                let c_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let nt_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::InterfaceMethodref { class_index: c_idx, name_and_type_index: nt_idx });
                i += 1;
            }
            12 => {
                let n_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let d_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::NameAndType { name_index: n_idx, descriptor_index: d_idx });
                i += 1;
            }
            15 => {
                let r_kind = cur.read_u8().map_err(|e| e.to_string())?;
                let r_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::MethodHandle { reference_kind: r_kind, reference_index: r_idx });
                i += 1;
            }
            16 => {
                let d_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::MethodType(d_idx));
                i += 1;
            }
            17 => {
                let b_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let nt_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Dynamic { bootstrap_method_attr_index: b_idx, name_and_type_index: nt_idx });
                i += 1;
            }
            18 => {
                let b_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                let nt_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::InvokeDynamic { bootstrap_method_attr_index: b_idx, name_and_type_index: nt_idx });
                i += 1;
            }
            19 => {
                let n_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Module(n_idx));
                i += 1;
            }
            20 => {
                let n_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                cp.push(CpEntry::Package(n_idx));
                i += 1;
            }
            other => return Err(format!("Unsupported constant pool tag: {other} at index {i}")),
        }
    }

    let get_utf8 = |idx: u16| -> Option<String> {
        match cp.get(idx as usize)? {
            CpEntry::Utf8(s) => Some(s.clone()),
            _ => None,
        }
    };

    let get_class_name = |idx: u16| -> Option<String> {
        match cp.get(idx as usize)? {
            CpEntry::Class(n_idx) => get_utf8(*n_idx),
            _ => None,
        }
    };

    let _access_flags = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
    let this_class_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
    let super_class_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;

    let class_name = get_class_name(this_class_idx)
        .ok_or_else(|| "Failed to resolve this_class".to_string())?
        .replace('/', ".");

    let super_class_name = if super_class_idx > 0 {
        get_class_name(super_class_idx).map(|s| s.replace('/', "."))
    } else {
        None
    };

    let interfaces_count = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())? as usize;
    for _ in 0..interfaces_count {
        let _ = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
    }

    // Fields
    let fields_count = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())? as usize;
    let mut fields = Vec::with_capacity(fields_count);
    let mut serial_version_uid = None;

    for _ in 0..fields_count {
        let f_access = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
        let f_name_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
        let f_desc_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
        let f_attr_count = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())? as usize;

        let f_name = get_utf8(f_name_idx).unwrap_or_default();
        let f_desc = get_utf8(f_desc_idx).unwrap_or_default();
        let is_public = (f_access & 0x0001) != 0;
        let is_protected = (f_access & 0x0004) != 0;
        let is_static = (f_access & 0x0008) != 0;
        let is_final = (f_access & 0x0010) != 0;

        for _ in 0..f_attr_count {
            let a_name_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
            let a_len = cur.read_u32::<BigEndian>().map_err(|e| e.to_string())? as usize;
            let a_name = get_utf8(a_name_idx).unwrap_or_default();

            if a_name == "ConstantValue" && a_len == 2 {
                let cv_idx = cur.read_u16::<BigEndian>().map_err(|e| e.to_string())?;
                if f_name == "serialVersionUID" {
                    if let Some(CpEntry::Long(val)) = cp.get(cv_idx as usize) {
                        serial_version_uid = Some(*val);
                    }
                }
            } else {
                // Skip attribute data
                let mut discard = vec![0u8; a_len];
                cur.read_exact(&mut discard).map_err(|e| e.to_string())?;
            }
        }

        fields.push(FieldInfo {
            name: f_name,
            descriptor: f_desc,
            is_public,
            is_protected,
            is_static,
            is_final,
        });
    }

    let mut hasher = Sha256::new();
    hasher.update(bytes);
    let sha256_hash = format!("{:x}", hasher.finalize());

    Ok(ParsedClass {
        class_name,
        super_class_name,
        serial_version_uid,
        sha256: sha256_hash,
        field_count: fields.len(),
        fields,
    })
}
