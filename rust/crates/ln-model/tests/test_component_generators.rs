use ln_model::*;

#[test]
fn test_generate_table_xml() {
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
                is_nullable: None,
                active: Some(true),
                facets: Default::default(),
            },
            TableFieldSpec {
                name: "lino".to_string(),
                description: Some("Line Number".to_string()),
                label_code: Some("txcmg011.lino".to_string()),
                domain: Some("tcmcs.long".to_string()),
                native_datatype: Some(3),
                display_length: Some(5),
                default_value: None,
                is_primary_key: Some(false),
                is_mandatory: None, // Line number rule should set this to false
                is_nullable: None,
                active: Some(true),
                facets: Default::default(),
            },
        ],
        indices: vec![IndexSpec {
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
        }],
        references: vec![TableReferenceSpec {
            reference_table: "tccom001".to_string(),
            name: Some("ref_tccom001".to_string()),
            delete_rule: Some("restrict".to_string()),
            update_rule: Some("restrict".to_string()),
            multiplicity: Some("one_to_many".to_string()),
            from_columns: vec!["btno".to_string()],
            to_columns: vec!["emno".to_string()],
        }],
    };

    let xml = generate_table_xml(
        &spec,
        "EXTce01107",
        "B61O_a_ext",
        Some("function extern long before.save.object() { return(0); }"),
        Some("2026-01-01T00:00:00Z"),
    );

    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Table>"#));
    assert!(xml.contains("<name>txcmg011</name>"));
    assert!(xml.contains("<type>table</type>"));
    assert!(xml.contains("<versionID>B61O_a_ext</versionID>"));
    assert!(xml.contains("<descriptionReference>txcmg011</descriptionReference>"));
    assert!(xml.contains("<isPrimaryKey>true</isPrimaryKey>"));
    assert!(xml.contains("<isMandatory>false</isMandatory>")); // lino check
    assert!(xml.contains("<toTable>tccom001</toTable>"));
    assert!(xml.contains("<expression>function extern long before.save.object() { return(0); }</expression>"));
    assert!(xml.ends_with("<application>EXTce01107</application></DR_Table>"));
}

#[test]
fn test_generate_session_xml() {
    let spec = SessionSpec {
        code: "txcmg0110m100".to_string(),
        description: Some("Billing Batch Controller".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        window_type: 3, // MMT
        sub_type: 1,
        table: Some("txcmg011".to_string()),
        table_description: Some("Billing Batch Header".to_string()),
        satellites: vec![SatelliteSpec {
            code: "txcmg0510m000".to_string(),
            description: Some("Satellite Lines".to_string()),
        }],
        form_commands: vec![FormCommandSpec {
            name: "exec.user.0".to_string(),
            function: Some("generate.billing".to_string()),
            label_code: Some("txcmg0110m100.cmd1".to_string()),
            description: Some("Generate Billing".to_string()),
            position: Some("1".to_string()),
            sequence: Some("10".to_string()),
        }],
        fields: vec![SessionFormFieldSpec {
            name: "btno".to_string(),
            description: Some("Batch Number".to_string()),
            label_code: Some("txcmg011.btno".to_string()),
            mandatory: Some(true),
            native_datatype: Some(3),
            length: Some(10),
            zoom_program: None,
            zoom_return_field: None,
        }],
        script: Some("declaration: table ttxcmg011".to_string()),
    };

    let xml = generate_session_xml(
        &spec,
        "EXTce01107",
        "B61O_a_ext",
        None,
        Some("2026-01-01T00:00:00Z"),
    );

    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Controller>"#));
    assert!(xml.contains("<name>txcmg0110m100</name>"));
    assert!(xml.contains("<windowType>3</windowType>"));
    assert!(xml.contains("<toTable>txcmg011</toTable>"));
    assert!(xml.contains("<toSession>txcmg0510m000</toSession>"));
    assert!(xml.contains("<FormCommand><name>exec.user.0</name>"));
    assert!(xml.contains("<activationName>generate.billing</activationName>"));
    assert!(xml.contains("<fieldName>txcmg011.btno</fieldName>"));
    assert!(xml.contains("<StandardCommand>"));
    assert!(xml.contains("<UIMethod><status>allowed</status>"));
    assert!(xml.contains("<expression>declaration: table ttxcmg011</expression>"));
    assert!(xml.ends_with("</DR_Controller>"));
}

#[test]
fn test_generate_domain_xml() {
    let spec = DomainSpec {
        name: "txcmg.stat".to_string(),
        description: "Batch Status".to_string(),
        native_datatype: 7, // Enum
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
                name: "closed".to_string(),
                description: "Closed".to_string(),
                position: 20,
                label_code: Some("txcmg.stat020".to_string()),
            },
        ],
        facets: Default::default(),
    };

    let xml = generate_domain_xml(&spec, "B61O_a_ext", "EXTce01107");
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Domain>"#));
    assert!(xml.contains("<name>txcmg.stat</name>"));
    assert!(xml.contains("<nativeDatatype>7</nativeDatatype>"));
    assert!(xml.contains("<Enumeration><descriptionReference>txcmg.stat010</descriptionReference><description>Open</description><name>open</name><position>10</position></Enumeration>"));
    assert!(xml.ends_with("</DR_Domain>"));
}

#[test]
fn test_generate_label_xml() {
    let xml = generate_label_xml(
        "txcmg011.btno",
        "Batch Number",
        "B61O_a_ext",
        "EXTce01107",
        Some(12),
        Some("2026-01-01T00:00:00Z"),
    );

    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Label>"#));
    assert!(xml.contains("<name>txcmg011.btno</name>"));
    assert!(xml.contains("<keyword>BATCH NUMBER</keyword>"));
    assert!(xml.contains("<length>12</length>"));
    assert!(xml.ends_with("</DR_Label>"));
}

#[test]
fn test_generate_library_xml() {
    let spec = LibrarySpec {
        code: "txibddllitem01".to_string(),
        description: Some("Item General DLL".to_string()),
        library_type: "dll".to_string(),
        target: None,
        version_id: Some("B61O_a_ext".to_string()),
        script: Some("function extern long get_item() { return(0); }".to_string()),
    };

    let xml = generate_library_xml(&spec, "EXTce01107", "B61O_a_ext", Some("2026-01-01T00:00:00Z"));
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Module>"#));
    assert!(xml.contains("<name>txibddllitem01</name>"));
    assert!(xml.contains("<type>library</type>"));
    assert!(xml.contains("<sourceType>6</sourceType>"));
    assert!(xml.contains("<expression>function extern long get_item() { return(0); }</expression>"));
    assert!(xml.ends_with("</DR_Module>"));
}

#[test]
fn test_generate_menu_xml() {
    let spec = MenuSpec {
        code: "txgld0000m001".to_string(),
        description: Some("Enhancements Menu".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        choices: vec![MenuChoiceSpec {
            position: 10,
            choice_type: "session".to_string(),
            target: "txcmg0110m100".to_string(),
            description: Some("Billing Batch".to_string()),
        }],
    };

    let xml = generate_menu_xml(&spec, "EXTce01107", "B61O_a_ext", Some("2026-01-01T00:00:00Z"));
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Menu>"#));
    assert!(xml.contains("<name>txgld0000m001</name>"));
    assert!(xml.contains("<menuFieldName>txcmg0110m100</menuFieldName>"));
    assert!(xml.contains("<menuFieldType>1</menuFieldType>"));
    assert!(xml.contains("<position>10</position>"));
    assert!(xml.ends_with("</DR_Menu>"));
}

#[test]
fn test_generate_report_xml() {
    let spec = ReportSpec {
        code: "txcmg04010100".to_string(),
        description: Some("Billing Batch Summary Report".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        paper_width: 80,
        input_fields: vec![ReportInputFieldSpec {
            fieldname: "btno".to_string(),
            domain: Some("tcmcs.long".to_string()),
            native_datatype: Some(3),
            is_table_field: Some(false),
            sort_sequence: 1,
            sort_mode: 1,
            label: Some("tcgen.btno".to_string()),
        }],
        layouts: vec![ReportLayoutSpec {
            layout_type: 4,
            rows: 2,
            columns: 80,
            output_expression: "1".to_string(),
            output_fields: vec![ReportOutputFieldSpec {
                print_expression: "btno".to_string(),
                domain: Some("tcmcs.long".to_string()),
                row: 1,
                col: 1,
                len: 10,
            }],
            specials: vec![],
        }],
        script: Some("detail.1: before.layout:".to_string()),
    };

    let xml = generate_report_xml(&spec, "EXTce01107", "B61O_a_ext", None);
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(xml.contains("<DR_Report"));
    assert!(xml.contains("<name>txcmg04010100</name>"));
    assert!(xml.contains("<printExpression>btno</printExpression>"));
    assert!(xml.contains("<expression><![CDATA[detail.1: before.layout:]]></expression>"));
    assert!(xml.ends_with("</DR_Report>\n"));
}

#[test]
fn test_generate_message_xml() {
    let spec = MessageSpec {
        code: "txcmg0001".to_string(),
        description: Some("Validation error for batch".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        severity: "3".to_string(),
        text: Some("Batch cannot be processed without approval.".to_string()),
        language: 2,
    };

    let xml = generate_message_xml(&spec, "EXTce01107", "B61O_a_ext");
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(xml.contains("<DR_Message"));
    assert!(xml.contains("<name>txcmg0001</name>"));
    assert!(xml.contains("<severity>3</severity>"));
    assert!(xml.contains("<text>Batch cannot be processed without approval.</text>"));
    assert!(xml.ends_with("</DR_Message>\n"));
}

#[test]
fn test_generate_question_xml() {
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

    let xml = generate_question_xml(&spec, "EXTce01107", "B61O_a_ext");
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(xml.contains("<DR_Question"));
    assert!(xml.contains("<name>txcmg0002</name>"));
    assert!(xml.contains("<domain>tcyesno</domain>"));
    assert!(xml.contains("<defaultAnswer>yes</defaultAnswer>"));
    assert!(xml.ends_with("</DR_Question>\n"));
}

#[test]
fn test_generate_function_xml() {
    let spec = FunctionSpec {
        code: "txcmgf001".to_string(),
        description: Some("Calculation function".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        script: Some("function extern long calc() { return(42); }".to_string()),
    };

    let xml = generate_function_xml(&spec, "EXTce01107", "B61O_a_ext");
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(xml.contains("<type>function</type>"));
    assert!(xml.contains("<name>txcmgf001</name>"));
    assert!(xml.contains("<expression><![CDATA[function extern long calc() { return(42); }]]></expression>"));
    assert!(xml.ends_with("</DR_Module>\n"));
}

#[test]
fn test_generate_additional_xml() {
    let spec = AdditionalFileSpec {
        code: "txcmgcfg".to_string(),
        description: Some("Configuration file".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        content: Some("{\"mode\": \"auto\"}".to_string()),
        keyword1: Some("billing".to_string()),
        keyword2: Some("config".to_string()),
        keyword3: None,
    };

    let xml = generate_additional_xml(&spec, "EXTce01107", "B61O_a_ext");
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(xml.contains("<DR_AdditionalFile"));
    assert!(xml.contains("<name>txcmgcfg</name>"));
    assert!(xml.contains("<keyword1>billing</keyword1>"));
    assert!(xml.contains("<content><![CDATA[{\"mode\": \"auto\"}]]></content>"));
    assert!(xml.ends_with("</DR_AdditionalFile>\n"));
}

#[test]
fn test_generate_business_object_xml() {
    let spec = BusinessObjectSpec {
        code: "txcmgbus01".to_string(),
        description: Some("Billing Business Object".to_string()),
        version_id: Some("B61O_a_ext".to_string()),
        application: Some("EXTce01107".to_string()),
        type_of_business_object: "document".to_string(),
        schema_version: "1.0".to_string(),
    };

    let xml = generate_business_object_xml(&spec, "EXTce01107", "B61O_a_ext", Some("2026-01-01T00:00:00Z"));
    assert!(xml.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_BusinessObject>"#));
    assert!(xml.contains("<name>txcmgbus01</name>"));
    assert!(xml.contains("<type>businessobject</type>"));
    assert!(xml.contains("<typeOfBusinessObject>document</typeOfBusinessObject>"));
    assert!(xml.contains("<lowerCaseBusinessObjectName>txcmgbus01</lowerCaseBusinessObjectName>"));
    assert!(xml.ends_with("</DR_BusinessObject>"));
}
