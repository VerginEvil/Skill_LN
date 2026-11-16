use std::fmt;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Serialize, Deserialize)]
pub enum Severity {
    Info,
    Warning,
    Error,
}

impl Severity {
    pub fn as_str(&self) -> &'static str {
        match self {
            Self::Info => "INFO",
            Self::Warning => "WARNING",
            Self::Error => "ERROR",
        }
    }
}

impl fmt::Display for Severity {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.as_str())
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Diagnostic {
    pub file: String,
    pub line: usize,
    pub column: usize,
    pub severity: Severity,
    pub code: String,
    pub message: String,
    pub snippet: String,
}

impl Diagnostic {
    pub fn new(
        file: impl Into<String>,
        line: usize,
        column: usize,
        severity: Severity,
        code: impl Into<String>,
        message: impl Into<String>,
        snippet: impl Into<String>,
    ) -> Self {
        Self {
            file: file.into(),
            line,
            column,
            severity,
            code: code.into(),
            message: message.into(),
            snippet: snippet.into().trim().to_string(),
        }
    }
}

impl fmt::Display for Diagnostic {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "[{}] {} {}:{}:{}: {}",
            self.severity, self.code, self.file, self.line, self.column, self.message
        )?;
        if !self.snippet.is_empty() {
            write!(f, "\n       -> {}", self.snippet)?;
        }
        Ok(())
    }
}
