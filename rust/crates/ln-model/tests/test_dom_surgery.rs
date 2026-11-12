use std::fs;
use tempfile::tempdir;

use ln_model::dom_surgery::{
    clone_component_xml, extract_script, inject_script, pre_put_merge_and_guard,
    PrePutGuardError,
};

#[test]
fn test_extract_script_cdata_and_entities() {
    let xml_cdata = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr">
  <name>txcmg011</name>
  <DR_Module>
    <Source>
      <expression><![CDATA[
function extern long test_func()
{
    return(0)
}
]]></expression>
    </Source>
  </DR_Module>
</DR_Table>"#;

    let extracted = extract_script(xml_cdata).expect("Should extract CDATA script");
    assert!(extracted.contains("function extern long test_func()"));
    assert!(extracted.contains("return(0)"));

    let xml_entities = r#"<DR_Module><Source><expression>if a &lt; b and c &gt; d then return(0) endif</expression></Source></DR_Module>"#;
    let extracted_ent = extract_script(xml_entities).expect("Should extract entity script");
    assert_eq!(extracted_ent, "if a < b and c > d then return(0) endif");
}

#[test]
fn test_lossless_dom_surgery_preserves_unknown_vendor_tags() {
    let original_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <!-- Proprietary Vendor Metadata Header -->
  <VendorExt:Metadata xmlns:VendorExt="http://custom.vendor.com/ext" priority="HIGH">
    <VendorBuildTimestamp>2026-04-01T12:00:00Z</VendorBuildTimestamp>
    <ProprietaryFlags secureMode="true" legacyCompatible="yes"/>
  </VendorExt:Metadata>
  <name>txcmg011</name>
  <package>tx</package>
  <module>cmg</module>
  <DR_Module>
    <Source>
      <expression><![CDATA[
// old script
]]></expression>
    </Source>
  </DR_Module>
  <!-- Trailing Vendor Node -->
  <VendorExt:Signature algo="SHA256">DEADBEEFCAFE0123</VendorExt:Signature>
</DR_Table>"#;

    let new_script = "function extern test_new() { return(42) }";
    let spliced_xml = inject_script(original_xml, new_script).expect("Should inject script");

    // Verify the new script is embedded
    assert!(spliced_xml.contains("function extern test_new() { return(42) }"));

    // Verify 100% of vendor comments, tags, namespaces, and signatures are preserved byte-for-byte!
    assert!(spliced_xml.contains("<!-- Proprietary Vendor Metadata Header -->"));
    assert!(spliced_xml.contains(r#"<VendorExt:Metadata xmlns:VendorExt="http://custom.vendor.com/ext" priority="HIGH">"#));
    assert!(spliced_xml.contains("<VendorBuildTimestamp>2026-04-01T12:00:00Z</VendorBuildTimestamp>"));
    assert!(spliced_xml.contains(r#"<ProprietaryFlags secureMode="true" legacyCompatible="yes"/>"#));
    assert!(spliced_xml.contains("<!-- Trailing Vendor Node -->"));
    assert!(spliced_xml.contains(r#"<VendorExt:Signature algo="SHA256">DEADBEEFCAFE0123</VendorExt:Signature>"#));

    // Verify extract roundtrip
    let extracted = extract_script(&spliced_xml).expect("Should extract injected script");
    assert_eq!(extracted, new_script);
}

#[test]
fn test_clone_component_xml_lossless() {
    let src_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Controller xmlns="http://www.infor.com/businessline/application/dr" version="1.0" name="txcmg0100m000" package="tx" module="cmg">
  <VendorPayload vendorCode="999">
    <CustomTag>Value</CustomTag>
  </VendorPayload>
  <name>txcmg0100m000</name>
  <package>tx</package>
  <module>cmg</module>
  <descriptionReference>txcmg0100m000.title</descriptionReference>
  <Form>
    <FormField>
      <fieldLabel>txcmg0100m000.field1</fieldLabel>
    </FormField>
  </Form>
</DR_Controller>"#;

    let cloned = clone_component_xml(
        src_xml,
        "txcmg0100m000",
        "txcmg0200m000",
        "tx",
        "tx",
        Some("cmg"),
        Some("cmg"),
    );

    assert!(cloned.contains(r#"name="txcmg0200m000""#));
    assert!(cloned.contains("<name>txcmg0200m000</name>"));
    assert!(cloned.contains("<descriptionReference>txcmg0200m000.title</descriptionReference>"));
    assert!(cloned.contains("<fieldLabel>txcmg0200m000.field1</fieldLabel>"));

    // Verify vendor payload preserved untouched
    assert!(cloned.contains(r#"<VendorPayload vendorCode="999">"#));
    assert!(cloned.contains("<CustomTag>Value</CustomTag>"));
}

#[test]
fn test_pre_put_merge_and_guardrail() {
    let tmp = tempdir().unwrap();
    let act_dir = tmp.path();

    let tbl_path = act_dir.join("txcmg011.tbl");
    let initial_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr">
  <name>txcmg011</name>
  <DR_Module>
    <Source>
      <expression><![CDATA[
function extern long old_code() { return(0) }
]]></expression>
    </Source>
  </DR_Module>
</DR_Table>"#;
    fs::write(&tbl_path, initial_xml).unwrap();

    // 1. Create a standalone .dal file with updated code
    let dal_path = act_dir.join("txcmg011.dal");
    let updated_dal = "function extern long updated_dal_code() { return(100) }";
    fs::write(&dal_path, updated_dal).unwrap();

    let merged = pre_put_merge_and_guard(&tbl_path, "txcmg011", "table", act_dir).unwrap();
    assert!(merged.contains("updated_dal_code()"));
    let disk_content = fs::read_to_string(&tbl_path).unwrap();
    assert!(disk_content.contains("updated_dal_code()"));

    // 2. Non-Empty Source Guardrail: wipe standalone script and try to put session
    let ses_path = act_dir.join("txcmg0100m000.ses");
    let empty_ses_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Controller xmlns="http://www.infor.com/businessline/application/dr">
  <name>txcmg0100m000</name>
  <DR_Module>
    <Source>
      <expression></expression>
    </Source>
  </DR_Module>
</DR_Controller>"#;
    fs::write(&ses_path, empty_ses_xml).unwrap();

    let err = pre_put_merge_and_guard(&ses_path, "txcmg0100m000", "session", act_dir).unwrap_err();
    match err {
        PrePutGuardError::EmptyScriptOverwrite { comp_name, comp_type } => {
            assert_eq!(comp_name, "txcmg0100m000");
            assert_eq!(comp_type, "session");
        }
        _ => panic!("Expected EmptyScriptOverwrite error, got {:?}", err),
    }
}
