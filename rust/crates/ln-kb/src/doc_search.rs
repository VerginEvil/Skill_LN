use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::{Path, PathBuf};
use regex::Regex;
use crate::types::{DocHit, DocSearchResult};

pub const MAX_OUTPUT_CHARS: usize = 12000;

pub fn find_progguide_references_dir() -> Option<PathBuf> {
    if let Ok(env_val) = std::env::var("ERP_LN_PROGGUIDE_DIR") {
        let p = PathBuf::from(env_val).join("references");
        if p.exists() {
            return Some(p);
        }
    }

    let candidates = [
        "erp-ln-progguide/references",
        "../erp-ln-progguide/references",
        "../../erp-ln-progguide/references",
        "../../../erp-ln-progguide/references",
    ];

    for c in candidates {
        let p = PathBuf::from(c);
        if p.exists() {
            return p.canonicalize().ok().or(Some(p));
        }
    }

    // Check relative to current exe
    if let Ok(exe) = std::env::current_exe() {
        if let Some(parent) = exe.parent() {
            for c in candidates {
                let p = parent.join(c);
                if p.exists() {
                    return p.canonicalize().ok().or(Some(p));
                }
            }
        }
    }

    None
}

/// Searches documentation markdown corpus, matching the scoring, ranking, and output of `search.py`.
pub fn search_docs(
    query: &str,
    dir_scope: Option<&str>,
    group_filter: Option<&str>,
    max_results: usize,
) -> (Vec<DocSearchResult>, String) {
    let q = query.trim();
    if q.is_empty() {
        return (Vec::new(), String::new());
    }

    let base_dir = match find_progguide_references_dir() {
        Some(d) => d,
        None => return (Vec::new(), "[WARN] erp-ln-progguide references directory not found".to_string()),
    };

    let target_dir = match dir_scope.unwrap_or("all") {
        "all" => base_dir.clone(),
        other => base_dir.join(other),
    };

    let re_opt = Regex::new(&format!("(?i){}", q)).ok();
    let terms: Vec<String> = q.split_whitespace().map(|s| s.to_lowercase()).collect();

    let mut scored: Vec<DocSearchResult> = Vec::new();
    let mut files_to_scan = Vec::new();
    collect_md_files(&target_dir, &mut files_to_scan);
    files_to_scan.sort();

    for file_path in files_to_scan {
        let rel_path = file_path
            .strip_prefix(base_dir.parent().unwrap_or(&base_dir))
            .unwrap_or(&file_path)
            .to_string_lossy()
            .replace('\\', "/");

        if let Some(group) = group_filter {
            if !rel_path.to_lowercase().contains(&group.to_lowercase()) {
                continue;
            }
        }

        let file = match File::open(&file_path) {
            Ok(f) => f,
            Err(_) => continue,
        };

        let reader = BufReader::new(file);
        let mut title = String::new();
        let mut hits = Vec::new();

        for (i, line_res) in reader.lines().enumerate() {
            let line = match line_res {
                Ok(l) => l,
                Err(_) => continue,
            };

            let line_num = i + 1;
            if line_num == 1 && line.starts_with('#') {
                title = line.trim_start_matches('#').trim().to_string();
            }

            let matches = if let Some(re) = &re_opt {
                re.is_match(&line)
            } else {
                let line_low = line.to_lowercase();
                terms.iter().all(|t| line_low.contains(t))
            };

            if matches {
                hits.push(DocHit {
                    line_number: line_num,
                    snippet: line.trim().to_string(),
                });
            }
        }

        if !hits.is_empty() {
            let score = hits.len();
            scored.push(DocSearchResult {
                rel_path,
                title,
                score,
                hits,
            });
        }
    }

    // Sort by (-score, len(rp))
    scored.sort_by(|a, b| {
        b.score.cmp(&a.score).then_with(|| a.rel_path.len().cmp(&b.rel_path.len()))
    });

    let mut out_lines = Vec::new();
    let mut total_chars = 0;
    let mut shown = 0;

    for item in &scored {
        if shown >= max_results || total_chars > MAX_OUTPUT_CHARS {
            break;
        }
        shown += 1;

        let head = if !item.title.is_empty() {
            format!("{} | {}", item.rel_path, item.title)
        } else {
            item.rel_path.clone()
        };
        total_chars += head.len() + 1;
        out_lines.push(head);

        for hit in item.hits.iter().take(6) {
            let snippet = if hit.snippet.len() > 160 {
                format!("{}...", &hit.snippet[..157])
            } else {
                hit.snippet.clone()
            };
            let line_str = format!("  {}: {}", hit.line_number, snippet);
            total_chars += line_str.len() + 1;
            out_lines.push(line_str);
        }

        if item.hits.len() > 6 {
            let more_str = format!("  ... +{} more lines", item.hits.len() - 6);
            total_chars += more_str.len() + 1;
            out_lines.push(more_str);
        }
    }

    if scored.len() > shown {
        out_lines.push(format!("({} more files matched; refine terms or raise --max)", scored.len() - shown));
    }

    let formatted_output = out_lines.join("\n");
    (scored, formatted_output)
}

fn collect_md_files(dir: &Path, acc: &mut Vec<PathBuf>) {
    if !dir.is_dir() {
        return;
    }
    let entries = match std::fs::read_dir(dir) {
        Ok(e) => e,
        Err(_) => return,
    };

    for entry in entries.flatten() {
        let p = entry.path();
        if p.is_dir() {
            collect_md_files(&p, acc);
        } else if p.extension().map(|e| e == "md").unwrap_or(false) {
            acc.push(p);
        }
    }
}
