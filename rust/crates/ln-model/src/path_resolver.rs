use std::path::{Path, PathBuf};
use thiserror::Error;

#[derive(Debug, Error, PartialEq, Eq)]
pub enum TdePathError {
    #[error("Legacy plural folder detected in path '{0}'. LN Studio Single-XML TDE requires singular folder names (e.g. 'table/' not 'tables/').")]
    LegacyPluralFolderBlocked(String),
    #[error("Unknown or unsupported component type '{0}'.")]
    UnknownComponentType(String),
    #[error("Invalid component name '{0}'. Must contain at least a 2-character package prefix.")]
    InvalidComponentName(String),
}

pub const MODULE_SCOPED_TYPES: &[&str] = &[
    "table", "session", "library", "function", "report", "menu", "additional", "businessobject",
];

pub const PACKAGE_SCOPED_TYPES: &[&str] = &[
    "domain", "label", "message", "question", "chart",
];

pub const LEGACY_PLURAL_FOLDERS: &[&str] = &[
    "tables", "sessions", "domains", "labels", "menus", "messages", "questions",
    "reports", "libraries", "functions", "additionals", "additional_files",
];

/// Splits an Infor LN component name (e.g. 'tcibd001' or 'txcmg.clor' or 'whinh4131m000') into (package, module, object).
pub fn split_component_name(comp_name: &str) -> (String, String, String) {
    let clean = comp_name.trim();
    if clean.len() < 2 {
        return (clean.to_lowercase(), String::new(), String::new());
    }

    let pkg = clean[..2].to_lowercase();
    if let Some((first, obj)) = clean.split_once('.') {
        let mod_code = if first.len() > 2 {
            first[2..].to_lowercase()
        } else {
            String::new()
        };
        (pkg, mod_code, obj.to_string())
    } else {
        let mod_code = if clean.len() >= 5 {
            clean[2..5].to_lowercase()
        } else {
            String::new()
        };
        let obj = if clean.len() > 5 {
            clean[5..].to_string()
        } else {
            String::new()
        };
        (pkg, mod_code, obj)
    }
}

/// Checks if a component type is module-scoped (requires a `{mod}` subfolder).
pub fn is_module_scoped(comp_type: &str) -> bool {
    let lower = comp_type.trim().to_lowercase();
    MODULE_SCOPED_TYPES.contains(&lower.as_str())
}

/// Validates that a target path does not use legacy plural folders.
pub fn validate_no_legacy_plural(path: &Path) -> Result<(), TdePathError> {
    for comp in path.components() {
        let s = comp.as_os_str().to_string_lossy().to_lowercase();
        if LEGACY_PLURAL_FOLDERS.contains(&s.as_str()) {
            return Err(TdePathError::LegacyPluralFolderBlocked(path.to_string_lossy().to_string()));
        }
    }
    Ok(())
}

/// Resolves the canonical relative TDE path for a component:
/// - Module-scoped: `{pkg}/{comp_type}/{mod}/{comp_name}.{ext}`
/// - Package-scoped: `{pkg}/{comp_type}/{comp_name}.{ext}`
pub fn resolve_tde_relative_path(comp_type: &str, comp_name: &str, ext: &str) -> Result<PathBuf, TdePathError> {
    let clean_type = comp_type.trim().to_lowercase();
    let clean_name = comp_name.trim();

    if clean_name.len() < 2 {
        return Err(TdePathError::InvalidComponentName(clean_name.to_string()));
    }

    let (pkg, mod_code, _) = split_component_name(clean_name);
    let ext_with_dot = if ext.starts_with('.') {
        ext.to_string()
    } else {
        format!(".{ext}")
    };

    let filename = format!("{clean_name}{ext_with_dot}");

    let mut path = PathBuf::new();
    path.push(&pkg);
    path.push(&clean_type);

    if is_module_scoped(&clean_type) {
        let eff_mod = if mod_code.is_empty() { "gen" } else { &mod_code };
        path.push(eff_mod);
    }

    path.push(filename);
    validate_no_legacy_plural(&path)?;

    Ok(path)
}
