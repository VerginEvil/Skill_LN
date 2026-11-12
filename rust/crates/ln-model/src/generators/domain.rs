use std::collections::HashMap;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EnumItem {
    pub name: String,
    pub description: String,
    pub position: usize,
    #[serde(default)]
    pub label_code: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DomainSpec {
    pub name: String,
    pub description: String,
    #[serde(default = "default_datatype")]
    pub native_datatype: u32,
    #[serde(default = "default_length")]
    pub display_length: usize,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub enums: Vec<EnumItem>,
    #[serde(default)]
    pub facets: HashMap<String, String>,
}

fn default_datatype() -> u32 {
    7 // Enum
}

fn default_length() -> usize {
    20
}

/// Generates production-grade `<DR_Domain>` XML matching Infor LN Studio 10.8.
pub fn generate_domain_xml(spec: &DomainSpec, default_ver: &str, default_app: &str) -> String {
    let ver = spec.version_id.as_deref().unwrap_or(default_ver);
    let app = spec.application.as_deref().unwrap_or(default_app);
    let c_time = "1970-01-01T00:00:00Z";

    let mut enums_xml = String::new();
    for e in &spec.enums {
        let e_ref = e.label_code.clone().unwrap_or_else(|| format!("{}{:03}", spec.name, e.position));
        enums_xml.push_str(&format!(
            "<Enumeration><descriptionReference>{}</descriptionReference><description>{}</description><name>{}</name><position>{}</position></Enumeration>",
            e_ref, e.description, e.name, e.position
        ));
    }

    let mut facets_xml = String::new();
    if spec.native_datatype == 7 {
        let tot = spec.facets.get("totalDigits").map(|s| s.as_str()).unwrap_or("20");
        facets_xml.push_str(&format!("<Facet><value>{tot}</value><type>totalDigits</type></Facet>"));
    } else if spec.native_datatype == 3 || spec.native_datatype == 5 {
        let tot = spec.facets.get("totalDigits").or_else(|| spec.facets.get("maxLength")).map(|s| s.as_str()).unwrap_or("20");
        facets_xml.push_str(&format!("<Facet><value>{tot}</value><type>totalDigits</type></Facet>"));
        if spec.native_datatype == 5 {
            facets_xml.push_str("<Facet><value>2</value><type>fractionDigits</type></Facet>");
        }
    } else {
        let max_l = spec.facets.get("maxLength").map(|s| s.as_str()).unwrap_or("20");
        let min_l = spec.facets.get("minLength").map(|s| s.as_str()).unwrap_or("1");
        facets_xml.push_str(&format!("<Facet><value>{max_l}</value><type>maxLength</type></Facet><Facet><value>{min_l}</value><type>minLength</type></Facet>"));
    }

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Domain><description>{}</description><versionID>{}</versionID><type>domain</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy/><creationDateTime>{}</creationDateTime><createdBy/></Version><documentation/><Attachment><type>relnotes</type><name>{}</name></Attachment><Attachment><type>techdoc</type><name>{}</name></Attachment>{}<rangeMessage/><range/><displayFormat/><roundingMethod>4</roundingMethod><divideFactor>0</divideFactor><displayLength>{}</displayLength><internalFormat/><conversion>4</conversion><alignment>5</alignment><application>{}</application><datatype>{}<nativeDatatype>{}</nativeDatatype></datatype></DR_Domain>"#,
        spec.description, ver, spec.name, c_time, c_time, spec.name, spec.name, enums_xml, spec.display_length, app, facets_xml, spec.native_datatype
    )
}
