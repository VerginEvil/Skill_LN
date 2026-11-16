use ln_model::{
    get_owtemplate, get_script_template, get_tde_schema, get_templates_catalog,
    lookup_class, lookup_root_component,
};

#[test]
fn test_embedded_schema_loads_cleanly() {
    let schema = get_tde_schema();
    assert_eq!(schema.version, "10.8.0.0640");
    assert!(!schema.classes.is_empty());
    assert!(schema.classes.len() >= 129);
}

#[test]
fn test_all_12_component_root_types_exist() {
    let root_types = [
        ("DR_Table", ".tbl", "table"),
        ("DR_Controller", ".ses", "session"),
        ("DR_Domain", ".dmn", "domain"),
        ("DR_Label", ".lbl", "label"),
        ("DR_Menu", ".mnu", "menu"),
        ("DR_Message", ".msg", "message"),
        ("DR_Question", ".qst", "question"),
        ("DR_Report", ".rpt", "report"),
        ("DR_AdditionalFile", ".add", "additional"),
        ("DR_BusinessObject", ".bus", "business_object"),
        ("DR_Module", ".lib", "library"),
        ("Procedure", ".fnc", "function"),
        ("DR_Solution", ".sol", "solution"),
    ];

    for (class_name, expected_ext, expected_type) in root_types {
        let cls = lookup_class(class_name);
        assert!(cls.is_some(), "Root class {class_name} not found in schema");
        let meta = cls.unwrap();
        assert!(meta.is_root_component, "{class_name} should be marked as root component");
        assert_eq!(meta.file_extension.as_deref(), Some(expected_ext), "Extension mismatch for {class_name}");

        let (ext, ctype) = lookup_root_component(class_name)
            .unwrap_or_else(|| panic!("lookup_root_component failed for {class_name}"));
        assert_eq!(ext, expected_ext);
        assert_eq!(ctype, expected_type);

        let (ext_by_type, _) = lookup_root_component(expected_type)
            .unwrap_or_else(|| panic!("lookup_root_component failed for type {expected_type}"));
        assert_eq!(ext_by_type, expected_ext);
    }
}

#[test]
fn test_dr_table_field_hierarchy_and_inheritance() {
    let table_cls = lookup_class("DR_Table").expect("DR_Table must exist");
    assert!(table_cls.has_field("application"));
    assert!(table_cls.has_field("Column"));
    assert!(table_cls.has_field("TableRelationship"));
    assert!(table_cls.has_field("Index"));
    assert!(table_cls.has_field("Source"));

    // Inherited from TDEProperties & TDEPropertiesLabeledComponent
    assert!(table_cls.has_field("name"), "Should inherit 'name' from TDEProperties");
    assert!(table_cls.has_field("description"), "Should inherit 'description' from TDEProperties");
    assert!(table_cls.has_field("versionID"), "Should inherit 'versionID' from TDEProperties");
    assert!(table_cls.has_field("Version"), "Should inherit 'Version' from TDEProperties");
    assert!(table_cls.has_field("descriptionReference"), "Should inherit 'descriptionReference' from TDEPropertiesLabeledComponent");

    // Check Column field kind
    let col_field = table_cls.get_field("Column").expect("Column field must exist");
    assert_eq!(col_field.kind, "list");
    assert_eq!(col_field.target_type.as_deref(), Some("Column"));

    // Check Column class schema
    let col_cls = lookup_class("Column").expect("Column class must exist");
    assert!(col_cls.has_field("name"));
    assert!(col_cls.has_field("datatype"));
    assert!(col_cls.has_field("isPrimaryKey"));
    assert!(col_cls.has_field("isMandatory"));
}

#[test]
fn test_dr_controller_field_hierarchy() {
    let ses_cls = lookup_class("DR_Controller").expect("DR_Controller must exist");
    assert!(ses_cls.has_field("name"));
    assert!(ses_cls.has_field("windowType"));
    assert!(ses_cls.has_field("Form"));
    assert!(ses_cls.has_field("StandardCommand"));
}

#[test]
fn test_dr_domain_field_hierarchy() {
    let dmn_cls = lookup_class("DR_Domain").expect("DR_Domain must exist");
    assert!(dmn_cls.has_field("name"));
    assert!(dmn_cls.has_field("datatype"));
    assert!(dmn_cls.has_field("displayLength"));
    assert!(dmn_cls.has_field("Enumeration"));
}

#[test]
fn test_owtemplates_catalog() {
    let catalog = get_templates_catalog();
    assert!(!catalog.owtemplates.is_empty());
    assert!(catalog.owtemplates.len() >= 39, "Should have at least 39 owtemplates, got {}", catalog.owtemplates.len());

    // Test specific templates from common.core and apps.ui
    let change_proj = get_owtemplate("ChangeSoftwareProject.xml").expect("ChangeSoftwareProject.xml must exist");
    assert_eq!(change_proj.source, "common.core");
    assert!(change_proj.content.contains("<SoftwareProject"));

    let create_app = get_owtemplate("CreateApplication.xml").expect("CreateApplication.xml must exist");
    assert_eq!(create_app.source, "apps.ui");
    assert!(create_app.content.contains("<Application>"));

    // Test ScriptTemplates
    assert_eq!(catalog.script_templates.len(), 9);
    let dal2_tpl = get_script_template("DalTwo").expect("DalTwo ScriptTemplate must exist");
    assert!(dal2_tpl.content.contains("Script Type: DAL"));
}
