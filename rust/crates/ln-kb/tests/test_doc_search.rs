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

#[test]
fn test_doc_search_external_cwd_fallback_and_multi_term_topics() {
    // 1. Multi-term query must match across lines/file rather than requiring adjacent exact regex
    let (multi_hits, _) = search_docs("query.extend.where EXTEND_OVERWRITE", None, None, 10);
    assert!(
        !multi_hits.is_empty(),
        "Multi-term query 'query.extend.where EXTEND_OVERWRITE' must return hits"
    );

    // 2. Common 4GL topics from handoff must return hits
    for topic in [
        "before.display.object",
        "method.is.allowed",
        "table.super",
        "tcsli.srtp",
        "utf8.export",
        "bic_utf8",
    ] {
        let (hits, _) = search_docs(topic, None, None, 5);
        assert!(
            !hits.is_empty(),
            "Expected non-zero doc_search hits for topic '{topic}'"
        );
    }

    // 3. Running from an unrelated temp dir without ancestors still resolves fallback references
    let unrelated = tempdir().unwrap();
    let fake_exe = unrelated.path().join("bin").join("skill-ln.exe");
    let resolved = ln_kb::doc_search::find_progguide_references_dir_with_home(
        Some(unrelated.path()),
        Some(&fake_exe),
        None,
    );
    assert!(
        resolved.is_some(),
        "Expected global/compile-time fallback when invoked from unrelated CWD"
    );

    // 4. When no corpus exists at all (with explicit missing home), search_docs returns a [WARN] message
    let missing_home = tempdir().unwrap();
    let none_dir = ln_kb::doc_search::find_progguide_references_dir_strict(
        Some(unrelated.path()),
        Some(&fake_exe),
        Some(missing_home.path()),
    );
    assert!(none_dir.is_none());
}
