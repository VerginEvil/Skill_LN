use ln_kb::{all_functions, lookup_function, search_functions};

#[test]
fn test_all_2266_functions_indexed() {
    let fns = all_functions();
    assert_eq!(fns.len(), 2266, "Exactly 2,266 bshell functions must be indexed at compile time");
}

#[test]
fn test_lookup_functions() {
    // 1. db.retry.point (Cloud: Trusted)
    let db_retry = lookup_function("db.retry.point").expect("db.retry.point must exist");
    assert_eq!(db_retry.name, "db.retry.point");
    assert!(db_retry.is_cloud_trusted);
    assert_eq!(db_retry.return_type, "void");
    assert_eq!(db_retry.min_args, 0);
    assert_eq!(db_retry.max_args, 0);
    assert!(!db_retry.is_variadic);
    assert!(db_retry.formatted_line.contains("[Cloud: Trusted]"));

    // Case-insensitive lookup
    let db_retry_upper = lookup_function("DB.RETRY.POINT").expect("Case insensitive lookup");
    assert_eq!(db_retry_upper.name, "db.retry.point");

    // 2. dal.set.error.message (Cloud: Trusted, variadic)
    let dal_err = lookup_function("dal.set.error.message").expect("dal.set.error.message must exist");
    assert_eq!(dal_err.name, "dal.set.error.message");
    assert!(dal_err.is_cloud_trusted);
    assert_eq!(dal_err.min_args, 1);
    assert!(dal_err.is_variadic);

    // 3. run.prog (Cloud: Untrusted - CLD001 rule target)
    let run_prog = lookup_function("run.prog").expect("run.prog must exist");
    assert_eq!(run_prog.name, "run.prog");
    assert!(!run_prog.is_cloud_trusted, "run.prog MUST be Untrusted for CloudSuite multi-tenant");
    assert_eq!(run_prog.return_type, "long");
    assert_eq!(run_prog.min_args, 3);
    assert_eq!(run_prog.max_args, 6);
    assert!(run_prog.formatted_line.contains("[Cloud: Untrusted]"));
}

#[test]
fn test_search_functions() {
    let results = search_functions("db.retry.point");
    assert!(!results.is_empty());
    assert!(results.iter().any(|f| f.name == "db.retry.point"));

    let dal_results = search_functions("dal.set.");
    assert!(dal_results.len() >= 3);
    assert!(dal_results.iter().any(|f| f.name == "dal.set.error.message"));
    assert!(dal_results.iter().any(|f| f.name == "dal.set.warning.message"));
    assert!(dal_results.iter().any(|f| f.name == "dal.set.info.message"));
}
