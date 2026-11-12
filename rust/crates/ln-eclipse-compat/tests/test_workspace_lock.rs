use ln_eclipse_compat::{
    is_workspace_locked, try_acquire_workspace_lock,
};
use tempfile::tempdir;

#[test]
fn test_workspace_lock_lifecycle() {
    let dir = tempdir().unwrap();
    let ws_path = dir.path();

    // 1. When .metadata/.lock doesn't exist, not locked
    assert!(!is_workspace_locked(ws_path));

    // 2. Acquire lock
    let lock = try_acquire_workspace_lock(ws_path).unwrap();
    assert!(lock.path.exists());

    // 3. Second acquire on same process/file on Windows or is_locked
    // Note: on Windows, while file handle is open with write access:
    #[cfg(windows)]
    {
        // Try acquiring another lock while first is held
        let lock2 = try_acquire_workspace_lock(ws_path);
        assert!(lock2.is_err(), "Second lock acquire should fail while first lock is held");
    }

    // 4. Release lock
    drop(lock);

    // After dropping lock, acquiring should succeed again
    let lock3 = try_acquire_workspace_lock(ws_path);
    assert!(lock3.is_ok(), "Should be able to acquire lock after drop");
}
