use std::fs;
use tempfile::tempdir;

use ln_model::inspector::inspect_unknown_nodes_with_log_path;

#[test]
fn test_inspect_clean_xml_produces_no_unmapped() {
    let clean_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>txcmg011</name>
  <package>tx</package>
  <module>cmg</module>
  <descriptionReference>txcmg011.desc</descriptionReference>
  <Column>
    <name>orno</name>
    <datatype>
      <nativeDatatype>3</nativeDatatype>
    </datatype>
  </Column>
  <Index>
    <name>1</name>
    <IndexColumn>
      <column>orno</column>
    </IndexColumn>
  </Index>
</DR_Table>"#;

    let unmapped = inspect_unknown_nodes_with_log_path(clean_xml, "txcmg011", None)
        .expect("Inspector should succeed");
    assert!(unmapped.is_empty(), "Clean XML should have 0 unmapped packets, got: {:?}", unmapped);
}

#[test]
fn test_inspect_unknown_tags_and_attributes_and_logs() {
    let xml_with_unknown = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>txcmg011</name>
  <CustomVendorWrapper customAttr="value123">
    <ProprietaryFeatureFlag enabled="true"/>
  </CustomVendorWrapper>
  <Column>
    <name>orno</name>
    <nativeDatatype>3</nativeDatatype>
    <UnmappedColumnFlag>TRUE</UnmappedColumnFlag>
  </Column>
  <Index>
    <name>1</name>
    <IndexColumn>
      <name>orno</name>
    </IndexColumn>
  </Index>
</DR_Table>"#;

    let tmp = tempdir().unwrap();
    let log_path = tmp.path().join("unmapped_packets.log");

    let unmapped = inspect_unknown_nodes_with_log_path(xml_with_unknown, "txcmg011", Some(&log_path))
        .expect("Inspector should succeed");

    assert!(!unmapped.is_empty(), "Should detect unmapped tags");

    let unknown_tags: Vec<String> = unmapped.iter().map(|u| u.unknown_tag.clone()).collect();
    assert!(unknown_tags.contains(&"CustomVendorWrapper".to_string()));
    assert!(unknown_tags.contains(&"@customAttr".to_string()));
    assert!(unknown_tags.contains(&"ProprietaryFeatureFlag".to_string()));
    assert!(unknown_tags.contains(&"UnmappedColumnFlag".to_string()));

    // Verify log file was written in JSONL format
    assert!(log_path.is_file(), "Log file should exist on disk");
    let log_content = fs::read_to_string(&log_path).unwrap();
    let lines: Vec<&str> = log_content.lines().collect();
    assert_eq!(lines.len(), unmapped.len());

    let first_line: serde_json::Value = serde_json::from_str(lines[0]).unwrap();
    assert_eq!(first_line["component"], "txcmg011");
    assert!(!first_line["timestamp"].as_str().unwrap().is_empty());
}
