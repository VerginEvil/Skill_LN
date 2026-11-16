use std::collections::BTreeMap;
use std::env;
use std::fs::File;
use std::io::{BufWriter, Write};
use std::path::PathBuf;
use regex::Regex;
use serde::Deserialize;

#[derive(Deserialize)]
struct RawFunction {
    name: String,
    syntax: Option<String>,
    return_type: Option<String>,
    trusted: Option<bool>,
    deprecated: Option<bool>,
    internal: Option<bool>,
    script_type: Option<String>,
    include: Option<String>,
    doc_path: Option<String>,
    description: Option<String>,
}

#[derive(Deserialize)]
struct RawDalFieldHook {
    suffix: String,
    #[serde(rename = "returnValue")]
    return_value: String,
    arguments: String,
    body: String,
}

#[derive(Deserialize)]
struct RawTemplate {
    id: String,
    name: String,
    description: String,
    context: String,
    pattern: String,
}

#[derive(Deserialize)]
struct RawSyntaxCompletion {
    keywords: Vec<String>,
    sql_keywords: Vec<String>,
    program_sections: Vec<String>,
    sub_sections: Vec<String>,
    choice_sections: Vec<String>,
    report_sections: Vec<String>,
    predefined_variables: Vec<String>,
    standard_defines: Vec<String>,
    other_keywords: Vec<String>,
    dal_object_hooks: Vec<String>,
    dal_field_hook_suffixes: Vec<RawDalFieldHook>,
    templates: Vec<RawTemplate>,
}

fn parse_argument_bounds(syntax: &str) -> (usize, usize, bool) {
    if !syntax.contains('(') || !syntax.contains(')') {
        return (0, 0, false);
    }
    let start = syntax.find('(').unwrap() + 1;
    let end = syntax.rfind(')').unwrap();
    if start >= end {
        return (0, 0, false);
    }
    let inside = syntax[start..end].trim();
    if inside.is_empty() || inside.eq_ignore_ascii_case("void") || inside.eq_ignore_ascii_case("none") {
        return (0, 0, false);
    }
    let is_variadic = inside.contains("...");

    let re_opt = Regex::new(r"\[.*?\]").unwrap();
    let mandatory = re_opt.replace_all(inside, "");
    let mand_parts: Vec<&str> = mandatory
        .split(',')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty() && *s != "...")
        .collect();
    let min_args = mand_parts.len();

    let clean_total = inside.replace('[', "").replace(']', "");
    let tot_parts: Vec<&str> = clean_total
        .split(',')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty() && *s != "...")
        .collect();
    let max_args = if is_variadic { 999 } else { tot_parts.len() };

    (min_args, max_args, is_variadic)
}

fn escape_rust_string(s: &str) -> String {
    s.replace('\\', "\\\\")
        .replace('"', "\\\"")
        .replace('\n', "\\n")
        .replace('\r', "\\r")
        .replace('\t', "\\t")
}

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    let manifest_dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap());
    let repo_root = manifest_dir.join("../../../");

    let fn_db_path = repo_root.join("erp-ln-progguide/index/functions_db.json");
    let syntax_path = repo_root.join("erp-ln-progguide/references/studio_syntax_completion.json");

    println!("cargo:rerun-if-changed={}", fn_db_path.display());
    println!("cargo:rerun-if-changed={}", syntax_path.display());

    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());
    let dest_path = out_dir.join("codegen_kb.rs");
    let mut f = BufWriter::new(File::create(&dest_path).unwrap());

    // 1. Process Functions DB
    let fn_db_content = std::fs::read_to_string(&fn_db_path)
        .unwrap_or_else(|e| panic!("Failed to read {}: {}", fn_db_path.display(), e));
    let raw_functions: BTreeMap<String, RawFunction> = serde_json::from_str(&fn_db_content).unwrap();

    let mut sorted_fns: Vec<RawFunction> = raw_functions.into_values().collect();
    sorted_fns.sort_by(|a, b| a.name.to_lowercase().cmp(&b.name.to_lowercase()));

    writeln!(f, "pub static ALL_FUNCTIONS: [FunctionEntry; {}] = [", sorted_fns.len()).unwrap();
    for func in &sorted_fns {
        let syn = func.syntax.as_deref().unwrap_or("");
        let (min_args, max_args, is_variadic) = parse_argument_bounds(syn);
        let trusted = func.trusted.unwrap_or(true);
        let deprecated = func.deprecated.unwrap_or(false);
        let internal = func.internal.unwrap_or(false);
        let ret_type = func.return_type.as_deref().unwrap_or("void");
        let script_type = func.script_type.as_deref().unwrap_or("all");
        let include = func.include.as_deref().unwrap_or("");
        let doc_path = func.doc_path.as_deref().unwrap_or("");
        let desc = func.description.as_deref().unwrap_or("");

        // Format single-line grep-friendly signature
        // Format: `- **<name>** | [Cloud: <Trusted|Untrusted>] [Deprecated] [Scope: <type>] [Inc: <<header>>] | <syntax> -> <doc_link>`
        let mut parts = Vec::new();
        parts.push(if trusted { "[Cloud: Trusted]" } else { "[Cloud: Untrusted]" });
        if deprecated {
            parts.push("[Deprecated]");
        }
        let scope_str = format!("[Scope: {script_type}]");
        parts.push(&scope_str);
        let inc_str = format!("[Inc: <{include}>]");
        if !include.is_empty() {
            parts.push(&inc_str);
        }
        let formatted = format!(
            "- **{}** | {} | {} -> {}",
            func.name,
            parts.join(" "),
            syn,
            doc_path
        );

        writeln!(
            f,
            r#"    FunctionEntry {{
        name: "{}",
        syntax: "{}",
        return_type: "{}",
        min_args: {},
        max_args: {},
        is_variadic: {},
        is_cloud_trusted: {},
        deprecated: {},
        internal: {},
        script_type: "{}",
        include: "{}",
        doc_path: {},
        description: "{}",
        formatted_line: "{}",
    }},"#,
            escape_rust_string(&func.name),
            escape_rust_string(syn),
            escape_rust_string(ret_type),
            min_args,
            max_args,
            is_variadic,
            trusted,
            deprecated,
            internal,
            escape_rust_string(script_type),
            escape_rust_string(include),
            if doc_path.is_empty() { "None".to_string() } else { format!("Some(\"{}\")", escape_rust_string(doc_path)) },
            escape_rust_string(desc),
            escape_rust_string(&formatted),
        ).unwrap();
    }
    writeln!(f, "];\n").unwrap();

    // 2. Process Syntax Completion
    let syntax_content = std::fs::read_to_string(&syntax_path)
        .unwrap_or_else(|e| panic!("Failed to read {}: {}", syntax_path.display(), e));
    let raw_syntax: RawSyntaxCompletion = serde_json::from_str(&syntax_content).unwrap();

    fn write_str_slice(f: &mut BufWriter<File>, name: &str, items: &[String]) {
        writeln!(f, "pub static {}: &[&str] = &[", name).unwrap();
        for item in items {
            writeln!(f, "    \"{}\",", escape_rust_string(item)).unwrap();
        }
        writeln!(f, "];\n").unwrap();
    }

    write_str_slice(&mut f, "SYNTAX_KEYWORDS", &raw_syntax.keywords);
    write_str_slice(&mut f, "SYNTAX_SQL_KEYWORDS", &raw_syntax.sql_keywords);
    write_str_slice(&mut f, "SYNTAX_PROGRAM_SECTIONS", &raw_syntax.program_sections);
    write_str_slice(&mut f, "SYNTAX_SUB_SECTIONS", &raw_syntax.sub_sections);
    write_str_slice(&mut f, "SYNTAX_CHOICE_SECTIONS", &raw_syntax.choice_sections);
    write_str_slice(&mut f, "SYNTAX_REPORT_SECTIONS", &raw_syntax.report_sections);
    write_str_slice(&mut f, "SYNTAX_PREDEFINED_VARIABLES", &raw_syntax.predefined_variables);
    write_str_slice(&mut f, "SYNTAX_STANDARD_DEFINES", &raw_syntax.standard_defines);
    write_str_slice(&mut f, "SYNTAX_OTHER_KEYWORDS", &raw_syntax.other_keywords);
    write_str_slice(&mut f, "SYNTAX_DAL_OBJECT_HOOKS", &raw_syntax.dal_object_hooks);

    writeln!(f, "pub static SYNTAX_DAL_FIELD_HOOK_SUFFIXES: &[DalFieldHookSuffix] = &[").unwrap();
    for hook in &raw_syntax.dal_field_hook_suffixes {
        writeln!(
            f,
            r#"    DalFieldHookSuffix {{
        suffix: "{}",
        return_value: "{}",
        arguments: "{}",
        body: "{}",
    }},"#,
            escape_rust_string(&hook.suffix),
            escape_rust_string(&hook.return_value),
            escape_rust_string(&hook.arguments),
            escape_rust_string(&hook.body),
        ).unwrap();
    }
    writeln!(f, "];\n").unwrap();

    writeln!(f, "pub static SYNTAX_TEMPLATES: &[SyntaxTemplate] = &[").unwrap();
    for tmpl in &raw_syntax.templates {
        writeln!(
            f,
            r#"    SyntaxTemplate {{
        id: "{}",
        name: "{}",
        description: "{}",
        context: "{}",
        pattern: "{}",
    }},"#,
            escape_rust_string(&tmpl.id),
            escape_rust_string(&tmpl.name),
            escape_rust_string(&tmpl.description),
            escape_rust_string(&tmpl.context),
            escape_rust_string(&tmpl.pattern),
        ).unwrap();
    }
    writeln!(f, "];\n").unwrap();
}
