use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MessageSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default = "default_severity")]
    pub severity: String, // 1 = Info, 2 = Warning, 3 = Error
    #[serde(default)]
    pub text: Option<String>,
    #[serde(default = "default_language")]
    pub language: usize, // 2 = English
}

fn default_severity() -> String {
    "3".to_string()
}

fn default_language() -> usize {
    2
}

/// Generates standard `<DR_Message>` XML matching Infor LN Studio 10.8.
pub fn generate_message_xml(
    spec: &MessageSpec,
    application: &str,
    default_version_id: &str,
) -> String {
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let text = spec.text.as_deref().unwrap_or(desc);
    let code = &spec.code;
    let severity = &spec.severity;
    let lang = spec.language;

    let lines = [
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#,
        r#"<DR_Message xmlns="http://www.infor.com/businessline/application/dr" version="1.0">"#,
        &format!("  <description>{desc}</description>"),
        &format!("  <versionID>{ver}</versionID>"),
        "  <type>message</type>",
        &format!("  <name>{code}</name>"),
        &format!("  <severity>{severity}</severity>"),
        "  <hasHelp>false</hasHelp>",
        "  <MessageTranslation>",
        &format!("    <language>{lang}</language>"),
        &format!("    <text>{text}</text>"),
        "  </MessageTranslation>",
        &format!("  <application>{app}</application>"),
        "</DR_Message>",
    ];

    lines.join("\n") + "\n"
}
