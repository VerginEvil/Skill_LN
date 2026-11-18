use std::sync::OnceLock;
use regex::Regex;
use serde::{Deserialize, Serialize};

pub const XML_DECL_STANDARD: &str = r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#;

fn escape_xml_text(s: &str) -> String {
    s.replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;")
}

fn unescape_xml_text(s: &str) -> String {
    s.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", "\"")
        .replace("&apos;", "'")
        .replace("&amp;", "&")
}

fn cdata_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| Regex::new(r"(?s)<!\[CDATA\[.*?\]\]>").unwrap())
}

fn preserved_tag_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| {
        Regex::new(r"(?s)(<expression\b[^>]*>.*?</expression>|<content\b[^>]*>.*?</content>|<documentation\b[^>]*>.*?</documentation>)").unwrap()
    })
}

fn xml_decl_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| Regex::new(r"(?s)^\s*<\?xml[^?]*\?>\s*").unwrap())
}

fn inter_tag_ws_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| Regex::new(r">\s+<").unwrap())
}

fn inter_tag_nl_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| Regex::new(r">\s*[\r\n]+\s*<").unwrap())
}

fn xml_comment_re() -> &'static Regex {
    static RE: OnceLock<Regex> = OnceLock::new();
    RE.get_or_init(|| Regex::new(r"(?s)<!--.*?-->").unwrap())
}

/// Returns `true` if XML contains inter-tag newlines outside `<![CDATA[...]]>`, `<expression>`, `<content>`, or `<documentation>` blocks.
pub fn has_multiline_outside_script(xml: &str) -> bool {
    let s1 = cdata_re().replace_all(xml, "<__X__/>");
    let stripped = preserved_tag_re().replace_all(&s1, "<__X__/>");
    inter_tag_nl_re().is_match(&stripped)
}

/// Compacts TDE component XML to single-line with `standalone="no"` header while preserving CDATA/`<expression>`/`<content>`.
pub fn compact_tde_xml(xml: &str) -> String {
    if xml.is_empty() || !xml.contains('<') {
        return xml.to_string();
    }
    let xml = xml.trim_start_matches('\u{FEFF}');
    let mut tokens: Vec<String> = Vec::new();
    // Pass 1: Mask CDATA first so </expression> inside 4GL string literals cannot terminate <expression> prematurely.
    let m1 = cdata_re().replace_all(xml, |caps: &regex::Captures| {
        let idx = tokens.len();
        tokens.push(caps[0].to_string());
        format!("<__LN_CDATA_TOKEN_{idx}__/>")
    });
    let masked = preserved_tag_re().replace_all(&m1, |caps: &regex::Captures| {
        let idx = tokens.len();
        tokens.push(caps[0].to_string());
        format!("<__LN_CDATA_TOKEN_{idx}__/>")
    });
    let no_decl = xml_decl_re().replace(&masked, "");
    let body = inter_tag_ws_re().replace_all(&no_decl, "><").trim().to_string();
    let mut out = format!("{XML_DECL_STANDARD}{body}");
    for idx in (0..tokens.len()).rev() {
        let placeholder = format!("<__LN_CDATA_TOKEN_{idx}__/>");
        out = out.replace(&placeholder, &tokens[idx]);
    }
    out
}

/// Ensures a `<DR_Label>` XML contains a `<LabelVariant>` with the requested `<context>`.
pub fn ensure_label_context_variant(
    xml_content: &str,
    context: u8,
    description: Option<&str>,
) -> (String, bool) {
    let cleaned = xml_comment_re().replace_all(xml_content, "");
    let variant_ctx_re = Regex::new(&format!(
        r"(?s)<LabelVariant\b[^>]*>(?:(?!</LabelVariant>).)*?<context>\s*{context}\s*</context>(?:(?!</LabelVariant>).)*?</LabelVariant>"
    )).unwrap();
    if variant_ctx_re.is_match(&cleaned) {
        let compacted = compact_tde_xml(xml_content);
        let changed = compacted != xml_content;
        return (compacted, changed);
    }

    let desc_re = Regex::new(r"<description>([^<]*)</description>").unwrap();
    let kw_re = Regex::new(r"(?s)<LabelVariant\b[^>]*>.*?<keyword>([^<]*)</keyword>").unwrap();
    let len_re = Regex::new(r"<length>(\d+)</length>").unwrap();

    let raw_desc = description
        .map(|s| s.to_string())
        .or_else(|| desc_re.captures(&cleaned).map(|c| unescape_xml_text(&c[1])))
        .unwrap_or_else(|| "Label".to_string());
    let raw_keyword = kw_re
        .captures(&cleaned)
        .map(|c| unescape_xml_text(&c[1]))
        .unwrap_or_else(|| {
            let kw: String = raw_desc.chars().take(14).collect();
            kw.to_uppercase().trim().to_string()
        });
    let lbl_len = len_re
        .captures(&cleaned)
        .map(|c| c[1].to_string())
        .unwrap_or_else(|| raw_desc.chars().count().max(1).to_string());

    let variant = format!(
        "<LabelVariant><keyword>{}</keyword><isActive>1</isActive><description>{}</description><height>1</height><length>{}</length><context>{}</context><language>2</language></LabelVariant>",
        escape_xml_text(&raw_keyword),
        escape_xml_text(&raw_desc),
        lbl_len,
        context
    );

    let updated = if let Some(idx) = xml_content.rfind("</LabelVariant>") {
        let pos = idx + "</LabelVariant>".len();
        format!("{}{variant}{}", &xml_content[..pos], &xml_content[pos..])
    } else if xml_content.contains("<application>") {
        xml_content.replacen("<application>", &format!("{variant}<application>"), 1)
    } else if xml_content.contains("</DR_Label>") {
        xml_content.replacen("</DR_Label>", &format!("{variant}</DR_Label>"), 1)
    } else {
        return (xml_content.to_string(), false);
    };

    (compact_tde_xml(&updated), true)
}

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

/// Generates standard `<DR_Label>` XML with explicit `<context>` (`1`=field, `2`=session/table, `10`=FormCommand).
pub fn generate_label_xml_with_context(
    name: &str,
    description: &str,
    version_id: &str,
    application: &str,
    length: Option<usize>,
    created_time: Option<&str>,
    context: u8,
) -> String {
    let c_time = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let lbl_len = length.unwrap_or_else(|| description.chars().count().max(1));
    let kw_take: String = description.chars().take(14).collect();
    let keyword = kw_take.to_uppercase().trim().to_string();
    let esc_desc = escape_xml_text(description);
    let esc_ver = escape_xml_text(version_id);
    let esc_name = escape_xml_text(name);
    let esc_kw = escape_xml_text(&keyword);
    let esc_app = escape_xml_text(application);

    format!(
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Label><description>{}</description><versionID>{}</versionID><type>label</type><name>{}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{}</modificationDateTime><modifiedBy/><creationDateTime>{}</creationDateTime><createdBy/></Version><Attachment><type>techdoc</type><name>{}</name></Attachment><LabelVariant><keyword>{}</keyword><isActive>1</isActive><description>{}</description><height>1</height><length>{}</length><context>{}</context><language>2</language></LabelVariant><application>{}</application></DR_Label>"#,
        esc_desc, esc_ver, esc_name, c_time, c_time, esc_name, esc_kw, esc_desc, lbl_len, context, esc_app
    )
}

/// Generates standard `<DR_Label>` XML (default `<context>1</context>`).
pub fn generate_label_xml(
    name: &str,
    description: &str,
    version_id: &str,
    application: &str,
    length: Option<usize>,
    created_time: Option<&str>,
) -> String {
    generate_label_xml_with_context(name, description, version_id, application, length, created_time, 1)
}
