use std::path::Path;
use ln_verify::class_parser::*;

#[test]
fn test_invalid_magic_rejected() {
    let bad_bytes = [0xDE, 0xAD, 0xBE, 0xEF, 0x00, 0x00, 0x00, 0x34];
    let err = parse_class_bytes(&bad_bytes).unwrap_err();
    assert!(err.contains("0xDEADBEEF"));
    assert!(err.contains("0xCAFEBABE"));
}

#[test]
fn test_parse_real_class_from_build0640_if_available() {
    let jar_path = Path::new("d:\\LN Studio\\April-2026\\InforLNStudio_10_8_0_build0640-x86_64\\plugins\\com.infor.ln.studio.common.core_10.8.0.0640.jar");
    if !jar_path.exists() {
        return;
    }

    use std::fs::File;
    use std::io::{Cursor, Read};
    use zip::ZipArchive;

    let f = File::open(jar_path).unwrap();
    let mut zip = ZipArchive::new(f).unwrap();

    let mut inner_jar_bytes = Vec::new();
    let mut inner_entry = zip.by_name("lnstudio_commoncore.jar").unwrap();
    inner_entry.read_to_end(&mut inner_jar_bytes).unwrap();

    let mut inner_zip = ZipArchive::new(Cursor::new(inner_jar_bytes)).unwrap();
    let mut class_entry = inner_zip.by_name("com/infor/ln/studio/common/core/cm/administration/AdministrationComponent.class").unwrap();
    let mut class_bytes = Vec::new();
    class_entry.read_to_end(&mut class_bytes).unwrap();

    let parsed = parse_class_bytes(&class_bytes).unwrap();
    assert_eq!(parsed.class_name, "com.infor.ln.studio.common.core.cm.administration.AdministrationComponent");
    assert_eq!(parsed.serial_version_uid, Some(2));
    let field_names: Vec<&str> = parsed.fields.iter().map(|f| f.name.as_str()).collect();
    assert!(field_names.contains(&"serialVersionUID"));
    assert!(field_names.contains(&"m_path"));
    assert!(field_names.contains(&"isCheckedout"));
    assert!(field_names.contains(&"isCreated"));
    assert!(field_names.contains(&"isEvercheckedIn"));
    assert!(field_names.contains(&"m_isDirty"));
    assert!(field_names.contains(&"m_isVSCHappy"));
    assert!(field_names.contains(&"isExpired"));
    assert_eq!(parsed.field_count, 8); // 1 serialVersionUID + 7 instance fields
}
