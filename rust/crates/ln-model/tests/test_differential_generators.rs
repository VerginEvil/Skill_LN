use std::io::Write;
use std::process::{Command, Stdio};
use ln_model::*;
use quick_xml::events::Event;
use quick_xml::Reader;

pub fn find_first_diff(path: &str, a: &CanonicalElement, b: &CanonicalElement) -> Option<String> {
    if a.name != b.name {
        return Some(format!("{path}: tag name mismatch: '{}' != '{}'", a.name, b.name));
    }
    if a.attributes != b.attributes {
        return Some(format!("{path}: attributes mismatch: {:?} != {:?}", a.attributes, b.attributes));
    }
    if a.text != b.text {
        return Some(format!("{path} ({}): text mismatch:\nA: '{}'\nB: '{}'", a.name, a.text, b.text));
    }
    if a.children.len() != b.children.len() {
        return Some(format!(
            "{path} ({}): children count mismatch: {} != {}. A: {:?}, B: {:?}",
            a.name, a.children.len(), b.children.len(),
            a.children.iter().map(|c| &c.name).collect::<Vec<_>>(),
            b.children.iter().map(|c| &c.name).collect::<Vec<_>>()
        ));
    }
    for (i, (ca, cb)) in a.children.iter().zip(b.children.iter()).enumerate() {
        let child_path = format!("{path}/{}[{i}]", ca.name);
        if let Some(diff) = find_first_diff(&child_path, ca, cb) {
            return Some(diff);
        }
    }
    None
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CanonicalElement {
    pub name: String,
    pub attributes: Vec<(String, String)>,
    pub text: String,
    pub children: Vec<CanonicalElement>,
}

pub fn parse_canonical_xml(xml: &str) -> CanonicalElement {
    let mut reader = Reader::from_str(xml);
    reader.config_mut().trim_text(true);

    let mut stack: Vec<CanonicalElement> = Vec::new();
    let mut root: Option<CanonicalElement> = None;

    loop {
        match reader.read_event() {
            Ok(Event::Start(ref e)) => {
                let name = String::from_utf8_lossy(e.name().as_ref()).to_string();
                let mut attrs = Vec::new();
                for a in e.attributes() {
                    if let Ok(attr) = a {
                        let k = String::from_utf8_lossy(attr.key.as_ref()).to_string();
                        let v = String::from_utf8_lossy(&attr.value).to_string();
                        attrs.push((k, v));
                    }
                }
                attrs.sort();
                stack.push(CanonicalElement {
                    name,
                    attributes: attrs,
                    text: String::new(),
                    children: Vec::new(),
                });
            }
            Ok(Event::End(_)) => {
                let mut elem = stack.pop().expect("Mismatched closing tag in XML");
                if elem.name == "modificationDateTime" || elem.name == "creationDateTime" {
                    elem.text = "TIMESTAMP".to_string();
                } else {
                    elem.text = elem.text.replace("\r\n", "\n");
                }
                if let Some(parent) = stack.last_mut() {
                    parent.children.push(elem);
                } else {
                    root = Some(elem);
                }
            }
            Ok(Event::Empty(ref e)) => {
                let name = String::from_utf8_lossy(e.name().as_ref()).to_string();
                let mut attrs = Vec::new();
                for a in e.attributes() {
                    if let Ok(attr) = a {
                        let k = String::from_utf8_lossy(attr.key.as_ref()).to_string();
                        let v = String::from_utf8_lossy(&attr.value).to_string();
                        attrs.push((k, v));
                    }
                }
                attrs.sort();
                let elem = CanonicalElement {
                    name,
                    attributes: attrs,
                    text: String::new(),
                    children: Vec::new(),
                };
                if let Some(parent) = stack.last_mut() {
                    parent.children.push(elem);
                } else {
                    root = Some(elem);
                }
            }
            Ok(Event::Text(ref t)) => {
                let text = t.unescape().unwrap_or_default().to_string();
                if !text.trim().is_empty() {
                    if let Some(current) = stack.last_mut() {
                        current.text.push_str(text.trim());
                    }
                }
            }
            Ok(Event::CData(ref c)) => {
                let text = String::from_utf8_lossy(c).to_string();
                if let Some(current) = stack.last_mut() {
                    current.text.push_str(text.trim());
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => panic!("XML parse error: {e:?} in xml:\n{xml}"),
            _ => {}
        }
    }

    root.expect("No root element found in XML")
}

fn call_python_generator(payload_json: &str) -> String {
    let manifest_dir = env!("CARGO_MANIFEST_DIR");
    let script_path = std::path::Path::new(manifest_dir).join("tests").join("generate_python_xml.py");

    let mut child = Command::new("python")
        .arg(&script_path)
        .current_dir(manifest_dir)
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .expect("Failed to spawn python generate_python_xml.py");

    {
        let stdin = child.stdin.as_mut().expect("Failed to open stdin");
        stdin.write_all(payload_json.as_bytes()).expect("Failed to write to stdin");
    }

    let output = child.wait_with_output().expect("Failed to wait on child process");
    if !output.status.success() {
        let err = String::from_utf8_lossy(&output.stderr);
        panic!("Python generator failed: {err}");
    }

    String::from_utf8_lossy(&output.stdout).to_string()
}

#[test]
fn test_differential_message_generator() {
    let spec = MessageSpec {
        code: "txcmg0001".to_string(),
        description: Some("Validation error for batch".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        severity: "3".to_string(),
        text: Some("Batch cannot be processed without approval.".to_string()),
        language: 2,
    };

    let rust_xml = generate_message_xml(&spec, "EXTce01107", "B61O_a_ext");

    let payload = serde_json::json!({
        "type": "message",
        "spec": {
            "code": "txcmg0001",
            "description": "Validation error for batch",
            "severity": "3",
            "text": "Batch cannot be processed without approval.",
            "version_id": "B61O_a_ext"
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Message XML DOM parity mismatch");
}

#[test]
fn test_differential_question_generator() {
    let spec = QuestionSpec {
        code: "txcmg0002".to_string(),
        description: Some("Confirm batch posting".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        severity: "2".to_string(),
        domain: "tcyesno".to_string(),
        default_answer: "yes".to_string(),
        text: Some("Do you want to post this billing batch?".to_string()),
        language: 2,
    };

    let rust_xml = generate_question_xml(&spec, "EXTce01107", "B61O_a_ext");

    let payload = serde_json::json!({
        "type": "question",
        "spec": {
            "code": "txcmg0002",
            "description": "Confirm batch posting",
            "severity": "2",
            "domain": "tcyesno",
            "default_answer": "yes",
            "text": "Do you want to post this billing batch?",
            "version_id": "B61O_a_ext"
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Question XML DOM parity mismatch");
}

#[test]
fn test_differential_function_generator() {
    let spec = FunctionSpec {
        code: "txcmgf001".to_string(),
        description: Some("Calculation function".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        script: Some("function extern long calc() { return(42); }".to_string()),
    };

    let rust_xml = generate_function_xml(&spec, "EXTce01107", "B61O_a_ext");

    let payload = serde_json::json!({
        "type": "function",
        "spec": {
            "code": "txcmgf001",
            "description": "Calculation function",
            "version_id": "B61O_a_ext",
            "script": "function extern long calc() { return(42); }"
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Function XML DOM parity mismatch");
}

#[test]
fn test_differential_additional_generator() {
    let spec = AdditionalFileSpec {
        code: "txcmgcfg".to_string(),
        description: Some("Config file".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        content: Some("{\"mode\": \"auto\"}".to_string()),
        keyword1: Some("billing".to_string()),
        keyword2: Some("config".to_string()),
        keyword3: Some(String::new()),
    };

    let rust_xml = generate_additional_xml(&spec, "EXTce01107", "B61O_a_ext");

    let payload = serde_json::json!({
        "type": "additional",
        "spec": {
            "code": "txcmgcfg",
            "description": "Config file",
            "version_id": "B61O_a_ext",
            "content": "{\"mode\": \"auto\"}",
            "keyword1": "billing",
            "keyword2": "config",
            "keyword3": ""
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Additional XML DOM parity mismatch");
}

#[test]
fn test_differential_label_generator() {
    let rust_xml = generate_label_xml("txcmg011", "Billing Batch", "B61O_a_ext", "EXTce01107", Some(13), Some("1970-01-01T00:00:00Z"));

    let payload = serde_json::json!({
        "type": "label",
        "spec": {
            "name": "txcmg011",
            "description": "Billing Batch",
            "length": 13
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Label XML DOM parity mismatch");
}

#[test]
fn test_differential_domain_generator() {
    let spec = DomainSpec {
        name: "txcmg.stat".to_string(),
        description: "Status".to_string(),
        native_datatype: 7,
        display_length: 20,
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        enums: vec![
            EnumItem {
                name: "open".to_string(),
                description: "Open".to_string(),
                position: 10,
                label_code: Some("txcmg.stat010".to_string()),
            },
            EnumItem {
                name: "approved".to_string(),
                description: "Approved".to_string(),
                position: 20,
                label_code: Some("txcmg.stat020".to_string()),
            },
        ],
        facets: Default::default(),
    };

    let rust_xml = generate_domain_xml(&spec, "B61O_a_ext", "EXTce01107");

    let payload = serde_json::json!({
        "type": "domain",
        "spec": {
            "name": "txcmg.stat",
            "description": "Status",
            "native_datatype": 7,
            "display_length": 20,
            "version_id": "B61O_a_ext",
            "application": "EXTce01107",
            "enums": [
                {"name": "open", "description": "Open", "position": 10, "label_code": "txcmg.stat010"},
                {"name": "approved", "description": "Approved", "position": 20, "label_code": "txcmg.stat020"}
            ]
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Domain XML DOM parity mismatch");
}

#[test]
fn test_differential_menu_generator() {
    let spec = MenuSpec {
        code: "txgld0000m001".to_string(),
        description: Some("Enhancements Menu".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        choices: vec![
            MenuChoiceSpec {
                position: 10,
                choice_type: "session".to_string(),
                target: "txcmg0110m100".to_string(),
                description: Some("Billing Batch".to_string()),
            },
            MenuChoiceSpec {
                position: 20,
                choice_type: "menu".to_string(),
                target: "txgld0000m002".to_string(),
                description: Some("Sub Menu".to_string()),
            },
        ],
    };

    let rust_xml = generate_menu_xml(&spec, "EXTce01107", "B61O_a_ext", Some("1970-01-01T00:00:00Z"));

    let payload = serde_json::json!({
        "type": "menu",
        "spec": {
            "code": "txgld0000m001",
            "description": "Enhancements Menu",
            "version_id": "B61O_a_ext",
            "application": "EXTce01107",
            "choices": [
                {"position": 10, "type": "session", "target": "txcmg0110m100", "description": "Billing Batch"},
                {"position": 20, "type": "menu", "target": "txgld0000m002", "description": "Sub Menu"}
            ]
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Menu XML DOM parity mismatch");
}

#[test]
fn test_differential_library_generator() {
    let spec = LibrarySpec {
        code: "txibddllitem01".to_string(),
        description: Some("Item General DLL".to_string()),
        library_type: "dll".to_string(),
        target: None,
        version_id: Some("B61O_a_ext".to_string()),
        script: Some("function extern long get_item() { return(0); }".to_string()),
    };

    let rust_xml = generate_library_xml(&spec, "EXTce01107", "B61O_a_ext", Some("1970-01-01T00:00:00Z"));

    let payload = serde_json::json!({
        "type": "library",
        "spec": {
            "code": "txibddllitem01",
            "description": "Item General DLL",
            "version_id": "B61O_a_ext",
            "type": "dll",
            "script": "function extern long get_item() { return(0); }"
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Library XML DOM parity mismatch");
}

#[test]
fn test_differential_report_generator() {
    let spec = ReportSpec {
        code: "txcmg04010100".to_string(),
        description: Some("Billing Summary Report".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        paper_width: 80,
        input_fields: vec![
            ReportInputFieldSpec {
                fieldname: "btno".to_string(),
                domain: Some("tcmcs.long".to_string()),
                native_datatype: Some(3),
                is_table_field: Some(false),
                sort_sequence: 1,
                sort_mode: 1,
                label: Some("tcgen.btno".to_string()),
            },
        ],
        layouts: vec![
            ReportLayoutSpec {
                layout_type: 2,
                rows: 2,
                columns: 80,
                output_expression: "1".to_string(),
                output_fields: vec![],
                specials: vec![
                    ReportSpecialSpec { special_type: 8, label: "tcgen.h.date".to_string(), row: 1, col: 1, len: 10 },
                    ReportSpecialSpec { special_type: 8, label: "tcgen.page".to_string(), row: 1, col: 65, len: 10 },
                ],
            },
            ReportLayoutSpec {
                layout_type: 4,
                rows: 2,
                columns: 80,
                output_expression: "1".to_string(),
                output_fields: vec![
                    ReportOutputFieldSpec {
                        print_expression: "btno".to_string(),
                        domain: Some("tcmcs.long".to_string()),
                        row: 1,
                        col: 1,
                        len: 9,
                    },
                ],
                specials: vec![],
            },
        ],
        script: Some("detail.1: before.layout:".to_string()),
    };

    let rust_xml = generate_report_xml(&spec, "EXTce01107", "B61O_a_ext", None);

    let payload = serde_json::json!({
        "type": "report",
        "spec": {
            "code": "txcmg04010100",
            "description": "Billing Summary Report",
            "version_id": "B61O_a_ext",
            "paper_width": 80,
            "input_fields": [
                {
                    "fieldname": "btno",
                    "domain": "tcmcs.long",
                    "is_table_field": false,
                    "sort_sequence": 1,
                    "sort_mode": 1,
                    "label": "tcgen.btno"
                }
            ],
            "layouts": [
                {
                    "type": 2,
                    "rows": 2,
                    "columns": 80,
                    "specials": [
                        {"type": 8, "label": "tcgen.h.date", "row": 1, "col": 1, "len": 10},
                        {"type": 8, "label": "tcgen.page", "row": 1, "col": 65, "len": 10}
                    ]
                },
                {
                    "type": 4,
                    "rows": 2,
                    "columns": 80,
                    "output_fields": [
                        {"print_expression": "btno", "domain": "tcmcs.long", "row": 1, "col": 1, "len": 9}
                    ]
                }
            ],
            "script": "detail.1: before.layout:"
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    assert_eq!(rust_dom, py_dom, "Report XML DOM parity mismatch");
}

#[test]
fn test_differential_table_generator() {
    let spec = TableSpec {
        code: "txcmg011".to_string(),
        description: Some("Billing Batch Header".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        package: Some("tx".to_string()),
        fields: vec![
            TableFieldSpec {
                name: "btno".to_string(),
                description: Some("Batch Number".to_string()),
                label_code: Some("txcmg011.btno".to_string()),
                domain: Some("tcmcs.long".to_string()),
                native_datatype: Some(3),
                display_length: Some(10),
                default_value: None,
                is_primary_key: Some(true),
                is_mandatory: Some(true),
                is_nullable: Some(false),
                active: Some(true),
                facets: Default::default(),
            },
        ],
        indices: vec![
            IndexSpec {
                id: "1".to_string(),
                description: Some("Primary Index".to_string()),
                label_code: Some("txcmg011.idx1".to_string()),
                primary_key: Some(true),
                unique: Some(true),
                active: Some(true),
                columns: vec![IndexColumnSpec {
                    column: "btno".to_string(),
                    sorting_order: "asc".to_string(),
                }],
            },
        ],
        references: vec![],
    };

    let rust_xml = generate_table_xml(&spec, "EXTce01107", "B61O_a_ext", None, Some("1970-01-01T00:00:00Z"));

    let payload = serde_json::json!({
        "type": "table",
        "spec": {
            "code": "txcmg011",
            "description": "Billing Batch Header",
            "version_id": "B61O_a_ext",
            "package": "tx",
            "module": "cmg",
            "fields": [
                {
                    "name": "btno",
                    "description": "Batch Number",
                    "label_code": "txcmg011.btno",
                    "domain": "tcmcs.long",
                    "native_datatype": 3,
                    "display_length": 10,
                    "is_primary_key": true,
                    "mandatory": true,
                    "position": 1
                }
            ],
            "indices": [
                {
                    "id": 1,
                    "description": "Primary Index",
                    "label_code": "txcmg011.idx1",
                    "primary_key": true,
                    "unique": true,
                    "active": true,
                    "columns": [{"column": "btno", "sorting_order": "asc"}]
                }
            ],
            "references": []
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    if let Some(diff) = find_first_diff("Table", &rust_dom, &py_dom) {
        panic!("Table diff: {diff}");
    }
    assert_eq!(rust_dom, py_dom, "Table XML DOM parity mismatch");
}

#[test]
fn test_differential_session_generator() {
    let spec = SessionSpec {
        code: "txcmg0110m100".to_string(),
        description: Some("Billing Batch Controller".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        window_type: 2,
        sub_type: 1,
        table: Some("txcmg011".to_string()),
        table_description: Some("Billing Batch Header".to_string()),
        satellites: vec![],
        form_commands: vec![],
        fields: vec![],
        script: None,
    };

    let rust_xml = generate_session_xml(&spec, "EXTce01107", "B61O_a_ext", None, Some("1970-01-01T00:00:00Z"));

    let payload = serde_json::json!({
        "type": "session",
        "spec": {
            "code": "txcmg0110m100",
            "description": "Billing Batch Controller",
            "version_id": "B61O_a_ext",
            "table": "txcmg011",
            "table_description": "Billing Batch Header",
            "window_type": 2,
            "sub_type": 1,
            "satellites": [],
            "form_commands": []
        },
        "table_spec": {
            "code": "txcmg011",
            "description": "Billing Batch Header",
            "fields": [],
            "indices": [1]
        },
        "app": "EXTce01107",
        "ver": "B61O_a_ext"
    }).to_string();

    let py_xml = call_python_generator(&payload);

    let rust_dom = parse_canonical_xml(&rust_xml);
    let py_dom = parse_canonical_xml(&py_xml);

    if let Some(diff) = find_first_diff("Session", &rust_dom, &py_dom) {
        panic!("Session diff: {diff}");
    }
    assert_eq!(rust_dom, py_dom, "Session XML DOM parity mismatch");
}
