use serde::{Deserialize, Serialize};

/// Ecore Native Integer Datatypes in Infor LN Studio 10.8 Build 0640.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[repr(u32)]
pub enum NativeDatatype {
    Byte = 1,
    Double = 2,
    Long = 3,
    Numeric = 5,
    String = 6,
    Enum = 7,
    Date = 9,
    Utc = 14,
}

impl NativeDatatype {
    pub fn as_u32(&self) -> u32 {
        *self as u32
    }

    pub fn from_u32(val: u32) -> Option<Self> {
        match val {
            1 => Some(NativeDatatype::Byte),
            2 => Some(NativeDatatype::Double),
            3 => Some(NativeDatatype::Long),
            5 => Some(NativeDatatype::Numeric),
            6 => Some(NativeDatatype::String),
            7 => Some(NativeDatatype::Enum),
            9 => Some(NativeDatatype::Date),
            14 => Some(NativeDatatype::Utc),
            _ => None,
        }
    }

    /// Infers NativeDatatype from a domain name or type string.
    pub fn from_str_hint(hint: &str) -> Self {
        let lower = hint.trim().to_lowercase();
        if lower == "byte" || lower == "1" {
            NativeDatatype::Byte
        } else if lower == "double" || lower == "float" || lower == "2" {
            NativeDatatype::Double
        } else if lower == "long" || lower == "int" || lower == "integer" || lower == "3" {
            NativeDatatype::Long
        } else if lower == "numeric" || lower == "amount" || lower == "amnt" || lower == "5" {
            NativeDatatype::Numeric
        } else if lower == "enum" || lower == "boolean" || lower == "bool" || lower == "yesno" || lower == "7" {
            NativeDatatype::Enum
        } else if lower.contains("date") || lower == "9" {
            NativeDatatype::Date
        } else if lower.contains("utc") || lower == "14" {
            NativeDatatype::Utc
        } else {
            NativeDatatype::String
        }
    }
}

/// Checks if a field name is a line-number column (`line`, `lino`, `seqn`)
/// that should default to non-mandatory (`isMandatory = false`) per TBL003 & ADR 0017.
pub fn is_line_number_column(name: &str) -> bool {
    let lower = name.trim().to_lowercase();
    matches!(lower.as_str(), "line" | "lino" | "seqn") || lower.ends_with("_line") || lower.ends_with("_lino")
}
