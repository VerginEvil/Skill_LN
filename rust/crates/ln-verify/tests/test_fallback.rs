use tempfile::tempdir;

use ln_verify::fallback::*;

#[test]
fn test_fallback_mode_parsing() {
    assert_eq!(FallbackMode::from_str("auto"), FallbackMode::Auto);
    assert_eq!(FallbackMode::from_str("AUTO"), FallbackMode::Auto);
    assert_eq!(FallbackMode::from_str("off"), FallbackMode::Off);
    assert_eq!(FallbackMode::from_str("OFF"), FallbackMode::Off);
    assert_eq!(FallbackMode::from_str("strict"), FallbackMode::Strict);
    assert_eq!(FallbackMode::from_str("anything_else"), FallbackMode::Strict);

    assert_eq!(FallbackMode::from_env_or_arg(Some("auto")), FallbackMode::Auto);
    assert_eq!(FallbackMode::from_env_or_arg(Some("off")), FallbackMode::Off);
}

#[test]
fn test_run_with_fallback_strict_saves_fixture() {
    let td = tempdir().unwrap();
    let crash_dir = td.path().join("unmapped");

    let res: Result<String, VerifyError> = run_with_fallback(
        FallbackMode::Strict,
        "DR_Table",
        "Compile",
        "SHOW",
        "<DR_Table><name>ttadv999</name></DR_Table>",
        &[],
        Some(&crash_dir),
        || Err("Simulated unhandled compiler panic".to_string()),
    );

    match res {
        Err(VerifyError::StrictFallbackBlocked(path)) => {
            assert!(path.exists());
            let text = std::fs::read_to_string(path).unwrap();
            assert!(text.contains("ttadv999"));
            assert!(text.contains("Simulated unhandled compiler panic"));
        }
        other => panic!("Expected StrictFallbackBlocked, got {:?}", other),
    }
}

#[test]
fn test_run_with_fallback_off_returns_error_without_fixture() {
    let td = tempdir().unwrap();
    let crash_dir = td.path().join("unmapped");

    let res: Result<String, VerifyError> = run_with_fallback(
        FallbackMode::Off,
        "DR_Table",
        "Compile",
        "SHOW",
        "<DR_Table/>",
        &[],
        Some(&crash_dir),
        || Err("Direct error".to_string()),
    );

    match res {
        Err(VerifyError::General(msg)) => assert_eq!(msg, "Direct error"),
        other => panic!("Expected General error, got {:?}", other),
    }

    assert!(!crash_dir.exists());
}

#[test]
fn test_find_python_builder_script() {
    let script = find_python_builder_script();
    assert!(script.is_some(), "ln_component_builder.py should be discoverable in workspace");
    let p = script.unwrap();
    assert!(p.exists());
    assert!(p.to_string_lossy().contains("ln_component_builder.py"));
}
