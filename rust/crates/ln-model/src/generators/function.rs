use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FunctionSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub script: Option<String>,
}

/// Generates standard `<DR_Module>` .fnc XML for an Include Function.
pub fn generate_function_xml(
    spec: &FunctionSpec,
    application: &str,
    default_version_id: &str,
) -> String {
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;
    let default_script = format!("| Function: {code}\nfunction extern void {code}_init()\n{{\n}}\n");
    let script = spec.script.as_deref().unwrap_or(&default_script);

    let lines = [
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#,
        r#"<DR_Module xmlns="http://www.infor.com/businessline/application/dr" version="1.0">"#,
        &format!("  <description>{desc}</description>"),
        &format!("  <versionID>{ver}</versionID>"),
        "  <type>function</type>",
        &format!("  <name>{code}</name>"),
        "  <Source>",
        &format!("    <expression><![CDATA[{script}]]></expression>"),
        "    <sourceType>6</sourceType>",
        &format!("    <sourceName>{code}</sourceName>"),
        "  </Source>",
        &format!("  <application>{app}</application>"),
        "</DR_Module>",
    ];

    lines.join("\n") + "\n"
}
