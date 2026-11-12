use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AdditionalFileSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub content: Option<String>,
    #[serde(default)]
    pub keyword1: Option<String>,
    #[serde(default)]
    pub keyword2: Option<String>,
    #[serde(default)]
    pub keyword3: Option<String>,
}

/// Generates standard `<DR_AdditionalFile>` .add XML.
pub fn generate_additional_xml(
    spec: &AdditionalFileSpec,
    application: &str,
    default_version_id: &str,
) -> String {
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;
    let content = spec.content.as_deref().unwrap_or("");
    let kw1 = spec.keyword1.as_deref().unwrap_or("");
    let kw2 = spec.keyword2.as_deref().unwrap_or("");
    let kw3 = spec.keyword3.as_deref().unwrap_or("");

    let lines = [
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#,
        r#"<DR_AdditionalFile xmlns="http://www.infor.com/businessline/application/dr" version="1.0">"#,
        &format!("  <description>{desc}</description>"),
        &format!("  <versionID>{ver}</versionID>"),
        "  <type>additional</type>",
        &format!("  <name>{code}</name>"),
        "  <isEditable>true</isEditable>",
        &format!("  <keyword1>{kw1}</keyword1>"),
        &format!("  <keyword2>{kw2}</keyword2>"),
        &format!("  <keyword3>{kw3}</keyword3>"),
        "  <includeContent>true</includeContent>",
        "  <FileContent>",
        &format!("    <content><![CDATA[{content}]]></content>"),
        "  </FileContent>",
        &format!("  <application>{app}</application>"),
        "</DR_AdditionalFile>",
    ];

    lines.join("\n") + "\n"
}
