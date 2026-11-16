use std::path::Path;
use ln_daemon::registry::{compute_workspace_hash, get_daemon_lock_file, get_daemon_reg_file};

#[test]
fn test_workspace_hash_calculation() {
    let path = Path::new("C:/Users/test/workspace_lnstudio");
    let hash = compute_workspace_hash(Some(path));
    assert_eq!(hash.len(), 16);

    // Global workspace fallback
    let global_hash = compute_workspace_hash(None);
    assert_eq!(global_hash, "global");

    let reg_file = get_daemon_reg_file(Some(path));
    assert!(reg_file.to_string_lossy().contains(&format!("daemon_{hash}.json")));

    let lock_file = get_daemon_lock_file(Some(path));
    assert!(lock_file.to_string_lossy().contains(&format!("daemon_{hash}.lock")));
}
