pub mod admin;
pub mod properties_index;
pub mod markers;
pub mod workspace_lock;

pub use admin::{
    AdminFile, AdministrationComponent, AdminError,
    normalize_admin_path, is_managed_extension, is_excluded_extension,
    MANAGED_EXTENSIONS, EXCLUDED_EXTENSIONS,
};
pub use properties_index::{
    PropertyBucket, ProjectProperties, StudioProjectSettings, PropertyBucketError,
};
pub use markers::{
    MarkersFile, ProblemMarker, MarkerSeverity, AttributeValue, MarkerError,
};
pub use workspace_lock::{
    is_workspace_locked, try_acquire_workspace_lock, try_acquire_file_lock, WorkspaceLock, LockError,
};
