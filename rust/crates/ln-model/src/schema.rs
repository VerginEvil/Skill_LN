use std::collections::HashMap;
use std::sync::OnceLock;
use serde::{Deserialize, Serialize};

pub const EMBEDDED_TDE_SCHEMA_JSON: &str = include_str!("../../../schemas/tde_schema_0640.json");
pub const EMBEDDED_OWTEMPLATES_JSON: &str = include_str!("../../../schemas/owtemplates_0640.json");

static TDE_SCHEMA: OnceLock<TdeSchema> = OnceLock::new();
static TEMPLATES_CATALOG: OnceLock<TemplatesCatalog> = OnceLock::new();

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FieldMeta {
    pub name: String,
    pub kind: String, // "string", "cdata", "list", "object"
    #[serde(default)]
    pub target_type: Option<String>,
    #[serde(default)]
    pub descriptor: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClassMeta {
    pub name: String,
    pub full_name: String,
    #[serde(default)]
    pub super_class: Option<String>,
    #[serde(default)]
    pub is_root_component: bool,
    #[serde(default)]
    pub file_extension: Option<String>,
    #[serde(default)]
    pub fields: Vec<FieldMeta>,
    #[serde(default)]
    pub all_fields: Vec<FieldMeta>,
}

impl ClassMeta {
    pub fn get_field(&self, name: &str) -> Option<&FieldMeta> {
        self.all_fields
            .iter()
            .find(|f| f.name.eq_ignore_ascii_case(name))
            .or_else(|| self.fields.iter().find(|f| f.name.eq_ignore_ascii_case(name)))
    }

    pub fn has_field(&self, name: &str) -> bool {
        self.get_field(name).is_some()
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RootComponentInfo {
    pub file_extension: String,
    pub type_name: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TdeSchema {
    pub version: String,
    pub root_components: HashMap<String, RootComponentInfo>,
    pub classes: HashMap<String, ClassMeta>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OwTemplate {
    pub name: String,
    pub source: String,
    pub root_tag: String,
    pub sha256: String,
    pub content: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScriptTemplate {
    pub name: String,
    pub source: String,
    pub sha256: String,
    pub content: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TemplatesCatalog {
    pub owtemplates: HashMap<String, OwTemplate>,
    pub script_templates: HashMap<String, ScriptTemplate>,
}

/// Returns a reference to the statically loaded TDE schema.
pub fn get_tde_schema() -> &'static TdeSchema {
    TDE_SCHEMA.get_or_init(|| {
        serde_json::from_str(EMBEDDED_TDE_SCHEMA_JSON)
            .expect("Failed to deserialize embedded tde_schema_0640.json")
    })
}

/// Returns a reference to the statically loaded owtemplates & ScriptTemplates catalog.
pub fn get_templates_catalog() -> &'static TemplatesCatalog {
    TEMPLATES_CATALOG.get_or_init(|| {
        serde_json::from_str(EMBEDDED_OWTEMPLATES_JSON)
            .expect("Failed to deserialize embedded owtemplates_0640.json")
    })
}

/// Looks up a TDE class by simple name (e.g. `DR_Table`, `Column`) or full name.
pub fn lookup_class(class_name: &str) -> Option<&'static ClassMeta> {
    let schema = get_tde_schema();
    schema.classes.get(class_name)
}

/// Looks up root component info by class name (e.g. `DR_Table`) or type name (`table`).
pub fn lookup_root_component(name_or_type: &str) -> Option<(&'static str, &'static str)> {
    let schema = get_tde_schema();
    if let Some(info) = schema.root_components.get(name_or_type) {
        return Some((info.file_extension.as_str(), info.type_name.as_str()));
    }
    for (class_name, info) in &schema.root_components {
        if info.type_name.eq_ignore_ascii_case(name_or_type) || class_name.eq_ignore_ascii_case(name_or_type) {
            return Some((info.file_extension.as_str(), info.type_name.as_str()));
        }
    }
    None
}

/// Returns the owtemplate content for a given template file name.
pub fn get_owtemplate(name: &str) -> Option<&'static OwTemplate> {
    let catalog = get_templates_catalog();
    catalog.owtemplates.get(name)
        .or_else(|| {
            let with_xml = format!("{name}.xml");
            catalog.owtemplates.get(&with_xml)
        })
}

/// Returns the ScriptTemplate content for a given archetype name (e.g. `DalTwo`, `Function`).
pub fn get_script_template(name: &str) -> Option<&'static ScriptTemplate> {
    let catalog = get_templates_catalog();
    catalog.script_templates.get(name)
}
