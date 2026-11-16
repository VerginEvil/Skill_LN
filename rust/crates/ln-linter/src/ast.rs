use std::collections::HashMap;
use crate::diagnostic::{Diagnostic, Severity};
use crate::lexer::{tokenize_4gl, Token4GL, TokenKind};

#[derive(Debug, Clone)]
pub struct FunctionASTNode {
    pub name: String,
    pub line: usize,
    pub end_line: usize,
    pub return_type: String,
    pub params: String,
    pub direct_tx_calls: Vec<(String, usize, usize, String)>,
    pub callees: Vec<(String, usize, usize, String)>,
    pub calls_inside_tx: Vec<(String, usize, usize, String, usize)>,
    pub nested_tx_starts: Vec<(String, usize, usize, String, usize)>,
}

impl FunctionASTNode {
    pub fn new(name: impl Into<String>, line: usize) -> Self {
        Self {
            name: name.into(),
            line,
            end_line: 0,
            return_type: String::new(),
            params: String::new(),
            direct_tx_calls: Vec::new(),
            callees: Vec::new(),
            calls_inside_tx: Vec::new(),
            nested_tx_starts: Vec::new(),
        }
    }
}

pub struct ASTParser4GL {
    pub file_path: String,
    pub raw_lines: Vec<String>,
    pub cleaned_lines: Vec<String>,
    pub tokens: Vec<Token4GL>,
    pub diagnostics: Vec<Diagnostic>,
    pub functions: HashMap<String, FunctionASTNode>,
}

impl ASTParser4GL {
    pub fn new(content: &str, file_path: &str) -> Self {
        Self {
            file_path: file_path.to_string(),
            raw_lines: content.lines().map(|s| s.to_string()).collect(),
            cleaned_lines: Vec::new(),
            tokens: Vec::new(),
            diagnostics: Vec::new(),
            functions: HashMap::new(),
        }
    }

    pub fn preprocess_and_tokenize(&mut self, content: &str) -> &[String] {
        let (cleaned, tokens) = tokenize_4gl(content);
        self.cleaned_lines = cleaned;
        self.tokens = tokens;
        &self.cleaned_lines
    }

    pub fn parse(&mut self) -> (&[Diagnostic], &HashMap<String, FunctionASTNode>) {
        let mut block_stack: Vec<(String, usize, String)> = Vec::new(); // (block_type, line_no, extra_state)
        let mut context_stack: Vec<(String, usize)> = Vec::new();
        let mut brace_stack: Vec<(char, usize)> = Vec::new();

        let mut paren_depth: usize = 0;
        let mut current_func_name: Option<String> = None;
        let mut tx_active_since_line: Option<usize> = None;

        let n = self.tokens.len();
        let mut i = 0;

        while i < n {
            let tok = &self.tokens[i];
            let val_lower = tok.value.to_lowercase();

            // 1. Directives (#context_on / #context_off)
            if tok.kind == TokenKind::Directive {
                if tok.value.starts_with("#context_on:") {
                    let ctx_name = tok.value.splitn(2, ':').nth(1).unwrap_or("unknown");
                    if let Some((parent_type, parent_line)) = context_stack.last() {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            format!(
                                "Nested '#context_on' is not allowed: block '{ctx_name}' opened inside '{parent_type}' (line {parent_line})."
                            ),
                            &tok.raw_line,
                        ));
                    }
                    context_stack.push((format!("#context_on \"{ctx_name}\""), tok.line));
                } else if tok.value == "#context_off" {
                    if context_stack.is_empty() {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched '#context_off' without corresponding '#context_on'.",
                            &tok.raw_line,
                        ));
                    } else {
                        context_stack.pop();
                    }
                }
                i += 1;
                continue;
            }

            // 2. Parentheses tracking
            if tok.kind == TokenKind::LParen {
                paren_depth += 1;
                i += 1;
                continue;
            }
            if tok.kind == TokenKind::RParen {
                paren_depth = paren_depth.saturating_sub(1);
                i += 1;
                continue;
            }

            // 3. Curly Braces & Function body tracking
            if tok.kind == TokenKind::LBrace {
                brace_stack.push(('{', tok.line));
                i += 1;
                continue;
            }
            if tok.kind == TokenKind::RBrace {
                if brace_stack.is_empty() {
                    self.diagnostics.push(Diagnostic::new(
                        &self.file_path,
                        tok.line,
                        tok.column,
                        Severity::Error,
                        "SYN001",
                        "Unmatched closing brace '}'.",
                        &tok.raw_line,
                    ));
                } else {
                    brace_stack.pop();
                    if let Some(ref fname) = current_func_name {
                        if brace_stack.is_empty() {
                            if let Some(fnode) = self.functions.get_mut(fname) {
                                fnode.end_line = tok.line;
                            }
                            current_func_name = None;
                            tx_active_since_line = None;
                        }
                    }
                }
                i += 1;
                continue;
            }

            // 4. Function Declarations: `function [extern] [<type>] <name>(...)`
            if tok.kind == TokenKind::Word && val_lower == "function" && brace_stack.is_empty() {
                let mut j = i + 1;
                let mut words_before_paren: Vec<&Token4GL> = Vec::new();
                while j < n && self.tokens[j].kind == TokenKind::Word && self.tokens[j].line == tok.line {
                    words_before_paren.push(&self.tokens[j]);
                    j += 1;
                }
                if !words_before_paren.is_empty() && j < n && self.tokens[j].kind == TokenKind::LParen {
                    let fn_tok = words_before_paren.last().unwrap();
                    let fn_name = fn_tok.value.to_lowercase();
                    let fn_node = FunctionASTNode::new(&fn_name, tok.line);
                    self.functions.insert(fn_name.clone(), fn_node);
                    current_func_name = Some(fn_name);
                    tx_active_since_line = None;
                }
                i += 1;
                continue;
            }

            // 5. Control & SQL Block Keywords
            if tok.kind == TokenKind::Word {
                // ON CASE
                if val_lower == "on" && i + 1 < n && self.tokens[i + 1].kind == TokenKind::Word && self.tokens[i + 1].value.eq_ignore_ascii_case("case") {
                    block_stack.push(("case".to_string(), tok.line, "open".to_string()));
                    i += 2;
                    continue;
                }

                if val_lower == "endcase" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("case") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'endcase' without corresponding 'on case'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // SELECT / SELECTDO / SELECTEMPTY / SELECTEOS / ENDSELECT
                if val_lower == "select" {
                    if paren_depth == 0 {
                        block_stack.push(("select".to_string(), tok.line, "query".to_string()));
                    }
                    i += 1;
                    continue;
                }

                if matches!(val_lower.as_str(), "selectdo" | "selectempty" | "selecteos") {
                    let mut select_idx = None;
                    for (idx, item) in block_stack.iter().enumerate().rev() {
                        if item.0 == "select" {
                            select_idx = Some(idx);
                            break;
                        }
                    }
                    if let Some(idx) = select_idx {
                        let (sel_type, sel_line, _) = &block_stack[idx];
                        block_stack[idx] = (sel_type.clone(), *sel_line, val_lower.clone());
                    } else {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            format!("'{val_lower}' statement outside of an active 'select' block."),
                            &tok.raw_line,
                        ));
                    }
                    i += 1;
                    continue;
                }

                if val_lower == "endselect" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("select") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'endselect' without corresponding 'select'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // FOR <var> = <init> TO <limit> (exclude SQL `for update`)
                if val_lower == "for" {
                    if i + 2 < n
                        && self.tokens[i + 1].kind == TokenKind::Word
                        && !self.tokens[i + 1].value.eq_ignore_ascii_case("update")
                        && self.tokens[i + 2].kind == TokenKind::Assign
                    {
                        block_stack.push(("for".to_string(), tok.line, "loop".to_string()));
                    }
                    i += 1;
                    continue;
                }

                if val_lower == "endfor" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("for") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'endfor' without corresponding 'for'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // WHILE / ENDWHILE
                if val_lower == "while" {
                    block_stack.push(("while".to_string(), tok.line, "loop".to_string()));
                    i += 1;
                    continue;
                }

                if val_lower == "endwhile" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("while") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'endwhile' without corresponding 'while'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // REPEAT / UNTIL
                if val_lower == "repeat" {
                    block_stack.push(("repeat".to_string(), tok.line, "loop".to_string()));
                    i += 1;
                    continue;
                }

                if val_lower == "until" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("repeat") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'until' without corresponding 'repeat'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // IF / ENDIF
                if val_lower == "if" {
                    block_stack.push(("if".to_string(), tok.line, "cond".to_string()));
                    i += 1;
                    continue;
                }

                if val_lower == "endif" {
                    if block_stack.last().map(|b| b.0.as_str()) != Some("if") {
                        self.diagnostics.push(Diagnostic::new(
                            &self.file_path,
                            tok.line,
                            tok.column,
                            Severity::Error,
                            "SYN001",
                            "Unmatched 'endif' without corresponding 'if'.",
                            &tok.raw_line,
                        ));
                    } else {
                        block_stack.pop();
                    }
                    i += 1;
                    continue;
                }

                // 6. Function Calls & Transaction State Tracking inside Function Bodies
                if let Some(ref fname) = current_func_name {
                    if i + 1 < n && self.tokens[i + 1].kind == TokenKind::LParen {
                        let cur_fn_line = self.functions.get(fname).map(|f| f.line).unwrap_or(0);
                        if tok.line != cur_fn_line || &val_lower != fname {
                            if matches!(val_lower.as_str(), "db.retry.point" | "commit.transaction" | "abort.transaction") {
                                if let Some(fnode) = self.functions.get_mut(fname) {
                                    fnode.direct_tx_calls.push((val_lower.clone(), tok.line, tok.column, tok.raw_line.clone()));
                                    if val_lower == "db.retry.point" {
                                        if let Some(active_line) = tx_active_since_line {
                                            fnode.nested_tx_starts.push((val_lower.clone(), tok.line, tok.column, tok.raw_line.clone(), active_line));
                                        } else {
                                            tx_active_since_line = Some(tok.line);
                                        }
                                    } else {
                                        tx_active_since_line = None;
                                    }
                                }
                            } else {
                                if let Some(fnode) = self.functions.get_mut(fname) {
                                    fnode.callees.push((val_lower.clone(), tok.line, tok.column, tok.raw_line.clone()));
                                    if let Some(active_line) = tx_active_since_line {
                                        fnode.calls_inside_tx.push((val_lower.clone(), tok.line, tok.column, tok.raw_line.clone(), active_line));
                                    }
                                }
                            }
                        }
                    }
                }
            }

            i += 1;
        }

        // End-of-file unclosed blocks (SYN001)
        while let Some((blk_type, blk_line, _)) = block_stack.pop() {
            self.diagnostics.push(Diagnostic::new(
                &self.file_path,
                blk_line,
                1,
                Severity::Error,
                "SYN001",
                format!("Unclosed '{blk_type}' statement opened at line {blk_line}."),
                "",
            ));
        }

        while let Some((ctx_type, ctx_line)) = context_stack.pop() {
            self.diagnostics.push(Diagnostic::new(
                &self.file_path,
                ctx_line,
                1,
                Severity::Error,
                "SYN001",
                format!("Unclosed '{ctx_type}' opened at line {ctx_line}."),
                "",
            ));
        }

        while let Some((brace_char, brace_line)) = brace_stack.pop() {
            self.diagnostics.push(Diagnostic::new(
                &self.file_path,
                brace_line,
                1,
                Severity::Error,
                "SYN001",
                format!("Unclosed brace '{brace_char}' opened at line {brace_line}."),
                "",
            ));
        }

        (&self.diagnostics, &self.functions)
    }

    pub fn find_transitive_tx_functions(&self) -> HashMap<String, Vec<String>> {
        let mut tx_map: HashMap<String, Vec<String>> = HashMap::new();
        for (fname, fnode) in &self.functions {
            if let Some((tx_fn, _, _, _)) = fnode.direct_tx_calls.first() {
                tx_map.insert(fname.clone(), vec![format!("{tx_fn}()")]);
            }
        }

        let mut changed = true;
        while changed {
            changed = false;
            for (fname, fnode) in &self.functions {
                if tx_map.contains_key(fname) {
                    continue;
                }
                for (callee_name, _, _, _) in &fnode.callees {
                    if let Some(chain) = tx_map.get(callee_name).cloned() {
                        let mut full_chain = vec![callee_name.clone()];
                        full_chain.extend(chain);
                        tx_map.insert(fname.clone(), full_chain);
                        changed = true;
                        break;
                    }
                }
            }
        }

        tx_map
    }
}
