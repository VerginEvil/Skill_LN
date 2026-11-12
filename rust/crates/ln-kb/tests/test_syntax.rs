use ln_kb::{
    choice_sections, dal_field_hook_suffixes, dal_object_hooks, keywords, other_keywords,
    predefined_variables, program_sections, report_sections, sql_keywords, standard_defines,
    sub_sections, templates,
};

#[test]
fn test_syntax_completion_categories() {
    assert_eq!(keywords().len(), 80);
    assert!(keywords().contains(&"while"));
    assert!(keywords().contains(&"case"));

    assert_eq!(sql_keywords().len(), 92);
    assert!(sql_keywords().contains(&"where"));
    assert!(sql_keywords().contains(&"select"));

    assert_eq!(program_sections().len(), 9);
    assert!(program_sections().contains(&"declaration:"));
    assert!(program_sections().contains(&"before.program:"));

    assert_eq!(sub_sections().len(), 43);
    assert_eq!(choice_sections().len(), 60);
    assert_eq!(report_sections().len(), 9);
    assert_eq!(predefined_variables().len(), 176);
    assert_eq!(standard_defines().len(), 49);
    assert_eq!(other_keywords().len(), 10);

    assert_eq!(dal_object_hooks().len(), 15);
    assert!(dal_object_hooks().contains(&"before.open.object.set"));

    assert_eq!(dal_field_hook_suffixes().len(), 10);
    assert!(dal_field_hook_suffixes().iter().any(|h| h.suffix == ".is.never.applicable"));

    assert_eq!(templates().len(), 12);
    assert!(templates().iter().any(|t| t.id == "%template.fourglcode.case"));
}
