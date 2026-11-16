use std::collections::HashMap;
use quick_xml::events::Event;
use quick_xml::Reader;

/// A lightweight in-memory XML node for parsing BDE and metadata payloads.
#[derive(Debug, Clone, Default)]
pub struct SimpleXmlNode {
    pub tag: String,
    pub attributes: HashMap<String, String>,
    pub text: String,
    pub children: Vec<SimpleXmlNode>,
}

impl SimpleXmlNode {
    /// Recursively finds the first node with the specified tag name (case-insensitive).
    pub fn find_first(&self, tag: &str) -> Option<&SimpleXmlNode> {
        if self.tag.eq_ignore_ascii_case(tag) {
            return Some(self);
        }
        for child in &self.children {
            if let Some(found) = child.find_first(tag) {
                return Some(found);
            }
        }
        None
    }

    /// Recursively finds all nodes with the specified tag name (case-insensitive).
    pub fn find_all(&self, tag: &str) -> Vec<&SimpleXmlNode> {
        let mut results = Vec::new();
        self.collect_all(tag, &mut results);
        results
    }

    fn collect_all<'a>(&'a self, tag: &str, results: &mut Vec<&'a SimpleXmlNode>) {
        if self.tag.eq_ignore_ascii_case(tag) {
            results.push(self);
        }
        for child in &self.children {
            child.collect_all(tag, results);
        }
    }

    /// Direct child node by tag name (case-insensitive).
    pub fn child(&self, tag: &str) -> Option<&SimpleXmlNode> {
        self.children.iter().find(|c| c.tag.eq_ignore_ascii_case(tag))
    }

    /// Direct child text by tag name (case-insensitive).
    pub fn child_text(&self, tag: &str) -> Option<&str> {
        self.child(tag).map(|c| c.text.trim())
    }

    /// Recursively finds the first occurrence of a tag and returns its text.
    pub fn find_text(&self, tag: &str) -> Option<&str> {
        self.find_first(tag).map(|c| c.text.trim())
    }

    /// Looks up an attribute value by name (case-insensitive).
    pub fn attr(&self, key: &str) -> Option<&str> {
        for (k, v) in &self.attributes {
            if k.eq_ignore_ascii_case(key) {
                return Some(v.as_str());
            }
        }
        None
    }
}

/// Parses raw XML text into a `SimpleXmlNode` tree.
/// Automatically handles both single-root documents and multi-element fragments.
pub fn parse_xml_to_tree(xml: &str) -> Result<SimpleXmlNode, String> {
    let trimmed = xml.trim();
    if trimmed.is_empty() {
        return Ok(SimpleXmlNode::default());
    }

    let xml_body = if trimmed.starts_with("<?xml") {
        if let Some(idx) = trimmed.find("?>") {
            trimmed[idx + 2..].trim()
        } else {
            trimmed
        }
    } else {
        trimmed
    };

    let wrapped = format!("<synthetic_root>{xml_body}</synthetic_root>");
    let mut reader = Reader::from_str(&wrapped);
    reader.config_mut().trim_text(true);
    let mut stack: Vec<SimpleXmlNode> = Vec::new();
    let mut root = None;

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                let tag = String::from_utf8_lossy(e.local_name().as_ref()).to_string();
                let mut attrs = HashMap::new();
                for a in e.attributes().flatten() {
                    let key = String::from_utf8_lossy(a.key.local_name().as_ref()).to_string();
                    let val = String::from_utf8_lossy(&a.value).to_string();
                    attrs.insert(key, val);
                }
                stack.push(SimpleXmlNode {
                    tag,
                    attributes: attrs,
                    text: String::new(),
                    children: Vec::new(),
                });
            }
            Ok(Event::End(_)) => {
                if let Some(node) = stack.pop() {
                    if let Some(parent) = stack.last_mut() {
                        parent.children.push(node);
                    } else {
                        root = Some(node);
                    }
                }
            }
            Ok(Event::Empty(e)) => {
                let tag = String::from_utf8_lossy(e.local_name().as_ref()).to_string();
                let mut attrs = HashMap::new();
                for a in e.attributes().flatten() {
                    let key = String::from_utf8_lossy(a.key.local_name().as_ref()).to_string();
                    let val = String::from_utf8_lossy(&a.value).to_string();
                    attrs.insert(key, val);
                }
                let node = SimpleXmlNode {
                    tag,
                    attributes: attrs,
                    text: String::new(),
                    children: Vec::new(),
                };
                if let Some(parent) = stack.last_mut() {
                    parent.children.push(node);
                } else {
                    root = Some(node);
                }
            }
            Ok(Event::Text(t)) => {
                if let Some(current) = stack.last_mut() {
                    let text = t.unescape().unwrap_or_default().to_string();
                    current.text.push_str(&text);
                }
            }
            Ok(Event::CData(c)) => {
                if let Some(current) = stack.last_mut() {
                    let text = String::from_utf8_lossy(&c).to_string();
                    current.text.push_str(&text);
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => return Err(format!("XML parse error: {e}")),
            _ => {}
        }
    }

    if let Some(mut synthetic) = root {
        if synthetic.children.len() == 1 {
            return Ok(synthetic.children.remove(0));
        }
        return Ok(synthetic);
    }

    Err("Empty XML document".to_string())
}
