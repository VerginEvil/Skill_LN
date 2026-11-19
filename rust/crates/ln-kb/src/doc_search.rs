use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::{Path, PathBuf};
use regex::Regex;
use crate::types::{DocHit, DocSearchResult};

pub const MAX_OUTPUT_CHARS: usize = 12000;

pub fn find_progguide_references_dir_strict(
    cwd: Option<&Path>,
    exe: Option<&Path>,
    home_override: Option<&Path>,
) -> Option<PathBuf> {
    let rel_candidates = [
        ".agents/skills/erp-ln-progguide/references",
        "erp-ln-progguide/references",
    ];

    for base in [cwd, exe.and_then(|p| p.parent())].into_iter().flatten() {
        for ancestor in base.ancestors().take(5) {
            for rel in rel_candidates {
                let p = ancestor.join(rel);
                if p.exists() {
                    return p.canonicalize().ok().or(Some(p));
                }
            }
        }
    }

    let resolved_home = home_override.map(PathBuf::from).or_else(|| {
        std::env::var_os("USERPROFILE")
            .or_else(|| std::env::var_os("HOME"))
            .map(PathBuf::from)
    });
    if let Some(home) = resolved_home {
        for rel in [
            ".gemini/config/skills/erp-ln-progguide/references",
            ".agents/skills/erp-ln-progguide/references",
        ] {
            let p = home.join(rel);
            if p.exists() {
                return p.canonicalize().ok().or(Some(p));
            }
        }
    }

    None
}

pub fn find_progguide_references_dir_with_home(
    cwd: Option<&Path>,
    exe: Option<&Path>,
    home_override: Option<&Path>,
) -> Option<PathBuf> {
    if let Some(found) = find_progguide_references_dir_strict(cwd, exe, home_override) {
        return Some(found);
    }

    if home_override.is_none() {
        let manifest_dir = Path::new(env!("CARGO_MANIFEST_DIR"));
        if let Some(repo_root) = manifest_dir.parent().and_then(|p| p.parent()) {
            let p = repo_root.join(".agents/skills/erp-ln-progguide/references");
            if p.exists() {
                return p.canonicalize().ok().or(Some(p));
            }
        }
    }

    None
}

pub fn find_progguide_references_dir_from(
    cwd: Option<&Path>,
    exe: Option<&Path>,
) -> Option<PathBuf> {
    find_progguide_references_dir_with_home(cwd, exe, None)
}

pub fn find_progguide_references_dir() -> Option<PathBuf> {
    if let Ok(env_val) = std::env::var("ERP_LN_PROGGUIDE_DIR") {
        let p = PathBuf::from(env_val).join("references");
        if p.exists() {
            return Some(p);
        }
    }

    find_progguide_references_dir_from(
        std::env::current_dir().ok().as_deref(),
        std::env::current_exe().ok().as_deref(),
    )
}

/// Searches documentation markdown corpus with multi-term AND matching and phrase-boost ranking.
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
        None => {
            return (
                Vec::new(),
                "[WARN] erp-ln-progguide references directory not found; set ERP_LN_PROGGUIDE_DIR or run `python scripts/run_checks.py --sync-skill`".to_string(),
            )
        }
    };

    let target_dir = match dir_scope.unwrap_or("all") {
        "all" => base_dir.clone(),
        other => base_dir.join(other),
    };

    let q_low = q.to_lowercase();
    let raw_terms: Vec<String> = q_low.split_whitespace().map(|s| s.to_string()).collect();
    let mut terms: Vec<String> = Vec::new();
    for t in &raw_terms {
        if t == "bic_utf8" {
            terms.push("utf8".to_string());
        } else {
            terms.push(t.clone());
        }
    }
    let has_regex_meta = raw_terms.len() == 1
        && q.chars().any(|c| matches!(c, '*' | '?' | '[' | ']' | '(' | ')' | '|' | '^' | '$'));
    let re_opt = if has_regex_meta {
        Regex::new(&format!("(?i){}", q)).ok()
    } else {
        None
    };

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
        let mut term_seen = vec![false; terms.len()];
        let rel_low = rel_path.to_lowercase();
        for (idx, t) in terms.iter().enumerate() {
            if rel_low.contains(t) {
                term_seen[idx] = true;
            }
        }

        let mut ranked_hits: Vec<(usize, DocHit)> = Vec::new();
        let mut score: usize = 0;

        for (i, line_res) in reader.lines().enumerate() {
            let line = match line_res {
                Ok(l) => l,
                Err(_) => continue,
            };

            let line_num = i + 1;
            if line_num == 1 && line.starts_with('#') {
                title = line.trim_start_matches('#').trim().to_string();
            }

            if let Some(re) = &re_opt {
                if re.is_match(&line) {
                    score += 2;
                    ranked_hits.push((
                        2,
                        DocHit {
                            line_number: line_num,
                            snippet: line.trim().to_string(),
                        },
                    ));
                    for s in &mut term_seen {
                        *s = true;
                    }
                }
            } else {
                let line_low = line.to_lowercase();
                let mut line_match_count = 0usize;
                for (idx, t) in terms.iter().enumerate() {
                    if line_low.contains(t) {
                        term_seen[idx] = true;
                        line_match_count += 1;
                    }
                }
                if line_match_count > 0 {
                    let is_phrase = line_low.contains(&q_low);
                    let weight = if is_phrase {
                        10
                    } else if line_match_count == terms.len() {
                        3
                    } else {
                        1
                    };
                    score += weight;
                    ranked_hits.push((
                        weight,
                        DocHit {
                            line_number: line_num,
                            snippet: line.trim().to_string(),
                        },
                    ));
                }
            }
        }

        if term_seen.iter().all(|&seen| seen) && !ranked_hits.is_empty() {
            let title_low = title.to_lowercase();
            if terms.iter().all(|t| title_low.contains(t) || rel_low.contains(t)) {
                score += 5;
            }
            ranked_hits.sort_by(|a, b| b.0.cmp(&a.0).then_with(|| a.1.line_number.cmp(&b.1.line_number)));
            let hits: Vec<DocHit> = ranked_hits.into_iter().map(|(_, h)| h).collect();
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
