use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LibrarySpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default = "default_lib_type")]
    pub library_type: String, // "dll", "table_extension", "session_extension"
    #[serde(default)]
    pub target: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub script: Option<String>,
}

fn default_lib_type() -> String {
    "dll".to_string()
}

/// Generates standard `<DR_Module>` .lib XML for DLL, ess, or est.
pub fn generate_library_xml(
    spec: &LibrarySpec,
    application: &str,
    default_version_id: &str,
    created_time: Option<&str>,
) -> String {
    let now_iso = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let code = &spec.code;
    let l_type = spec.library_type.to_lowercase();
    let source_type = if l_type == "session_extension" { "8" } else { "6" };

    let script_code = if let Some(ref s) = spec.script {
        s.clone()
    } else {
        format!("| DLL: {code}\nfunction extern long {code}.init()\n{{\n\treturn(0)\n}}\n")
    };

    let escaped_script = script_code
        .replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;");

    let mut attachments = format!("<Attachment><type>techdoc</type><name>{code}</name></Attachment>");
    if l_type != "session_extension" {
        attachments = format!("<Attachment><type>relnotes</type><name>{code}</name></Attachment>{attachments}");
    }

    let extra_constraints = if l_type != "session_extension" {
        "<additionalConstraints>2610</additionalConstraints><additionalInstructions/><keyword>||</keyword>"
    } else {
        ""
    };

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Module><description>{}</description><versionID>{}</versionID><type>library</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{}</creationDateTime><createdBy>agent</createdBy></Version><Source><sourceVersion><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{}</creationDateTime><createdBy>agent</createdBy></sourceVersion><sourceVersionID>{}</sourceVersionID><sourceObjectID>1</sourceObjectID><expression>{}</expression><expressionLanguageType>Baan4C</expressionLanguageType><sourceType>{}</sourceType><sourceDescription>{}</sourceDescription><sourceName>{}</sourceName></Source><documentation/>{}{}<application>{}</application></DR_Module>"#,
        desc, ver, code, now_iso, now_iso, now_iso, now_iso, ver, escaped_script, source_type, desc, code, attachments, extra_constraints, application
    )
}
