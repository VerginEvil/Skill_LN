use ln_jca::filter::{
    BdeFilter, BdeSelection, ComparisonOperator, FilterExpression, LogicalOperator,
};

#[test]
fn test_selection_xml_generation() {
    let mut sel = BdeSelection::new();
    assert_eq!(sel.to_xml(), "");

    sel.add_selection("t$item");
    sel.add_selection("t$dsca");
    // Duplicate should be ignored
    sel.add_selection("t$item");

    assert_eq!(
        sel.to_xml(),
        "<Selection><selectionAttribute>t$item</selectionAttribute><selectionAttribute>t$dsca</selectionAttribute></Selection>"
    );
}

#[test]
fn test_filter_single_condition_parsing() {
    // 1. Equal with quotes
    let f1 = BdeFilter::parse("t$cprj == 'PRJ001'").expect("Valid condition");
    assert_eq!(
        f1.expression,
        Some(FilterExpression::Comparison {
            operator: ComparisonOperator::Eq,
            attribute: "t$cprj".into(),
            value: "PRJ001".into(),
        })
    );
    assert!(f1.to_xml().contains("<comparisonOperator>eq</comparisonOperator>"));
    assert!(f1.to_xml().contains("<attributeName>t$cprj</attributeName>"));
    assert!(f1.to_xml().contains("<instanceValue>PRJ001</instanceValue>"));

    // 2. Not equal with <>
    let f2 = BdeFilter::parse("status <> 9").expect("Valid condition");
    assert_eq!(
        f2.expression,
        Some(FilterExpression::Comparison {
            operator: ComparisonOperator::Ne,
            attribute: "status".into(),
            value: "9".into(),
        })
    );
    assert!(f2.to_xml().contains("<comparisonOperator>ne</comparisonOperator>"));

    // 3. Greater or equal
    let f3 = BdeFilter::parse("amount >= 100").expect("Valid condition");
    assert_eq!(
        f3.expression,
        Some(FilterExpression::Comparison {
            operator: ComparisonOperator::Ge,
            attribute: "amount".into(),
            value: "100".into(),
        })
    );

    // 4. LIKE operator
    let f4 = BdeFilter::parse("t$dsca LIKE 'BOLT*'").expect("Valid condition");
    assert_eq!(
        f4.expression,
        Some(FilterExpression::Comparison {
            operator: ComparisonOperator::Like,
            attribute: "t$dsca".into(),
            value: "BOLT*".into(),
        })
    );
    assert!(f4.to_xml().contains("<comparisonOperator>like</comparisonOperator>"));
}

#[test]
fn test_filter_compound_expression_parsing() {
    // 1. AND expression
    let f_and = BdeFilter::parse("cprj == 'P1' AND status == 'A'").expect("Valid AND expression");
    match &f_and.expression {
        Some(FilterExpression::Logical { operator, expressions }) => {
            assert_eq!(*operator, LogicalOperator::And);
            assert_eq!(expressions.len(), 2);
        }
        other => panic!("Expected Logical AND, got {:?}", other),
    }
    let xml = f_and.to_xml();
    assert!(xml.contains("<LogicalExpression><logicalOperator>and</logicalOperator>"));

    // 2. OR expression
    let f_or = BdeFilter::parse("status == 'A' OR status == 'B'").expect("Valid OR expression");
    match &f_or.expression {
        Some(FilterExpression::Logical { operator, expressions }) => {
            assert_eq!(*operator, LogicalOperator::Or);
            assert_eq!(expressions.len(), 2);
        }
        other => panic!("Expected Logical OR, got {:?}", other),
    }
    let xml_or = f_or.to_xml();
    assert!(xml_or.contains("<LogicalExpression><logicalOperator>or</logicalOperator>"));
}
