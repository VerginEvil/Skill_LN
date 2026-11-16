use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LabelSpec {
    #[serde(alias = "code")]
    pub name: String,
    #[serde(alias = "text", default)]
    pub description: String,
    #[serde(default)]
    pub length: Option<usize>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
}

/// Generates standard `<DR_Label>` XML.
pub fn generate_label_xml(
    name: &str,
    description: &str,
    version_id: &str,
    application: &str,
    length: Option<usize>,
    created_time: Option<&str>,
) -> String {
    let c_time = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let lbl_len = length.unwrap_or_else(|| description.chars().count().max(1));
    let kw_take: String = description.chars().take(14).collect();
    let keyword = kw_take.to_uppercase().trim().to_string();

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Label><description>{}</description><versionID>{}</versionID><type>label</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy/><creationDateTime>{}</creationDateTime><createdBy/></Version><Attachment><type>techdoc</type><name>{}</name></Attachment><LabelVariant><keyword>{}</keyword><isActive>1</isActive><description>{}</description><height>1</height><length>{}</length><context>3</context><language>2</language></LabelVariant><application>{}</application></DR_Label>"#,
        description, version_id, name, c_time, c_time, name, keyword, description, lbl_len, application
    )
}
