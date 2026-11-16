use std::path::{Path, PathBuf};
use std::process::Command;
use serde::{Deserialize, Serialize};
use thiserror::Error;

use crate::crash_recorder::record_crash_fixture;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum FallbackMode {
    Auto,
    Strict,
    Off,
}

impl FallbackMode {
    pub fn from_str(s: &str) -> Self {
        match s.trim().to_lowercase().as_str() {
            "auto" => Self::Auto,
            "off" => Self::Off,
            _ => Self::Strict,
        }
    }

    pub fn from_env_or_arg(cli_arg: Option<&str>) -> Self {
        if let Some(arg) = cli_arg {
            return Self::from_str(arg);
        }
        if let Ok(env_val) = std::env::var("LN_FALLBACK_MODE") {
            return Self::from_str(&env_val);
        }
        Self::Strict
    }
}

#[derive(Error, Debug)]
pub enum VerifyError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("JVM class parse error: {0}")]
    ClassParse(String),

    #[error("ZIP error: {0}")]
    Zip(#[from] zip::result::ZipError),

    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),

    #[error("Strict fallback blocked. Saved fixture to {0}")]
    StrictFallbackBlocked(PathBuf),

    #[error("Python fallback execution failed: {0}")]
    PythonFallback(String),

    #[error("{0}")]
    General(String),
}

/// Discovers the location of `ln_component_builder.py` in the workspace or repository.
pub fn find_python_builder_script() -> Option<PathBuf> {
    if let Ok(cur_dir) = std::env::current_dir() {
        let mut d = cur_dir.as_path();
        loop {
            let cand = d.join("ln_studio_skill").join("tools").join("ln_component_builder.py");
            if cand.exists() {
                return cand.canonicalize().ok().or(Some(cand));
            }
            if let Some(parent) = d.parent() {
                d = parent;
            } else {
                break;
            }
        }
    }

    if let Ok(cur_exe) = std::env::current_exe() {
        let mut d = cur_exe.as_path();
        while let Some(parent) = d.parent() {
            let cand = parent.join("ln_studio_skill").join("tools").join("ln_component_builder.py");
            if cand.exists() {
                return cand.canonicalize().ok().or(Some(cand));
            }
            d = parent;
        }
    }

    None
}

/// Invokes the legacy Python tool `ln_component_builder.py` with the supplied command line arguments.
pub fn invoke_python_fallback(args: &[String]) -> Result<String, VerifyError> {
    let builder_script = find_python_builder_script()
        .ok_or_else(|| VerifyError::PythonFallback("Could not find ln_component_builder.py".to_string()))?;

    let py_cmd = if cfg!(windows) { "python" } else { "python3" };

    let mut cmd = Command::new(py_cmd);
    cmd.arg(&builder_script);
    cmd.args(args);

    let output = cmd.output().map_err(|e| VerifyError::PythonFallback(format!("Failed to execute python: {e}")))?;

    let stdout_str = String::from_utf8_lossy(&output.stdout).to_string();
    let stderr_str = String::from_utf8_lossy(&output.stderr).to_string();

    if !output.status.success() {
        return Err(VerifyError::PythonFallback(format!(
            "Python script exited with {}: {stderr_str}\n{stdout_str}",
            output.status
        )));
    }

    Ok(stdout_str)
}

/// Fallback executor wrapper around an operation.
pub fn run_with_fallback<T, F>(
    mode: FallbackMode,
    bde: &str,
    method: &str,
    bde_mode: &str,
    request_xml: &str,
    command_args: &[String],
    custom_crash_dir: Option<&Path>,
    operation: F,
) -> Result<T, VerifyError>
where
    F: FnOnce() -> Result<T, String>,
    T: From<String>,
{
    match operation() {
        Ok(val) => Ok(val),
        Err(err_msg) => match mode {
            FallbackMode::Off => Err(VerifyError::General(err_msg)),
            FallbackMode::Strict => {
                let fixture_path = record_crash_fixture(
                    bde,
                    method,
                    bde_mode,
                    request_xml,
                    None,
                    None,
                    "",
                    &err_msg,
                    custom_crash_dir,
                )?;
                Err(VerifyError::StrictFallbackBlocked(fixture_path))
            }
            FallbackMode::Auto => {
                let fixture_path = record_crash_fixture(
                    bde,
                    method,
                    bde_mode,
                    request_xml,
                    None,
                    None,
                    "",
                    &err_msg,
                    custom_crash_dir,
                )?;
                eprintln!("[WARN: Fallback Triggered -> saved fixture {}]", fixture_path.display());
                if !command_args.is_empty() {
                    let py_out = invoke_python_fallback(command_args)?;
                    Ok(T::from(py_out))
                } else {
                    Err(VerifyError::StrictFallbackBlocked(fixture_path))
                }
            }
        },
    }
}
