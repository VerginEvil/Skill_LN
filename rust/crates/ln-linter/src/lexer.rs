use regex::Regex;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum TokenKind {
    Word,
    LBrace,
    RBrace,
    LParen,
    RParen,
    Colon,
    Assign,
    Directive,
    Symbol,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Token4GL {
    pub kind: TokenKind,
    pub value: String,
    pub line: usize,
    pub column: usize,
    pub raw_line: String,
}

/// Strip string literals and pipe comments from a line, preserving code structure.
pub fn strip_4gl_comments_and_strings(line: &str, in_multiline_doc: bool) -> (String, bool) {
    let line_lower = line.trim().to_lowercase();
    if in_multiline_doc {
        if line_lower.contains("enddllusage") || line_lower.contains("endfunctionusage") {
            return (String::new(), false);
        }
        return (String::new(), true);
    }

    if line_lower.starts_with("dllusage") || line_lower.starts_with("functionusage") {
        return (String::new(), true);
    }

    let mut res = Vec::new();
    let chars: Vec<char> = line.chars().collect();
    let n = chars.len();
    let mut i = 0;
    let mut in_str = false;
    let mut str_char = ' ';

    while i < n {
        let c = chars[i];
        if in_str {
            if c == '\\' && i + 1 < n {
                i += 2;
                continue;
            }
            if c == str_char {
                in_str = false;
            }
            i += 1;
            continue;
        }

        if c == '"' || c == '\'' {
            in_str = true;
            str_char = c;
            res.push(' ');
            i += 1;
            continue;
        }

        if c == '|' {
            break;
        }

        res.push(c);
        i += 1;
    }

    (res.into_iter().collect(), false)
}

/// Tokenizes Baan 4GL source into clean lines and token stream.
pub fn tokenize_4gl(content: &str) -> (Vec<String>, Vec<Token4GL>) {
    let mut cleaned_lines = Vec::new();
    let mut tokens = Vec::new();
    let mut in_multiline_doc = false;
    let mut in_define_continuation = false;

    let re_directive = Regex::new(r"^\s*#\s*(define|pragma|ident|ifdef|ifndef|elif|else|endif|undef)\b").unwrap();
    let re_ctx_on = Regex::new(r#"^\s*#context_on\s*(?:["']([^"']+)["'])?"#).unwrap();
    let re_ctx_off = Regex::new(r"^\s*#context_off\b").unwrap();
    let re_include = Regex::new(r"^\s*#include\b").unwrap();

    let token_pattern = Regex::new(
        r"(\{|\}|\(|\)|:=|==|<>|<=|>=|=|:|,|;|\b[a-zA-Z_][a-zA-Z0-9_.]*\b)"
    ).unwrap();

    for (line_idx, raw_line) in content.lines().enumerate() {
        let line_no = line_idx + 1;
        let stripped_lower = raw_line.trim().to_lowercase();

        if in_multiline_doc {
            cleaned_lines.push(String::new());
            if stripped_lower.contains("enddllusage") || stripped_lower.contains("endfunctionusage") {
                in_multiline_doc = false;
            }
            continue;
        }

        if stripped_lower.starts_with("dllusage") || stripped_lower.starts_with("functionusage") {
            cleaned_lines.push(String::new());
            in_multiline_doc = true;
            continue;
        }

        let (code_line, doc_state) = strip_4gl_comments_and_strings(raw_line, in_multiline_doc);
        in_multiline_doc = doc_state;
        let code_stripped = code_line.trim();

        if in_define_continuation {
            cleaned_lines.push(String::new());
            if !code_stripped.ends_with('\\') {
                in_define_continuation = false;
            }
            continue;
        }

        if re_directive.is_match(&code_line) {
            if code_stripped.ends_with('\\') {
                in_define_continuation = true;
            }
            cleaned_lines.push(String::new());
            continue;
        }

        cleaned_lines.push(code_line.clone());

        if let Some(caps) = re_ctx_on.captures(raw_line) {
            let ctx_name = caps.get(1).map(|m| m.as_str()).unwrap_or("unknown");
            tokens.push(Token4GL {
                kind: TokenKind::Directive,
                value: format!("#context_on:{ctx_name}"),
                line: line_no,
                column: 1,
                raw_line: raw_line.to_string(),
            });
            continue;
        }

        if re_ctx_off.is_match(raw_line) {
            tokens.push(Token4GL {
                kind: TokenKind::Directive,
                value: "#context_off".to_string(),
                line: line_no,
                column: 1,
                raw_line: raw_line.to_string(),
            });
            continue;
        }

        if re_include.is_match(raw_line) {
            continue;
        }

        // Tokenize code line
        for mat in token_pattern.find_iter(&code_line) {
            let val = mat.as_str();
            let col = mat.start() + 1;
            let kind = match val {
                "{" => TokenKind::LBrace,
                "}" => TokenKind::RBrace,
                "(" => TokenKind::LParen,
                ")" => TokenKind::RParen,
                ":" => TokenKind::Colon,
                "=" | ":=" => TokenKind::Assign,
                s if s.starts_with(|c: char| c.is_alphabetic() || c == '_') => TokenKind::Word,
                _ => TokenKind::Symbol,
            };

            tokens.push(Token4GL {
                kind,
                value: val.to_string(),
                line: line_no,
                column: col,
                raw_line: raw_line.to_string(),
            });
        }
    }

    (cleaned_lines, tokens)
}
