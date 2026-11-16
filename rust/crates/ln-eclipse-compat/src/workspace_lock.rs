use std::fs::{File, OpenOptions};
use std::io;
use std::path::{Path, PathBuf};
use thiserror::Error;

#[cfg(windows)]
use std::os::windows::fs::OpenOptionsExt;

#[derive(Error, Debug)]
pub enum LockError {
    #[error(transparent)]
    Io(#[from] io::Error),
    #[error("Workspace is locked by another process (Eclipse or LN Studio active)")]
    Locked,
}

/// Active lock guard holding `<workspace>/.metadata/.lock`.
#[derive(Debug)]
pub struct WorkspaceLock {
    _file: File,
    pub path: PathBuf,
}

/// Checks if `<workspace>/.metadata/.lock` is currently locked by another process.
/// Non-blocking check.
pub fn is_workspace_locked(workspace_path: &Path) -> bool {
    let lock_file = workspace_path.join(".metadata").join(".lock");
    if !lock_file.exists() {
        return false;
    }

    let mut opts = OpenOptions::new();
    opts.read(true).write(true);
    #[cfg(windows)]
    opts.share_mode(0); // Exclusive access

    match opts.open(&lock_file) {
        Ok(_file) => false,
        Err(e) => {
            if let Some(code) = e.raw_os_error() {
                // Windows: 32 = ERROR_SHARING_VIOLATION, 33 = ERROR_LOCK_VIOLATION
                code == 32 || code == 33
            } else {
                e.kind() == io::ErrorKind::PermissionDenied
            }
        }
    }
}

/// Attempts to acquire an exclusive lock on an arbitrary lock file path.
pub fn try_acquire_file_lock(lock_path: &Path) -> Result<WorkspaceLock, LockError> {
    if let Some(parent) = lock_path.parent() {
        if !parent.exists() {
            std::fs::create_dir_all(parent)?;
        }
    }

    let mut opts = OpenOptions::new();
    opts.read(true).write(true).create(true).truncate(false);
    #[cfg(windows)]
    opts.share_mode(0); // Exclusive access: blocks subsequent openers with ERROR_SHARING_VIOLATION (32)

    let file = match opts.open(lock_path) {
        Ok(f) => f,
        Err(e) => {
            if let Some(code) = e.raw_os_error() {
                if code == 32 || code == 33 {
                    return Err(LockError::Locked);
                }
            }
            if e.kind() == io::ErrorKind::PermissionDenied {
                return Err(LockError::Locked);
            }
            return Err(LockError::Io(e));
        }
    };

    Ok(WorkspaceLock {
        _file: file,
        path: lock_path.to_path_buf(),
    })
}

/// Attempts to acquire an exclusive lock on `<workspace>/.metadata/.lock`.
/// Returns Ok(WorkspaceLock) if successful, or Err(LockError::Locked) if already locked.
pub fn try_acquire_workspace_lock(workspace_path: &Path) -> Result<WorkspaceLock, LockError> {
    let lock_path = workspace_path.join(".metadata").join(".lock");
    try_acquire_file_lock(&lock_path)
}
