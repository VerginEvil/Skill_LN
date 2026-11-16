use std::fs;
use std::path::{Path, PathBuf};
use regex::Regex;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum DomSurgeryError {
    #[error("Could not find <expression> tag in target XML file")]
    ExpressionNotFound,
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Regex error: {0}")]
    Regex(#[from] regex::Error),
}

#[derive(Debug, Error)]
pub enum PrePutGuardError {
    #[error("DomSurgery error: {0}")]
    DomSurgery(#[from] DomSurgeryError),
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("[PRE-PUT GUARDRAIL] Aborted Put for '{comp_name}' ({comp_type}): Outgoing payload contains an empty source <expression>, but a non-empty script exists on disk or in previous XML. Wiping out code on the server is prohibited.")]
    EmptyScriptOverwrite {
        comp_name: String,
        comp_type: String,
    },
}

/// Unescapes XML entities back to plain Baan 4GL source code.
pub fn unescape_xml_to_4gl(xml_text: &str) -> String {
    xml_text
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", "\"")
        .replace("&apos;", "'")
        .replace("&amp;", "&")
}

/// Escapes plain Baan 4GL source code for inclusion in standard XML text node.
pub fn escape_4gl_to_xml(source_code: &str) -> String {
    source_code
        .replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;")
}

/// Extracts the Baan 4GL source code from `<expression>...</expression>` in XML content.
/// Unwraps CDATA if present or unescapes XML entities.
pub fn extract_script(xml_content: &str) -> Option<String> {
    let re = Regex::new(r"(?s)<expression>(.*?)</expression>").ok()?;
    let captures = re.captures(xml_content)?;
    let raw_expr = captures.get(1)?.as_str();
    let stripped = raw_expr.trim();

    if stripped.starts_with("<![CDATA[") && stripped.ends_with("]]>") {
        let inner = &stripped[9..stripped.len() - 3];
        Some(inner.trim().to_string())
    } else {
        Some(unescape_xml_to_4gl(raw_expr).trim().to_string())
    }
}

/// Safely injects 4GL source code into the `<expression>` tag of an existing XML content
/// using Lossless DOM byte-span splicing to preserve 100% of unmapped tags, comments, and ordering.
pub fn inject_script(xml_content: &str, script_code: &str) -> Result<String, DomSurgeryError> {
    let re = Regex::new(r"(?s)<expression>(.*?)</expression>")?;
    if let Some(captures) = re.captures(xml_content) {
        let inner_match = captures.get(1).unwrap();

        let raw_inner = inner_match.as_str();
        let replacement = if raw_inner.contains("<![CDATA[") {
            format!("<![CDATA[\n{}\n]]>", script_code)
        } else {
            // Check if surrounding XML uses CDATA or entity escaping
            // If the script code contains characters needing escaping and CDATA was not used,
            // we can format with CDATA if clean or escape entities.
            // Following Python parity: if CDATA was present, use CDATA; else escape entities.
            escape_4gl_to_xml(script_code)
        };

        let start = inner_match.start();
        let end = inner_match.end();
        let mut result = String::with_capacity(xml_content.len() + replacement.len());
        result.push_str(&xml_content[..start]);
        result.push_str(&replacement);
        result.push_str(&xml_content[end..]);
        Ok(result)
    } else {
        // If no <expression> exists, splice it into <Source> or <DR_Module>
        let cdata_block = format!("<expression><![CDATA[\n{}\n]]></expression>", script_code);
        if let Some(source_idx) = xml_content.find("</Source>") {
            let mut result = String::with_capacity(xml_content.len() + cdata_block.len() + 16);
            result.push_str(&xml_content[..source_idx]);
            result.push_str("  ");
            result.push_str(&cdata_block);
            result.push('\n');
            result.push_str(&xml_content[source_idx..]);
            Ok(result)
        } else if let Some(module_idx) = xml_content.rfind("</DR_Module>") {
            let source_wrapper = format!("  <Source>\n    {}\n  </Source>\n", cdata_block);
            let mut result = String::with_capacity(xml_content.len() + source_wrapper.len() + 16);
            result.push_str(&xml_content[..module_idx]);
            result.push_str(&source_wrapper);
            result.push_str(&xml_content[module_idx..]);
            Ok(result)
        } else if let Some(root_close_idx) = xml_content.rfind("</") {
            // Insert before root closing tag
            let wrapper = if xml_content.contains("<DR_Table")
                || xml_content.contains("<DR_Controller")
                || xml_content.contains("<DR_Session")
            {
                format!(
                    "  <DR_Module>\n    <Source>\n      {}\n    </Source>\n  </DR_Module>\n",
                    cdata_block
                )
            } else {
                format!("  <Source>\n    {}\n  </Source>\n", cdata_block)
            };
            let mut result = String::with_capacity(xml_content.len() + wrapper.len() + 16);
            result.push_str(&xml_content[..root_close_idx]);
            result.push_str(&wrapper);
            result.push_str(&xml_content[root_close_idx..]);
            Ok(result)
        } else {
            Err(DomSurgeryError::ExpressionNotFound)
        }
    }
}

/// Rewrites component identifiers, package, module, and labels across component XML
/// using byte-level replacement while preserving 100% of vendor/unmapped XML tags, comments, and spacing.
pub fn clone_component_xml(
    source_xml: &str,
    source_name: &str,
    target_name: &str,
    source_pkg: &str,
    target_pkg: &str,
    source_mod: Option<&str>,
    target_mod: Option<&str>,
) -> String {
    let mut xml = source_xml.to_string();

    // 1. Rename component name attribute and tag
    let attr_name = format!("name=\"{}\"", source_name);
    let attr_name_repl = format!("name=\"{}\"", target_name);
    xml = xml.replace(&attr_name, &attr_name_repl);

    let tag_name = format!("<name>{}</name>", source_name);
    let tag_name_repl = format!("<name>{}</name>", target_name);
    xml = xml.replace(&tag_name, &tag_name_repl);

    // 2. Rename package attribute and tag
    let attr_pkg = format!("package=\"{}\"", source_pkg);
    let attr_pkg_repl = format!("package=\"{}\"", target_pkg);
    xml = xml.replace(&attr_pkg, &attr_pkg_repl);

    let tag_pkg = format!("<package>{}</package>", source_pkg);
    let tag_pkg_repl = format!("<package>{}</package>", target_pkg);
    xml = xml.replace(&tag_pkg, &tag_pkg_repl);

    // 3. Rename module if provided
    if let (Some(s_mod), Some(t_mod)) = (source_mod, target_mod) {
        let attr_mod = format!("module=\"{}\"", s_mod);
        let attr_mod_repl = format!("module=\"{}\"", t_mod);
        xml = xml.replace(&attr_mod, &attr_mod_repl);

        let tag_mod = format!("<module>{}</module>", s_mod);
        let tag_mod_repl = format!("<module>{}</module>", t_mod);
        xml = xml.replace(&tag_mod, &tag_mod_repl);
    }

    // 4. Rename label references: label="source_name.X" -> label="target_name.X"
    if let Ok(lbl_attr_re) = Regex::new(&format!(r#"label="{}\.([A-Za-z0-9_]+)""#, regex::escape(source_name))) {
        xml = lbl_attr_re.replace_all(&xml, format!(r#"label="{}.$1""#, target_name)).to_string();
    }
    if let Ok(dref_attr_re) = Regex::new(&format!(r#"descriptionReference="{}\.([A-Za-z0-9_]+)""#, regex::escape(source_name))) {
        xml = dref_attr_re.replace_all(&xml, format!(r#"descriptionReference="{}.$1""#, target_name)).to_string();
    }
    if let Ok(flbl_attr_re) = Regex::new(&format!(r#"fieldLabel="{}\.([A-Za-z0-9_]+)""#, regex::escape(source_name))) {
        xml = flbl_attr_re.replace_all(&xml, format!(r#"fieldLabel="{}.$1""#, target_name)).to_string();
    }
    if let Ok(dref_tag_re) = Regex::new(&format!(r#"<descriptionReference>{}\.([A-Za-z0-9_]+)</descriptionReference>"#, regex::escape(source_name))) {
        xml = dref_tag_re.replace_all(&xml, format!(r#"<descriptionReference>{}.$1</descriptionReference>"#, target_name)).to_string();
    }
    if let Ok(flbl_tag_re) = Regex::new(&format!(r#"<fieldLabel>{}\.([A-Za-z0-9_]+)</fieldLabel>"#, regex::escape(source_name))) {
        xml = flbl_tag_re.replace_all(&xml, format!(r#"<fieldLabel>{}.$1</fieldLabel>"#, target_name)).to_string();
    }

    xml
}

/// Finds any standalone script file associated with component in the activity directory.
pub fn find_standalone_script_file(
    activity_dir: &Path,
    comp_name: &str,
    comp_type: &str,
) -> Option<PathBuf> {
    let script_exts = match comp_type.to_lowercase().as_str() {
        "table" => vec![".dal", ".4gl"],
        "session" => vec![".cln", ".4gl", ".src"],
        "library" => vec![".lib", ".4gl"],
        "function" => vec![".fnc", ".4gl"],
        "report" => vec![".4gl", ".src"],
        _ => vec![".4gl", ".dal", ".cln", ".src", ".lib"],
    };

    // Check direct path or recursive search in activity_dir
    for ext in &script_exts {
        let direct_candidate = activity_dir.join(format!("{}{}", comp_name, ext));
        if direct_candidate.is_file() {
            return Some(direct_candidate);
        }
    }

    // Recursively walk activity directory for matching script file
    if let Ok(entries) = walk_dir_find(activity_dir, comp_name, &script_exts) {
        if let Some(p) = entries.into_iter().next() {
            return Some(p);
        }
    }

    None
}

fn walk_dir_find(dir: &Path, base_name: &str, exts: &[&str]) -> Result<Vec<PathBuf>, std::io::Error> {
    let mut matches = Vec::new();
    if !dir.is_dir() {
        return Ok(matches);
    }
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let p = entry.path();
        if p.is_dir() {
            if let Some(name) = p.file_name().and_then(|n| n.to_str()) {
                if !name.starts_with('.') {
                    matches.extend(walk_dir_find(&p, base_name, exts)?);
                }
            }
        } else if p.is_file() {
            if let Some(stem) = p.file_stem().and_then(|s| s.to_str()) {
                if stem.eq_ignore_ascii_case(base_name) {
                    if let Some(ext) = p.extension().and_then(|e| e.to_str()) {
                        let dot_ext = format!(".{}", ext);
                        if exts.iter().any(|e| e.eq_ignore_ascii_case(&dot_ext)) {
                            matches.push(p);
                        }
                    }
                }
            }
        }
    }
    Ok(matches)
}

/// Pre-Put Script Merge & Non-Empty Source Guardrail:
/// 1. If standalone script exists and is newer or different, merges it into the target XML.
/// 2. Validates Non-Empty Source Guardrail: if component is script-bearing and the source expression is
///    empty while an existing script existed on disk or in prior XML, aborts with `EmptyScriptOverwrite`
///    to prevent wiping out server code.
/// 3. Writes merged XML back to target_file and returns the final XML content string.
pub fn pre_put_merge_and_guard(
    target_xml_path: &Path,
    comp_name: &str,
    comp_type: &str,
    activity_dir: &Path,
) -> Result<String, PrePutGuardError> {
    let mut xml_content = fs::read_to_string(target_xml_path)?;
    let prior_script = extract_script(&xml_content);

    let script_file = find_standalone_script_file(activity_dir, comp_name, comp_type);
    let mut has_standalone = false;
    let mut standalone_code = String::new();

    if let Some(ref sf) = script_file {
        if sf.is_file() {
            if let Ok(code) = fs::read_to_string(sf) {
                if !code.trim().is_empty() {
                    has_standalone = true;
                    standalone_code = code;
                }
            }
        }
    }

    if has_standalone {
        let prior_trimmed = prior_script.as_deref().unwrap_or("").trim();
        let standalone_trimmed = standalone_code.trim();

        let is_different = prior_trimmed != standalone_trimmed;
        let is_newer = if let (Ok(meta_sf), Ok(meta_xf)) = (
            fs::metadata(script_file.as_ref().unwrap()),
            fs::metadata(target_xml_path),
        ) {
            meta_sf.modified().unwrap_or(std::time::UNIX_EPOCH)
                >= meta_xf.modified().unwrap_or(std::time::UNIX_EPOCH)
        } else {
            false
        };

        if is_different || is_newer {
            xml_content = inject_script(&xml_content, &standalone_code)?;
            fs::write(target_xml_path, &xml_content)?;
        }
    }

    // Non-Empty Source Guardrail
    let ctype_lower = comp_type.to_lowercase();
    let current_script = extract_script(&xml_content);
    let is_empty = current_script.as_deref().unwrap_or("").trim().is_empty();

    if is_empty {
        let had_prior = (prior_script.is_some() && !prior_script.as_deref().unwrap().trim().is_empty())
            || has_standalone;
        let is_prohibited = matches!(
            ctype_lower.as_str(),
            "session" | "library" | "function" | "report"
        ) || (ctype_lower == "table" && had_prior);

        if is_prohibited {
            return Err(PrePutGuardError::EmptyScriptOverwrite {
                comp_name: comp_name.to_string(),
                comp_type: comp_type.to_string(),
            });
        }
    }

    Ok(xml_content)
}
