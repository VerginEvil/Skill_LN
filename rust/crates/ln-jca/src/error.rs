use std::fmt;
use thiserror::Error;

#[derive(Debug, Clone, Error)]
pub struct BdeExecutionError {
    pub message: String,
    pub bde: String,
    pub method: String,
    pub status_code: Option<u16>,
    pub exception_code: Option<i32>,
    pub raw_response: String,
}

impl fmt::Display for BdeExecutionError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "BDE Execution Error for '{}.{}' (status: {:?}, code: {:?}): {}",
            self.bde, self.method, self.status_code, self.exception_code, self.message
        )
    }
}

#[derive(Error, Debug)]
pub enum JcaError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("HTTP error: {0}")]
    Http(#[from] reqwest::Error),
    #[error("URL parse error: {0}")]
    Url(#[from] url::ParseError),
    #[error("XML error: {0}")]
    Xml(String),
    #[error("BDE execution error: {0}")]
    Bde(#[from] BdeExecutionError),
    #[error("Authentication error: {0}")]
    Auth(String),
    #[error("Protocol error: {0}")]
    Protocol(String),
    #[error("Operation prohibited by safety policy: {0}")]
    Prohibited(String),
}
