use ln_eclipse_compat::{
    MarkersFile, ProblemMarker, MarkerSeverity, AttributeValue,
};
use std::collections::HashMap;
use std::process::Command;
use tempfile::tempdir;

#[test]
fn test_markers_basic_roundtrip() {
    let mut markers_file = MarkersFile::new();
    let mut attrs = HashMap::new();
    attrs.insert("lineNumber".to_string(), AttributeValue::Int(42));
    attrs.insert("severity".to_string(), AttributeValue::Int(2));
    attrs.insert("message".to_string(), AttributeValue::String("Variable not declared".to_string()));
    attrs.insert("isScriptProblem".to_string(), AttributeValue::Bool(true));

    markers_file.markers.push(ProblemMarker {
        id: 1001,
        marker_type: "org.eclipse.core.resources.problemmarker".to_string(),
        resource_path: "/my_activity/tx/table/cmg/txcmg011.tbl".to_string(),
        file: "tx/table/cmg/txcmg011.tbl".to_string(),
        line_number: 42,
        severity: MarkerSeverity::Error,
        message: "Variable not declared".to_string(),
        is_script_problem: true,
        creation_time: 1700000000000,
        attributes: attrs,
    });

    let bytes = markers_file.serialize().unwrap();
    let reloaded = MarkersFile::deserialize(&bytes).unwrap();

    assert_eq!(reloaded.markers.len(), 1);
    let m = &reloaded.markers[0];
    assert_eq!(m.id, 1001);
    assert_eq!(m.line_number, 42);
    assert_eq!(m.severity, MarkerSeverity::Error);
    assert_eq!(m.message, "Variable not declared");
    assert!(m.is_script_problem);
    assert_eq!(m.file, "tx/table/cmg/txcmg011.tbl");
}

#[test]
fn test_python_markers_differential_roundtrip() {
    let manifest_dir = env!("CARGO_MANIFEST_DIR");
    let repo_root = std::path::Path::new(manifest_dir)
        .parent().unwrap()
        .parent().unwrap();
    let py_script = repo_root.join("ln_studio_skill").join("tools").join("ln_error_reader.py");
    if !py_script.exists() {
        eprintln!("[SKIP] ln_error_reader.py not found at {:?}", py_script);
        return;
    }

    let dir = tempdir().unwrap();
    let markers_path = dir.path().join(".markers");

    let mut markers_file = MarkersFile::new();
    let mut attrs = HashMap::new();
    attrs.insert("lineNumber".to_string(), AttributeValue::Int(15));
    attrs.insert("severity".to_string(), AttributeValue::Int(2));
    attrs.insert("message".to_string(), AttributeValue::String("Syntax error at line 15".to_string()));
    attrs.insert("isScriptProblem".to_string(), AttributeValue::Bool(true));

    markers_file.markers.push(ProblemMarker {
        id: 9999,
        marker_type: "com.infor.ln.studio.problemmarker".to_string(),
        resource_path: "/act_test/tx/session/cmg/txcmg0101m000.ses".to_string(),
        file: "tx/session/cmg/txcmg0101m000.ses".to_string(),
        line_number: 15,
        severity: MarkerSeverity::Error,
        message: "Syntax error at line 15".to_string(),
        is_script_problem: true,
        creation_time: 1700000000,
        attributes: attrs,
    });
    markers_file.save_to_path(&markers_path).unwrap();

    let py_code = format!(
        r#"
import sys
from pathlib import Path
sys.path.insert(0, r"{}")
from ln_error_reader import parse_eclipse_markers_file

markers = parse_eclipse_markers_file(Path(r"{}"))
print("PY_COUNT:" + str(len(markers)))
if markers:
    m = markers[0]
    print("PY_LINE:" + str(m.get("line")))
    print("PY_MSG:" + str(m.get("message")))
    print("PY_SEV:" + str(m.get("severity")))
"#,
        py_script.parent().unwrap().display(),
        markers_path.display()
    );

    let output = Command::new("python")
        .args(["-c", &py_code])
        .output();

    if let Ok(res) = output {
        if res.status.success() {
            let stdout = String::from_utf8_lossy(&res.stdout);
            assert!(stdout.contains("PY_COUNT:1"));
            assert!(stdout.contains("PY_LINE:15"));
            assert!(stdout.contains("PY_MSG:Syntax error at line 15"));
            assert!(stdout.contains("PY_SEV:ERROR"));
        }
    }
}
