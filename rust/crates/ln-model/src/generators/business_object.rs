use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BusinessObjectSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default = "default_bo_type")]
    pub type_of_business_object: String, // "document", "master"
    #[serde(default = "default_schema_ver")]
    pub schema_version: String,
}

fn default_bo_type() -> String {
    "document".to_string()
}

fn default_schema_ver() -> String {
    "1.0".to_string()
}

/// Generates standard `<DR_BusinessObject>` .bus XML matching Infor LN Studio 10.8.
pub fn generate_business_object_xml(
    spec: &BusinessObjectSpec,
    application: &str,
    default_version_id: &str,
    created_time: Option<&str>,
) -> String {
    let now_iso = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;
    let lower_name = code.to_lowercase();
    let bo_type = &spec.type_of_business_object;
    let schema_ver = &spec.schema_version;

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_BusinessObject><description>{}</description><versionID>{}</versionID><type>businessobject</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{}</creationDateTime><createdBy>agent</createdBy></Version><descriptionReference>{}</descriptionReference><documentation/><application>{}</application><businessObject>{}</businessObject><maintainedInStudio>true</maintainedInStudio><typeOfBusinessObject>{}</typeOfBusinessObject><lowerCaseBusinessObjectName>{}</lowerCaseBusinessObjectName><schemaVersion>{}</schemaVersion></DR_BusinessObject>"#,
        desc, ver, code, now_iso, now_iso, code, app, code, bo_type, lower_name, schema_ver
    )
}
