use std::time::Instant;
use ln_kb::search_docs;

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
