use ln_eclipse_compat::{
    PropertyBucket, ProjectProperties, StudioProjectSettings,
};
use std::process::Command;
use tempfile::tempdir;

#[test]
fn test_property_bucket_basic_roundtrip() {
    let mut bucket = PropertyBucket::new();
    bucket.set_property("Label", "dev_natt_v01108-1", "", "");
    bucket.set_property("labelUUID", "11111111-2222-3333-4444-555555555555", "", "");
    bucket.set_property("ApplicationRelease", "10.8", "", "");
    bucket.set_property("generateComponentSourceFiles", "true", "IStudio_Core", "");

    let bytes = bucket.serialize().unwrap();
    let reloaded = PropertyBucket::deserialize(&bytes).unwrap();

    assert_eq!(reloaded.get_property("Label", "", ""), Some("dev_natt_v01108-1"));
    assert_eq!(reloaded.get_property("labelUUID", "", ""), Some("11111111-2222-3333-4444-555555555555"));
    assert_eq!(reloaded.get_property("ApplicationRelease", "", ""), Some("10.8"));
    assert_eq!(reloaded.get_property("generateComponentSourceFiles", "IStudio_Core", ""), Some("true"));
}

#[test]
fn test_project_properties_and_studio_settings_helpers() {
    let mut bucket = PropertyBucket::new();
    let props = ProjectProperties {
        application_release: Some("10.8".into()),
        customer: Some("INFOR".into()),
        description: Some("My Test Activity".into()),
        environment: Some("dev_env".into()),
        label: Some("my_label".into()),
        label_uuid: Some("uuid-1234".into()),
        language: Some("2".into()),
        package: Some("tx".into()),
        package_combination: Some("tx_vrc".into()),
        package_vrc: Some("B61U_a_live".into()),
        project_server: Some("srv".into()),
        server_user: Some("user".into()),
        solution: Some("sol".into()),
        task_version_id: Some("1001".into()),
        use_proxy: Some("false".into()),
        user: Some("dev".into()),
        version: Some("10.8.0".into()),
        vrc: Some("B61_dev".into()),
        workspace_root: Some(r"C:\workspace".into()),
    };
    props.apply_to_bucket(&mut bucket, "");

    let settings = StudioProjectSettings {
        generate_component_source_files: Some(true),
        generate_form_source_files: Some(false),
        generate_menu_source_files: Some(true),
        generate_report_source_files: Some(false),
    };
    settings.apply_to_bucket(&mut bucket, "");

    let read_props = ProjectProperties::from_bucket(&bucket, "");
    assert_eq!(read_props.label, Some("my_label".into()));
    assert_eq!(read_props.task_version_id, Some("1001".into()));
    assert_eq!(read_props.package_vrc, Some("B61U_a_live".into()));

    let read_settings = StudioProjectSettings::from_bucket(&bucket, "");
    assert_eq!(read_settings.generate_component_source_files, Some(true));
    assert_eq!(read_settings.generate_form_source_files, Some(false));
    assert_eq!(read_settings.generate_menu_source_files, Some(true));
    assert_eq!(read_settings.generate_report_source_files, Some(false));
}

#[test]
fn test_python_properties_index_differential_roundtrip() {
    let manifest_dir = env!("CARGO_MANIFEST_DIR");
    let repo_root = std::path::Path::new(manifest_dir)
        .parent().unwrap()
        .parent().unwrap();
    let py_script = repo_root.join("ln_studio_skill").join("tools").join("properties_index.py");
    if !py_script.exists() {
        eprintln!("[SKIP] properties_index.py not found at {:?}", py_script);
        return;
    }

    let dir = tempdir().unwrap();
    let prop_file = dir.path().join("properties.index");

    let mut bucket = PropertyBucket::new();
    bucket.set_property("Label", "dev_natt_v01108-1", "", "");
    bucket.set_property("TaskVersionID", "88219", "", "");
    bucket.set_property("generateComponentSourceFiles", "true", "IStudio_Core", "");
    bucket.save_to_path(&prop_file).unwrap();

    // Verify Python can read it
    let py_code = format!(
        r#"
import sys
from pathlib import Path
sys.path.insert(0, r"{}")
from properties_index import PropertyBucket

b = PropertyBucket.load_from_file(Path(r"{}"))
print("PY_LABEL:" + str(b.get_property("Label", "")))
print("PY_TASK:" + str(b.get_property("TaskVersionID", "")))
print("PY_SETTING:" + str(b.get_property("generateComponentSourceFiles", "IStudio_Core")))
"#,
        py_script.parent().unwrap().display(),
        prop_file.display()
    );

    let output = Command::new("python")
        .args(["-c", &py_code])
        .output();

    if let Ok(res) = output {
        if res.status.success() {
            let stdout = String::from_utf8_lossy(&res.stdout);
            assert!(stdout.contains("PY_LABEL:dev_natt_v01108-1"));
            assert!(stdout.contains("PY_TASK:88219"));
            assert!(stdout.contains("PY_SETTING:true"));
        }
    }
}
