pub mod ast;
pub mod auditor;
pub mod dd_cache;
pub mod diagnostic;
pub mod lexer;

pub use ast::{ASTParser4GL, FunctionASTNode};
pub use auditor::Auditor4GL;
pub use dd_cache::{DataDictionaryCache, DomainMeta, FieldMeta, TableMeta, BSHELL_PSEUDO_FIELDS};
pub use diagnostic::{Diagnostic, Severity};
pub use lexer::{strip_4gl_comments_and_strings, tokenize_4gl, Token4GL, TokenKind};

/// Convenient one-liner for auditing 4GL content with default auditor settings.
pub fn audit_content(
    content: &str,
    file_path: &str,
    cloud_mode: bool,
    mode: Option<&str>,
) -> Vec<Diagnostic> {
    let auditor = Auditor4GL::new().with_cloud_mode(cloud_mode);
    auditor.audit_content(content, file_path, mode, None)
}
