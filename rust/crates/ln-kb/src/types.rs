use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct FunctionEntry {
    pub name: &'static str,
    pub syntax: &'static str,
    pub return_type: &'static str,
    pub min_args: usize,
    pub max_args: usize,
    pub is_variadic: bool,
    pub is_cloud_trusted: bool,
    pub deprecated: bool,
    pub internal: bool,
    pub script_type: &'static str,
    pub include: &'static str,
    pub doc_path: Option<&'static str>,
    pub description: &'static str,
    pub formatted_line: &'static str,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct DalFieldHookSuffix {
    pub suffix: &'static str,
    pub return_value: &'static str,
    pub arguments: &'static str,
    pub body: &'static str,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct SyntaxTemplate {
    pub id: &'static str,
    pub name: &'static str,
    pub description: &'static str,
    pub context: &'static str,
    pub pattern: &'static str,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DocHit {
    pub line_number: usize,
    pub snippet: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DocSearchResult {
    pub rel_path: String,
    pub title: String,
    pub score: usize,
    pub hits: Vec<DocHit>,
}
