use std::collections::{HashMap, HashSet};
use std::fs;
use std::path::{Path, PathBuf};
use quick_xml::events::Event;
use quick_xml::Reader;
use regex::Regex;
use serde::{Deserialize, Serialize};
use thiserror::Error;

use ln_eclipse_compat::AdminFile;
use ln_linter::{audit_content, Severity as LinterSeverity};
use crate::dom_surgery::extract_script;
use crate::generators::label::{compact_tde_xml, generate_label_xml_with_context, has_multiline_outside_script};

pub const MANAGED_EXTENSIONS: &[&str] = &[
    ".tbl", ".ses", ".dmn", ".lib", ".mnu", ".lbl", ".rpt", ".msg", ".qst", ".fnc", ".add", ".bus", ".rptdsrc"
];

pub const VALID_DATATYPES: &[i64] = &[1, 2, 3, 5, 6, 7, 9, 14];

#[derive(Debug, Error)]
pub enum ValidationError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Admin file error: {0}")]
    Admin(String),
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum ValidationSeverity {
    Error,
    Warning,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ValidationDiagnostic {
    pub file_path: String,
    pub line: usize,
    pub col: usize,
    pub severity: ValidationSeverity,
    pub message: String,
    pub layer: usize,
}

impl std::fmt::Display for ValidationDiagnostic {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let sev = match self.severity {
            ValidationSeverity::Error => "ERROR",
            ValidationSeverity::Warning => "WARNING",
        };
        write!(
            f,
            "{}:{}:{} [{}] [Layer {}] {}",
            self.file_path, self.line, self.col, sev, self.layer, self.message
        )
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ValidationReport {
    pub target_path: PathBuf,
    pub files_scanned: usize,
    pub diagnostics: Vec<ValidationDiagnostic>,
    pub repaired_items: Vec<String>,
}

impl ValidationReport {
    pub fn new(target_path: PathBuf) -> Self {
        Self {
            target_path,
            files_scanned: 0,
            diagnostics: Vec::new(),
            repaired_items: Vec::new(),
        }
    }

    pub fn add(&mut self, file_path: &str, line: usize, col: usize, severity: ValidationSeverity, message: &str, layer: usize) {
        self.diagnostics.push(ValidationDiagnostic {
            file_path: file_path.to_string(),
            line,
            col,
            severity,
            message: message.to_string(),
            layer,
        });
    }

    pub fn errors(&self) -> Vec<&ValidationDiagnostic> {
        self.diagnostics.iter().filter(|d| d.severity == ValidationSeverity::Error).collect()
    }

    pub fn warnings(&self) -> Vec<&ValidationDiagnostic> {
        self.diagnostics.iter().filter(|d| d.severity == ValidationSeverity::Warning).collect()
    }

    pub fn has_errors(&self) -> bool {
        self.diagnostics.iter().any(|d| d.severity == ValidationSeverity::Error)
    }
}

#[derive(Debug, Clone, Default)]
struct TableMeta {
    path: PathBuf,
    table_code: String,
    description_reference: String,
    columns: HashSet<String>,
    column_datatypes: Vec<(String, Option<String>)>,
    indexes: Vec<Vec<String>>,
    raw_xml: String,
}

#[derive(Debug, Clone, Default)]
struct FormCommandMeta {
    name: String,
    cmd_type: String,
    activation_type: String,
    activation_name: String,
    show_as_button: String,
}

#[derive(Debug, Clone, Default)]
struct FormFieldPos {
    field_name: String,
    group_id: String,
    row: String,
    col: String,
}

#[derive(Debug, Clone, Default)]
struct SessionMeta {
    path: PathBuf,
    session_code: String,
    description_reference: String,
    controller_table: String,
    controller_tables: HashSet<String>,
    form_fields: HashSet<String>,
    form_field_names: Vec<String>,
    form_field_positions: Vec<FormFieldPos>,
    commands: HashSet<String>,
    form_commands_meta: Vec<FormCommandMeta>,
    groups: HashMap<String, FormGroupInfo>,
    embedded_script: Option<String>,
    raw_xml: String,
}

#[derive(Debug, Clone, Default)]
struct FormGroupInfo {
    parent_group: String,
    first_child_group: String,
    next_group: String,
    previous_group: String,
}

#[derive(Debug, Clone, Default)]
struct MenuMeta {
    path: PathBuf,
    choices: Vec<MenuChoiceInfo>,
}

#[derive(Debug, Clone, Default)]
struct MenuChoiceInfo {
    choice_type: String,
    target: String,
}

#[derive(Debug, Clone, Default)]
struct ReportMeta {
    path: PathBuf,
    report_code: String,
    description_reference: String,
    referenced_labels: HashSet<String>,
    input_fields: Vec<ReportInputFieldInfo>,
    raw_xml: String,
}

#[derive(Debug, Clone, Default)]
struct ReportInputFieldInfo {
    name: String,
    domain: String,
    _description_reference: String,
}

pub struct ActivityValidator {
    pub activity_path: PathBuf,
    pub strict: bool,
    pub fix: bool,
    pub report: ValidationReport,

    packages: HashSet<String>,
    tables: HashMap<String, TableMeta>,
    sessions: HashMap<String, SessionMeta>,
    domains: HashMap<String, PathBuf>,
    labels: HashSet<String>,
    reference_labels: HashSet<String>,
    server_labels: HashSet<String>,
    online: bool,
    libraries: HashMap<String, PathBuf>,
    menus: HashMap<String, MenuMeta>,
    reports: HashMap<String, ReportMeta>,
    functions: HashMap<String, PathBuf>,
    admin_loaded: bool,
    created_or_untracked: HashSet<String>,
    multiline_files: Vec<PathBuf>,
    command_labels: HashSet<String>,
    desc_labels: HashSet<String>,
    filter_patterns: Vec<String>,
    target_files: Vec<PathBuf>,
}

impl ActivityValidator {
    pub fn new(activity_path: PathBuf, strict: bool, fix: bool) -> Self {
        let abs_path = fs::canonicalize(&activity_path).unwrap_or(activity_path);
        let report = ValidationReport::new(abs_path.clone());
        Self {
            activity_path: abs_path,
            strict,
            fix,
            report,
            packages: HashSet::new(),
            tables: HashMap::new(),
            sessions: HashMap::new(),
            domains: HashMap::new(),
            labels: HashSet::new(),
            reference_labels: HashSet::new(),
            server_labels: HashSet::new(),
            online: false,
            libraries: HashMap::new(),
            menus: HashMap::new(),
            reports: HashMap::new(),
            functions: HashMap::new(),
            admin_loaded: false,
            created_or_untracked: HashSet::new(),
            multiline_files: Vec::new(),
            command_labels: HashSet::new(),
            desc_labels: HashSet::new(),
            filter_patterns: Vec::new(),
            target_files: Vec::new(),
        }
    }

    pub fn set_online_labels(&mut self, labels: HashSet<String>) {
        self.online = true;
        self.server_labels = labels;
    }

    pub fn set_scope(&mut self, filters: Vec<String>, files: Vec<PathBuf>) {
        self.filter_patterns = filters.into_iter().filter(|f| !f.trim().is_empty()).collect();
        self.target_files = files;
    }

    fn has_scope(&self) -> bool {
        !self.filter_patterns.is_empty() || !self.target_files.is_empty()
    }

    fn path_matches_scope(&self, candidate: &Path) -> bool {
        if !self.has_scope() {
            return true;
        }
        let abs_cand = fs::canonicalize(candidate).unwrap_or_else(|_| candidate.to_path_buf());
        for tf in &self.target_files {
            let abs_tf = if tf.is_absolute() {
                fs::canonicalize(tf).unwrap_or_else(|_| tf.clone())
            } else {
                fs::canonicalize(self.activity_path.join(tf)).unwrap_or_else(|_| self.activity_path.join(tf))
            };
            if abs_cand == abs_tf || candidate == tf {
                return true;
            }
        }
        let fname = candidate.file_name().and_then(|s| s.to_str()).unwrap_or("").to_ascii_lowercase();
        let stem = candidate.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_ascii_lowercase();
        let rel = candidate
            .strip_prefix(&self.activity_path)
            .unwrap_or(candidate)
            .to_string_lossy()
            .replace('\\', "/")
            .to_ascii_lowercase();
        for pat in &self.filter_patterns {
            let p_low = pat.trim().replace('\\', "/").to_ascii_lowercase();
            if glob_matches(&p_low, &fname) || glob_matches(&p_low, &stem) || glob_matches(&p_low, &rel) {
                return true;
            }
        }
        false
    }

    fn diag_matches_scope(&self, diag: &ValidationDiagnostic) -> bool {
        if !self.has_scope() {
            return true;
        }
        let p = Path::new(&diag.file_path);
        if self.path_matches_scope(p) {
            return true;
        }
        // Activity/admin level diagnostic: retain only if message references a scoped component
        if diag.file_path == self.activity_path.to_string_lossy()
            || diag.file_path.ends_with(".admin")
        {
            let msg_low = diag.message.to_ascii_lowercase();
            for tf in &self.target_files {
                let n = tf.file_name().and_then(|s| s.to_str()).unwrap_or("").to_ascii_lowercase();
                if !n.is_empty() && msg_low.contains(&n) {
                    return true;
                }
            }
            for pat in &self.filter_patterns {
                let needle = pat.trim_matches('*').to_ascii_lowercase();
                if !needle.is_empty() && msg_low.contains(&needle) {
                    return true;
                }
            }
        }
        false
    }

    pub fn run(&mut self) -> &ValidationReport {
        self.discover_packages();
        self.index_activity_components();

        self.validate_layer1_scm();
        self.validate_layer2_structure();
        self.validate_layer3_cross_references();
        self.validate_layer4_scripts();

        if self.has_scope() {
            let scoped_diags: Vec<ValidationDiagnostic> = self
                .report
                .diagnostics
                .iter()
                .filter(|d| self.diag_matches_scope(d))
                .cloned()
                .collect();
            self.report.diagnostics = scoped_diags;
            let multiline = std::mem::take(&mut self.multiline_files);
            self.multiline_files = multiline
                .into_iter()
                .filter(|p| self.path_matches_scope(p))
                .collect();
        }

        if self.fix {
            self.execute_safe_fixes();
        }

        &self.report
    }

    fn discover_packages(&mut self) {
        if let Ok(entries) = fs::read_dir(&self.activity_path) {
            for entry in entries.flatten() {
                let p = entry.path();
                if p.is_dir() {
                    let name = p.file_name().and_then(|n| n.to_str()).unwrap_or("");
                    if !name.starts_with('.') {
                        if let Ok(subs) = fs::read_dir(&p) {
                            let sub_names: HashSet<String> = subs
                                .flatten()
                                .filter_map(|s| {
                                    if s.path().is_dir() {
                                        s.file_name().into_string().ok()
                                    } else {
                                        None
                                    }
                                })
                                .collect();
                            let known_subdirs = [
                                "table", "session", "label", "menu", "library", "domain",
                                "report", "message", "question", "function", "additional",
                                "businessobject", ".admin",
                            ];
                            if known_subdirs.iter().any(|k| sub_names.contains(*k)) {
                                self.packages.insert(name.to_ascii_lowercase());
                            }
                        }
                    }
                }
            }
        }
    }

    fn index_activity_components(&mut self) {
        let managed_ext_set: HashSet<&str> = MANAGED_EXTENSIONS.iter().copied().collect();
        let all_files = walk_managed_files(&self.activity_path, &managed_ext_set);

        for path in all_files {
            self.report.files_scanned += 1;
            let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("").to_ascii_lowercase();
            let dot_ext = format!(".{}", ext);
            let code = path.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_ascii_lowercase();

            match dot_ext.as_str() {
                ".tbl" => {
                    let meta = self.parse_table_metadata(&path);
                    self.tables.insert(code, meta);
                }
                ".ses" => {
                    let meta = self.parse_session_metadata(&path);
                    self.sessions.insert(code, meta);
                }
                ".dmn" => {
                    self.domains.insert(code, path);
                }
                ".lbl" => {
                    self.labels.insert(code);
                }
                ".lib" => {
                    self.libraries.insert(code, path);
                }
                ".mnu" => {
                    let meta = self.parse_menu_metadata(&path);
                    self.menus.insert(code, meta);
                }
                ".rpt" | ".rptdsrc" => {
                    let meta = self.parse_report_metadata(&path);
                    self.reports.insert(code, meta);
                }
                ".fnc" => {
                    self.functions.insert(code, path);
                }
                _ => {}
            }
        }

        if let Some(ws_dir) = self.activity_path.parent() {
            let ref_lbl_dir = ws_dir.join(".reference").join("label");
            if ref_lbl_dir.is_dir() {
                if let Ok(entries) = fs::read_dir(&ref_lbl_dir) {
                    for entry in entries.flatten() {
                        let p = entry.path();
                        if p.is_file() && p.extension().and_then(|e| e.to_str()).map(|s| s.eq_ignore_ascii_case("lbl")).unwrap_or(false) {
                            if let Some(stem) = p.file_stem().and_then(|s| s.to_str()) {
                                self.reference_labels.insert(stem.to_ascii_lowercase());
                            }
                        }
                    }
                }
            }
        }
    }

    fn parse_table_metadata(&self, path: &Path) -> TableMeta {
        let mut meta = TableMeta {
            path: path.to_path_buf(),
            table_code: path.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string(),
            ..Default::default()
        };

        if let Ok(content) = fs::read_to_string(path) {
            meta.raw_xml = content.clone();
            if let Some(m) = Regex::new(r#"descriptionReference="([^"]+)""#).ok().and_then(|re| re.captures(&content)) {
                meta.description_reference = m.get(1).unwrap().as_str().to_string();
            }

            // DOM traversal via quick-xml tag stack so nested <DatatypeReference><name>
            // and <Index><name> never shadow direct <Column><name> or <IndexColumn><column>.
            let mut reader = Reader::from_str(&content);
            reader.config_mut().trim_text(true);
            let mut stack: Vec<String> = Vec::new();
            let mut cur_text = String::new();

            let mut cur_col_name: Option<String> = None;
            let mut cur_col_dt: Option<String> = None;
            let mut pending_cols: Vec<(String, Option<String>)> = Vec::new();

            let mut cur_idx_cols: Vec<String> = Vec::new();
            let mut cur_ic_col: Option<String> = None;
            let mut cur_ic_name: Option<String> = None;

            loop {
                match reader.read_event() {
                    Ok(Event::Start(e)) => {
                        let tag = String::from_utf8_lossy(e.name().as_ref()).to_string();
                        cur_text.clear();
                        match tag.as_str() {
                            "Column" => {
                                cur_col_name = None;
                                cur_col_dt = None;
                            }
                            "Index" => {
                                cur_idx_cols.clear();
                            }
                            "IndexColumn" => {
                                cur_ic_col = None;
                                cur_ic_name = None;
                            }
                            _ => {}
                        }
                        stack.push(tag);
                    }
                    Ok(Event::Empty(e)) => {
                        let tag = String::from_utf8_lossy(e.name().as_ref()).to_string();
                        if tag == "Index" {
                            meta.indexes.push(Vec::new());
                        }
                    }
                    Ok(Event::Text(e)) => {
                        if let Ok(t) = e.unescape() {
                            cur_text.push_str(&t);
                        }
                    }
                    Ok(Event::CData(e)) => {
                        cur_text.push_str(&String::from_utf8_lossy(e.as_ref()));
                    }
                    Ok(Event::End(e)) => {
                        let tag = String::from_utf8_lossy(e.name().as_ref()).to_string();
                        let text = cur_text.trim().to_string();
                        let parent = if stack.len() >= 2 { Some(stack[stack.len() - 2].as_str()) } else { None };
                        let root_tag = stack.first().map(|s| s.as_str());

                        if tag == "name" && stack.len() == 2 && root_tag == Some("DR_Table") && !text.is_empty() {
                            meta.table_code = text.clone();
                        } else if tag == "descriptionReference" && stack.len() == 2 && root_tag == Some("DR_Table") && !text.is_empty() {
                            meta.description_reference = text.clone();
                        } else if tag == "name" && parent == Some("Column") && !text.is_empty() {
                            cur_col_name = Some(text.clone());
                        } else if tag == "nativeDatatype" && stack.iter().any(|s| s == "Column") && !text.is_empty() {
                            cur_col_dt = Some(text.clone());
                        } else if tag == "column" && parent == Some("IndexColumn") && !text.is_empty() {
                            cur_ic_col = Some(text.clone());
                        } else if tag == "name" && parent == Some("IndexColumn") && !text.is_empty() {
                            cur_ic_name = Some(text.clone());
                        } else if tag == "IndexColumn" {
                            if let Some(col_ref) = cur_ic_col.take().or_else(|| cur_ic_name.take()) {
                                let bare = col_ref.split('.').last().unwrap_or(&col_ref).to_string();
                                cur_idx_cols.push(bare);
                            }
                        } else if tag == "Index" {
                            meta.indexes.push(std::mem::take(&mut cur_idx_cols));
                        } else if tag == "Column" {
                            if let Some(cname) = cur_col_name.take() {
                                pending_cols.push((cname, cur_col_dt.take()));
                            }
                        }

                        cur_text.clear();
                        stack.pop();
                    }
                    Ok(Event::Eof) | Err(_) => break,
                    _ => {}
                }
            }

            // Determine package-prefixed alias too if table_code lacks package prefix (e.g. cmg011 -> txcmg011)
            let pkg_prefix = path
                .strip_prefix(&self.activity_path)
                .ok()
                .and_then(|rel| rel.components().next())
                .and_then(|c| c.as_os_str().to_str())
                .map(|s| s.to_ascii_lowercase())
                .unwrap_or_default();
            let full_table_code = if !pkg_prefix.is_empty() && !meta.table_code.to_ascii_lowercase().starts_with(&pkg_prefix) {
                format!("{}{}", pkg_prefix, meta.table_code)
            } else {
                meta.table_code.clone()
            };

            for (cname, dt) in pending_cols {
                meta.columns.insert(cname.clone());
                meta.columns.insert(format!("{}.{}", meta.table_code, cname));
                meta.columns.insert(format!("{}.{}", full_table_code, cname));
                meta.column_datatypes.push((cname, dt));
            }
        }
        meta
    }

    fn parse_session_metadata(&self, path: &Path) -> SessionMeta {
        let mut meta = SessionMeta {
            path: path.to_path_buf(),
            session_code: path.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string(),
            ..Default::default()
        };

        if let Ok(content) = fs::read_to_string(path) {
            meta.raw_xml = content.clone();
            if let Some(m) = Regex::new(r"<name>([^<]+)</name>").ok().and_then(|re| re.captures(&content)) {
                meta.session_code = m.get(1).unwrap().as_str().to_string();
            }
            if let Some(m) = Regex::new(r"<toTable>([^<]+)</toTable>").ok().and_then(|re| re.captures(&content)) {
                meta.controller_table = m.get(1).unwrap().as_str().to_string();
            }
            if let Some(m) = Regex::new(r#"descriptionReference="([^"]+)""#).ok().and_then(|re| re.captures(&content)) {
                meta.description_reference = m.get(1).unwrap().as_str().to_string();
            }

            let to_tbl_re = Regex::new(r"<toTable>([^<]+)</toTable>").unwrap();
            for tc in to_tbl_re.captures_iter(&content) {
                meta.controller_tables.insert(tc[1].trim().to_ascii_lowercase());
            }
            meta.embedded_script = extract_script(&content);

            // Form fields
            let ff_re = Regex::new(r"(?s)<FormField>(.*?)</FormField>").unwrap();
            let fname_re = Regex::new(r"<fieldName>([^<]+)</fieldName>").unwrap();
            let flabel_re = Regex::new(r"<fieldLabel>([^<]+)</fieldLabel>").unwrap();
            let gid_re = Regex::new(r"<groupID>([^<]+)</groupID>").unwrap();
            let row_re = Regex::new(r"<rowScreenPosition>([^<]+)</rowScreenPosition>").unwrap();
            let col_re = Regex::new(r"<columnScreenPosition>([^<]+)</columnScreenPosition>").unwrap();
            for ff_cap in ff_re.captures_iter(&content) {
                let ff_xml = ff_cap.get(1).unwrap().as_str();
                let f_name = fname_re.captures(ff_xml).map(|c| c[1].trim().to_string()).unwrap_or_default();
                if !f_name.is_empty() {
                    meta.form_fields.insert(f_name.clone());
                    meta.form_field_names.push(f_name.clone());
                }
                if let Some(fl_cap) = flabel_re.captures(ff_xml) {
                    meta.form_fields.insert(fl_cap.get(1).unwrap().as_str().to_string());
                }
                let group_id = gid_re.captures(ff_xml).map(|c| c[1].trim().to_string()).unwrap_or_default();
                let row = row_re.captures(ff_xml).map(|c| c[1].trim().to_string()).unwrap_or_default();
                let col = col_re.captures(ff_xml).map(|c| c[1].trim().to_string()).unwrap_or_default();
                if !f_name.is_empty() {
                    meta.form_field_positions.push(FormFieldPos {
                        field_name: f_name,
                        group_id,
                        row,
                        col,
                    });
                }
            }

            // Form commands
            let cmd_re = Regex::new(r"(?s)<FormCommand>(.*?)</FormCommand>").unwrap();
            let cname_re = Regex::new(r"<name>([^<]+)</name>").unwrap();
            let ctype_re = Regex::new(r"<type>([^<]+)</type>").unwrap();
            let catype_re = Regex::new(r"<activationType>([^<]+)</activationType>").unwrap();
            let caname_re = Regex::new(r"<activationName>([^<]+)</activationName>").unwrap();
            let csab_re = Regex::new(r"<showAsButton>([^<]+)</showAsButton>").unwrap();
            for cmd_cap in cmd_re.captures_iter(&content) {
                let cmd_xml = cmd_cap.get(1).unwrap().as_str();
                let cname = cname_re.captures(cmd_xml).map(|c| c[1].trim().to_string()).unwrap_or_default();
                if !cname.is_empty() {
                    meta.commands.insert(cname.clone());
                }
                meta.form_commands_meta.push(FormCommandMeta {
                    name: cname,
                    cmd_type: ctype_re.captures(cmd_xml).map(|c| c[1].trim().to_string()).unwrap_or_default(),
                    activation_type: catype_re.captures(cmd_xml).map(|c| c[1].trim().to_string()).unwrap_or_default(),
                    activation_name: caname_re.captures(cmd_xml).map(|c| c[1].trim().to_string()).unwrap_or_default(),
                    show_as_button: csab_re.captures(cmd_xml).map(|c| c[1].trim().to_string()).unwrap_or_default(),
                });
            }

            // Form groups (both LN 10.8 <groupID> and legacy <groupNumber>)
            let grp_re = Regex::new(r"(?s)<FormGroup>(.*?)</FormGroup>").unwrap();
            let gnum_re = Regex::new(r"<(?:groupID|groupNumber)>([^<]+)</(?:groupID|groupNumber)>").unwrap();
            let pgrp_re = Regex::new(r"<parentGroup>([^<]+)</parentGroup>").unwrap();
            let cgrp_re = Regex::new(r"<firstChildGroup>([^<]+)</firstChildGroup>").unwrap();
            let ngrp_re = Regex::new(r"<nextGroup>([^<]+)</nextGroup>").unwrap();
            let vgrp_re = Regex::new(r"<previousGroup>([^<]+)</previousGroup>").unwrap();

            for grp_cap in grp_re.captures_iter(&content) {
                let g_xml = grp_cap.get(1).unwrap().as_str();
                if let Some(gn_cap) = gnum_re.captures(g_xml) {
                    let gnum = gn_cap.get(1).unwrap().as_str().to_string();
                    let parent = pgrp_re.captures(g_xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                    let child = cgrp_re.captures(g_xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                    let nxt = ngrp_re.captures(g_xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                    let prev = vgrp_re.captures(g_xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();

                    meta.groups.insert(gnum, FormGroupInfo {
                        parent_group: parent,
                        first_child_group: child,
                        next_group: nxt,
                        previous_group: prev,
                    });
                }
            }
        }
        meta
    }

    fn parse_menu_metadata(&self, path: &Path) -> MenuMeta {
        let mut meta = MenuMeta {
            path: path.to_path_buf(),
            ..Default::default()
        };
        if let Ok(content) = fs::read_to_string(path) {
            let choice_re = Regex::new(r"(?s)<MenuChoice>(.*?)</MenuChoice>").unwrap();
            let type_re = Regex::new(r"<menuFieldType>([^<]+)</menuFieldType>").unwrap();
            let target_re = Regex::new(r"<(?:menuFieldName|menuField)>([^<]+)</(?:menuFieldName|menuField)>").unwrap();

            for cap in choice_re.captures_iter(&content) {
                let xml = cap.get(1).unwrap().as_str();
                let ctype = type_re.captures(xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                let target = target_re.captures(xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                meta.choices.push(MenuChoiceInfo { choice_type: ctype, target });
            }
        }
        meta
    }

    fn parse_report_metadata(&self, path: &Path) -> ReportMeta {
        let mut meta = ReportMeta {
            path: path.to_path_buf(),
            report_code: path.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string(),
            ..Default::default()
        };
        if let Ok(content) = fs::read_to_string(path) {
            meta.raw_xml = content.clone();
            if let Some(m) = Regex::new(r"<name>([^<]+)</name>").ok().and_then(|re| re.captures(&content)) {
                meta.report_code = m.get(1).unwrap().as_str().to_string();
            }
            if let Some(m) = Regex::new(r#"descriptionReference="([^"]+)""#).ok().and_then(|re| re.captures(&content)) {
                meta.description_reference = m.get(1).unwrap().as_str().to_string();
                meta.referenced_labels.insert(meta.description_reference.clone());
            }

            let inp_re = Regex::new(r"(?s)<InputField>(.*?)</InputField>").unwrap();
            let iname_re = Regex::new(r"<name>([^<]+)</name>").unwrap();
            let idom_re = Regex::new(r"<domain>([^<]+)</domain>").unwrap();
            let idref_re = Regex::new(r#"descriptionReference="([^"]+)""#).unwrap();

            for cap in inp_re.captures_iter(&content) {
                let xml = cap.get(1).unwrap().as_str();
                let iname = iname_re.captures(xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                let idom = idom_re.captures(xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                let idref = idref_re.captures(xml).map(|c| c.get(1).unwrap().as_str().to_string()).unwrap_or_default();
                if !idref.is_empty() {
                    meta.referenced_labels.insert(idref.clone());
                }
                meta.input_fields.push(ReportInputFieldInfo {
                    name: iname,
                    domain: idom,
                    _description_reference: idref,
                });
            }

            let spec_re = Regex::new(r#"<ReportSpecial[^>]*descriptionReference="([^"]+)""#).unwrap();
            for cap in spec_re.captures_iter(&content) {
                meta.referenced_labels.insert(cap.get(1).unwrap().as_str().to_string());
            }
        }
        meta
    }

    // ----------------------------------------------------
    // Layer 1: SCM, .admin & Layout Validation
    // ----------------------------------------------------
    fn validate_layer1_scm(&mut self) {
        let admin_file = self.activity_path.join(".admin");
        let mut registered_map: HashMap<String, (bool, bool)> = HashMap::new(); // (is_checked_out, is_created)
        let admin_loaded = if admin_file.is_file() {
            match AdminFile::load_from_path(&admin_file) {
                Ok(af) => {
                    for (p, comp) in &af.entries {
                        registered_map.insert(p.replace('\\', "/"), (comp.is_checked_out, comp.is_created));
                    }
                    true
                }
                Err(e) => {
                    self.report.add(
                        admin_file.to_str().unwrap_or(".admin"),
                        1, 1,
                        ValidationSeverity::Error,
                        &format!("Failed to parse .admin: {}", e),
                        1,
                    );
                    false
                }
            }
        } else {
            let sev = if self.strict {
                ValidationSeverity::Error
            } else {
                ValidationSeverity::Warning
            };
            self.report.add(
                self.activity_path.to_str().unwrap_or("activity"),
                1, 1,
                sev,
                "Activity missing .admin SCM file",
                1,
            );
            false
        };
        self.admin_loaded = admin_loaded;

        let managed_ext_set: HashSet<&str> = MANAGED_EXTENSIONS.iter().copied().collect();
        let disk_files = walk_managed_files(&self.activity_path, &managed_ext_set);
        let mut disk_rel_set: HashSet<String> = HashSet::new();

        for p in disk_files {
            let p_str = p.to_string_lossy();
            if is_extension_component(&p) {
                continue;
            }

            // Check for legacy plural folders (ADR 0012)
            if p_str.contains("/tables/") || p_str.contains("\\tables\\")
                || p_str.contains("/sessions/") || p_str.contains("\\sessions\\")
                || p_str.contains("/domains/") || p_str.contains("\\domains\\")
                || p_str.contains("/reports/") || p_str.contains("\\reports\\")
                || p_str.contains("/labels/") || p_str.contains("\\labels\\")
                || p_str.contains("/menus/") || p_str.contains("\\menus\\")
                || p_str.contains("/libraries/") || p_str.contains("\\libraries\\")
            {
                self.report.add(
                    &p_str, 1, 1,
                    ValidationSeverity::Error,
                    "Legacy plural directory structure detected. Components must use singular layout ({pkg}/{type}/...).",
                    1,
                );
            }

            if let Ok(rel) = p.strip_prefix(&self.activity_path) {
                let rel_str = rel.to_string_lossy().replace('\\', "/");
                disk_rel_set.insert(rel_str.clone());

                if admin_loaded {
                    match registered_map.get(&rel_str) {
                        None => {
                            self.created_or_untracked.insert(p_str.to_string());
                            let sev = if self.strict {
                                ValidationSeverity::Error
                            } else {
                                ValidationSeverity::Warning
                            };
                            self.report.add(
                                &p_str, 1, 1,
                                sev,
                                &format!("Component '{}' exists on disk but is not registered in .admin.", rel_str),
                                1,
                            );
                        }
                        Some((_, is_created)) if *is_created => {
                            self.created_or_untracked.insert(p_str.to_string());
                        }
                        _ => {}
                    }
                } else {
                    self.created_or_untracked.insert(p_str.to_string());
                }
            }
        }

        // Check missing disk files registered in .admin
        if admin_loaded {
            for (rel_path, _) in &registered_map {
                let full_cand = self.activity_path.join(rel_path);
                if is_extension_component(&full_cand) {
                    continue;
                }
                if !disk_rel_set.contains(rel_path) {
                    self.report.add(
                        admin_file.to_str().unwrap_or(".admin"),
                        1, 1,
                        ValidationSeverity::Error,
                        &format!("Component '{}' registered in .admin but not found on disk.", rel_path),
                        1,
                    );
                }
            }
        }
    }

    // ----------------------------------------------------
    // Layer 2: XML Structure & Ecore Compliance
    // ----------------------------------------------------
    fn validate_layer2_structure(&mut self) {
        // 1. Table structure
        for (_code, tdata) in &self.tables {
            let p_str = tdata.path.to_string_lossy().to_string();
            let xml = &tdata.raw_xml;

            if !xml.contains("<DR_Table") {
                self.report.add(
                    &p_str, 1, 1,
                    ValidationSeverity::Error,
                    "Expected root <DR_Table>",
                    2,
                );
            }

            // Columns datatype check (DOM-extracted)
            for (cname, dt_opt) in &tdata.column_datatypes {
                if let Some(dt_str) = dt_opt {
                    if let Ok(dt) = dt_str.parse::<i64>() {
                        if !VALID_DATATYPES.contains(&dt) {
                            self.report.add(
                                &p_str, 1, 1,
                                ValidationSeverity::Error,
                                &format!("Column '{}' has invalid nativeDatatype {}", cname, dt),
                                2,
                            );
                        }
                    } else {
                        self.report.add(
                            &p_str, 1, 1,
                            ValidationSeverity::Error,
                            &format!("Column '{}' missing valid nativeDatatype", cname),
                            2,
                        );
                    }
                } else {
                    self.report.add(
                        &p_str, 1, 1,
                        ValidationSeverity::Error,
                        &format!("Column '{}' missing valid nativeDatatype", cname),
                        2,
                    );
                }
            }

            // At least one index required
            if tdata.indexes.is_empty() {
                self.report.add(
                    &p_str, 1, 1,
                    ValidationSeverity::Error,
                    "Table must define at least one <Index>",
                    2,
                );
            }
        }

        // 2. Session structure & FormGroup tree
        for (_code, sdata) in &self.sessions {
            let p_str = sdata.path.to_string_lossy().to_string();
            let xml = &sdata.raw_xml;

            if !xml.contains("<DR_Controller") && !xml.contains("<DR_Session") {
                self.report.add(
                    &p_str, 1, 1,
                    ValidationSeverity::Error,
                    "Expected root <DR_Session> or <DR_Controller>",
                    2,
                );
            }

            for (gnum, ginfo) in &sdata.groups {
                if !ginfo.parent_group.is_empty() && ginfo.parent_group != "0" && !sdata.groups.contains_key(&ginfo.parent_group) {
                    self.report.add(
                        &p_str, 1, 1,
                        ValidationSeverity::Error,
                        &format!("FormGroup {} has non-existent parentGroup '{}'", gnum, ginfo.parent_group),
                        2,
                    );
                }
                if !ginfo.first_child_group.is_empty() && ginfo.first_child_group != "0" && !sdata.groups.contains_key(&ginfo.first_child_group) {
                    self.report.add(
                        &p_str, 1, 1,
                        ValidationSeverity::Error,
                        &format!("FormGroup {} has non-existent firstChildGroup '{}'", gnum, ginfo.first_child_group),
                        2,
                    );
                }
                if !ginfo.next_group.is_empty() && ginfo.next_group != "0" && !sdata.groups.contains_key(&ginfo.next_group) {
                    self.report.add(
                        &p_str, 1, 1,
                        ValidationSeverity::Error,
                        &format!("FormGroup {} has non-existent nextGroup '{}'", gnum, ginfo.next_group),
                        2,
                    );
                }
                if !ginfo.previous_group.is_empty() && ginfo.previous_group != "0" && !sdata.groups.contains_key(&ginfo.previous_group) {
                    self.report.add(
                        &p_str, 1, 1,
                        ValidationSeverity::Error,
                        &format!("FormGroup {} has non-existent previousGroup '{}'", gnum, ginfo.previous_group),
                        2,
                    );
                }
            }

            // .ses UI Checks: showAsButton=false and overlapping (rowScreenPosition, columnScreenPosition)
            for cmd in &sdata.form_commands_meta {
                if cmd.show_as_button.eq_ignore_ascii_case("false")
                    && (matches!(cmd.cmd_type.as_str(), "1" | "user" | "")
                        || matches!(cmd.activation_type.as_str(), "5" | "function" | ""))
                {
                    self.report.add(
                        &p_str,
                        1,
                        1,
                        ValidationSeverity::Warning,
                        &format!(
                            "FormCommand '{}' has <showAsButton>false</showAsButton>; dialog/user command may be hidden from toolbar.",
                            cmd.name
                        ),
                        2,
                    );
                }
            }

            let mut seen_pos: HashMap<(String, String, String), String> = HashMap::new();
            for fp in &sdata.form_field_positions {
                if !fp.row.is_empty() && fp.row != "0" && !fp.col.is_empty() && fp.col != "0" {
                    let key = (fp.group_id.clone(), fp.row.clone(), fp.col.clone());
                    if let Some(prev) = seen_pos.get(&key) {
                        if prev != &fp.field_name {
                            self.report.add(
                                &p_str,
                                1,
                                1,
                                ValidationSeverity::Warning,
                                &format!(
                                    "FormField '{}' and '{}' overlap at row={}, col={} in groupID={}.",
                                    prev, fp.field_name, fp.row, fp.col, fp.group_id
                                ),
                                2,
                            );
                        }
                    } else {
                        seen_pos.insert(key, fp.field_name.clone());
                    }
                }
            }

            // Session Script-Form Parity (embedded <DR_Module><Source><expression>)
            if let Some(ref script) = sdata.embedded_script {
                if !script.trim().is_empty() {
                    let script_low = script.to_ascii_lowercase();
                    for fname in &sdata.form_field_names {
                        let f_low = fname.to_ascii_lowercase();
                        if f_low.is_empty() || f_low == "label.only" {
                            continue;
                        }
                        let is_tbl_field = if let Some((t, _)) = f_low.split_once('.') {
                            sdata.controller_tables.contains(t) || (!sdata.controller_table.is_empty() && t == sdata.controller_table.to_ascii_lowercase())
                        } else {
                            false
                        };
                        if !is_tbl_field {
                            let re_ext = Regex::new(&format!(r"(?i)\bextern\b[^\n]*\b{}\b", regex::escape(&f_low))).unwrap();
                            if !re_ext.is_match(&script_low) {
                                self.report.add(
                                    &p_str,
                                    1,
                                    1,
                                    ValidationSeverity::Warning,
                                    &format!(
                                        "Session FormField '{}' is not bound to a controller table and has no matching 'extern' declaration in embedded UI script.",
                                        fname
                                    ),
                                    3,
                                );
                            }
                        }
                    }
                    for cmd in &sdata.form_commands_meta {
                        if matches!(cmd.activation_type.as_str(), "5" | "function") && !cmd.activation_name.is_empty() {
                            let re_fn = Regex::new(&format!(r"(?i)\bfunction\s+extern\b[^\n]*\b{}\s*\(", regex::escape(&cmd.activation_name))).unwrap();
                            if !re_fn.is_match(script) {
                                self.report.add(
                                    &p_str,
                                    1,
                                    1,
                                    ValidationSeverity::Warning,
                                    &format!(
                                        "FormCommand '{}' activationName '{}' has no matching 'function extern' handler in embedded UI script.",
                                        cmd.name, cmd.activation_name
                                    ),
                                    3,
                                );
                            }
                        }
                    }
                }
            }
        }

        // 3. Report root check
        for (_code, rdata) in &self.reports {
            let p_str = rdata.path.to_string_lossy().to_string();
            if !rdata.raw_xml.contains("<DR_Report") {
                self.report.add(
                    &p_str, 1, 1,
                    ValidationSeverity::Error,
                    "Expected root <DR_Report>",
                    2,
                );
            }
        }

        // 4. Single-line TDE XML check (Eclipse CMComponentProperties ClassCastException prevention)
        self.multiline_files.clear();
        let managed_ext_set: HashSet<&str> = MANAGED_EXTENSIONS.iter().copied().collect();
        for p in walk_managed_files(&self.activity_path, &managed_ext_set) {
            if is_extension_component(&p) {
                continue;
            }
            if let Ok(raw_txt) = fs::read_to_string(&p) {
                if raw_txt.contains('<') && has_multiline_outside_script(&raw_txt) {
                    let p_str = p.to_string_lossy().to_string();
                    self.multiline_files.push(p);
                    self.report.add(
                        &p_str,
                        1,
                        1,
                        ValidationSeverity::Error,
                        "Component XML must be single-line (no inter-tag whitespace/newlines outside CDATA/expression) for Eclipse CMComponentProperties compatibility.",
                        2,
                    );
                }
            }
        }
    }

    fn owner_pkg_for_path(&self, comp_path: &Path, comp_code: &str) -> String {
        if let Ok(rel) = comp_path.strip_prefix(&self.activity_path) {
            if let Some(first) = rel.components().next() {
                let first_str = first.as_os_str().to_string_lossy().to_ascii_lowercase();
                if self.packages.contains(&first_str) {
                    return first_str;
                }
            }
        }
        if comp_code.len() >= 2 {
            comp_code[..2].to_ascii_lowercase()
        } else {
            String::new()
        }
    }

    // ----------------------------------------------------
    // Layer 3: Cross-Object Reference Integrity
    // ----------------------------------------------------
    fn validate_layer3_cross_references(&mut self) {
        use std::sync::OnceLock;
        static ATTR_DREF_RE: OnceLock<Regex> = OnceLock::new();
        static ELEM_DREF_RE: OnceLock<Regex> = OnceLock::new();
        static FLBL_RE: OnceLock<Regex> = OnceLock::new();
        static CMD_LBL_ATTR_RE: OnceLock<Regex> = OnceLock::new();
        static CMD_BLOCK_RE: OnceLock<Regex> = OnceLock::new();
        static IDX_BLOCK_RE: OnceLock<Regex> = OnceLock::new();

        // (label_code, file_path, is_field_label, owner_pkg)
        let mut referenced_labels: HashSet<(String, String, bool, String)> = HashSet::new();
        let attr_dref_re = ATTR_DREF_RE.get_or_init(|| Regex::new(r#"descriptionReference="([^"]+)""#).unwrap());
        let elem_dref_re = ELEM_DREF_RE.get_or_init(|| Regex::new(r"<descriptionReference>([^<]+)</descriptionReference>").unwrap());
        let flbl_re = FLBL_RE.get_or_init(|| Regex::new(r"<fieldLabel>([^<]+)</fieldLabel>").unwrap());
        let cmd_lbl_attr_re = CMD_LBL_ATTR_RE.get_or_init(|| Regex::new(r#"<FormCommand[^>]*descriptionReference="([^"]+)""#).unwrap());
        let cmd_block_re = CMD_BLOCK_RE.get_or_init(|| Regex::new(r"(?s)<FormCommand\b[^>]*>.*?</FormCommand>").unwrap());
        let idx_block_re = IDX_BLOCK_RE.get_or_init(|| Regex::new(r"(?s)<Index\b[^>]*>.*?</Index>").unwrap());

        // 1. Collect referenced labels from tables
        for (code, tdata) in &self.tables {
            let p_str = tdata.path.to_string_lossy().to_string();
            let opkg = self.owner_pkg_for_path(&tdata.path, code);
            if !tdata.description_reference.is_empty() {
                self.desc_labels.insert(tdata.description_reference.to_ascii_lowercase());
                referenced_labels.insert((tdata.description_reference.clone(), p_str.clone(), false, opkg.clone()));
            }
            for cap in attr_dref_re.captures_iter(&tdata.raw_xml) {
                referenced_labels.insert((cap.get(1).unwrap().as_str().to_string(), p_str.clone(), false, opkg.clone()));
            }
            for cap in elem_dref_re.captures_iter(&tdata.raw_xml) {
                referenced_labels.insert((cap.get(1).unwrap().as_str().to_string(), p_str.clone(), false, opkg.clone()));
            }
            for m in idx_block_re.find_iter(&tdata.raw_xml) {
                if let Some(cap) = elem_dref_re.captures(m.as_str()) {
                    self.desc_labels.insert(cap.get(1).unwrap().as_str().to_ascii_lowercase());
                }
            }
        }

        // 2. Collect referenced labels from sessions
        for (code, sdata) in &self.sessions {
            let p_str = sdata.path.to_string_lossy().to_string();
            let opkg = self.owner_pkg_for_path(&sdata.path, code);
            if !sdata.description_reference.is_empty() {
                self.desc_labels.insert(sdata.description_reference.to_ascii_lowercase());
                referenced_labels.insert((sdata.description_reference.clone(), p_str.clone(), false, opkg.clone()));
            }
            for cap in flbl_re.captures_iter(&sdata.raw_xml) {
                referenced_labels.insert((cap.get(1).unwrap().as_str().to_string(), p_str.clone(), true, opkg.clone()));
            }
            for cap in cmd_lbl_attr_re.captures_iter(&sdata.raw_xml) {
                let lbl = cap.get(1).unwrap().as_str().to_string();
                self.command_labels.insert(lbl.to_ascii_lowercase());
                referenced_labels.insert((lbl, p_str.clone(), false, opkg.clone()));
            }
            for m in cmd_block_re.find_iter(&sdata.raw_xml) {
                if let Some(cap) = elem_dref_re.captures(m.as_str()) {
                    let lbl = cap.get(1).unwrap().as_str().to_string();
                    self.command_labels.insert(lbl.to_ascii_lowercase());
                    referenced_labels.insert((lbl, p_str.clone(), false, opkg.clone()));
                }
            }
        }

        // 3. Collect referenced labels from reports
        for (code, rdata) in &self.reports {
            let p_str = rdata.path.to_string_lossy().to_string();
            let opkg = self.owner_pkg_for_path(&rdata.path, code);
            for lbl in &rdata.referenced_labels {
                referenced_labels.insert((lbl.clone(), p_str.clone(), false, opkg.clone()));
            }
        }

        let catalog: HashSet<String> = self
            .labels
            .iter()
            .chain(self.reference_labels.iter())
            .chain(self.server_labels.iter())
            .cloned()
            .collect();

        // Validate labels against catalog (skip server-resident labels when referencing component
        // is an already checked-in server component unless --strict or --online).
        for (lbl_code, ref_path, is_field_label, opkg) in referenced_labels {
            if !self.strict && !self.online && self.admin_loaded && !self.created_or_untracked.contains(&ref_path) {
                continue;
            }
            let lbl_lower = lbl_code.to_ascii_lowercase();
            if is_field_label {
                if lbl_lower.starts_with("tc") && opkg != "tc" {
                    if self.online {
                        let prefixed = format!("{opkg}{lbl_lower}");
                        if !catalog.contains(&lbl_lower) && !catalog.contains(&prefixed) {
                            self.report.add(
                                &ref_path, 1, 1,
                                ValidationSeverity::Error,
                                &format!("Referenced label '{}' not found in server 'tc' or activity label catalog.", lbl_code),
                                3,
                            );
                        }
                    }
                    continue;
                }

                let prefixed = if opkg.is_empty() { lbl_lower.clone() } else { format!("{opkg}{lbl_lower}") };
                let found = catalog.contains(&prefixed) || catalog.contains(&lbl_lower);
                if !found {
                    self.report.add(
                        &ref_path, 1, 1,
                        ValidationSeverity::Error,
                        &format!("Referenced label '{}' (from fieldLabel '{}') not found in activity label catalog.", prefixed, lbl_code),
                        3,
                    );
                }
            } else {
                let is_local = self.packages.iter().any(|pkg| lbl_lower.starts_with(pkg));
                if is_local {
                    let found = catalog.contains(&lbl_lower)
                        || catalog.iter().any(|l| l == &lbl_lower || l.ends_with(&lbl_lower) || lbl_lower.ends_with(l));
                    if !found {
                        self.report.add(
                            &ref_path, 1, 1,
                            ValidationSeverity::Error,
                            &format!("Referenced label '{}' not found in activity label catalog.", lbl_code),
                            3,
                        );
                    }
                } else if self.online && !catalog.contains(&lbl_lower) {
                    self.report.add(
                        &ref_path, 1, 1,
                        ValidationSeverity::Error,
                        &format!("Referenced label '{}' not found in activity or server label catalog.", lbl_code),
                        3,
                    );
                }
            }
        }

        // 4. Session controller table & form field cross-checks
        for (_code, sdata) in &self.sessions {
            let p_str = sdata.path.to_string_lossy().to_string();
            let ctrl_table = &sdata.controller_table;
            if !ctrl_table.is_empty() {
                let ctrl_lower = ctrl_table.to_ascii_lowercase();
                let found_table = self.tables.get(&ctrl_lower).or_else(|| {
                    self.tables.values().find(|t| {
                        t.table_code.eq_ignore_ascii_case(ctrl_table)
                            || ctrl_lower.ends_with(&t.table_code.to_ascii_lowercase())
                    })
                });
                if let Some(tdata) = found_table {
                    for ff in &sdata.form_fields {
                        if ff.contains('.') {
                            let col_name = ff.split('.').last().unwrap_or(ff);
                            if !tdata.columns.contains(ff) && !tdata.columns.contains(col_name) {
                                self.report.add(
                                    &p_str, 1, 1,
                                    ValidationSeverity::Warning,
                                    &format!("Session FormField '{}' does not match any column in controller table '{}'.", ff, ctrl_table),
                                    3,
                                );
                            }
                        }
                    }
                }
            }
        }

        // 5. Table index column cross-checks
        for (_code, tdata) in &self.tables {
            let p_str = tdata.path.to_string_lossy().to_string();
            for idx_cols in &tdata.indexes {
                for ic in idx_cols {
                    if !tdata.columns.contains(ic) && !tdata.columns.contains(&format!("{}.{}", tdata.table_code, ic)) {
                        self.report.add(
                            &p_str, 1, 1,
                            ValidationSeverity::Error,
                            &format!("IndexColumn '{}' does not match any defined Column in table '{}'.", ic, tdata.table_code),
                            3,
                        );
                    }
                }
            }
        }

        // 6. Menu choice target sessions
        for (_code, mdata) in &self.menus {
            let p_str = mdata.path.to_string_lossy().to_string();
            for ch in &mdata.choices {
                if ch.choice_type == "1" {
                    let tgt_lower = ch.target.to_ascii_lowercase();
                    if self.packages.iter().any(|pkg| tgt_lower.starts_with(pkg)) {
                        if !self.sessions.contains_key(&tgt_lower) {
                            self.report.add(
                                &p_str, 1, 1,
                                ValidationSeverity::Warning,
                                &format!("MenuChoice target session '{}' not found in current activity.", ch.target),
                                3,
                            );
                        }
                    }
                }
            }
        }

        // 7. Report input domains
        for (_code, rdata) in &self.reports {
            let p_str = rdata.path.to_string_lossy().to_string();
            for inp in &rdata.input_fields {
                let dom = &inp.domain;
                if !dom.is_empty() {
                    let dom_lower = dom.to_ascii_lowercase();
                    if self.packages.iter().any(|pkg| dom_lower.starts_with(pkg)) {
                        if !self.domains.contains_key(&dom_lower) {
                            self.report.add(
                                &p_str, 1, 1,
                                ValidationSeverity::Warning,
                                &format!("Report input field '{}' references unknown activity domain '{}'.", inp.name, dom),
                                3,
                            );
                        }
                    }
                }
            }
        }
    }

    // ----------------------------------------------------
    // Layer 4: Static 4GL Script Validation
    // ----------------------------------------------------
    fn validate_layer4_scripts(&mut self) {
        let mut script_targets: Vec<(PathBuf, String, String)> = Vec::new(); // (path, xml, mode)

        for (_code, tdata) in &self.tables {
            script_targets.push((tdata.path.clone(), tdata.raw_xml.clone(), "table".to_string()));
        }
        for (_code, sdata) in &self.sessions {
            script_targets.push((sdata.path.clone(), sdata.raw_xml.clone(), "session".to_string()));
        }
        for (_code, rdata) in &self.reports {
            script_targets.push((rdata.path.clone(), rdata.raw_xml.clone(), "report".to_string()));
        }
        for (_code, path) in &self.libraries {
            if let Ok(xml) = fs::read_to_string(path) {
                script_targets.push((path.clone(), xml, "library".to_string()));
            }
        }
        for (_code, path) in &self.functions {
            if let Ok(xml) = fs::read_to_string(path) {
                script_targets.push((path.clone(), xml, "function".to_string()));
            }
        }

        for (path, xml, mode) in script_targets {
            if let Some(script) = extract_script(&xml) {
                if !script.trim().is_empty() {
                    let p_str = path.to_string_lossy().to_string();
                    let diags = audit_content(&script, &p_str, false, Some(&mode));
                    for d in diags {
                        let sev = match d.severity {
                            LinterSeverity::Error => ValidationSeverity::Error,
                            LinterSeverity::Warning | LinterSeverity::Info => ValidationSeverity::Warning,
                        };
                        self.report.add(&d.file, d.line, d.column, sev, &d.message, 4);
                    }
                }
            }
        }
    }

    // ----------------------------------------------------
    // Safe Fixes Execution
    // ----------------------------------------------------
    fn default_app_and_version(&self) -> (String, String) {
        let folder = self.activity_path.file_name().and_then(|s| s.to_str()).unwrap_or("");
        let app = if let (Some(s), Some(e)) = (folder.find('['), folder.find(']')) {
            if e > s + 1 {
                folder[s + 1..e].to_string()
            } else {
                "EXTce01108".to_string()
            }
        } else {
            "EXTce01108".to_string()
        };
        (app, "B61O_a_ext".to_string())
    }

    fn execute_safe_fixes(&mut self) {
        // 0. Compact writable pretty-printed component XMLs
        for p in self.multiline_files.clone() {
            if p.is_file() {
                let is_ro = fs::metadata(&p).map(|m| m.permissions().readonly()).unwrap_or(true);
                if !is_ro {
                    if let Ok(raw_txt) = fs::read_to_string(&p) {
                        let compacted = compact_tde_xml(&raw_txt);
                        if compacted != raw_txt && fs::write(&p, &compacted).is_ok() {
                            let fname = p.file_name().and_then(|s| s.to_str()).unwrap_or("file");
                            self.report.repaired_items.push(format!("Compacted single-line XML: {}", fname));
                        }
                    }
                }
            }
        }

        // 1. Fix missing labels
        let missing_labels: Vec<String> = self
            .report
            .diagnostics
            .iter()
            .filter_map(|d| {
                if d.layer == 3 && d.message.starts_with("Referenced label '") && d.message.contains("not found in activity label catalog.") {
                    let start = "Referenced label '".len();
                    let end = d.message[start..].find('\'')? + start;
                    Some(d.message[start..end].to_ascii_lowercase())
                } else {
                    None
                }
            })
            .collect();

        let (app_code, ver_id) = self.default_app_and_version();

        for lbl_code in missing_labels {
            let pkg = self.packages.iter().find(|p| lbl_code.starts_with(p.as_str())).cloned();
            if let Some(p) = pkg {
                let lbl_dir = self.activity_path.join(&p).join("label");
                let _ = fs::create_dir_all(&lbl_dir);
                let lbl_file = lbl_dir.join(format!("{}.lbl", lbl_code));

                if !lbl_file.is_file() {
                    let lbl_ctx = if self.command_labels.contains(&lbl_code) {
                        10
                    } else if self.desc_labels.contains(&lbl_code) {
                        2
                    } else {
                        1
                    };
                    let xml_content = generate_label_xml_with_context(
                        &lbl_code,
                        &lbl_code,
                        &ver_id,
                        &app_code,
                        Some(30),
                        None,
                        lbl_ctx,
                    );
                    if fs::write(&lbl_file, xml_content).is_ok() {
                        self.report.repaired_items.push(format!("Auto-generated missing label: {}.lbl", lbl_code));
                        self.labels.insert(lbl_code);
                    }
                }
            }
        }

        // 2. Synchronize .admin registration
        let admin_file = self.activity_path.join(".admin");
        if admin_file.is_file() {
            if let Ok(mut af) = AdminFile::load_from_path(&admin_file) {
                let mut registered_set: HashSet<String> = af
                    .entries
                    .keys()
                    .map(|k| k.replace('\\', "/"))
                    .collect();

                let managed_ext_set: HashSet<&str> = MANAGED_EXTENSIONS.iter().copied().collect();
                let disk_files = walk_managed_files(&self.activity_path, &managed_ext_set);
                let mut added_count = 0;

                for p in disk_files {
                    if is_extension_component(&p) {
                        continue;
                    }
                    if let Ok(rel) = p.strip_prefix(&self.activity_path) {
                        let rel_str = rel.to_string_lossy().replace('\\', "/");
                        if !registered_set.contains(&rel_str) {
                            af.after_create(&rel_str);
                            registered_set.insert(rel_str);
                            added_count += 1;
                        }
                    }
                }

                if added_count > 0 {
                    if af.save_to_path(&admin_file).is_ok() {
                        self.report.repaired_items.push(format!(
                            "Registered {} untracked component(s) in .admin",
                            added_count
                        ));
                    }
                }
            }
        }
    }
}

pub fn validate_activity(activity_path: &Path, strict: bool, fix: bool) -> ValidationReport {
    let mut validator = ActivityValidator::new(activity_path.to_path_buf(), strict, fix);
    validator.run();
    validator.report
}

fn walk_managed_files(dir: &Path, managed_exts: &HashSet<&str>) -> Vec<PathBuf> {
    let mut files = Vec::new();
    if !dir.is_dir() {
        return files;
    }
    if let Ok(entries) = fs::read_dir(dir) {
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                let name = p.file_name().and_then(|n| n.to_str()).unwrap_or("");
                if !name.starts_with('.') || name == ".admin" {
                    if name != ".admin" {
                        files.extend(walk_managed_files(&p, managed_exts));
                    }
                }
            } else if p.is_file() {
                if let Some(ext) = p.extension().and_then(|e| e.to_str()) {
                    let dot_ext = format!(".{}", ext.to_ascii_lowercase());
                    if managed_exts.contains(dot_ext.as_str()) {
                        files.push(p);
                    }
                }
            }
        }
    }
    files
}

fn is_extension_component(path: &Path) -> bool {
    let p_str = path.to_string_lossy().to_ascii_lowercase();
    p_str.contains("/ess/") || p_str.contains("\\ess\\")
        || p_str.contains("/est/") || p_str.contains("\\est\\")
        || p_str.contains("/esb/") || p_str.contains("\\esb\\")
        || p_str.contains("/esm/") || p_str.contains("\\esm\\")
        || p_str.contains("/esr/") || p_str.contains("\\esr\\")
        || p_str.ends_with(".eso")
        || p_str.ends_with(".eto")
        || p_str.ends_with(".ere")
}

fn glob_matches(pattern: &str, text: &str) -> bool {
    let p: Vec<char> = pattern.chars().collect();
    let t: Vec<char> = text.chars().collect();
    let (m, n) = (p.len(), t.len());
    let mut dp = vec![vec![false; n + 1]; m + 1];
    dp[0][0] = true;
    for i in 1..=m {
        if p[i - 1] == '*' {
            dp[i][0] = dp[i - 1][0];
        }
    }
    for i in 1..=m {
        for j in 1..=n {
            if p[i - 1] == '*' {
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            } else if p[i - 1] == '?' || p[i - 1] == t[j - 1] {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }
    dp[m][n]
}
