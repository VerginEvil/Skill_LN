use std::collections::HashMap;
use std::path::Path;
use std::time::Instant;

use ln_verify::class_parser::ParsedClass;
use ln_verify::studio_differ::*;

#[test]
fn test_live_verify_studio_build_0640_if_present() {
    let studio_home = Path::new("d:\\LN Studio\\April-2026\\InforLNStudio_10_8_0_build0640-x86_64");
    if !studio_home.exists() {
        eprintln!("Studio home not found at {}, skipping live differ test", studio_home.display());
        return;
    }

    let start = Instant::now();
    let report = verify_studio_build(studio_home).unwrap();
    let elapsed = start.elapsed();

    println!("Verification finished in {:?}", elapsed);
    println!("{}", report.summary_markdown);

    // Speed invariant: must complete in < 1 second!
    assert!(elapsed.as_millis() < 1000, "Verification took {:?}, expected < 1 second", elapsed);

    // Baseline match
    assert!(report.admin_component_verified, "AdministrationComponent must be verified");
    assert!(report.matched_classes >= 129, "Expected at least 129 matched model classes, got {}", report.matched_classes);
    assert_eq!(report.diff_classes.len(), 0, "Expected 0 class differences against Build 0640 baseline");
    assert!(report.matched_owtemplates >= 34, "Expected at least 34 matched owtemplates, got {}", report.matched_owtemplates);
    assert!(report.is_100_percent_match, "Expected 100% match with Build 0640 baseline");
}

#[test]
fn test_synthetic_differ_mutation_flags() {
    // 1. Baseline matching classes
    let classes = vec![
        ParsedClass {
            class_name: "com.infor.ln.studio.common.core.cm.administration.AdministrationComponent".to_string(),
            super_class_name: None,
            serial_version_uid: Some(2),
            sha256: String::new(),
            field_count: 8,
            fields: (0..7).map(|i| ln_verify::class_parser::FieldInfo {
                name: format!("f{i}"),
                descriptor: "Ljava/lang/String;".to_string(),
                is_public: true,
                is_protected: false,
                is_static: false,
                is_final: false,
            }).collect(),
        },
        ParsedClass {
            class_name: "com.infor.ln.studio.common.core.model.tde.AnyTypeTDENode".to_string(),
            super_class_name: None,
            serial_version_uid: None,
            sha256: String::new(),
            field_count: 1,
            fields: vec![ln_verify::class_parser::FieldInfo {
                name: "field1".to_string(),
                descriptor: "Ljava/lang/String;".to_string(),
                is_public: true,
                is_protected: false,
                is_static: false,
                is_final: false,
            }],
        },
    ];

    let mut templates = HashMap::new();
    templates.insert("ApplicationHasModifiedComponents.xml".to_string(), b"<Application><name>%name</name><ApplicationPackage><applicationPackageName>%applicationPackageName</applicationPackageName></ApplicationPackage></Application>".to_vec());

    // Clean diff
    let clean_res = diff_studio_artifacts(&classes, &templates, "test_home").unwrap();
    assert!(clean_res.admin_component_verified);

    // 2. Mutate AdministrationComponent serialVersionUID -> flags diff
    let bad_admin_classes = vec![
        ParsedClass {
            class_name: "com.infor.ln.studio.common.core.cm.administration.AdministrationComponent".to_string(),
            super_class_name: None,
            serial_version_uid: Some(999), // Corrupted/mutated serialVersionUID
            sha256: String::new(),
            field_count: 8,
            fields: (0..7).map(|i| ln_verify::class_parser::FieldInfo {
                name: format!("f{i}"),
                descriptor: "Ljava/lang/String;".to_string(),
                is_public: true,
                is_protected: false,
                is_static: false,
                is_final: false,
            }).collect(),
        },
    ];
    let bad_res = diff_studio_artifacts(&bad_admin_classes, &templates, "test_home").unwrap();
    assert!(!bad_res.is_100_percent_match);
    assert!(!bad_res.admin_component_verified);
    assert_eq!(bad_res.diff_classes.len(), 1);
    assert!(bad_res.diff_classes[0].issue.contains("AdministrationComponent"));

    // 3. Mutate template hash -> flags diff
    let mut bad_templates = HashMap::new();
    bad_templates.insert("ApplicationHasModifiedComponents.xml".to_string(), b"<CorruptedContent/>".to_vec());
    let bad_tmpl_res = diff_studio_artifacts(&classes, &bad_templates, "test_home").unwrap();
    assert!(!bad_tmpl_res.is_100_percent_match);
    assert!(bad_tmpl_res.diff_owtemplates.iter().any(|d| d.contains("hash mismatch")));
}

#[test]
fn test_invalid_studio_home_path_error() {
    let err = verify_studio_build(Path::new("c:\\non_existent_ln_studio_path_12345")).unwrap_err();
    assert!(err.to_string().contains("does not exist"));
}
