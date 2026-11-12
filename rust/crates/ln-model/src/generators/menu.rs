use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MenuChoiceSpec {
    #[serde(default = "default_choice_pos")]
    pub position: usize,
    #[serde(default = "default_choice_type")]
    pub choice_type: String, // "session" or "menu"
    #[serde(default)]
    pub target: String,
    #[serde(default)]
    pub description: Option<String>,
}

fn default_choice_pos() -> usize {
    10
}

fn default_choice_type() -> String {
    "session".to_string()
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MenuSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub choices: Vec<MenuChoiceSpec>,
}

/// Generates standard `<DR_Menu>` XML matching Infor LN Studio 10.8.
pub fn generate_menu_xml(
    spec: &MenuSpec,
    application: &str,
    default_version_id: &str,
    created_time: Option<&str>,
) -> String {
    let now_iso = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;

    let mut choices_xml = String::new();
    for ch in &spec.choices {
        let ch_pos = ch.position;
        let ch_type = if ch.choice_type.to_lowercase() == "session" { 1 } else { 2 };
        let ch_target = &ch.target;
        let ch_desc = ch.description.as_deref().unwrap_or(ch_target);

        choices_xml.push_str(&format!(
            "<MenuChoice><descriptionReference/><description>{ch_desc}</description><initialHidden>false</initialHidden><filterFunction/><filterLibrary/><isActive>true</isActive><processInfo/><menuFieldName>{ch_target}</menuFieldName><menuFieldType>{ch_type}</menuFieldType><descriptionIsLinked>true</descriptionIsLinked><position>{ch_pos}</position></MenuChoice>"
        ));
    }

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Menu><description>{}</description><versionID>{}</versionID><type>menu</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy/><creationDateTime>{}</creationDateTime><createdBy>agent</createdBy></Version><descriptionReference>{}</descriptionReference>{}<Attachment><type>relnotes</type><name>{}</name></Attachment><Attachment><type>techdoc</type><name>{}</name></Attachment><documentation/><application>{}</application></DR_Menu>"#,
        desc, ver, code, now_iso, now_iso, code, choices_xml, code, code, app
    )
}
