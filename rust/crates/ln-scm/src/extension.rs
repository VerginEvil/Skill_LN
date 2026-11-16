use std::fs;
use std::path::{Path, PathBuf};
use regex::Regex;
use serde::{Deserialize, Serialize};

use crate::scm_engine::ScmError;

pub const DEFAULT_TABLE_EXTENSION_TEMPLATE: &str = r#"|*******************************************************************************
|* Extension Script for Table {target}
|* Author: {author}
|* Generated: {date}
|* Target Session: ttext1500m000 (Extension Modeler)
|* Note: Maintained in local Git repo. Do not edit in LN Studio SCM.
|*******************************************************************************

| Hook declarations
#context_on "declarations"
table   t{target}
#include <bic_dal2>
#include <bic_tableext>

| Common module-level declarations
#context_off

| Hook functions
#context_on "functions"
| Common validation and calculation helper functions
function extern boolean validate_custom_rule_{target}()
{
    return(true)
}
#context_off

| Hook method.is.allowed
#context_on "method.is.allowed"
function extern boolean method.is.allowed(long method)
{
    on case method
    case DAL_NEW:
        break
    case DAL_UPDATE:
        break
    case DAL_DESTROY:
        break
    endcase
    return(true)
}
#context_off

| Hook before.save.object
#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    | Business logic executed before saving object
    return(0)
}
#context_off

| Hook after.save.object
#context_on "after.save.object"
function extern long after.save.object(long mode)
{
    | Business logic executed after saving object
    return(0)
}
#context_off

| Hook before.destroy.object
#context_on "before.destroy.object"
function extern long before.destroy.object()
{
    | Business logic executed before deleting object
    return(0)
}
#context_off

| Hook after.destroy.object
#context_on "after.destroy.object"
function extern long after.destroy.object()
{
    | Business logic executed after deleting object
    return(0)
}
#context_off
"#;

pub const DEFAULT_SESSION_EXTENSION_TEMPLATE: &str = r#"|*******************************************************************************
|* Extension Script for Session {target}
|* Author: {author}
|* Generated: {date}
|* Target Session: ttext1500m000 (Extension Modeler)
|* Note: Maintained in local Git repo. Do not edit in LN Studio SCM.
|*******************************************************************************

| Hook declarations
#context_on "declarations"
#include <bic_sessionext>

| Common module-level declarations
#context_off

| Hook functions
#context_on "functions"
| Common helper functions for session commands
function extern void helper_action_{target}()
{
}
#context_off

| Hook function.custom.action.is.enabled
#context_on "function.custom.action.is.enabled"
function extern boolean function.custom.action.is.enabled()
{
    return(true)
}
#context_off

| Hook function.custom.action.before.command
#context_on "function.custom.action.before.command"
function extern void function.custom.action.before.command()
{
    | Logic executed before command runs
    | Call choice.again() to cancel command execution
}
#context_off

| Hook function.custom.action.after.command
#context_on "function.custom.action.after.command"
function extern void function.custom.action.after.command()
{
    | Logic executed after command completes
}
#context_off
"#;

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct HookBlock {
    pub name: String,
    pub start_line: usize,
    pub end_line: usize,
    pub lines: Vec<String>,
}

impl HookBlock {
    /// Returns the hook code stripped of `#context_on` and `#context_off` wrappers.
    pub fn clean_code(&self) -> String {
        let code_lines: Vec<&str> = self
            .lines
            .iter()
            .filter(|line| !is_context_on(line) && !is_context_off(line))
            .map(|s| s.as_str())
            .collect();
        let joined = code_lines.join("\n");
        format!("{}\n", joined.trim_matches(|c| c == '\r' || c == '\n'))
    }

    /// Returns the number of non-wrapper lines in this hook block.
    pub fn code_lines_count(&self) -> usize {
        self.lines
            .iter()
            .filter(|line| !is_context_on(line) && !is_context_off(line))
            .count()
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct HookSummary {
    pub name: String,
    pub start_line: usize,
    pub end_line: usize,
    pub code_lines: usize,
}

fn is_context_on(line: &str) -> bool {
    let trimmed = line.trim();
    trimmed.starts_with("#context_on")
}

fn is_context_off(line: &str) -> bool {
    let trimmed = line.trim();
    trimmed.starts_with("#context_off")
}

/// Parses all `#context_on ... #context_off` hook blocks from a file or source string.
pub fn parse_extension_hooks(content: &str) -> Vec<HookBlock> {
    let re_on = Regex::new(r#"^\s*#context_on\s+["']([^"']+)["']"#).unwrap();
    let re_off = Regex::new(r#"^\s*#context_off\b"#).unwrap();

    let mut hooks = Vec::new();
    let mut curr_name: Option<String> = None;
    let mut curr_start: usize = 0;
    let mut curr_lines: Vec<String> = Vec::new();

    let lines: Vec<&str> = content.lines().collect();
    for (idx, line) in lines.iter().enumerate() {
        let line_num = idx + 1;

        if let Some(caps) = re_on.captures(line) {
            if let Some(prev_name) = curr_name.take() {
                hooks.push(HookBlock {
                    name: prev_name,
                    start_line: curr_start,
                    end_line: line_num - 1,
                    lines: curr_lines,
                });
                curr_lines = Vec::new();
            }
            curr_name = Some(caps.get(1).unwrap().as_str().trim().to_string());
            curr_start = line_num;
            curr_lines.push(line.to_string());
            continue;
        }

        if re_off.is_match(line) {
            if let Some(name) = curr_name.take() {
                curr_lines.push(line.to_string());
                hooks.push(HookBlock {
                    name,
                    start_line: curr_start,
                    end_line: line_num,
                    lines: curr_lines,
                });
                curr_lines = Vec::new();
            }
            continue;
        }

        if curr_name.is_some() {
            curr_lines.push(line.to_string());
        }
    }

    if let Some(name) = curr_name {
        hooks.push(HookBlock {
            name,
            start_line: curr_start,
            end_line: lines.len(),
            lines: curr_lines,
        });
    }

    hooks
}

/// Returns a summary list of all hooks present in an extension file or content.
pub fn list_hooks(content: &str) -> Vec<HookSummary> {
    parse_extension_hooks(content)
        .into_iter()
        .map(|h| {
            let count = h.code_lines_count();
            HookSummary {
                name: h.name,
                start_line: h.start_line,
                end_line: h.end_line,
                code_lines: count,
            }
        })
        .collect()
}

/// Finds a specific hook block by name (case-insensitive).
pub fn get_hook(content: &str, hook_name: &str) -> Option<HookBlock> {
    let lower = hook_name.to_lowercase();
    parse_extension_hooks(content)
        .into_iter()
        .find(|h| h.name.to_lowercase() == lower)
}

/// Scaffolds a new local extension `.4gl` file from official templates.
/// - `ext_type`: `"table"` or `"session"`
/// - `target`: Component code (e.g. `whwmd400`, `whwmd4300m000`)
pub fn new_extension(
    ext_type: &str,
    target: &str,
    output_path: Option<&Path>,
    author: &str,
    project_root: Option<&Path>,
) -> Result<PathBuf, ScmError> {
    let norm_type = match ext_type.trim().to_lowercase().as_str() {
        "table" | "tbl" | "table_extension" | "est" => "table",
        "session" | "ses" | "session_extension" | "ess" => "session",
        _ => {
            return Err(ScmError::Other(format!(
                "Unsupported extension type: '{ext_type}'. Expected 'table' or 'session'."
            )));
        }
    };

    let template_content = if norm_type == "table" {
        DEFAULT_TABLE_EXTENSION_TEMPLATE
    } else {
        DEFAULT_SESSION_EXTENSION_TEMPLATE
    };

    let today = crate::scm_engine::iso8601_now();
    let date_str = today.split('T').next().unwrap_or(&today);

    let rendered = template_content
        .replace("{target}", target)
        .replace("{author}", author)
        .replace("{date}", date_str);

    let out_p = if let Some(p) = output_path {
        p.to_path_buf()
    } else {
        let root = project_root
            .map(|p| p.to_path_buf())
            .unwrap_or_else(|| std::env::current_dir().unwrap_or_else(|_| PathBuf::from(".")));
        root.join("extensions").join(norm_type).join(format!("{target}_ext.4gl"))
    };

    if let Some(parent) = out_p.parent() {
        fs::create_dir_all(parent)?;
    }
    fs::write(&out_p, rendered)?;

    Ok(out_p)
}

/// Infers extension type (`"table"` or `"session"`) and target component code.
pub fn infer_extension_metadata(source_path: &Path, raw_text: &str) -> (String, String) {
    let stem = source_path.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_lowercase();
    let mut ext_type = "table".to_string();
    let mut target = stem.clone();

    if raw_text.contains("<sourceType>8</sourceType>") || raw_text.contains("bic_sessionext") {
        ext_type = "session".to_string();
    } else if raw_text.contains("<sourceType>6</sourceType>") || raw_text.contains("bic_tableext") || raw_text.contains("bic_dal2") {
        ext_type = "table".to_string();
    }

    if stem.starts_with("txest") {
        ext_type = "table".to_string();
        target = stem[5..].to_string();
    } else if stem.starts_with("txess") {
        ext_type = "session".to_string();
        target = stem[5..].to_string();
    } else if source_path.iter().any(|part| part == "est") {
        ext_type = "table".to_string();
        if stem.starts_with("tx") {
            target = stem[2..].to_string();
        }
    } else if source_path.iter().any(|part| part == "ess") {
        ext_type = "session".to_string();
        if stem.starts_with("tx") {
            target = stem[2..].to_string();
        }
    }

    if target.ends_with("_ext") {
        target = target[..target.len() - 4].to_string();
    }

    (ext_type, target)
}

/// Imports an extension script from an XML component definition or `.4gl` file,
/// normalizing `#context_on` blocks into standard local project format.
pub fn import_extension(
    source_path: &Path,
    output_path: Option<&Path>,
    ext_type_override: Option<&str>,
    project_root: Option<&Path>,
) -> Result<PathBuf, ScmError> {
    if !source_path.exists() {
        return Err(ScmError::FileNotFound(format!("Source file does not exist: {:?}", source_path)));
    }

    let raw = fs::read_to_string(source_path)?;

    // If XML (.lib or <DR_Module>), extract script from <expression>
    let script_code = if source_path.extension().and_then(|e| e.to_str()).map(|e| e.eq_ignore_ascii_case("lib")).unwrap_or(false)
        || raw.contains("<DR_Module>")
        || raw.contains("<expression>")
    {
        ln_model::dom_surgery::extract_script(&raw)
            .ok_or_else(|| ScmError::Other(format!("No <expression> 4GL script found in {:?}", source_path)))?
    } else {
        raw.clone()
    };

    let (inferred_type, target) = infer_extension_metadata(source_path, &raw);
    let final_type = ext_type_override.unwrap_or(&inferred_type).to_lowercase();

    let out_p = if let Some(p) = output_path {
        p.to_path_buf()
    } else {
        let root = project_root
            .map(|p| p.to_path_buf())
            .unwrap_or_else(|| std::env::current_dir().unwrap_or_else(|_| PathBuf::from(".")));
        root.join("extensions").join(&final_type).join(format!("{target}_ext.4gl"))
    };

    let normalized: String = script_code
        .lines()
        .map(|l| l.trim_end())
        .collect::<Vec<_>>()
        .join("\n")
        .trim()
        .to_string()
        + "\n";

    if let Some(parent) = out_p.parent() {
        fs::create_dir_all(parent)?;
    }
    fs::write(&out_p, normalized)?;

    Ok(out_p)
}

/// Formats the Agent Guide-and-Paste Protocol Markdown for `ttext1500m000` hook-by-hook instructions.
pub fn format_guide_and_paste_protocol(file_path: &Path) -> Result<String, ScmError> {
    let content = fs::read_to_string(file_path)?;
    let hooks = parse_extension_hooks(&content);

    let comp_name = file_path.file_stem().and_then(|s| s.to_str()).unwrap_or("extension");

    let mut lines = Vec::new();
    lines.push("# Agent Guide-and-Paste Protocol (Infor LN Extension Modeler)".to_string());
    lines.push("Per ADR 0006, Extension Modeler scripts are segregated from LN Studio BDE SCM.".to_string());
    lines.push("Follow these instructions to apply hooks directly in Infor LN UI:\n".to_string());
    lines.push(format!("- **Target Session**: `ttext1500m000` (Extension Modeler)"));
    lines.push(format!("- **Extension Component**: `{comp_name}`"));
    lines.push(format!("- **Total Hook Blocks**: {}", hooks.len()));
    lines.push(format!("- **Source File**: `{}`\n", file_path.to_string_lossy()));

    for (idx, hook) in hooks.iter().enumerate() {
        lines.push(format!("### Hook {}/{}: `{}`", idx + 1, hooks.len(), hook.name));
        lines.push(format!("- Lines {}-{} ({} code lines)", hook.start_line, hook.end_line, hook.code_lines_count()));
        lines.push("- Paste the following clean code block into the corresponding hook in `ttext1500m000`:\n".to_string());
        lines.push("```4gl".to_string());
        lines.push(hook.clean_code().trim_end().to_string());
        lines.push("```\n".to_string());
    }

    Ok(lines.join("\n"))
}

/// Runs `ln-linter` rules `EXT001`–`EXT003` on an extension file and returns diagnostics.
pub fn lint_extension(file_path: &Path) -> Vec<ln_linter::Diagnostic> {
    let source = fs::read_to_string(file_path).unwrap_or_default();
    ln_linter::audit_content(&source, &file_path.to_string_lossy(), false, None)
}

/// Runs `ln-linter` rules on extension source code string.
pub fn lint_extension_source(source: &str, file_name: &str) -> Vec<ln_linter::Diagnostic> {
    ln_linter::audit_content(source, file_name, false, None)
}
