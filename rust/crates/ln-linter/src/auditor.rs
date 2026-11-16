use quick_xml::events::Event;
use quick_xml::Reader;
use rayon::prelude::*;
use regex::Regex;
use std::collections::HashSet;
use std::fs;
use std::path::Path;

use ln_kb::{
    lookup_function,
    syntax::{choice_sections, program_sections, report_sections, sub_sections},
};

use crate::ast::ASTParser4GL;
use crate::dd_cache::DataDictionaryCache;
use crate::diagnostic::{Diagnostic, Severity};

pub const STD_EXTENSION_INCLUDES: &[&str] = &[
    "bic_dal2", "bic_tableext", "bic_sessionext", "bic_text",
    "bic_interface", "bic_dam", "bic_view",
];

pub const STD_FRAMEWORK_FUNCTIONS: &[&str] = &[
    "get.extension.point.version", "ext.is.cdfs.of.ref.tables.selected",
    "ext.get.form.fields", "ext.get.session.indices",
    "ext.get.command.extensions", "ext.get.report.extensions",
];

fn is_preceded_by_dot_or_word(text: &str, start_idx: usize) -> bool {
    if start_idx == 0 {
        return false;
    }
    let prev_char = text[..start_idx].chars().next_back().unwrap_or(' ');
    prev_char == '.' || prev_char.is_alphanumeric() || prev_char == '_'
}

enum Extracted4gl<'a> {
    Raw(&'a str),
    Extracted(String),
    EmptyXml,
}

/// Extracts and XML-unescapes `<expression>` payloads when auditing Single-XML
/// LN Studio component files (`.lib`, `.tbl`, `.ses`, `.rpt`, `.fnc`).
fn extract_4gl_from_xml_if_needed<'a>(raw: &'a str) -> Extracted4gl<'a> {
    let trimmed = raw.trim_start();
    let looks_like_xml = trimmed.starts_with("<?xml")
        || (trimmed.starts_with('<')
            && (trimmed.contains("<DR_")
                || trimmed.contains("<Library")
                || trimmed.contains("<expression>")));
    if !looks_like_xml {
        return Extracted4gl::Raw(raw);
    }

    let mut reader = Reader::from_str(raw);
    reader.config_mut().trim_text(false);
    let mut expressions: Vec<String> = Vec::new();
    let mut in_expr_depth: usize = 0;
    let mut current_expr = String::new();

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                if e.name().as_ref() == b"expression" {
                    in_expr_depth += 1;
                    if in_expr_depth == 1 {
                        current_expr.clear();
                    }
                }
            }
            Ok(Event::Text(e)) => {
                if in_expr_depth > 0 {
                    if let Ok(unescaped) = e.unescape() {
                        current_expr.push_str(&unescaped);
                    }
                }
            }
            Ok(Event::CData(e)) => {
                if in_expr_depth > 0 {
                    current_expr.push_str(&String::from_utf8_lossy(e.as_ref()));
                }
            }
            Ok(Event::End(e)) => {
                if e.name().as_ref() == b"expression" && in_expr_depth > 0 {
                    in_expr_depth -= 1;
                    if in_expr_depth == 0 && !current_expr.trim().is_empty() {
                        expressions.push(std::mem::take(&mut current_expr));
                    }
                }
            }
            Ok(Event::Eof) | Err(_) => break,
            _ => {}
        }
    }

    if expressions.is_empty() {
        Extracted4gl::EmptyXml
    } else {
        Extracted4gl::Extracted(expressions.join("\n"))
    }
}

pub struct Auditor4GL {
    pub cloud_mode: bool,
    pub min_severity: Severity,
    pub strict: bool,
    pub main_table: Option<String>,
    pub auto_fetch_dd: bool,
    pub dd_cache: Option<DataDictionaryCache>,
    all_known_sections: Vec<String>,
}

impl Default for Auditor4GL {
    fn default() -> Self {
        Self::new()
    }
}

impl Auditor4GL {
    pub fn new() -> Self {
        let mut sections = Vec::new();
        sections.extend(program_sections().iter().map(|s| s.to_lowercase()));
        sections.extend(choice_sections().iter().map(|s| s.to_lowercase()));
        sections.extend(sub_sections().iter().map(|s| s.to_lowercase()));
        sections.extend(report_sections().iter().map(|s| s.to_lowercase()));
        sections.sort();
        sections.dedup();

        Self {
            cloud_mode: false,
            min_severity: Severity::Info,
            strict: false,
            main_table: None,
            auto_fetch_dd: false,
            dd_cache: None,
            all_known_sections: sections,
        }
    }

    pub fn with_cloud_mode(mut self, cloud_mode: bool) -> Self {
        self.cloud_mode = cloud_mode;
        self
    }

    pub fn with_min_severity(mut self, min_severity: Severity) -> Self {
        self.min_severity = min_severity;
        self
    }

    pub fn with_strict(mut self, strict: bool) -> Self {
        self.strict = strict;
        self
    }

    pub fn with_main_table(mut self, main_table: impl Into<String>) -> Self {
        self.main_table = Some(main_table.into().to_lowercase().trim().to_string());
        self
    }

    pub fn with_dd_cache(mut self, cache: DataDictionaryCache) -> Self {
        self.dd_cache = Some(cache);
        self
    }

    pub fn with_auto_fetch_dd(mut self, auto_fetch: bool) -> Self {
        self.auto_fetch_dd = auto_fetch;
        self
    }

    pub fn is_valid_section_header(&self, token: &str) -> bool {
        let t = token.trim().to_lowercase();
        if !t.ends_with(':') {
            return false;
        }

        if self.all_known_sections.contains(&t) {
            return true;
        }

        if t.starts_with("field.") || t.starts_with("choice.") || t.starts_with("zoom.from.") {
            return true;
        }

        let re_group = Regex::new(r"^group\.[0-9a-zA-Z_]+:$").unwrap();
        if re_group.is_match(&t) {
            return true;
        }

        let re_form = Regex::new(r"^form\.[0-9a-zA-Z_]+:$").unwrap();
        if re_form.is_match(&t) {
            return true;
        }

        let re_report = Regex::new(r"^(header|detail|before|after)\.[0-9]+:$").unwrap();
        if re_report.is_match(&t) {
            return true;
        }

        false
    }

    pub fn detect_archetype(&self, file_path: &str, content: &str) -> String {
        let path_lower = file_path.to_lowercase();
        if path_lower.ends_with(".dal") || path_lower.ends_with(".dalsrc") || path_lower.contains("dal2") {
            return "dal2".to_string();
        }
        if path_lower.ends_with(".ue") || path_lower.contains("uedll") {
            return "uedll".to_string();
        }

        let normalized_path = path_lower.replace('\\', "/");
        let re_session_code = Regex::new(r"[a-z]{5}\d{3,4}[ms]\d{3}").unwrap();
        let re_m_code = Regex::new(r"m\d{3}").unwrap();

        let is_session = re_session_code.is_match(&path_lower)
            || re_m_code.is_match(&path_lower)
            || content.to_lowercase().contains("bic_sessionext")
            || content.to_lowercase().contains("bic_interface")
            || normalized_path.contains("/session")
            || normalized_path.contains("ess");

        if is_session {
            return "general".to_string();
        }

        let content_lower = content.to_lowercase();
        if content_lower.contains("function extern long before.save.object")
            || content_lower.contains("dal.set.error.message")
            || content_lower.contains("bic_tableext")
        {
            return "dal2".to_string();
        }

        if (path_lower.contains("table") || path_lower.contains("est"))
            && (path_lower.contains("_ext.4gl") || path_lower.contains(".4gl") || path_lower.contains(".cln"))
        {
            return "dal2".to_string();
        }

        if content_lower.contains("bic_dal2") {
            return "dal2".to_string();
        }

        if content_lower.contains("ue.before.save") || content_lower.contains("ue.after.save") {
            return "uedll".to_string();
        }

        "general".to_string()
    }

    pub fn infer_main_table(&self, file_path: &str, content: &str, mode: &str) -> Option<String> {
        if let Some(ref tbl) = self.main_table {
            return Some(tbl.clone());
        }

        if !file_path.is_empty() && file_path != "<stdin>" {
            if let Some(stem_os) = Path::new(file_path).file_stem() {
                let mut stem = stem_os.to_string_lossy().to_lowercase();
                if stem.ends_with("_ext") {
                    stem = stem[..stem.len() - 4].to_string();
                }
                let re_tbl = Regex::new(r"^[a-z]{5}\d{3}$").unwrap();
                if re_tbl.is_match(&stem) {
                    return Some(stem);
                }
            }
        }

        if mode == "dal2" {
            let re_hook_tbl = Regex::new(r"\bfunction\s+extern\s+[a-zA-Z0-9_.]+\s+([a-z]{5}\d{3})\.[a-z0-9_]+\s*\(").unwrap();
            if let Some(caps) = re_hook_tbl.captures(content) {
                return Some(caps.get(1).unwrap().as_str().to_lowercase());
            }
        }

        None
    }

    pub fn is_string_domain(&self, domain_name: &str, dd_cache: Option<&DataDictionaryCache>) -> bool {
        let dmn_lower = domain_name.trim().to_lowercase();
        if let Some(cache) = dd_cache {
            if let Some(meta) = cache.get_domain(&dmn_lower) {
                if let Some(dt_val) = &meta.datatype {
                    let dt = dt_val.to_string().to_lowercase();
                    if dt.contains("string") || dt.contains("1") || dt.contains("2") || dt.contains("str") {
                        return true;
                    }
                    if dt.contains("long") || dt.contains("double") || dt.contains("float")
                        || dt.contains("date") || dt.contains("utc") || dt.contains("enum")
                        || dt.contains("boolean")
                    {
                        return false;
                    }
                }
            }
        }

        let non_string_suffixes = [
            "amnt", "qana", "wght", "amt", "docn", "lino", "pono", "sqnb",
            "year", "peri", "date", "dat", "time", "yesno", "bool", "trec", "stdd",
        ];
        let leaf = dmn_lower.split('.').last().unwrap_or("");
        if non_string_suffixes.contains(&leaf)
            || non_string_suffixes.iter().any(|s| dmn_lower.ends_with(&format!(".{s}")) || dmn_lower.ends_with(&format!("_{s}")))
        {
            return false;
        }

        let string_indicators = [
            "bpid", "ttyp", "orno", "item", "sotp", "cprj", "nama", "desc",
            "dsca", "text", "mess", "user", "code", "clan", "cntr",
        ];
        if string_indicators.contains(&leaf)
            || string_indicators.iter().any(|s| dmn_lower.ends_with(&format!(".{s}")))
        {
            return true;
        }

        if dmn_lower.starts_with("tccom.")
            || matches!(dmn_lower.as_str(), "tcorno" | "tcitem" | "tcsotp" | "tcclot" | "tccitg" | "tcsern")
        {
            return true;
        }

        if dmn_lower.contains("str") {
            return true;
        }

        false
    }

    fn find_closest_section(&self, misspelled: &str) -> Option<String> {
        let mut best: Option<(&str, f64)> = None;
        for s in &self.all_known_sections {
            let sim = string_similarity(misspelled, s);
            if sim >= 0.6 {
                if let Some((_, best_sim)) = best {
                    if sim > best_sim {
                        best = Some((s, sim));
                    }
                } else {
                    best = Some((s, sim));
                }
            }
        }
        best.map(|(s, _)| s.to_string())
    }

    fn resolve_dd_cache<'a>(&'a self, file_path: &str, override_cache: Option<&'a DataDictionaryCache>) -> Option<&'a DataDictionaryCache> {
        if override_cache.is_some() {
            return override_cache;
        }
        if self.dd_cache.is_some() {
            return self.dd_cache.as_ref();
        }

        // Try searching upward from target path
        if !file_path.is_empty() && file_path != "<stdin>" {
            let mut cur = Path::new(file_path).parent();
            while let Some(dir) = cur {
                let candidate = dir.join(".ln_dd_cache.json");
                if candidate.exists() {
                    // Cache exists on disk; cannot return borrow of local so rely on configured dd_cache
                    break;
                }
                cur = dir.parent();
            }
        }

        None
    }

    pub fn audit_content(
        &self,
        content: &str,
        file_path: &str,
        mode_override: Option<&str>,
        dd_cache_override: Option<&DataDictionaryCache>,
    ) -> Vec<Diagnostic> {
        let extracted_buf;
        let content = match extract_4gl_from_xml_if_needed(content) {
            Extracted4gl::Raw(s) => s,
            Extracted4gl::Extracted(s) => {
                extracted_buf = s;
                &extracted_buf
            }
            Extracted4gl::EmptyXml => return Vec::new(),
        };

        let mode = match mode_override {
            Some(m) if m != "auto" => m.to_string(),
            _ => self.detect_archetype(file_path, content),
        };

        let effective_main_table = self.infer_main_table(file_path, content, &mode);
        let active_dd = self.resolve_dd_cache(file_path, dd_cache_override);

        let mut diagnostics = Vec::new();
        let lines: Vec<&str> = content.lines().collect();

        // Run AST Tokenizer & Parser (SYN001 & CAV003 call-graph)
        let mut ast_parser = ASTParser4GL::new(content, file_path);
        let cleaned_lines = ast_parser.preprocess_and_tokenize(content).to_vec();
        let (ast_diags, _) = ast_parser.parse();
        diagnostics.extend(ast_diags.iter().cloned());
        let transitive_tx_map = ast_parser.find_transitive_tx_functions();
        let ast_functions = ast_parser.functions.clone();

        // Includes collection
        let mut includes_found = HashSet::new();
        let re_inc = Regex::new(r#"^\s*#include\s+[<"]([a-zA-Z0-9_.]+)[>"]"#).unwrap();
        for raw_line in &lines {
            if let Some(caps) = re_inc.captures(raw_line) {
                let mut inc_name = caps.get(1).unwrap().as_str().to_lowercase();
                if inc_name.ends_with(".h") {
                    inc_name = inc_name[..inc_name.len() - 2].to_string();
                }
                includes_found.insert(inc_name);
            }
        }

        // Pass 1: Extract `table t<tablename>` declarations (TBL001)
        let mut declared_tables = HashSet::new();
        let re_tbl_keyword = Regex::new(r"\btable\b").unwrap();
        let re_t_name = Regex::new(r"\bt([a-z]{5}\d{3})\b").unwrap();
        for code_line in &cleaned_lines {
            if re_tbl_keyword.is_match(code_line) {
                for m_tbl in re_t_name.captures_iter(code_line) {
                    declared_tables.insert(m_tbl.get(1).unwrap().as_str().to_lowercase());
                }
            }
        }

        let mut in_case_block = false;
        let mut brace_depth: usize = 0;
        let mut had_positive_brace = false;
        let mut current_func_name: Option<String> = None;
        let mut _current_func_ret_type: Option<String> = None;
        let mut current_func_is_void = false;
        let mut current_func_hook_suffix: Option<String> = None;
        let mut reported_tbl001 = HashSet::new();

        // Extension Modeler State
        let path_lower = file_path.to_lowercase();
        let stem = Path::new(file_path).file_stem().map(|s| s.to_string_lossy().to_lowercase()).unwrap_or_default();
        let content_lower = content.to_lowercase();
        let norm_path = path_lower.replace('\\', "/");

        let is_extension = content_lower.contains("#context_on")
            || content_lower.contains("#context_off")
            || path_lower.ends_with(".cln")
            || path_lower.contains("_ext.4gl")
            || norm_path.contains("/est/")
            || norm_path.contains("/ess/")
            || path_lower.contains("table_extension")
            || path_lower.contains("session_extension");

        let re_session_code = Regex::new(r"[a-z]{5}\d{3,4}[ms]\d{3}").unwrap();
        let re_m_code = Regex::new(r"m\d{3}").unwrap();
        let is_session_ext = is_extension && (
            re_session_code.is_match(&path_lower)
            || re_m_code.is_match(&path_lower)
            || content_lower.contains("bic_sessionext")
            || content_lower.contains("bic_interface")
            || norm_path.contains("/session")
            || norm_path.contains("ess")
        );

        let re_tbl_stem = Regex::new(r"^(?:txest)?[a-z]{5}\d{3}(?:_ext)?$").unwrap();
        let is_table_ext = is_extension && !is_session_ext && (
            re_tbl_stem.is_match(&stem)
            || content_lower.contains("bic_tableext")
            || norm_path.contains("/table")
            || norm_path.contains("est")
        );

        let mut current_context: Option<String> = None;
        let mut context_stack: Vec<(String, usize)> = Vec::new();
        let mut in_additional_declarations = false;
        let mut has_additional_declarations = false;
        let mut found_get_extension_point_version = false;
        let mut declarations_includes = HashSet::new();
        let mut dal_call_lines: Vec<(usize, String)> = Vec::new();

        let re_add_decl = Regex::new(r"\|\s*Additional generated declaration(?:s|\s+lines)").unwrap();
        let re_ctx_on = Regex::new(r#"^\s*#context_on\s*(?:["']([^"']+)["'])?"#).unwrap();
        let re_ctx_off = Regex::new(r"^\s*#context_off\b").unwrap();
        let re_ext_inc = Regex::new(r#"^\s*#include\s+([<"][^>"]+[>"])"#).unwrap();
        let re_ext_dal_call = Regex::new(r"\b(dal\.change\.object|dal\.set\.field|dal\.save\.object|dal\.new\.object|dal\.destroy\.object)\s*\(").unwrap();
        let re_sec = Regex::new(r"^([a-zA-Z0-9_.]+)\s*:$").unwrap();
        let re_dmn_decl = Regex::new(r"\bdomain\s+([a-zA-Z][a-zA-Z0-9_.]*)\b").unwrap();
        let re_arr002 = Regex::new(r"\bdomain\s+([a-zA-Z][a-zA-Z0-9_.]*)\s+([^;\n]+)").unwrap();
        let re_tbl_ref = Regex::new(r"\b([a-z]{5}\d{3})\.([a-z0-9_]+)").unwrap();
        let re_func_decl = Regex::new(r"^\s*(?:function\s+)?(?:extern\s+)?(?:([a-zA-Z0-9_.]+)\s+)?([a-zA-Z0-9_.]+)\s*\((.*?)\)").unwrap();
        let re_return = Regex::new(r#"\breturn\s*(?:\((.*?)\)|([a-zA-Z0-9_.+\-*/"':]+))"#).unwrap();
        let re_msg = Regex::new(r"\bmessage\s*\(").unwrap();
        let re_dal_ui = Regex::new(r"\b(message|ask\.enum|box|input\.string)\s*\(").unwrap();
        let re_dal_tx = Regex::new(r"\b(commit\.transaction|abort\.transaction|db\.retry\.point)\s*\(").unwrap();
        let re_db_mut = Regex::new(r"\b(db\.insert|db\.update|db\.delete|db\.write)\s*\(\s*([a-zA-Z0-9_]+)").unwrap();
        let re_assign = Regex::new(r"^\s*([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*)\s*=\s*(.+)$").unwrap();
        let re_cmp = Regex::new(r"\b([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*)\s*(==|<>|!=|<=|>=|<|>|\bin\b)\s*([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*)\b").unwrap();
        let re_sql_host = Regex::new(r":([a-zA-Z_][a-zA-Z0-9_.]*)\s*[(\[]").unwrap();
        let re_float_cmp1 = Regex::new(r"==\s*\d+\.\d+|\d+\.\d+\s*==").unwrap();
        let re_float_cmp2 = Regex::new(r"==\s*0\.0\b|0\.0\s*==").unwrap();
        let re_call = Regex::new(r"\b([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)+)\s*\(").unwrap();

        for (line_idx, raw_line) in lines.iter().enumerate() {
            let line_no = line_idx + 1;
            if re_add_decl.is_match(raw_line) {
                in_additional_declarations = true;
                has_additional_declarations = true;
            }

            let code_line = if line_idx < cleaned_lines.len() {
                &cleaned_lines[line_idx]
            } else {
                ""
            };
            let code_line_stripped = code_line.trim();
            if code_line_stripped.is_empty() {
                continue;
            }

            // Directives (#context_on / #context_off)
            if let Some(m_ctx) = re_ctx_on.captures(raw_line) {
                in_additional_declarations = false;
                let ctx_name = m_ctx.get(1).map(|m| m.as_str()).unwrap_or("").trim();
                current_context = Some(ctx_name.to_lowercase());
                if let Some((parent_name, parent_line)) = context_stack.last() {
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        1,
                        Severity::Error,
                        "EXT003",
                        format!("EXT003: Nested '#context_on' is not allowed: block '{ctx_name}' opened inside '{parent_name}' (line {parent_line})."),
                        *raw_line,
                    ));
                }
                context_stack.push((format!("#context_on \"{ctx_name}\""), line_no));

                let ctx_lower = ctx_name.to_lowercase();
                let is_cmd_hook = (
                    ctx_lower.starts_with("function.")
                        && (ctx_lower.ends_with(".before.command") || ctx_lower.ends_with(".after.command")
                            || ctx_lower.ends_with(".is.enabled") || ctx_lower.ends_with(".is.visible"))
                ) || ctx_lower.ends_with(".before.command") || ctx_lower.ends_with(".after.command");

                let is_dal_hook = matches!(
                    ctx_lower.as_str(),
                    "before.save.object" | "after.save.object" | "before.destroy.object"
                        | "after.destroy.object" | "before.open.object.set" | "after.open.object.set"
                        | "method.is.allowed" | "set.object.defaults" | "ue.before.save" | "ue.after.save"
                ) || ctx_lower.ends_with(".is.valid") || ctx_lower.ends_with(".update")
                    || ctx_lower.ends_with(".check") || ctx_lower.ends_with(".set.defaults");

                if is_table_ext && is_cmd_hook {
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        1,
                        Severity::Error,
                        "EXT002",
                        format!("Form Command hook '{ctx_name}' is not supported in Table Extension; Form Command hooks belong in Session Extensions."),
                        *raw_line,
                    ));
                } else if is_session_ext && is_dal_hook {
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        1,
                        Severity::Error,
                        "EXT002",
                        format!("Table DAL hook '{ctx_name}' is not supported in Session Extension; Table DAL hooks belong in Table Extensions."),
                        *raw_line,
                    ));
                }
            }

            if re_ctx_off.is_match(raw_line) {
                current_context = None;
                if context_stack.is_empty() {
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        1,
                        Severity::Error,
                        "EXT003",
                        "EXT003: Unmatched '#context_off' without corresponding '#context_on'.",
                        *raw_line,
                    ));
                } else {
                    context_stack.pop();
                }
            }

            // EXT001: Check #include placement in Extension scripts
            if is_extension {
                if let Some(m_inc) = re_ext_inc.captures(raw_line) {
                    let inc_raw = m_inc.get(1).unwrap().as_str();
                    let inc_clean = inc_raw.trim_matches(|c| c == '<' || c == '>' || c == '"' || c == '\'').trim_end_matches(".h").to_lowercase();
                    if current_context.as_deref() == Some("declarations") {
                        declarations_includes.insert(inc_clean);
                    } else if (in_additional_declarations && (STD_EXTENSION_INCLUDES.contains(&inc_clean.as_str()) || inc_clean.starts_with("bic_")))
                        || matches!(
                            inc_clean.as_str(),
                            "bic_interface" | "bic_sessionext" | "bic_tableext" | "bic_reportext"
                        )
                    {
                        declarations_includes.insert(inc_clean);
                    } else {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            1,
                            Severity::Error,
                            "EXT001",
                            format!("Direct '#include {inc_raw}' outside '#context_on \"declarations\"' will not be compiled by Extension Modeler; move inside '#context_on \"declarations\"' block."),
                            *raw_line,
                        ));
                    }
                }

                if re_ext_dal_call.is_match(code_line) {
                    dal_call_lines.push((line_no, (*raw_line).to_string()));
                }
            }

            // Case context tracking
            let code_lower = code_line.to_lowercase();
            if code_lower.contains("on case") {
                in_case_block = true;
            } else if code_lower.contains("endcase") {
                in_case_block = false;
            }

            for ch in code_line.chars() {
                if ch == '{' {
                    brace_depth += 1;
                    had_positive_brace = true;
                } else if ch == '}' {
                    brace_depth = brace_depth.saturating_sub(1);
                }
            }

            // 1. Section Header Checks (SYN002)
            if let Some(sec_match) = re_sec.captures(code_line_stripped) {
                let raw_token = sec_match.get(1).unwrap().as_str();
                let header_name = format!("{}:", raw_token.to_lowercase());

                if matches!(raw_token.to_lowercase().as_str(), "default" | "case")
                    || (in_case_block && (raw_token.to_lowercase().starts_with("case ") || raw_token.chars().all(|c| c.is_uppercase())))
                {
                    // Ignored inside case
                } else if !self.is_valid_section_header(&header_name) {
                    let suggestion = if let Some(closest) = self.find_closest_section(&header_name) {
                        format!(" Did you mean '{closest}'?")
                    } else {
                        String::new()
                    };
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        1,
                        Severity::Error,
                        "SYN002",
                        format!("Unrecognized or misspelled section header '{header_name}'.{suggestion}"),
                        *raw_line,
                    ));
                }
            }

            // 2. Table Declaration (TBL001) & Schema Field/Domain Checks (TBL002, DMN001)
            // 2a. Domain declarations: `domain <domain_name> <var>`
            for m_dmn in re_dmn_decl.captures_iter(code_line) {
                let dmn_name = m_dmn.get(1).unwrap().as_str();
                let dmn_lower = dmn_name.to_lowercase();
                if matches!(dmn_lower.as_str(), "error" | "true" | "false") {
                    continue;
                }
                if let Some(cache) = active_dd {
                    if cache.has_data() && !cache.has_domain(&dmn_lower) {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            m_dmn.get(1).unwrap().start() + 1,
                            Severity::Error,
                            "DMN001",
                            format!("Domain '{dmn_name}' does not exist in Data Dictionary cache (.ln_dd_cache.json)."),
                            *raw_line,
                        ));
                    }
                }
            }

            // 2a-2. Rule ARR002: Detect 1D domain string array declarations
            for m_arr in re_arr002.captures_iter(code_line) {
                let d_name = m_arr.get(1).unwrap().as_str();
                if self.is_string_domain(d_name, active_dd) {
                    let vars_chunk = m_arr.get(2).unwrap().as_str();
                    let re_var = Regex::new(r"\b([a-zA-Z_][a-zA-Z0-9_.]*)\s*\(([^)]+)\)").unwrap();
                    for m_v in re_var.captures_iter(vars_chunk) {
                        let v_name = m_v.get(1).unwrap().as_str();
                        let dim_expr = m_v.get(2).unwrap().as_str().trim();
                        if !dim_expr.contains(',') {
                            let col_pos = m_arr.get(2).unwrap().start() + m_v.get(1).unwrap().start() + 1;
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                col_pos,
                                Severity::Warning,
                                "ARR002",
                                format!(
                                    "Domain string array '{v_name}' declared with 1D syntax; bshell treats this as string length. Use 2D syntax 'string arr(len, count)' and access with 'arr(1, idx)'."
                                ),
                                *raw_line,
                            ));
                        }
                    }
                }
            }

            // 2b. Table field references: `<table>.<field>` (matching `([a-z]{5}\d{3})\.([a-z0-9_]+)`)
            for m_ref in re_tbl_ref.captures_iter(code_line) {
                if is_preceded_by_dot_or_word(code_line, m_ref.get(0).unwrap().start()) {
                    continue;
                }
                let prefix_before = code_line[..m_ref.get(0).unwrap().start()].trim_end().to_lowercase();
                if prefix_before.ends_with("domain") || prefix_before.ends_with("zoom.from") {
                    continue;
                }

                let tbl_code = m_ref.get(1).unwrap().as_str().to_lowercase();
                let fld_code = m_ref.get(2).unwrap().as_str().to_lowercase();
                let col_pos = m_ref.get(1).unwrap().start() + 1;

                // Rule TBL001: Check table declaration in `declaration:` (excluding component's main table)
                if Some(&tbl_code) != effective_main_table.as_ref() && !declared_tables.contains(&tbl_code) {
                    if reported_tbl001.insert((tbl_code.clone(), line_no)) {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            col_pos,
                            Severity::Error,
                            "TBL001",
                            format!("Table '{tbl_code}' referenced via '{tbl_code}.{fld_code}' is missing 'table t{tbl_code}' in declaration: section."),
                            *raw_line,
                        ));
                    }
                }

                // Rule TBL002: Validate field existence against `.ln_dd_cache.json`
                if let Some(cache) = active_dd {
                    if cache.has_table(&tbl_code) {
                        if !cache.has_field(&tbl_code, &fld_code) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                col_pos,
                                Severity::Error,
                                "TBL002",
                                format!("Field '{tbl_code}.{fld_code}' does not exist in Data Dictionary schema for table '{tbl_code}'."),
                                *raw_line,
                            ));
                        }
                    } else if self.auto_fetch_dd {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            col_pos,
                            Severity::Error,
                            "TBL002",
                            format!("Table '{tbl_code}' (for '{tbl_code}.{fld_code}') could not be found in Data Dictionary cache or server."),
                            *raw_line,
                        ));
                    }
                }
            }

            // 3. Function & DAL Hook Signatures (DAL002, DAL003)
            // EXT003: Non-context statements & declarations check
            if is_extension && current_context.is_none() && current_func_name.is_none() {
                if !code_line_stripped.is_empty() && !code_line_stripped.starts_with('#') {
                    let re_tbl_st = Regex::new(r"^\s*table\s+[a-zA-Z0-9_]+").unwrap();
                    let re_fn_st = Regex::new(r"^\s*(?:function\s+)?(?:extern\s+)?(?:[a-zA-Z0-9_.]+\s+)?[a-zA-Z0-9_.]+\s*\(").unwrap();
                    let re_var_st = Regex::new(r"^(?:extern\s+|global\s+)?(?:domain\s+[a-zA-Z0-9_.]+|long|string|double|boolean)\s+").unwrap();

                    if in_additional_declarations && (re_tbl_st.is_match(code_line_stripped) || re_var_st.is_match(code_line_stripped)) {
                        // Permitted in additional declarations
                    } else if re_fn_st.is_match(code_line_stripped) {
                        // Function start
                    } else if re_var_st.is_match(code_line_stripped) {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            1,
                            Severity::Error,
                            "EXT003",
                            "EXT003: Custom declaration placed outside '#context' block; custom declarations must reside inside '#context_on \"declarations\"'.",
                            *raw_line,
                        ));
                    } else if !re_tbl_st.is_match(code_line_stripped) {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            1,
                            Severity::Error,
                            "EXT003",
                            "EXT003: Executable statement placed outside '#context' block; custom logic must reside inside '#context_on' blocks.",
                            *raw_line,
                        ));
                    }
                }
            }

            if let Some(func_decl) = re_func_decl.captures(code_line) {
                let f_candidate = func_decl.get(2).unwrap().as_str().to_lowercase();
                let is_keyword = matches!(
                    f_candidate.as_str(),
                    "return" | "if" | "while" | "for" | "on" | "case" | "select"
                        | "endselect" | "endif" | "endwhile" | "endfor" | "endcase"
                        | "break" | "continue"
                ) || f_candidate.starts_with("db.")
                    || f_candidate.starts_with("dal.")
                    || f_candidate.starts_with("commit.")
                    || f_candidate.starts_with("abort.")
                    || f_candidate.starts_with("message")
                    || f_candidate.starts_with("ask.")
                    || f_candidate.starts_with("box")
                    || f_candidate.starts_with("show.");

                if !is_keyword {
                    in_additional_declarations = false;
                    let ret_type = func_decl.get(1).map(|m| m.as_str().to_lowercase()).unwrap_or_default();
                    let func_name = f_candidate;
                    let params = func_decl.get(3).map(|m| m.as_str().trim()).unwrap_or_default();

                    current_func_name = Some(func_name.clone());
                    _current_func_ret_type = Some(ret_type.clone());
                    current_func_is_void = ret_type == "void"
                        || (ret_type.is_empty() && (func_name.ends_with(".before.command") || func_name.ends_with(".after.command")));
                    current_func_hook_suffix = None;

                    // EXT003: Anti-tamper & standard framework function boundary
                    if is_extension {
                        let is_std_framework_func = STD_FRAMEWORK_FUNCTIONS.contains(&func_name.as_str())
                            || func_name.starts_with("ext.get.")
                            || func_name.starts_with("ext.is.");

                        if current_context.is_some() {
                            if is_std_framework_func {
                                diagnostics.push(Diagnostic::new(
                                    file_path,
                                    line_no,
                                    1,
                                    Severity::Error,
                                    "EXT003",
                                    format!("EXT003: Standard framework function '{func_name}' must remain outside '#context' blocks in the immutable standard code section."),
                                    *raw_line,
                                ));
                            }
                        } else {
                            if !is_std_framework_func {
                                diagnostics.push(Diagnostic::new(
                                    file_path,
                                    line_no,
                                    1,
                                    Severity::Error,
                                    "EXT003",
                                    format!("EXT003: Custom function '{func_name}' declared outside '#context' block; custom functions must reside inside '#context_on' blocks."),
                                    *raw_line,
                                ));
                            } else {
                                if func_name == "get.extension.point.version" {
                                    found_get_extension_point_version = true;
                                    if ret_type != "long" {
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            1,
                                            Severity::Error,
                                            "EXT003",
                                            format!("EXT003: Standard framework function 'get.extension.point.version' has invalid return type '{}'; expected 'long'.", if ret_type.is_empty() { "void" } else { &ret_type }),
                                            *raw_line,
                                        ));
                                    }
                                } else if func_name == "ext.is.cdfs.of.ref.tables.selected" {
                                    if ret_type != "boolean" && ret_type != "long" {
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            1,
                                            Severity::Error,
                                            "EXT003",
                                            format!("EXT003: Standard framework function '{func_name}' has invalid return type '{}'; expected 'boolean'.", if ret_type.is_empty() { "void" } else { &ret_type }),
                                            *raw_line,
                                        ));
                                    }
                                } else if matches!(
                                    func_name.as_str(),
                                    "ext.get.form.fields"
                                        | "ext.get.session.indices"
                                        | "ext.get.command.extensions"
                                        | "ext.get.report.extensions"
                                ) {
                                    if !ret_type.is_empty() && ret_type != "void" && ret_type != "long" {
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            1,
                                            Severity::Error,
                                            "EXT003",
                                            format!("EXT003: Standard framework function '{func_name}' has invalid return type '{ret_type}'; expected 'long' or 'void'."),
                                            *raw_line,
                                        ));
                                    }
                                } else if func_name.starts_with("ext.get.") && !ret_type.is_empty() && ret_type != "void" {
                                    diagnostics.push(Diagnostic::new(
                                        file_path,
                                        line_no,
                                        1,
                                        Severity::Error,
                                        "EXT003",
                                        format!("EXT003: Standard framework function '{func_name}' has invalid return type '{ret_type}'; expected 'void'."),
                                        *raw_line,
                                    ));
                                }
                            }
                        }
                    }

                    // Check EXT002 on function declaration
                    let is_cmd_hook = (
                        func_name.starts_with("function.")
                            && (func_name.ends_with(".before.command") || func_name.ends_with(".after.command")
                                || func_name.ends_with(".is.enabled") || func_name.ends_with(".is.visible"))
                    ) || func_name.ends_with(".before.command") || func_name.ends_with(".after.command");

                    let is_dal_hook = matches!(
                        func_name.as_str(),
                        "before.save.object" | "after.save.object" | "before.destroy.object"
                            | "after.destroy.object" | "before.open.object.set" | "after.open.object.set"
                            | "method.is.allowed" | "set.object.defaults" | "ue.before.save" | "ue.after.save"
                    ) || func_name.ends_with(".is.valid") || func_name.ends_with(".update")
                        || func_name.ends_with(".check") || func_name.ends_with(".set.defaults");

                    if is_table_ext && is_cmd_hook {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            1,
                            Severity::Error,
                            "EXT002",
                            format!("Form Command hook '{func_name}' is not supported in Table Extension; Form Command hooks belong in Session Extensions."),
                            *raw_line,
                        ));
                    } else if is_session_ext && is_dal_hook {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            1,
                            Severity::Error,
                            "EXT002",
                            format!("Table DAL hook '{func_name}' is not supported in Session Extension; Table DAL hooks belong in Table Extensions."),
                            *raw_line,
                        ));
                    }

                    // DAL002 validation
                    if func_name == "before.save.object" {
                        if ret_type == "void" || ret_type == "boolean" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'before.save.object' must return 'long' (returns error code or 0). Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                        let re_mode = Regex::new(r"\blong\s+[a-zA-Z0-9_.]+\b").unwrap();
                        if !re_mode.is_match(params) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'before.save.object' must declare parameter 'long mode'. Found: '({params})'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name == "after.save.object" {
                        if !ret_type.is_empty() && ret_type != "long" && ret_type != "void" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'after.save.object' must return 'long' or 'void'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name == "before.destroy.object" {
                        if !ret_type.is_empty() && ret_type != "long" && ret_type != "void" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'before.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name == "after.destroy.object" {
                        if !ret_type.is_empty() && ret_type != "long" && ret_type != "void" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'after.destroy.object' must return 'long' or 'void'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name == "method.is.allowed" {
                        if !ret_type.is_empty() && ret_type != "boolean" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'method.is.allowed' must return 'boolean'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                        let re_method = Regex::new(r"\blong\s+[a-zA-Z0-9_.]+\b").unwrap();
                        if !re_method.is_match(params) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Hook 'method.is.allowed' must declare parameter 'long method'. Found: '({params})'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name.ends_with(".is.valid")
                        || func_name.ends_with(".is.readonly")
                        || func_name.ends_with(".is.mandatory")
                        || func_name.ends_with(".is.applicable")
                        || func_name.ends_with(".is.never.applicable")
                    {
                        if !ret_type.is_empty() && ret_type != "boolean" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Field hook '{func_name}' must return 'boolean'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                        current_func_hook_suffix = Some(".is.valid".to_string());
                    } else if func_name.starts_with("function.") && (func_name.ends_with(".is.enabled") || func_name.ends_with(".is.visible")) {
                        if !ret_type.is_empty() && ret_type != "boolean" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("Command hook '{func_name}' must return 'boolean'. Found: '{ret_type}'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name.starts_with("function.") && (func_name.ends_with(".before.command") || func_name.ends_with(".after.command")) {
                        if !ret_type.is_empty() && ret_type != "void" && ret_type != "long" {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!(
                                    "Command hook '{func_name}' must return 'void' or 'long'. Found: '{ret_type}'. Form Command execution hooks in Extension Modeler have a 'void' prototype."
                                ),
                                *raw_line,
                            ));
                        }
                    }

                    // Field hook suffixes like .update, .check, .set.defaults
                    if func_name.ends_with(".update") {
                        current_func_hook_suffix = Some(".update".to_string());
                        current_func_is_void = true;
                        let re_imode = Regex::new(r"\blong\s+i\.mode\b").unwrap();
                        if !re_imode.is_match(params) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("DAL hook '{func_name}' must declare parameter 'long i.mode'. Found: '({params})'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name.ends_with(".check") {
                        current_func_hook_suffix = Some(".check".to_string());
                        let re_changed = Regex::new(r"\blong\s+has_changed\b").unwrap();
                        if !re_changed.is_match(params) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("DAL hook '{func_name}' must declare parameter 'long has_changed'. Found: '({params})'."),
                                *raw_line,
                            ));
                        }
                    } else if func_name.ends_with(".set.defaults") {
                        current_func_hook_suffix = Some(".set.defaults".to_string());
                        let re_changed = Regex::new(r"\blong\s+has_changed\b").unwrap();
                        if !re_changed.is_match(params) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                1,
                                Severity::Error,
                                "DAL002",
                                format!("DAL hook '{func_name}' must declare parameter 'long has_changed'. Found: '({params})'."),
                                *raw_line,
                            ));
                        }
                    }
                }
            }

            // 4. DAL003: Return values in void functions & DAL hooks
            let is_func_decl_line = re_func_decl.is_match(code_line)
                && code_line_stripped.to_lowercase().starts_with("function");
            if let Some(ref cur_fn) = current_func_name {
                if !is_func_decl_line {
                    if let Some(ret_match) = re_return.captures(code_line) {
                        if !is_preceded_by_dot_or_word(code_line, ret_match.get(0).unwrap().start()) {
                            let ret_val = ret_match
                                .get(1)
                                .or_else(|| ret_match.get(2))
                                .map(|m| m.as_str().trim())
                                .unwrap_or_default();

                            if current_func_is_void && !ret_val.is_empty() {
                                diagnostics.push(Diagnostic::new(
                                    file_path,
                                    line_no,
                                    1,
                                    Severity::Error,
                                    "DAL003",
                                    format!(
                                        "Return value '{ret_val}' inside void function/hook '{cur_fn}' is not allowed in Baan 4GL; compiler blocks with 'Return value for void function not allowed'. Use bare 'return' or 'return()' without an expression."
                                    ),
                                    *raw_line,
                                ));
                            }

                            if cur_fn == "get.extension.point.version" {
                                if !ret_val.chars().all(|c| c.is_ascii_digit()) {
                                    diagnostics.push(Diagnostic::new(
                                        file_path,
                                        line_no,
                                        1,
                                        Severity::Error,
                                        "EXT003",
                                        "EXT003: Standard framework function 'get.extension.point.version' modified; must return a valid integer version number (e.g. return(3)).",
                                        *raw_line,
                                    ));
                                }
                            } else if let Some(ref sfx) = current_func_hook_suffix {
                                if sfx.ends_with(".is.valid")
                                    || sfx.ends_with(".is.readonly")
                                    || sfx.ends_with(".is.mandatory")
                                    || sfx.ends_with(".is.applicable")
                                    || sfx.ends_with(".is.never.applicable")
                                {
                                    let val_lower = ret_val.to_lowercase();
                                    if !val_lower.is_empty()
                                        && !matches!(val_lower.as_str(), "true" | "false" | "0" | "1")
                                        && (val_lower.contains("dalhookerror") || val_lower.starts_with('-'))
                                    {
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            1,
                                            Severity::Error,
                                            "DAL003",
                                            format!("Boolean DAL hook '{cur_fn}' cannot return error code '{ret_val}'; must return true or false."),
                                            *raw_line,
                                        ));
                                    }
                                } else if sfx == ".update" && !ret_val.is_empty() {
                                    diagnostics.push(Diagnostic::new(
                                        file_path,
                                        line_no,
                                        1,
                                        Severity::Error,
                                        "DAL003",
                                        format!("Void DAL hook '{cur_fn}' cannot return a value '{ret_val}'."),
                                        *raw_line,
                                    ));
                                }
                            }
                        }
                    }
                }
            }

            // 5. Interactive UI & Transaction Controls (DAL001, DAL005, DBG001, CAV003 direct in DAL/UEDLL)
            if mode != "dal2" {
                for mm in re_msg.find_iter(code_line) {
                    if is_preceded_by_dot_or_word(code_line, mm.start()) {
                        continue;
                    }
                    let is_batch = mode == "batch" || content_lower.contains("type 4") || self.cloud_mode;
                    let sev = if is_batch { Severity::Error } else { Severity::Warning };
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        mm.start() + 1,
                        sev,
                        "DBG001",
                        "Interactive 'message()' popup in non-dialog script will halt headless/batch execution; remove ephemeral debug messages before release.",
                        *raw_line,
                    ));
                }
            }

            if mode == "dal2" {
                for uim in re_dal_ui.captures_iter(code_line) {
                    let mat = uim.get(1).unwrap();
                    if is_preceded_by_dot_or_word(code_line, mat.start()) {
                        continue;
                    }
                    let func_called = mat.as_str().to_lowercase();
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        mat.start() + 1,
                        Severity::Error,
                        "DAL001",
                        format!("Interactive dialog '{func_called}()' is prohibited in DAL scripts and Table Extension hooks; use 'dal.set.error.message()' instead."),
                        *raw_line,
                    ));
                }

                for tm in re_dal_tx.captures_iter(code_line) {
                    let mat = tm.get(1).unwrap();
                    if is_preceded_by_dot_or_word(code_line, mat.start()) {
                        continue;
                    }
                    let func_called = mat.as_str().to_lowercase();
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        mat.start() + 1,
                        Severity::Error,
                        "DAL005",
                        format!("Transaction control '{func_called}()' is prohibited in DAL/Table Extension hooks; transaction lifecycle is managed by the DAL engine."),
                        *raw_line,
                    ));
                }
            }

            // CAV003 in DAL/UEDLL subroutines
            if mode == "dal2" || mode == "uedll" {
                for tm in re_dal_tx.captures_iter(code_line) {
                    let mat = tm.get(1).unwrap();
                    if is_preceded_by_dot_or_word(code_line, mat.start()) {
                        continue;
                    }
                    let func_called = mat.as_str().to_lowercase();
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        line_no,
                        mat.start() + 1,
                        Severity::Warning,
                        "CAV003",
                        format!("Nested transaction statement '{func_called}()' is prohibited in {} scripts; transaction boundaries are managed by the caller.", mode.to_uppercase()),
                        *raw_line,
                    ));
                }
            }

            // 6. Raw DB Mutation in UI Script (DAL004) & DAL Main Table mutation (DAL003)
            if mode == "general" {
                for dbm in re_db_mut.captures_iter(code_line) {
                    let mat = dbm.get(1).unwrap();
                    if is_preceded_by_dot_or_word(code_line, mat.start()) {
                        continue;
                    }
                    let mut_fn = mat.as_str().to_lowercase();
                    let target_tbl = dbm.get(2).unwrap().as_str().to_lowercase();
                    let tbl_name = if target_tbl.starts_with('t') && target_tbl.len() > 1 {
                        &target_tbl[1..]
                    } else {
                        &target_tbl
                    };
                    let mut is_temp = tbl_name.contains("temp") || tbl_name.ends_with("010");
                    if let Some(cache) = active_dd {
                        if let Some(t_meta) = cache.tables.get(tbl_name) {
                            if let Some(ref d) = t_meta.description {
                                if d.to_lowercase().contains("temp") {
                                    is_temp = true;
                                }
                            }
                        }
                    }
                    if !is_temp {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            mat.start() + 1,
                            Severity::Error,
                            "DAL004",
                            format!("Direct database mutation '{mut_fn}()' on table '{tbl_name}' in UI script violates Separation of Concerns; use DAL2 instead."),
                            *raw_line,
                        ));
                    }
                }
            } else if mode == "dal2" {
                if let Some(ref m_tbl) = effective_main_table {
                    for dbm in re_db_mut.captures_iter(code_line) {
                        let mat = dbm.get(1).unwrap();
                        if is_preceded_by_dot_or_word(code_line, mat.start()) {
                            continue;
                        }
                        let mut_fn = mat.as_str().to_lowercase();
                        let target_tbl = dbm.get(2).unwrap().as_str().to_lowercase();
                        let tbl_name = if target_tbl.starts_with('t') && target_tbl.len() > 1 {
                            &target_tbl[1..]
                        } else {
                            &target_tbl
                        };
                        if tbl_name == m_tbl {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                mat.start() + 1,
                                Severity::Error,
                                "DAL003",
                                format!("Direct database mutation '{mut_fn}()' on DAL main table '{tbl_name}' is not allowed; use dal.new.object, dal.change.object, or dal.destroy.object instead."),
                                *raw_line,
                            ));
                        }
                    }
                }
            }

            // 7. Date Safety (DMN002), Mandatory Zero (TBL003), and STR001
            if let Some(m_assign) = re_assign.captures(code_line) {
                let rhs_raw = m_assign.get(2).unwrap().as_str().trim();
                if !rhs_raw.starts_with('=') {
                    let target_var = m_assign.get(1).unwrap().as_str().to_lowercase();
                    let target_parts: Vec<&str> = target_var.split('.').collect();
                    let mut tbl_name = "";
                    let mut fld_name = "";
                    if target_parts.len() == 1 {
                        fld_name = target_parts[0];
                    } else if target_parts.len() == 2 {
                        tbl_name = target_parts[0];
                        fld_name = target_parts[1];
                    } else if target_parts.len() >= 3 && target_parts[1] == "cdf" {
                        tbl_name = target_parts[0];
                    }

                    let mut fld_info = None;
                    let mut is_target_date = false;

                    if let Some(cache) = active_dd {
                        if !tbl_name.is_empty() && !fld_name.is_empty() {
                            if let Some(fi) = cache.get_field(tbl_name, fld_name) {
                                fld_info = Some(fi);
                                if let Some(ref d) = fi.domain {
                                    if d.to_lowercase().contains("date") {
                                        is_target_date = true;
                                    }
                                }
                                if let Some(ref dt) = fi.datatype {
                                    let dt_str = dt.to_string().to_lowercase();
                                    if dt_str.contains("date") || dt_str.contains("9") {
                                        is_target_date = true;
                                    }
                                }
                            }
                        }
                    }

                    if !is_target_date {
                        let var_leaf = target_parts.last().copied().unwrap_or("");
                        let date_leaves = [
                            "docd", "dued", "date", "datt", "odat", "idat", "pdat", "rdat",
                            "fdat", "tdat", "sdat", "edat", "bdat", "ldat", "vdat",
                        ];
                        if date_leaves.contains(&var_leaf)
                            || var_leaf.ends_with("_docd")
                            || var_leaf.ends_with("_dued")
                            || var_leaf.ends_with("_date")
                        {
                            if !target_var.contains("utc") && !target_var.contains("clld") && !target_var.contains("time") {
                                is_target_date = true;
                            }
                        }
                    }

                    // DMN002 Check
                    if is_target_date {
                        let re_utc = Regex::new(r"\b(date\.to\.utc|utc\.num)\s*\(").unwrap();
                        if let Some(m_utc) = re_utc.captures(rhs_raw) {
                            let called_utc_fn = m_utc.get(1).unwrap().as_str().to_lowercase();
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                m_assign.get(1).unwrap().start() + 1,
                                Severity::Error,
                                "DMN002",
                                format!("Assigning UTC timestamp (seconds) from '{called_utc_fn}()' to Date field '{target_var}' will trigger Fatal Error 205 (Value is out of range) at runtime. Date fields use Julian Day integers (~740k); use 'date.num()' or Julian date assignments directly."),
                                *raw_line,
                            ));
                        }
                    }

                    // TBL003 Check: Mandatory numeric field assigned 0
                    if let Some(fi) = fld_info {
                        if fi.is_mandatory == Some(true) {
                            let re_zero = Regex::new(r"^0\s*;").unwrap();
                            let is_assigning_zero = rhs_raw == "0"
                                || re_zero.is_match(rhs_raw)
                                || rhs_raw.eq_ignore_ascii_case("tfacr500.line")
                                || rhs_raw.eq_ignore_ascii_case("tfacr200.line");
                            if is_assigning_zero {
                                diagnostics.push(Diagnostic::new(
                                    file_path,
                                    line_no,
                                    m_assign.get(1).unwrap().start() + 1,
                                    Severity::Error,
                                    "TBL003",
                                    format!("Assigning '{rhs_raw}' to mandatory numeric column '{target_var}' will trigger Fatal Error 205 (Value is out of range) at runtime upon db.insert(). In Infor LN, mandatory numeric fields forbid 0. If zero is valid (e.g. invoice header line), define column as Mandatory: No."),
                                    *raw_line,
                                ));
                            }
                        }
                    }

                    // STR001 Check
                    if rhs_raw.to_lowercase().contains("logname$") {
                        let is_user_field = target_var.ends_with(".user")
                            || fld_name == "user"
                            || fld_info.and_then(|fi| fi.domain.as_deref()).map(|d| d.eq_ignore_ascii_case("tfgld.user")).unwrap_or(false);
                        let re_slice1 = Regex::new(r"\(1\s*;\s*16\)").unwrap();
                        let re_slice2 = Regex::new(r"\[1\s*:\s*16\]").unwrap();
                        let has_slice = re_slice1.is_match(rhs_raw) || re_slice2.is_match(rhs_raw);

                        if is_user_field && !has_slice {
                            let sev = if self.cloud_mode { Severity::Error } else { Severity::Warning };
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                m_assign.get(1).unwrap().start() + 1,
                                sev,
                                "STR001",
                                format!(
                                    "Un-sliced 'logname$' assigned to 16-character user field '{target_var}'. In Infor LN Cloud Single Sign-On (SSO), usernames often exceed 16 characters; use 'strip$(shiftl$(logname$))(1; 16)' to prevent string truncation errors."
                                ),
                                *raw_line,
                            ));
                        }
                    }
                }
            }

            // 7c. Enum Domain Safety & Literal Checks (DMN003)
            if let Some(cache) = active_dd {
                for m_cmp in re_cmp.captures_iter(code_line) {
                    let side1 = m_cmp.get(1).unwrap().as_str().to_lowercase();
                    let side2 = m_cmp.get(3).unwrap().as_str().to_lowercase();

                    let check_pairs = [(&side1, &side2), (&side2, &side1)];
                    for (col_cand, val_cand) in check_pairs {
                        let parts: Vec<&str> = col_cand.split('.').collect();
                        if parts.len() >= 2 {
                            let tbl_n = parts[0];
                            let fld_n = if parts.len() >= 3 && parts[1] == "cdf" {
                                format!("{}_{}", parts[1], parts[2])
                            } else {
                                parts[1].to_string()
                            };

                            if let Some(f_meta) = cache.get_field(tbl_n, &fld_n) {
                                let f_dt = f_meta.datatype.as_ref().map(|dt| dt.to_string().to_lowercase()).unwrap_or_default();
                                let d_name = f_meta.domain.clone().unwrap_or_default().to_lowercase();
                                let mut is_enum = f_dt.contains("enum") || f_dt == "7";
                                if !is_enum && !d_name.is_empty() {
                                    if let Some(d_meta) = cache.get_domain(&d_name) {
                                        let dm_dt = d_meta.datatype.as_ref().map(|dt| dt.to_string().to_lowercase()).unwrap_or_default();
                                        if dm_dt.contains("enum") || dm_dt == "7" || d_meta.constants.is_some() {
                                            is_enum = true;
                                        }
                                    }
                                }

                                if is_enum && !d_name.is_empty() {
                                    // Case 1: Compared against 0 (Warning)
                                    if *val_cand == "0" {
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            m_cmp.get(0).unwrap().start() + 1,
                                            Severity::Warning,
                                            "DMN003",
                                            format!("Comparison of enum column '{col_cand}' (domain '{d_name}') against 0. Verify if 0 is the intended empty state; custom domains often define explicit non-zero default symbols (e.g. '{d_name}.not.applic')."),
                                            *raw_line,
                                        ));
                                    } else if val_cand.chars().all(|c| c.is_ascii_digit()) && val_cand.parse::<usize>().unwrap_or(0) >= 1 {
                                        // Case 2: Compared against integer literal >= 1 (Error)
                                        diagnostics.push(Diagnostic::new(
                                            file_path,
                                            line_no,
                                            m_cmp.get(0).unwrap().start() + 1,
                                            Severity::Error,
                                            "DMN003",
                                            format!("Integer literal '{val_cand}' compared against enum column '{col_cand}' (domain '{d_name}'). Use symbolic enum constant (e.g. '{d_name}.<symbol>') instead of raw integer literals to prevent logical inversions."),
                                            *raw_line,
                                        ));
                                    } else if val_cand.contains('.') && !val_cand.starts_with(&format!("t{tbl_n}")) {
                                        // Case 3: Cross-domain enum constant
                                        let c_parts: Vec<&str> = val_cand.split('.').collect();
                                        if c_parts.len() >= 2 && !val_cand.starts_with(&format!("{d_name}.")) {
                                            let const_domain = c_parts[..c_parts.len() - 1].join(".");
                                            diagnostics.push(Diagnostic::new(
                                                file_path,
                                                line_no,
                                                m_cmp.get(0).unwrap().start() + 1,
                                                Severity::Error,
                                                "DMN003",
                                                format!("Cross-domain enum comparison: column '{col_cand}' has domain '{d_name}' but is compared against constant '{val_cand}' from domain '{const_domain}'. Cross-domain comparisons compile to conflicting integer values causing silent logical inversions."),
                                                *raw_line,
                                            ));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            // 8. Rule SQL008: Array Subscript in SQL Host Variable
            for m_host in re_sql_host.captures_iter(code_line) {
                let host_var = m_host.get(1).unwrap().as_str();
                diagnostics.push(Diagnostic::new(
                    file_path,
                    line_no,
                    m_host.get(0).unwrap().start() + 1,
                    Severity::Error,
                    "SQL008",
                    format!(
                        "Array subscript or parentheses detected in SQL host variable ':{host_var}(...)'. Baan SQL precompiler does not support subscripts in host variables; stage array elements into scalar variables before the query."
                    ),
                    *raw_line,
                ));
            }

            // 9. Float Equality Anti-Pattern (CAV001)
            if re_float_cmp1.is_match(code_line) || re_float_cmp2.is_match(code_line) {
                diagnostics.push(Diagnostic::new(
                    file_path,
                    line_no,
                    1,
                    Severity::Warning,
                    "CAV001",
                    "Direct floating-point equality comparison '==' detected; use tolerance/epsilon check instead.",
                    *raw_line,
                ));
            }

            // 10. Function Call Catalog Inspections (CLD001, CLD002, INC001)
            for cm in re_call.captures_iter(code_line) {
                let called_fn = cm.get(1).unwrap().as_str();
                if let Some(fn_info) = lookup_function(called_fn) {
                    if self.cloud_mode && !fn_info.is_cloud_trusted {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            cm.get(1).unwrap().start() + 1,
                            Severity::Error,
                            "CLD001",
                            format!("Function '{called_fn}' is untrusted for Infor LN Cloud Multi-Tenant environments."),
                            *raw_line,
                        ));
                    }

                    if fn_info.deprecated {
                        diagnostics.push(Diagnostic::new(
                            file_path,
                            line_no,
                            cm.get(1).unwrap().start() + 1,
                            Severity::Warning,
                            "CLD002",
                            format!("Function '{called_fn}' is deprecated in Infor LN Studio catalog."),
                            *raw_line,
                        ));
                    }

                    let req_inc = fn_info.include.trim().to_lowercase();
                    if !req_inc.is_empty() {
                        let req_inc_clean = if req_inc.ends_with(".h") {
                            &req_inc[..req_inc.len() - 2]
                        } else {
                            &req_inc
                        };
                        if !includes_found.contains(req_inc_clean) {
                            diagnostics.push(Diagnostic::new(
                                file_path,
                                line_no,
                                cm.get(1).unwrap().start() + 1,
                                Severity::Warning,
                                "INC001",
                                format!("Function '{called_fn}' requires '#include <{req_inc}>', which is missing."),
                                *raw_line,
                            ));
                        }
                    }
                }
            }

            // Reset current function state when exiting function curly braces
            if had_positive_brace && brace_depth == 0 {
                current_func_name = None;
                _current_func_ret_type = None;
                current_func_is_void = false;
                current_func_hook_suffix = None;
                had_positive_brace = false;
            }
        }

        // EXT001: Missing #include <bic_dam> or <bic_dal2> in declarations context
        if is_extension && !dal_call_lines.is_empty() {
            if !declarations_includes.contains("bic_dam") && !declarations_includes.contains("bic_dal2") {
                let (first_line, ref first_raw) = dal_call_lines[0];
                diagnostics.push(Diagnostic::new(
                    file_path,
                    first_line,
                    1,
                    Severity::Error,
                    "EXT001",
                    "Missing '#include <bic_dam>' (or '<bic_dal2>') inside '#context_on \"declarations\"'; Extension Modeler compiler will fail with unresolved reference to function 'dal.*'.",
                    first_raw,
                ));
            }
        }

        // 11. Intra-File Call Graph Nested Transaction Detection (CAV003)
        for (fn_name, fn_node) in ast_functions {
            // Direct nested db.retry.point() inside an already open transaction in the same function
            for (tx_fn, call_line, call_col, raw_l, start_line) in &fn_node.nested_tx_starts {
                diagnostics.push(Diagnostic::new(
                    file_path,
                    *call_line,
                    *call_col,
                    Severity::Error,
                    "CAV003",
                    format!("Nested transaction '{tx_fn}()' inside function '{fn_name}' while transaction opened at line {start_line} is still active."),
                    raw_l,
                ));
            }

            // Calling a helper function that directly or transitively starts/commits a transaction while inside an active transaction
            for (callee_name, call_line, call_col, raw_l, start_line) in &fn_node.calls_inside_tx {
                if let Some(chain_tail) = transitive_tx_map.get(callee_name) {
                    let mut chain = vec![callee_name.clone()];
                    chain.extend(chain_tail.clone());
                    diagnostics.push(Diagnostic::new(
                        file_path,
                        *call_line,
                        *call_col,
                        Severity::Error,
                        "CAV003",
                        format!(
                            "Nested transaction via call graph: '{fn_name}' calls '{callee_name}()' inside an active transaction (opened at line {start_line}), which executes '{}'.",
                            chain.join(" -> ")
                        ),
                        raw_l,
                    ));
                }
            }
        }

        // EXT003: Missing or removed standard framework function
        if is_extension && has_additional_declarations && !found_get_extension_point_version {
            diagnostics.push(Diagnostic::new(
                file_path,
                lines.len(),
                1,
                Severity::Error,
                "EXT003",
                "EXT003: Standard framework function 'get.extension.point.version' is missing or was removed; standard framework functions outside '#context' must not be deleted.",
                "",
            ));
        }

        // EXT003: Unclosed context blocks
        while let Some((ctx_type, ctx_line)) = context_stack.pop() {
            diagnostics.push(Diagnostic::new(
                file_path,
                ctx_line,
                1,
                Severity::Error,
                "EXT003",
                format!("EXT003: Unclosed '{ctx_type}' directive (opened at line {ctx_line})."),
                if ctx_line >= 1 && ctx_line <= lines.len() { lines[ctx_line - 1] } else { "" },
            ));
        }

        // Filter by min_severity
        diagnostics.into_iter().filter(|d| d.severity >= self.min_severity).collect()
    }

    /// Parallel multi-threaded auditing across files or directories using `rayon`.
    pub fn audit_path(&self, target: &Path, mode: Option<&str>) -> Result<Vec<Diagnostic>, std::io::Error> {
        if target.is_file() {
            let content = fs::read_to_string(target)?;
            return Ok(self.audit_content(&content, target.to_str().unwrap_or("<stdin>"), mode, None));
        }

        if target.is_dir() {
            let mut matched_files = Vec::new();
            let patterns = [
                ".cln", ".dal", ".dalsrc", ".lib", ".ue", ".3gl", ".4gl", ".spt", ".tbl", ".ses",
                ".rpt", ".fnc",
            ];
            Self::collect_files_recursive(target, &patterns, &mut matched_files);
            matched_files.sort();
            matched_files.dedup();

            let all_diags: Vec<Diagnostic> = matched_files
                .par_iter()
                .filter_map(|fpath| {
                    if let Ok(content) = fs::read_to_string(fpath) {
                        Some(self.audit_content(&content, fpath.to_str().unwrap_or("<unknown>"), mode, None))
                    } else {
                        None
                    }
                })
                .flatten()
                .collect();

            return Ok(all_diags);
        }

        Err(std::io::Error::new(
            std::io::ErrorKind::NotFound,
            format!("Path not found: {}", target.display()),
        ))
    }

    fn collect_files_recursive(dir: &Path, extensions: &[&str], out: &mut Vec<std::path::PathBuf>) {
        if let Ok(entries) = fs::read_dir(dir) {
            for entry in entries.flatten() {
                let p = entry.path();
                if p.is_dir() {
                    Self::collect_files_recursive(&p, extensions, out);
                } else if p.is_file() {
                    if let Some(ext) = p.extension() {
                        let dot_ext = format!(".{}", ext.to_string_lossy().to_lowercase());
                        if extensions.contains(&dot_ext.as_str()) {
                            out.push(p);
                        }
                    }
                }
            }
        }
    }
}

fn string_similarity(s1: &str, s2: &str) -> f64 {
    let len1 = s1.chars().count();
    let len2 = s2.chars().count();
    if len1 == 0 && len2 == 0 {
        return 1.0;
    }
    let max_len = len1.max(len2);
    let dist = levenshtein(s1, s2);
    1.0 - (dist as f64 / max_len as f64)
}

fn levenshtein(s1: &str, s2: &str) -> usize {
    let v1: Vec<char> = s1.chars().collect();
    let v2: Vec<char> = s2.chars().collect();
    let m = v1.len();
    let n = v2.len();
    let mut dp = vec![vec![0; n + 1]; m + 1];

    for i in 0..=m {
        dp[i][0] = i;
    }
    for j in 0..=n {
        dp[0][j] = j;
    }

    for i in 1..=m {
        for j in 1..=n {
            let cost = if v1[i - 1] == v2[j - 1] { 0 } else { 1 };
            dp[i][j] = (dp[i - 1][j] + 1)
                .min(dp[i][j - 1] + 1)
                .min(dp[i - 1][j - 1] + cost);
        }
    }

    dp[m][n]
}
