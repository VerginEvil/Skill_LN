use std::collections::HashMap;
use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use ln_eclipse_compat::AdminFile;
use ln_jca::bde_manager::{BdeExecutionMode, BdeParams, JcaBdeManager};
use ln_jca::client::HttpClient;
use ln_jca::error::JcaError;
use ln_jca::filter::{BdeFilter, BdeSelection};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct BdeTypeInfo {
    pub bde: &'static str,
    pub ext: &'static str,
    pub subfolder: &'static str,
    pub type_attr: Option<&'static str>,
    pub readonly_only: bool,
}

pub fn get_bde_type_info(comp_type: &str) -> Option<BdeTypeInfo> {
    match comp_type.trim().to_lowercase().as_str() {
        "table" => Some(BdeTypeInfo { bde: "DR_Table", ext: ".tbl", subfolder: "tables", type_attr: None, readonly_only: false }),
        "session" => Some(BdeTypeInfo { bde: "DR_Controller", ext: ".ses", subfolder: "sessions", type_attr: None, readonly_only: false }),
        "library" => Some(BdeTypeInfo { bde: "DR_Module", ext: ".lib", subfolder: "libraries", type_attr: Some("library"), readonly_only: false }),
        "extension" => Some(BdeTypeInfo { bde: "DR_Module", ext: ".lib", subfolder: "extensions", type_attr: Some("extension"), readonly_only: true }),
        "function" => Some(BdeTypeInfo { bde: "DR_Module", ext: ".fnc", subfolder: "functions", type_attr: Some("function"), readonly_only: false }),
        "domain" => Some(BdeTypeInfo { bde: "DR_Domain", ext: ".dmn", subfolder: "domains", type_attr: None, readonly_only: false }),
        "label" => Some(BdeTypeInfo { bde: "DR_Label", ext: ".lbl", subfolder: "labels", type_attr: None, readonly_only: false }),
        "report" => Some(BdeTypeInfo { bde: "DR_Report", ext: ".rpt", subfolder: "reports", type_attr: None, readonly_only: false }),
        "message" => Some(BdeTypeInfo { bde: "DR_Message", ext: ".msg", subfolder: "messages", type_attr: None, readonly_only: false }),
        "question" => Some(BdeTypeInfo { bde: "DR_Question", ext: ".qst", subfolder: "questions", type_attr: None, readonly_only: false }),
        "menu" => Some(BdeTypeInfo { bde: "DR_Menu", ext: ".mnu", subfolder: "menus", type_attr: None, readonly_only: false }),
        "additional" => Some(BdeTypeInfo { bde: "DR_AdditionalFile", ext: ".add", subfolder: "additional_files", type_attr: None, readonly_only: false }),
        _ => None,
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ExtensionResolution {
    pub library_name: String,
    pub ext_type: String,
    pub target_code: String,
    pub component_type: String,
    pub is_extension: bool,
}

/// Deterministically resolves standard table/session codes to Extension Modeler library names
/// and vice-versa (ADR 0006, 0014).
pub fn resolve_extension_component_name(comp_name: &str, comp_type: &str) -> ExtensionResolution {
    let clean = comp_name.trim().to_lowercase();
    let ctype = comp_type.trim().to_lowercase();

    if clean.starts_with("txest") {
        return ExtensionResolution {
            library_name: clean.clone(),
            ext_type: "est".to_string(),
            target_code: if clean.len() > 5 { clean[5..].to_string() } else { String::new() },
            component_type: "table".to_string(),
            is_extension: true,
        };
    }
    if clean.starts_with("txess") {
        let mod_code = if clean.len() > 5 { clean[5..].to_string() } else { String::new() };
        return ExtensionResolution {
            library_name: clean,
            ext_type: "ess".to_string(),
            target_code: mod_code,
            component_type: "session".to_string(),
            is_extension: true,
        };
    }
    if clean.starts_with("txesb") || clean.starts_with("txesm") || clean.starts_with("txesr") {
        let ext_type = if clean.len() >= 5 { clean[2..5].to_string() } else { "ess".to_string() };
        return ExtensionResolution {
            library_name: clean.clone(),
            ext_type,
            target_code: clean,
            component_type: "extension".to_string(),
            is_extension: true,
        };
    }

    let is_table_code = (clean.len() == 8 && clean[5..].chars().all(|c| c.is_ascii_digit())) || ctype == "table";
    let is_session_code = (clean.len() >= 12 && (clean.contains('m') || clean.contains('s'))) || ctype == "session";

    if (ctype == "extension" || ctype.is_empty()) && is_table_code && !is_session_code {
        ExtensionResolution {
            library_name: format!("txest{clean}"),
            ext_type: "est".to_string(),
            target_code: clean,
            component_type: "table".to_string(),
            is_extension: true,
        }
    } else if (ctype == "extension" || ctype.is_empty()) && is_session_code {
        let session_body = if clean.len() > 2 { &clean[2..] } else { clean.as_str() };
        let lib_name = if session_body.len() >= 3 {
            let mod_part = &session_body[..3];
            let code_part = &session_body[3..];
            let pos = code_part.find('m').or_else(|| code_part.find('s'));
            if let Some(p) = pos {
                let end = (p + 2).min(code_part.len());
                format!("txess{mod_part}{}", &code_part[..end])
            } else {
                format!("txess{session_body}")
            }
        } else {
            format!("txess{session_body}")
        };
        ExtensionResolution {
            library_name: lib_name,
            ext_type: "ess".to_string(),
            target_code: clean,
            component_type: "session".to_string(),
            is_extension: true,
        }
    } else if ctype == "extension" {
        ExtensionResolution {
            library_name: clean.clone(),
            ext_type: "ess".to_string(),
            target_code: clean,
            component_type: "extension".to_string(),
            is_extension: true,
        }
    } else {
        ExtensionResolution {
            library_name: clean.clone(),
            ext_type: String::new(),
            target_code: clean,
            component_type: ctype,
            is_extension: false,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct BrowsedComponent {
    pub name: String,
    pub comp_type: String,
    pub package: String,
    pub module: String,
    pub description: String,
    pub version_id: String,
    pub is_checked_out: String,
    pub is_expired: String,
}

/// Browses server components using `StudioComponent.GetBrowseList` BDE in `BROWSELIST` mode
/// with Controlling Attributes, selection fields, and filter expression.
pub async fn browse_components(
    client: &HttpClient,
    package: &str,
    comp_type: &str,
    name_filter: &str,
    connection_point: &str,
) -> Result<Vec<BrowsedComponent>, JcaError> {
    let ctype = if comp_type.is_empty() { "table" } else { comp_type }.to_lowercase();
    let bde_name = get_bde_type_info(&ctype).map(|i| i.bde).unwrap_or("DR_Table");

    let mut ctrl_attrs = HashMap::new();
    ctrl_attrs.insert("GetBrowseList;package;in;false".to_string(), package.to_string());
    ctrl_attrs.insert("GetBrowseList;type;in;false".to_string(), ctype.clone());
    ctrl_attrs.insert("GetBrowseList;includeExpired;in;false".to_string(), "no".to_string());
    ctrl_attrs.insert("GetBrowseList;includeProjectLock;in;false".to_string(), "yes".to_string());

    let mut selection = BdeSelection::new();
    selection.add(&format!("{bde_name}.name"));
    selection.add(&format!("{bde_name}.description"));
    selection.add(&format!("{bde_name}.additionalInfo"));
    selection.add(&format!("{bde_name}.type"));
    selection.add(&format!("{bde_name}.versionID"));
    selection.add(&format!("{bde_name}.Version.isExpired"));
    selection.add(&format!("{bde_name}.Version.isCheckedOut"));
    selection.add(&format!("{bde_name}.Version.isCheckedOutParallel"));

    let filter = if !name_filter.is_empty() {
        Some(BdeFilter::from_raw(&format!("{bde_name}.name LIKE '{name_filter}'")))
    } else {
        None
    };

    let cp = if connection_point.is_empty() { "ProjectServer" } else { connection_point };
    let mgr = JcaBdeManager::new(client, cp);

    let params = BdeParams {
        bde_name: "StudioComponent".to_string(),
        method_name: "GetBrowseList".to_string(),
        mode: Some(BdeExecutionMode::BrowseList),
        request_xml: None,
        selection: Some(selection),
        filter,
        controlling_attributes: ctrl_attrs,
        ..Default::default()
    };

    let resp_xml = match mgr.execute(&params).await {
        Ok(res) => res,
        Err(_) => {
            // Fallback XML request
            let mut req_parts = String::from("<StudioComponent><GetBrowseListRequest>");
            if !package.is_empty() {
                req_parts.push_str(&format!("<package>{package}</package>"));
            }
            if !comp_type.is_empty() {
                req_parts.push_str(&format!("<type>{comp_type}</type>"));
            }
            if !name_filter.is_empty() {
                req_parts.push_str(&format!("<filter>{name_filter}</filter>"));
            }
            req_parts.push_str("</GetBrowseListRequest></StudioComponent>");

            let fb_params = BdeParams {
                bde_name: "StudioComponent".to_string(),
                method_name: "GetBrowseList".to_string(),
                mode: Some(BdeExecutionMode::Bde),
                request_xml: Some(req_parts),
                ..Default::default()
            };
            mgr.execute(&fb_params).await?
        }
    };

    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;
    let mut components = Vec::new();

    let candidates = if let Some(da) = tree.find_first("DataArea") {
        da.children.iter().collect::<Vec<_>>()
    } else {
        let comps = tree.find_all("Component");
        if !comps.is_empty() {
            comps
        } else {
            tree.children.iter().filter(|c| c.tag != "ControlArea" && c.tag != "Header").collect::<Vec<_>>()
        }
    };

    for elem in candidates {
        let name = elem.child_text("name")
            .or_else(|| elem.child_text("Name"))
            .or_else(|| elem.attr("name"))
            .unwrap_or_default()
            .to_string();
        let item_type = elem.child_text("type")
            .or_else(|| elem.child_text("Type"))
            .or_else(|| elem.attr("type"))
            .unwrap_or(&ctype)
            .to_string();
        let pkg = elem.child_text("package")
            .or_else(|| elem.child_text("Package"))
            .or_else(|| elem.attr("package"))
            .unwrap_or_else(|| if name.len() >= 2 { &name[..2] } else { "" })
            .to_string();
        let mod_code = elem.child_text("module")
            .or_else(|| elem.child_text("Module"))
            .or_else(|| elem.attr("module"))
            .unwrap_or_else(|| if name.len() >= 5 { &name[2..5] } else { "" })
            .to_string();
        let desc = elem.child_text("description")
            .or_else(|| elem.child_text("Description"))
            .or_else(|| elem.attr("description"))
            .unwrap_or_default()
            .to_string();
        let ver_id = elem.child_text("versionID")
            .or_else(|| elem.attr("versionID"))
            .unwrap_or_default()
            .to_string();
        let is_co = elem.find_text("isCheckedOut")
            .or_else(|| elem.attr("isCheckedOut"))
            .unwrap_or("no")
            .to_string();
        let is_exp = elem.find_text("isExpired")
            .or_else(|| elem.attr("isExpired"))
            .unwrap_or("no")
            .to_string();

        if !name.is_empty() {
            components.push(BrowsedComponent {
                name,
                comp_type: item_type,
                package: pkg,
                module: mod_code,
                description: desc,
                version_id: ver_id,
                is_checked_out: is_co,
                is_expired: is_exp,
            });
        }
    }

    Ok(components)
}

/// Fetches component source XML using authentic `StudioComponent.GetActivitySource` / `StudioComponent.GetProjectSource`
/// with graceful fallback to `CmGet` or `Get`.
pub async fn fetch_component_xml(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    connection_point: &str,
    context_xml: Option<&str>,
    base_vrc: Option<&str>,
) -> Result<String, JcaError> {
    let ctype_lower = comp_type.to_lowercase();
    let info = get_bde_type_info(&ctype_lower)
        .ok_or_else(|| JcaError::Protocol(format!("Unsupported component type '{comp_type}'")))?;

    let bde_name = info.bde;
    let eff_vrc = base_vrc.unwrap_or("B61O_a_ext");
    let cp = if connection_point.is_empty() { "ProjectServer" } else { connection_point };
    let mgr = JcaBdeManager::new(client, cp);

    let method = if context_xml.is_some() { "GetActivitySource" } else { "GetProjectSource" };
    let eff_type = if ctype_lower == "extension" || comp_name.to_lowercase().starts_with("txes") {
        "library"
    } else {
        &ctype_lower
    };

    let req_xml = format!(
        "<StudioComponent>\n\
        \x20 <type>{eff_type}</type>\n\
        \x20 <name>{comp_name}</name>\n\
        \x20 <versionID>{eff_vrc}</versionID>\n\
        </StudioComponent>"
    );

    let params = BdeParams {
        bde_name: "StudioComponent".to_string(),
        method_name: method.to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml: context_xml.map(|s| s.to_string()),
        ..Default::default()
    };

    if let Ok(resp) = mgr.execute(&params).await {
        if !resp.is_empty() && (resp.contains('<') || resp.contains("DR_")) {
            return Ok(resp);
        }
    }

    // Fallback 1: CmGet on bde_name
    let cm_req = format!(
        "<{bde_name}>\n\
        \x20 <name>{comp_name}</name>\n\
        \x20 <type>{ctype_lower}</type>\n\
        \x20 <includeCustomerFields>yes</includeCustomerFields>\n\
        \x20 <optionalContent>yes</optionalContent>\n\
        </{bde_name}>"
    );

    let cm_params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "CmGet".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(cm_req),
        context_xml: context_xml.map(|s| s.to_string()),
        ..Default::default()
    };

    if let Ok(resp) = mgr.execute(&cm_params).await {
        if !resp.is_empty() && (resp.contains('<') || resp.contains("DR_")) {
            return Ok(resp);
        }
    }

    // Fallback 2: Get on bde_name
    let (pkg, mod_code, _) = ln_model::path_resolver::split_component_name(comp_name);
    let legacy_req = format!(
        "<{bde_name}>\n\
        \x20 <GetRequest>\n\
        \x20   <name>{comp_name}</name>\n\
        \x20   <package>{pkg}</package>\n\
        \x20   <module>{mod_code}</module>\n\
        \x20 </GetRequest>\n\
        </{bde_name}>"
    );

    let legacy_params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "Get".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(legacy_req),
        context_xml: context_xml.map(|s| s.to_string()),
        ..Default::default()
    };

    mgr.execute(&legacy_params).await
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DdField {
    pub name: String,
    pub domain: String,
    pub datatype: String,
    pub max_length: String,
    pub mandatory: bool,
    pub label: String,
    pub description: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DdEnum {
    pub position: String,
    pub description: String,
    pub label: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DdTableEntry {
    pub name: String,
    pub description: String,
    pub fields: HashMap<String, DdField>,
    pub indices: HashMap<String, Vec<String>>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DdDomainEntry {
    pub name: String,
    pub description: String,
    pub datatype: String,
    pub facets: HashMap<String, String>,
    pub enums: HashMap<String, DdEnum>,
    pub enum_values: Vec<String>,
}

pub enum ParsedDdResult {
    Table(DdTableEntry, HashMap<String, serde_json::Value>),
    Domain(DdDomainEntry),
}

/// Parses `.tbl` (`<DR_Table>`) or `.dmn` (`<DR_Domain>`) XML document into a structured Data Dictionary cache entry.
pub fn parse_dd_xml_to_entry(xml_content: &str, hint_name: &str) -> Option<ParsedDdResult> {
    let tree = parse_xml_to_tree(xml_content).ok()?;
    let root_tag = tree.tag.to_lowercase();

    if root_tag == "dr_table" {
        let tbl_name = tree.attr("name")
            .or_else(|| tree.child_text("name"))
            .unwrap_or(hint_name)
            .trim()
            .to_lowercase();

        if tbl_name.is_empty() {
            return None;
        }

        let desc = tree.child_text("description").or_else(|| tree.attr("description")).unwrap_or_default().to_string();
        let mut fields = HashMap::new();
        let mut inferred_domains = HashMap::new();

        // 1. Real Ecore <Column> elements
        for col in tree.find_all("Column") {
            let c_name = col.attr("name").or_else(|| col.child_text("name")).unwrap_or_default().trim().to_lowercase();
            if c_name.is_empty() {
                continue;
            }
            let mut dmn_name = String::new();
            let mut native_dt = String::new();
            let mut max_len = String::new();

            if let Some(dt) = col.find_first("datatype") {
                dmn_name = dt.child_text("name").or_else(|| dt.attr("name")).unwrap_or_default().trim().to_string();
                native_dt = dt.child_text("nativeDatatype").or_else(|| dt.attr("nativeDatatype")).unwrap_or_default().trim().to_string();
                for facet in dt.find_all("Facet") {
                    if facet.child_text("type").unwrap_or_default() == "maxLength" {
                        max_len = facet.child_text("value").unwrap_or_default().trim().to_string();
                    }
                }
            }
            if dmn_name.is_empty() {
                dmn_name = col.attr("domain").or_else(|| col.child_text("domain")).unwrap_or_default().trim().to_string();
            }
            let c_desc = col.child_text("description").or_else(|| col.attr("description")).unwrap_or_default().trim().to_string();
            let c_lbl = col.child_text("descriptionReference")
                .or_else(|| col.child_text("fieldLabel"))
                .or_else(|| col.attr("label"))
                .or_else(|| col.child_text("label"))
                .unwrap_or_default()
                .trim()
                .to_string();
            let is_mand = col.child_text("isMandatory")
                .or_else(|| col.attr("mandatory"))
                .map(|v| v.eq_ignore_ascii_case("true"))
                .unwrap_or(false);

            fields.insert(c_name.clone(), DdField {
                name: c_name,
                domain: dmn_name.clone(),
                datatype: native_dt.clone(),
                max_length: max_len,
                mandatory: is_mand,
                label: c_lbl,
                description: c_desc,
            });

            if !dmn_name.is_empty() {
                inferred_domains.insert(
                    dmn_name.to_lowercase(),
                    serde_json::json!({
                        "name": dmn_name.to_lowercase(),
                        "datatype": native_dt,
                        "inferred_from_table": tbl_name,
                    }),
                );
            }
        }

        // 2. Legacy/mock <Field> elements
        for fld in tree.find_all("Field") {
            let f_name = fld.attr("name").or_else(|| fld.child_text("name")).unwrap_or_default().trim().to_lowercase();
            if f_name.is_empty() || fields.contains_key(&f_name) {
                continue;
            }
            let dmn_name = fld.attr("domain").or_else(|| fld.child_text("domain")).unwrap_or_default().trim().to_string();
            let native_dt = fld.attr("type").or_else(|| fld.child_text("type")).unwrap_or_default().trim().to_string();
            let c_lbl = fld.attr("label").or_else(|| fld.child_text("label")).unwrap_or_default().trim().to_string();
            let is_mand = fld.attr("mandatory").map(|v| v.eq_ignore_ascii_case("true")).unwrap_or(false);
            let c_desc = fld.attr("description").or_else(|| fld.child_text("description")).unwrap_or_default().trim().to_string();

            fields.insert(f_name.clone(), DdField {
                name: f_name,
                domain: dmn_name.clone(),
                datatype: native_dt.clone(),
                max_length: String::new(),
                mandatory: is_mand,
                label: c_lbl,
                description: c_desc,
            });

            if !dmn_name.is_empty() {
                inferred_domains.insert(
                    dmn_name.to_lowercase(),
                    serde_json::json!({
                        "name": dmn_name.to_lowercase(),
                        "datatype": native_dt,
                        "inferred_from_table": tbl_name,
                    }),
                );
            }
        }

        let mut indices = HashMap::new();
        for (idx_pos, idx) in tree.find_all("Index").iter().enumerate() {
            let idx_name = idx.attr("name")
                .or_else(|| idx.attr("number"))
                .or_else(|| idx.child_text("name"))
                .unwrap_or(&format!("{}", idx_pos + 1))
                .trim()
                .to_string();

            let mut cols = Vec::new();
            for ic in idx.find_all("IndexColumn") {
                let col_ref = ic.child_text("column")
                    .or_else(|| ic.child_text("name"))
                    .or_else(|| ic.attr("column"))
                    .or_else(|| ic.attr("name"))
                    .unwrap_or_default()
                    .trim()
                    .to_lowercase();
                if !col_ref.is_empty() && !cols.contains(&col_ref) {
                    cols.push(col_ref);
                }
            }
            for mf in idx.find_all("Field") {
                let col_ref = mf.attr("name").or_else(|| mf.child_text("name")).unwrap_or_default().trim().to_lowercase();
                if !col_ref.is_empty() && !cols.contains(&col_ref) {
                    cols.push(col_ref);
                }
            }
            indices.insert(idx_name, cols);
        }

        Some(ParsedDdResult::Table(
            DdTableEntry {
                name: tbl_name,
                description: desc,
                fields,
                indices,
            },
            inferred_domains,
        ))
    } else if root_tag == "dr_domain" {
        let dmn_name = tree.attr("name")
            .or_else(|| tree.child_text("name"))
            .unwrap_or(hint_name)
            .trim()
            .to_lowercase();

        if dmn_name.is_empty() {
            return None;
        }

        let desc = tree.child_text("description").or_else(|| tree.attr("description")).unwrap_or_default().to_string();
        let mut native_dt = String::new();
        let mut facets = HashMap::new();

        if let Some(dt) = tree.find_first("datatype") {
            native_dt = dt.child_text("nativeDatatype").or_else(|| dt.attr("nativeDatatype")).unwrap_or_default().trim().to_string();
            for facet in dt.find_all("Facet") {
                let ftype = facet.child_text("type").unwrap_or_default().trim().to_string();
                let fval = facet.child_text("value").unwrap_or_default().trim().to_string();
                if !ftype.is_empty() {
                    facets.insert(ftype, fval);
                }
            }
        }
        if native_dt.is_empty() {
            native_dt = tree.child_text("nativeDatatype")
                .or_else(|| tree.attr("nativeDatatype"))
                .or_else(|| tree.attr("type"))
                .or_else(|| tree.child_text("type"))
                .unwrap_or_default()
                .trim()
                .to_string();
        }

        let mut enums = HashMap::new();
        for en in tree.find_all("Enumeration") {
            let e_name = en.attr("name")
                .or_else(|| en.child_text("name"))
                .or_else(|| en.child_text("constant"))
                .or_else(|| en.attr("constant"))
                .unwrap_or_default()
                .trim()
                .to_string();
            if !e_name.is_empty() {
                enums.insert(e_name, DdEnum {
                    position: en.child_text("position").or_else(|| en.attr("position")).unwrap_or_default().trim().to_string(),
                    description: en.child_text("description").or_else(|| en.attr("description")).unwrap_or_default().trim().to_string(),
                    label: en.child_text("descriptionReference").unwrap_or_default().trim().to_string(),
                });
            }
        }
        for ev in tree.find_all("EnumValue") {
            let e_name = ev.attr("name").or_else(|| ev.attr("const")).or_else(|| ev.child_text("name")).unwrap_or_default().trim().to_string();
            if !e_name.is_empty() && !enums.contains_key(&e_name) {
                enums.insert(e_name, DdEnum {
                    position: ev.attr("value").unwrap_or_default().trim().to_string(),
                    description: ev.attr("description").unwrap_or_default().trim().to_string(),
                    label: String::new(),
                });
            }
        }

        let enum_values = enums.keys().cloned().collect();

        Some(ParsedDdResult::Domain(DdDomainEntry {
            name: dmn_name,
            description: desc,
            datatype: native_dt,
            facets,
            enums,
            enum_values,
        }))
    } else {
        None
    }
}

/// Parses `.tbl` or `.dmn` XML content and atomically updates `.ln_dd_cache.json`.
pub fn update_dd_cache_from_xml(
    xml_content: &str,
    dd_cache_path: &Path,
    hint_name: &str,
) -> Option<String> {
    let parsed = parse_dd_xml_to_entry(xml_content, hint_name)?;

    let mut cache: serde_json::Value = if dd_cache_path.exists() {
        std::fs::read_to_string(dd_cache_path)
            .ok()
            .and_then(|s| serde_json::from_str(&s).ok())
            .unwrap_or_else(|| serde_json::json!({ "version": "1.0", "tables": {}, "domains": {} }))
    } else {
        serde_json::json!({ "version": "1.0", "tables": {}, "domains": {} })
    };

    if !cache.is_object() {
        cache = serde_json::json!({ "version": "1.0", "tables": {}, "domains": {} });
    }

    let tables_obj = cache.as_object_mut().unwrap().entry("tables").or_insert_with(|| serde_json::json!({}));
    if !tables_obj.is_object() {
        *tables_obj = serde_json::json!({});
    }
    let domains_obj = cache.as_object_mut().unwrap().entry("domains").or_insert_with(|| serde_json::json!({}));
    if !domains_obj.is_object() {
        *domains_obj = serde_json::json!({});
    }

    let indexed_name = match parsed {
        ParsedDdResult::Table(tbl, inferred) => {
            let name = tbl.name.clone();
            let tbl_json = serde_json::to_value(&tbl).unwrap_or_default();
            cache["tables"][&name] = tbl_json;
            for (d_name, d_val) in inferred {
                if cache["domains"].get(&d_name).is_none() {
                    cache["domains"][&d_name] = d_val;
                }
            }
            name
        }
        ParsedDdResult::Domain(dmn) => {
            let name = dmn.name.clone();
            let dmn_json = serde_json::to_value(&dmn).unwrap_or_default();
            cache["domains"][&name] = dmn_json;
            name
        }
    };

    cache["updated_at"] = serde_json::json!("2026-11-12T00:00:00Z");

    if let Some(parent) = dd_cache_path.parent() {
        let _ = std::fs::create_dir_all(parent);
    }
    if let Ok(formatted) = serde_json::to_string_pretty(&cache) {
        let _ = std::fs::write(dd_cache_path, formatted);
    }

    Some(indexed_name)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ComponentInspection {
    pub name: String,
    pub comp_type: String,
    pub package: String,
    pub module: String,
    pub description: String,
    pub fields: Vec<serde_json::Value>,
    pub indices: HashMap<String, Vec<String>>,
    pub datatype: String,
    pub enums: HashMap<String, DdEnum>,
    pub script: String,
    pub raw_xml: String,
}

/// Inspects component schema and embedded script in-memory without modifying the local Activity directory.
pub async fn inspect_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    connection_point: &str,
    dd_cache_path: Option<&Path>,
    context_xml: Option<&str>,
    base_vrc: Option<&str>,
) -> Result<ComponentInspection, JcaError> {
    let ext_info = resolve_extension_component_name(comp_name, comp_type);
    let eff_name = if ext_info.is_extension { &ext_info.library_name } else { comp_name };
    let eff_type = if ext_info.is_extension { "library" } else { comp_type };

    let (pkg, mod_code, _) = ln_model::path_resolver::split_component_name(eff_name);

    let resp_xml = fetch_component_xml(
        client,
        eff_type,
        eff_name,
        connection_point,
        context_xml,
        base_vrc,
    ).await?;

    if let Some(dd_path) = dd_cache_path {
        if comp_type.eq_ignore_ascii_case("table") || comp_type.eq_ignore_ascii_case("domain") {
            update_dd_cache_from_xml(&resp_xml, dd_path, comp_name);
        }
    }

    let parsed_dd = parse_dd_xml_to_entry(&resp_xml, comp_name);
    let mut fields_list = Vec::new();
    let mut indices_map = HashMap::new();
    let mut datatype = String::new();
    let mut enums_map = HashMap::new();

    if let Some(ParsedDdResult::Table(tbl, _)) = &parsed_dd {
        for (f_name, f_meta) in &tbl.fields {
            fields_list.push(serde_json::json!({
                "name": f_name,
                "domain": f_meta.domain,
                "label": f_meta.label,
                "datatype": f_meta.datatype,
                "mandatory": f_meta.mandatory,
            }));
        }
        indices_map = tbl.indices.clone();
    } else if let Some(ParsedDdResult::Domain(dmn)) = &parsed_dd {
        datatype = dmn.datatype.clone();
        enums_map = dmn.enums.clone();
    }

    let script = ln_model::dom_surgery::extract_script(&resp_xml).unwrap_or_default();

    let tree = parse_xml_to_tree(&resp_xml).ok();
    let desc = tree.as_ref()
        .and_then(|t| t.find_text("description"))
        .unwrap_or_default()
        .to_string();

    Ok(ComponentInspection {
        name: comp_name.to_string(),
        comp_type: comp_type.to_string(),
        package: pkg,
        module: mod_code,
        description: desc,
        fields: fields_list,
        indices: indices_map,
        datatype,
        enums: enums_map,
        script,
        raw_xml: resp_xml,
    })
}

/// Fetches component XML from server, writes it to activity directory in Native Single-XML TDE Layout,
/// enforces OS Read-Only flag when appropriate, registers it in `.admin` via `after_get`, and updates `.ln_dd_cache.json`.
pub async fn get_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    read_only: bool,
    connection_point: &str,
    dd_cache_path: Option<&Path>,
    activity_uuid: Option<&str>,
    base_vrc: Option<&str>,
    export_script: Option<&Path>,
) -> Result<PathBuf, JcaError> {
    let ctype_lower = comp_type.to_lowercase();
    let info = get_bde_type_info(&ctype_lower)
        .ok_or_else(|| JcaError::Protocol(format!("Unsupported component type '{comp_type}'")))?;

    let ext_info = resolve_extension_component_name(comp_name, comp_type);
    let is_ext = ext_info.is_extension;
    let eff_name = if is_ext { &ext_info.library_name } else { comp_name };
    let eff_type = if is_ext { "library" } else { &ctype_lower };
    let eff_info = get_bde_type_info(eff_type).unwrap_or(info);
    let ext = eff_info.ext;

    let eff_readonly = read_only || is_ext || ctype_lower == "extension" || eff_info.readonly_only;

    // Resolve context_xml and eff_cp from activity_dir if not explicitly provided
    let (act_ctx, act_cp) = crate::activity::resolve_activity_context(activity_dir);
    let context_xml = if activity_uuid.is_some() {
        Some(format!("<ActivityID><activityUUID>{}</activityUUID></ActivityID>", activity_uuid.unwrap()))
    } else {
        act_ctx
    };
    let eff_cp = if connection_point.is_empty() || connection_point == "ProjectServer" {
        &act_cp
    } else {
        connection_point
    };

    let resp_xml = fetch_component_xml(
        client,
        eff_type,
        eff_name,
        eff_cp,
        context_xml.as_deref(),
        base_vrc,
    ).await?;

    let rel_path = if is_ext {
        PathBuf::from(format!("tx/library/{}/{}", ext_info.ext_type, format!("{eff_name}.lib")))
    } else {
        ln_model::path_resolver::resolve_tde_relative_path(eff_type, eff_name, ext)
            .map_err(|e| JcaError::Protocol(format!("TDE path error: {e}")))?
    };

    let target_file = activity_dir.join(&rel_path);
    if let Some(parent) = target_file.parent() {
        std::fs::create_dir_all(parent)?;
    }

    if target_file.exists() {
        if let Ok(mut perms) = std::fs::metadata(&target_file).map(|m| m.permissions()) {
            perms.set_readonly(false);
            let _ = std::fs::set_permissions(&target_file, perms);
        }
    }

    std::fs::write(&target_file, &resp_xml)?;

    if eff_readonly {
        if let Ok(mut perms) = std::fs::metadata(&target_file).map(|m| m.permissions()) {
            perms.set_readonly(true);
            let _ = std::fs::set_permissions(&target_file, perms);
        }
    }

    if ctype_lower == "table" || ctype_lower == "domain" {
        let eff_dd = dd_cache_path
            .map(|p| p.to_path_buf())
            .unwrap_or_else(|| activity_dir.parent().unwrap_or(activity_dir).join(".ln_dd_cache.json"));
        update_dd_cache_from_xml(&resp_xml, &eff_dd, eff_name);
    }

    if let Some(exp_p) = export_script {
        let script_file = if exp_p.is_dir() || (!exp_p.extension().is_some() && !exp_p.exists()) {
            std::fs::create_dir_all(exp_p)?;
            let t_code = if !ext_info.target_code.is_empty() { &ext_info.target_code } else { eff_name };
            exp_p.join(format!("{t_code}.cln"))
        } else {
            if let Some(parent) = exp_p.parent() {
                std::fs::create_dir_all(parent)?;
            }
            exp_p.to_path_buf()
        };

        if let Some(script_text) = ln_model::dom_surgery::extract_script(&resp_xml) {
            let normalized = script_text.replace("\r\n", "\n").trim_end().to_string() + "\n";
            std::fs::write(script_file, normalized)?;
        }
    }

    if !is_ext && ctype_lower != "extension" {
        let norm_rel = rel_path.to_string_lossy().replace('\\', "/");
        let admin_path = activity_dir.join(".admin");
        let mut admin_file = AdminFile::load_from_path(&admin_path).unwrap_or_default();
        admin_file.after_get(&norm_rel);
        let _ = admin_file.save_to_path(&admin_path);
    }

    Ok(target_file)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SyncReferenceResult {
    pub comp_type: String,
    pub pattern: String,
    pub reference_dir: String,
    pub dd_cache_path: String,
    pub synced_count: usize,
    pub files: Vec<String>,
    pub dd_indexed: Vec<String>,
    pub read_only: bool,
}

/// Downloads requested components in Read-Only reference mode into `<workspace_dir>/.reference/<type>/`
/// without modifying any Activity `.admin` file. Automatically parses `.tbl` and `.dmn` and updates `.ln_dd_cache.json`.
pub async fn sync_reference(
    client: &HttpClient,
    comp_type: &str,
    name_pattern: &str,
    workspace_dir: &Path,
    dd_cache_path: Option<&Path>,
    connection_point: &str,
) -> Result<SyncReferenceResult, JcaError> {
    let ctype_lower = comp_type.to_lowercase();
    let info = get_bde_type_info(&ctype_lower)
        .ok_or_else(|| JcaError::Protocol(format!("Unsupported component type '{comp_type}'")))?;

    let _cur_ext = info.ext;
    let ref_dir = workspace_dir.join(".reference").join(&ctype_lower);
    std::fs::create_dir_all(&ref_dir)?;

    let eff_dd = dd_cache_path
        .map(|p| p.to_path_buf())
        .unwrap_or_else(|| workspace_dir.join(".ln_dd_cache.json"));

    let mut target_names = Vec::new();
    if name_pattern.contains('*') || name_pattern.contains('?') {
        let pkg_prefix = if name_pattern.len() >= 2 { &name_pattern[..2] } else { "" };
        let browsed = browse_components(
            client,
            pkg_prefix,
            if ctype_lower == "extension" { "library" } else { &ctype_lower },
            name_pattern,
            connection_point,
        ).await?;

        for b in browsed {
            target_names.push(b.name);
        }
    } else {
        target_names.push(name_pattern.to_string());
    }

    let mut synced_files = Vec::new();
    let mut dd_indexed = Vec::new();

    for comp_name in target_names {
        let ext_info = resolve_extension_component_name(&comp_name, comp_type);
        let eff_name = if ext_info.is_extension { &ext_info.library_name } else { &comp_name };
        let eff_type = if ext_info.is_extension { "library" } else { &ctype_lower };
        let eff_info = get_bde_type_info(eff_type).unwrap_or(info);
        let this_ext = eff_info.ext;

        let resp_xml = match fetch_component_xml(
            client,
            eff_type,
            eff_name,
            connection_point,
            None,
            Some("B61O_a_ext"),
        ).await {
            Ok(x) if !x.trim().is_empty() => x,
            _ => continue,
        };

        let out_file = ref_dir.join(format!("{eff_name}{this_ext}"));
        if out_file.exists() {
            if let Ok(mut perms) = std::fs::metadata(&out_file).map(|m| m.permissions()) {
                perms.set_readonly(false);
                let _ = std::fs::set_permissions(&out_file, perms);
            }
        }

        std::fs::write(&out_file, &resp_xml)?;
        if let Ok(mut perms) = std::fs::metadata(&out_file).map(|m| m.permissions()) {
            perms.set_readonly(true);
            let _ = std::fs::set_permissions(&out_file, perms);
        }

        synced_files.push(out_file.to_string_lossy().to_string());

        if ctype_lower == "table" || ctype_lower == "domain" || resp_xml.contains("<DR_Table") || resp_xml.contains("<DR_Domain") {
            if let Some(idx_name) = update_dd_cache_from_xml(&resp_xml, &eff_dd, eff_name) {
                dd_indexed.push(idx_name);
            }
        }
    }

    Ok(SyncReferenceResult {
        comp_type: ctype_lower,
        pattern: name_pattern.to_string(),
        reference_dir: ref_dir.to_string_lossy().to_string(),
        dd_cache_path: eff_dd.to_string_lossy().to_string(),
        synced_count: synced_files.len(),
        files: synced_files,
        dd_indexed,
        read_only: true,
    })
}

/// Clones an existing component to a target component, updating internal names and labels,
/// writing to activity in Single-XML TDE layout, registering in `.admin` via `after_create`,
/// and invoking `DR_Create` on the server sending raw `<DR_*>` root XML directly.
/// Strictly blocks Extension Modeler components per ADR 0006.
pub async fn clone_component(
    client: &HttpClient,
    comp_type: &str,
    source_name: &str,
    target_name: &str,
    activity_dir: &Path,
    register_on_server: bool,
    connection_point: &str,
    activity_uuid: Option<&str>,
) -> Result<PathBuf, JcaError> {
    let ctype_lower = comp_type.to_lowercase();
    if ctype_lower == "extension"
        || source_name.to_lowercase().ends_with(".eso")
        || source_name.to_lowercase().ends_with(".eto")
        || source_name.to_lowercase().ends_with(".ere")
        || resolve_extension_component_name(source_name, comp_type).is_extension
    {
        return Err(JcaError::Protocol(
            "Extension Modeler Rule (ADR 0006): Extension objects cannot be cloned, checked out, \
            modified, or pushed to LN Studio. Use 'sync-reference --type extension' for read-only reference \
            and author extension hooks via manual Copy-Paste in LN UI Cloud (ttext1500m000).".to_string()
        ));
    }

    let info = get_bde_type_info(&ctype_lower)
        .ok_or_else(|| JcaError::Protocol(format!("Unsupported component type '{comp_type}'")))?;

    let bde_name = info.bde;
    let ext = info.ext;

    let (src_pkg, src_mod, _) = ln_model::path_resolver::split_component_name(source_name);
    let (tgt_pkg, tgt_mod, _) = ln_model::path_resolver::split_component_name(target_name);

    let (act_ctx, act_cp) = crate::activity::resolve_activity_context(activity_dir);
    let context_xml = if let Some(uuid) = activity_uuid {
        Some(format!("<ActivityID><activityUUID>{uuid}</activityUUID></ActivityID>"))
    } else {
        act_ctx
    };
    let eff_cp = if connection_point.is_empty() || connection_point == "ProjectServer" {
        &act_cp
    } else {
        connection_point
    };

    let resp_xml = fetch_component_xml(
        client,
        comp_type,
        source_name,
        eff_cp,
        context_xml.as_deref(),
        None,
    ).await?;

    let renamed_xml = ln_model::dom_surgery::clone_component_xml(
        &resp_xml,
        source_name,
        target_name,
        &src_pkg,
        &tgt_pkg,
        if src_mod.is_empty() { None } else { Some(&src_mod) },
        if tgt_mod.is_empty() { None } else { Some(&tgt_mod) },
    );

    let rel_path = ln_model::path_resolver::resolve_tde_relative_path(&ctype_lower, target_name, ext)
        .map_err(|e| JcaError::Protocol(format!("TDE path error: {e}")))?;

    let target_file = activity_dir.join(&rel_path);
    if let Some(parent) = target_file.parent() {
        std::fs::create_dir_all(parent)?;
    }

    if target_file.exists() {
        if let Ok(mut perms) = std::fs::metadata(&target_file).map(|m| m.permissions()) {
            perms.set_readonly(false);
            let _ = std::fs::set_permissions(&target_file, perms);
        }
    }

    std::fs::write(&target_file, &renamed_xml)?;

    // Register in .admin cache via after_create
    let norm_rel = rel_path.to_string_lossy().replace('\\', "/");
    let admin_path = activity_dir.join(".admin");
    let mut admin_file = AdminFile::load_from_path(&admin_path).unwrap_or_default();
    admin_file.after_create(&norm_rel);
    let _ = admin_file.save_to_path(&admin_path);

    // Register on server via DR_Create sending raw <DR_*> root XML directly
    if register_on_server {
        let mgr = JcaBdeManager::new(client, eff_cp);
        let params = BdeParams {
            bde_name: bde_name.to_string(),
            method_name: "DR_Create".to_string(),
            mode: Some(BdeExecutionMode::Bde),
            request_xml: Some(renamed_xml),
            context_xml,
            ..Default::default()
        };
        let _ = mgr.execute(&params).await?;
    }

    Ok(target_file)
}
