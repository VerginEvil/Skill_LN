use ln_jca::security::{assert_not_prohibited_operation, PROHIBITED_BDE_METHODS, PROHIBITED_XML_TAGS};

#[test]
fn test_prohibited_bde_methods_blocked() {
    for method in PROHIBITED_BDE_METHODS {
        let res = assert_not_prohibited_operation("ActivityManager", method, "");
        assert!(res.is_err(), "Method '{}' must be prohibited", method);

        let res_upper = assert_not_prohibited_operation("ActivityManager", &method.to_uppercase(), "");
        assert!(res_upper.is_err(), "Method uppercase '{}' must be prohibited", method);

        let res_bde = assert_not_prohibited_operation(method, "execute", "");
        assert!(res_bde.is_err(), "BDE containing '{}' must be prohibited", method);
    }
}

#[test]
fn test_prohibited_xml_tags_blocked() {
    for tag in PROHIBITED_XML_TAGS {
        let payload = format!("<Request><ControlArea/>{}</Request>", tag);
        let res = assert_not_prohibited_operation("GenericBde", "executeMethod", &payload);
        assert!(res.is_err(), "XML tag '{}' must be prohibited", tag);

        let payload_upper = format!("<Request><ControlArea/>{}</Request>", tag.to_uppercase());
        let res_upper = assert_not_prohibited_operation("GenericBde", "executeMethod", &payload_upper);
        assert!(res_upper.is_err(), "XML uppercase tag '{}' must be prohibited", tag);
    }
}

#[test]
fn test_permitted_operations_pass() {
    let allowed_methods = [
        "GetModifiedComponents",
        "CmGet",
        "CmPut",
        "CmCheckIn",
        "CmCheckOut",
        "CmUnCheckOut",
        "Compile",
        "CRDD",
        "CreateTables",
        "prepare-end-activity",
    ];

    for method in allowed_methods {
        let res = assert_not_prohibited_operation("CMLabel", method, "<Request><DataArea/></Request>");
        assert!(res.is_ok(), "Method '{}' should be permitted", method);
    }
}
