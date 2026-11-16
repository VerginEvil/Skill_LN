use std::time::Instant;
use ln_kb::doc_search::find_progguide_references_dir_from;
use ln_kb::search_docs;
use tempfile::tempdir;

#[test]
fn test_doc_search_execution() {
    let start = Instant::now();
    let (results, formatted) = search_docs("seq.open", None, None, 10);
    let elapsed = start.elapsed();

    println!("doc_search elapsed: {:?}", elapsed);
    assert!(!results.is_empty(), "Should find doc hits for seq.open");
    assert!(formatted.contains("seq.open"));

    // Check first hit
    let first = &results[0];
    assert!(!first.rel_path.is_empty());
    assert!(!first.hits.is_empty());
}

#[test]
fn test_find_progguide_references_dir_prefers_agents_layout_with_root_fallback() {
    let td = tempdir().unwrap();
    let root = td.path();
    let nested = root.join("rust").join("crates");
    std::fs::create_dir_all(&nested).unwrap();

    // Only root layout exists -> falls back to root
    let root_refs = root.join("erp-ln-progguide").join("references");
    std::fs::create_dir_all(&root_refs).unwrap();
    let resolved_fallback = find_progguide_references_dir_from(Some(&nested), None).unwrap();
    assert_eq!(resolved_fallback, root_refs.canonicalize().unwrap());

    // When .agents/skills layout also exists -> prefers .agents/skills
    let agents_refs = root.join(".agents").join("skills").join("erp-ln-progguide").join("references");
    std::fs::create_dir_all(&agents_refs).unwrap();
    let resolved_agents = find_progguide_references_dir_from(Some(&nested), None).unwrap();
    assert_eq!(resolved_agents, agents_refs.canonicalize().unwrap());
}
