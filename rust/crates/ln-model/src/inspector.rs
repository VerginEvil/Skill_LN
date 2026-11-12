use std::fs::{self, OpenOptions};
use std::io::Write;
use std::path::{Path, PathBuf};
use quick_xml::events::Event;
use quick_xml::Reader;
use serde::{Deserialize, Serialize};
use thiserror::Error;

use crate::schema::{get_tde_schema, lookup_class};

#[derive(Debug, Error)]
pub enum InspectorError {
    #[error("XML parse error: {0}")]
    Xml(#[from] quick_xml::Error),
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Serialization error: {0}")]
    Serde(#[from] serde_json::Error),
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct UnmappedPacket {
    pub timestamp: String,
    pub component: String,
    pub xml_path: String,
    pub unknown_tag: String,
    pub parent_class: String,
}

/// Computes an exact ISO 8601 UTC timestamp string without third-party dependencies.
pub fn current_iso_timestamp() -> String {
    let now = std::time::SystemTime::now();
    let duration = now.duration_since(std::time::UNIX_EPOCH).unwrap_or_default();
    let secs = duration.as_secs();

    let days = secs / 86400;
    let rem_secs = secs % 86400;
    let hours = rem_secs / 3600;
    let mins = (rem_secs % 3600) / 60;
    let s = rem_secs % 60;

    let mut year = 1970;
    let mut d = days;
    loop {
        let leap = if (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) { 1 } else { 0 };
        let days_in_year = 365 + leap;
        if d >= days_in_year {
            d -= days_in_year;
            year += 1;
        } else {
            break;
        }
    }
    let leap = if (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) { 1 } else { 0 };
    let days_in_month = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let mut month = 1;
    for &dim in &days_in_month {
        if d >= dim {
            d -= dim;
            month += 1;
        } else {
            break;
        }
    }
    let day = d + 1;
    format!("{:04}-{:02}-{:02}T{:02}:{:02}:{:02}Z", year, month, day, hours, mins, s)
}

/// Resolves default path for `unmapped_packets.log` under `~/.ln_studio/`.
pub fn default_unmapped_log_path() -> Option<PathBuf> {
    if let Ok(override_path) = std::env::var("LN_UNMAPPED_LOG") {
        return Some(PathBuf::from(override_path));
    }
    dirs::home_dir().map(|h| h.join(".ln_studio").join("unmapped_packets.log"))
}

/// Standard XML / JCA envelope tags and attributes to ignore during unknown tag inspection.
fn is_standard_attribute(attr_name: &str) -> bool {
    let lower = attr_name.to_ascii_lowercase();
    matches!(
        lower.as_str(),
        "xmlns"
            | "version"
            | "name"
            | "package"
            | "module"
            | "language"
            | "xsi:type"
            | "xmlns:xsi"
            | "xmlns:dr"
            | "xmlns:xmi"
            | "xmi:version"
            | "xmlns:scenarios"
            | "xmlns:xsd"
    ) || lower.starts_with("xmlns:")
        || lower.starts_with("xsi:")
        || lower.starts_with("xmi:")
}

fn is_envelope_tag(tag_name: &str) -> bool {
    matches!(
        tag_name,
        "DataArea"
            | "BDE"
            | "Method"
            | "Message"
            | "ControlArea"
            | "Header"
            | "Show"
            | "List"
            | "SpecialList"
            | "expression"
            | "Source"
            | "DR_Module"
            | "owtemplate"
            | "documentation"
            | "package"
            | "module"
            | "nativeDatatype"
            | "Facet"
    )
}

/// Inspects an XML document against `tde_schema_0640.json` without modifying or stripping any node.
/// If unknown XML tags or attributes are found, logs them to `~/.ln_studio/unmapped_packets.log`
/// and returns the detected `UnmappedPacket` list.
pub fn inspect_unknown_nodes(
    xml_content: &str,
    component_name: &str,
    log_to_file: bool,
) -> Result<Vec<UnmappedPacket>, InspectorError> {
    let log_path = if log_to_file { default_unmapped_log_path() } else { None };
    inspect_unknown_nodes_with_log_path(xml_content, component_name, log_path.as_deref())
}

/// Inspects an XML document against `tde_schema_0640.json` with an explicit log path.
pub fn inspect_unknown_nodes_with_log_path(
    xml_content: &str,
    component_name: &str,
    log_path: Option<&Path>,
) -> Result<Vec<UnmappedPacket>, InspectorError> {
    let mut reader = Reader::from_str(xml_content);
    reader.config_mut().trim_text(true);

    let mut unmapped = Vec::new();
    let mut path_stack: Vec<(String, Option<String>)> = Vec::new(); // (tag_name, class_name)
    let timestamp = current_iso_timestamp();

    let mut buf = Vec::new();

    loop {
        match reader.read_event_into(&mut buf)? {
            Event::Start(e) => {
                let raw_name = String::from_utf8_lossy(e.name().as_ref()).to_string();
                let clean_name = raw_name.rsplit(':').next().unwrap_or(&raw_name).to_string();

                let current_path = if path_stack.is_empty() {
                    clean_name.clone()
                } else {
                    let parent_paths: Vec<&str> = path_stack.iter().map(|(p, _)| p.as_str()).collect();
                    format!("{}/{}", parent_paths.join("/"), clean_name)
                };

                let parent_class = path_stack.last().and_then(|(_, c)| c.clone());

                // Check if current tag is known
                let matched_class = resolve_tag_class(&clean_name, parent_class.as_deref());

                if matched_class.is_none() && !is_envelope_tag(&clean_name) {
                    // Check if clean_name is a known field of parent_class
                    let is_parent_field = if let Some(ref p_cls_name) = parent_class {
                        if let Some(p_meta) = lookup_class(p_cls_name) {
                            p_meta.has_field(&clean_name)
                        } else {
                            false
                        }
                    } else {
                        false
                    };

                    if !is_parent_field {
                        unmapped.push(UnmappedPacket {
                            timestamp: timestamp.clone(),
                            component: component_name.to_string(),
                            xml_path: current_path.clone(),
                            unknown_tag: clean_name.clone(),
                            parent_class: parent_class.clone().unwrap_or_else(|| "ROOT".into()),
                        });
                    }
                }

                // Check attributes of tag
                for attr_res in e.attributes() {
                    if let Ok(attr) = attr_res {
                        let attr_name = String::from_utf8_lossy(attr.key.as_ref()).to_string();
                        let clean_attr = attr_name.rsplit(':').next().unwrap_or(&attr_name);

                        if !is_standard_attribute(&attr_name) {
                            let is_known_field = if let Some(ref cur_cls) = matched_class {
                                if let Some(c_meta) = lookup_class(cur_cls) {
                                    c_meta.has_field(clean_attr)
                                } else {
                                    false
                                }
                            } else if let Some(ref p_cls) = parent_class {
                                if let Some(p_meta) = lookup_class(p_cls) {
                                    p_meta.has_field(clean_attr)
                                } else {
                                    false
                                }
                            } else {
                                false
                            };

                            if !is_known_field {
                                unmapped.push(UnmappedPacket {
                                    timestamp: timestamp.clone(),
                                    component: component_name.to_string(),
                                    xml_path: format!("{}/@{}", current_path, clean_attr),
                                    unknown_tag: format!("@{}", clean_attr),
                                    parent_class: matched_class.clone().or_else(|| parent_class.clone()).unwrap_or_else(|| "ROOT".into()),
                                });
                            }
                        }
                    }
                }

                path_stack.push((clean_name, matched_class));
            }
            Event::Empty(e) => {
                let raw_name = String::from_utf8_lossy(e.name().as_ref()).to_string();
                let clean_name = raw_name.rsplit(':').next().unwrap_or(&raw_name).to_string();

                let current_path = if path_stack.is_empty() {
                    clean_name.clone()
                } else {
                    let parent_paths: Vec<&str> = path_stack.iter().map(|(p, _)| p.as_str()).collect();
                    format!("{}/{}", parent_paths.join("/"), clean_name)
                };

                let parent_class = path_stack.last().and_then(|(_, c)| c.clone());
                let matched_class = resolve_tag_class(&clean_name, parent_class.as_deref());

                if matched_class.is_none() && !is_envelope_tag(&clean_name) {
                    let is_parent_field = if let Some(ref p_cls_name) = parent_class {
                        if let Some(p_meta) = lookup_class(p_cls_name) {
                            p_meta.has_field(&clean_name)
                        } else {
                            false
                        }
                    } else {
                        false
                    };

                    if !is_parent_field {
                        unmapped.push(UnmappedPacket {
                            timestamp: timestamp.clone(),
                            component: component_name.to_string(),
                            xml_path: current_path.clone(),
                            unknown_tag: clean_name.clone(),
                            parent_class: parent_class.clone().unwrap_or_else(|| "ROOT".into()),
                        });
                    }
                }

                // Check attributes of empty tag
                for attr_res in e.attributes() {
                    if let Ok(attr) = attr_res {
                        let attr_name = String::from_utf8_lossy(attr.key.as_ref()).to_string();
                        let clean_attr = attr_name.rsplit(':').next().unwrap_or(&attr_name);

                        if !is_standard_attribute(&attr_name) {
                            let is_known_field = if let Some(ref cur_cls) = matched_class {
                                if let Some(c_meta) = lookup_class(cur_cls) {
                                    c_meta.has_field(clean_attr)
                                } else {
                                    false
                                }
                            } else if let Some(ref p_cls) = parent_class {
                                if let Some(p_meta) = lookup_class(p_cls) {
                                    p_meta.has_field(clean_attr)
                                } else {
                                    false
                                }
                            } else {
                                false
                            };

                            if !is_known_field {
                                unmapped.push(UnmappedPacket {
                                    timestamp: timestamp.clone(),
                                    component: component_name.to_string(),
                                    xml_path: format!("{}/@{}", current_path, clean_attr),
                                    unknown_tag: format!("@{}", clean_attr),
                                    parent_class: matched_class.clone().or_else(|| parent_class.clone()).unwrap_or_else(|| "ROOT".into()),
                                });
                            }
                        }
                    }
                }
            }
            Event::End(_) => {
                path_stack.pop();
            }
            Event::Eof => break,
            _ => {}
        }
        buf.clear();
    }

    // Append to unmapped_packets.log if requested
    if let Some(lp) = log_path {
        if !unmapped.is_empty() {
            if let Some(parent) = lp.parent() {
                let _ = fs::create_dir_all(parent);
            }
            if let Ok(mut file) = OpenOptions::new().create(true).append(true).open(lp) {
                for packet in &unmapped {
                    if let Ok(line) = serde_json::to_string(packet) {
                        let _ = writeln!(file, "{}", line);
                    }
                }
            }
        }
    }

    Ok(unmapped)
}

fn resolve_tag_class(tag_name: &str, parent_class: Option<&str>) -> Option<String> {
    let schema = get_tde_schema();

    // 1. Direct class match
    if schema.classes.contains_key(tag_name) {
        return Some(tag_name.to_string());
    }

    // 2. Try prefix "DR_" or strip "DR_"
    let alt_name = if tag_name.starts_with("DR_") {
        &tag_name[3..]
    } else {
        tag_name
    };
    if schema.classes.contains_key(alt_name) {
        return Some(alt_name.to_string());
    }

    // 3. If parent class exists, check if parent class has a field targeting a known class
    if let Some(p_cls_name) = parent_class {
        if let Some(p_meta) = lookup_class(p_cls_name) {
            if let Some(field) = p_meta.get_field(tag_name) {
                if let Some(ref target) = field.target_type {
                    return Some(target.clone());
                }
            }
        }
    }

    None
}
