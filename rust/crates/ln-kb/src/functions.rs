use regex::Regex;
use crate::types::{DalFieldHookSuffix, FunctionEntry, SyntaxTemplate};

include!(concat!(env!("OUT_DIR"), "/codegen_kb.rs"));

/// O(1) / O(log N) zero-copy static lookup by function name.
/// Returns exact signature, argument bounds, and Cloud Trust status.
pub fn lookup_function(name: &str) -> Option<&'static FunctionEntry> {
    let query = name.trim().to_lowercase();
    if query.is_empty() {
        return None;
    }

    // Binary search over sorted static slice
    if let Ok(idx) = ALL_FUNCTIONS.binary_search_by(|entry| entry.name.to_lowercase().cmp(&query)) {
        return Some(&ALL_FUNCTIONS[idx]);
    }

    // Linear fallback for any special casing or alias
    for entry in ALL_FUNCTIONS.iter() {
        if entry.name.eq_ignore_ascii_case(name.trim()) {
            return Some(entry);
        }
    }

    None
}

/// Fast search across all 2,266 functions by name, syntax, or description.
/// Returns matched function entries.
pub fn search_functions(query: &str) -> Vec<&'static FunctionEntry> {
    let q = query.trim();
    if q.is_empty() {
        return ALL_FUNCTIONS.iter().collect();
    }

    // Attempt regex match if regex characters exist
    if let Ok(re) = Regex::new(&format!("(?i){}", q)) {
        let mut results = Vec::new();
        for entry in ALL_FUNCTIONS.iter() {
            if re.is_match(entry.name) || re.is_match(entry.syntax) || re.is_match(entry.description) {
                results.push(entry);
            }
        }
        if !results.is_empty() {
            return results;
        }
    }

    // Substring fallback
    let q_low = q.to_lowercase();
    let terms: Vec<&str> = q_low.split_whitespace().collect();

    ALL_FUNCTIONS
        .iter()
        .filter(|entry| {
            let name_low = entry.name.to_lowercase();
            let syn_low = entry.syntax.to_lowercase();
            let desc_low = entry.description.to_lowercase();

            terms.iter().all(|t| {
                name_low.contains(t) || syn_low.contains(t) || desc_low.contains(t)
            })
        })
        .collect()
}

pub fn all_functions() -> &'static [FunctionEntry] {
    &ALL_FUNCTIONS
}
