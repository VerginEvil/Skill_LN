use serde::{Deserialize, Serialize};

use crate::datatypes::NativeDatatype;

pub const DEFAULT_80COL_GRID_BASE64: &str =
    "AQgBjDoBEwGMWwEZAYwsAR4BjF0BSwGMOgJLAYs6/yAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg\
    ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg\
    ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg\
    ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA=";

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReportInputFieldSpec {
    pub fieldname: String,
    #[serde(default)]
    pub domain: Option<String>,
    #[serde(default)]
    pub native_datatype: Option<u32>,
    #[serde(default)]
    pub is_table_field: Option<bool>,
    #[serde(default = "default_sort_seq")]
    pub sort_sequence: usize,
    #[serde(default = "default_sort_mode")]
    pub sort_mode: usize, // 1 = asc, 2 = desc, 4 = none
    #[serde(default)]
    pub label: Option<String>,
}

fn default_sort_seq() -> usize {
    99
}

fn default_sort_mode() -> usize {
    1
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReportOutputFieldSpec {
    pub print_expression: String,
    #[serde(default)]
    pub domain: Option<String>,
    #[serde(default = "default_one")]
    pub row: usize,
    #[serde(default = "default_one")]
    pub col: usize,
    #[serde(default = "default_output_len")]
    pub len: usize,
}

fn default_one() -> usize {
    1
}

fn default_output_len() -> usize {
    30
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReportSpecialSpec {
    #[serde(default = "default_special_type")]
    pub special_type: usize, // 8 = label, 3 = date, 6 = page
    pub label: String,
    #[serde(default = "default_one")]
    pub row: usize,
    #[serde(default = "default_one")]
    pub col: usize,
    #[serde(default = "default_special_len")]
    pub len: usize,
}

fn default_special_type() -> usize {
    8
}

fn default_special_len() -> usize {
    10
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReportLayoutSpec {
    #[serde(default = "default_layout_type")]
    pub layout_type: usize, // 2 = page_header, 4 = detail, 6 = footer
    #[serde(default = "default_two")]
    pub rows: usize,
    #[serde(default = "default_cols")]
    pub columns: usize,
    #[serde(default = "default_expr_one")]
    pub output_expression: String,
    #[serde(default)]
    pub output_fields: Vec<ReportOutputFieldSpec>,
    #[serde(default)]
    pub specials: Vec<ReportSpecialSpec>,
}

fn default_layout_type() -> usize {
    4
}

fn default_two() -> usize {
    2
}

fn default_cols() -> usize {
    80
}

fn default_expr_one() -> String {
    "1".to_string()
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReportSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default = "default_cols")]
    pub paper_width: usize,
    #[serde(default)]
    pub input_fields: Vec<ReportInputFieldSpec>,
    #[serde(default)]
    pub layouts: Vec<ReportLayoutSpec>,
    #[serde(default)]
    pub script: Option<String>,
}

/// Generates standard `<DR_Report>` XML matching Infor LN Studio 10.8.
pub fn generate_report_xml(
    spec: &ReportSpec,
    application: &str,
    default_version_id: &str,
    script_override: Option<&str>,
) -> String {
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;
    let paper_width = spec.paper_width;

    let mut lines = Vec::new();
    lines.push(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#.to_string());
    lines.push(r#"<DR_Report xmlns="http://www.infor.com/businessline/application/dr" version="1.0">"#.to_string());
    lines.push(format!("  <description>{desc}</description>"));
    lines.push(format!("  <versionID>{ver}</versionID>"));
    lines.push("  <type>report</type>".to_string());
    lines.push(format!("  <name>{code}</name>"));
    lines.push("  <Version>".to_string());
    lines.push("    <ObjectID/><classID/><checkInLabel/><documentation/>".to_string());
    lines.push("    <isExpired>no</isExpired>".to_string());
    lines.push("    <isCheckedOutParallel>no</isCheckedOutParallel>".to_string());
    lines.push("    <isCheckedOut>no</isCheckedOut>".to_string());
    lines.push("  </Version>".to_string());
    lines.push(format!("  <descriptionReference>{code}</descriptionReference>"));
    lines.push("  <SSRSDesignPresent>false</SSRSDesignPresent>".to_string());

    // Input Fields
    let default_fields;
    let input_fields: &[ReportInputFieldSpec] = if spec.input_fields.is_empty() {
        default_fields = vec![ReportInputFieldSpec {
            fieldname: "dummy".to_string(),
            domain: Some("tcmcs.long".to_string()),
            native_datatype: Some(3),
            is_table_field: Some(false),
            sort_sequence: 99,
            sort_mode: 1,
            label: None,
        }];
        &default_fields
    } else {
        &spec.input_fields
    };

    for f in input_fields {
        let fname = &f.fieldname;
        let dom = f.domain.as_deref().unwrap_or("tcdsca");
        let dt = f.native_datatype.unwrap_or_else(|| NativeDatatype::from_str_hint(dom).as_u32());
        let is_tbl = if f.is_table_field.unwrap_or(false) { "yes" } else { "no" };
        let s_seq = f.sort_sequence;
        let s_mode = f.sort_mode;
        let lbl = f.label.as_deref().unwrap_or("");

        lines.push("  <InputField>".to_string());
        lines.push(format!("    <label>{lbl}</label>"));
        lines.push(format!("    <nativeDatatype>{dt}</nativeDatatype>"));
        lines.push(format!("    <isTableField>{is_tbl}</isTableField>"));
        lines.push(format!("    <sortSequence>{s_seq}</sortSequence>"));
        lines.push(format!("    <sortMode>{s_mode}</sortMode>"));
        lines.push(format!("    <domain>{dom}</domain>"));
        lines.push("    <depth>0</depth>".to_string());
        lines.push(format!("    <fieldname>{fname}</fieldname>"));
        lines.push("  </InputField>".to_string());
    }

    // Layouts
    let default_layouts;
    let layouts: &[ReportLayoutSpec] = if spec.layouts.is_empty() {
        let dummy_name = &input_fields[0].fieldname;
        let dummy_dom = input_fields[0].domain.as_deref().unwrap_or("tcdsca");
        default_layouts = vec![
            ReportLayoutSpec {
                layout_type: 2, // header
                rows: 2,
                columns: paper_width,
                output_expression: "1".to_string(),
                output_fields: Vec::new(),
                specials: vec![
                    ReportSpecialSpec { special_type: 8, label: "tcgen.h.date".to_string(), row: 1, col: 1, len: 10 },
                    ReportSpecialSpec { special_type: 8, label: "tcgen.page".to_string(), row: 1, col: 65, len: 10 },
                ],
            },
            ReportLayoutSpec {
                layout_type: 4, // detail
                rows: 2,
                columns: paper_width,
                output_expression: "1".to_string(),
                output_fields: vec![
                    ReportOutputFieldSpec { print_expression: dummy_name.clone(), domain: Some(dummy_dom.to_string()), row: 1, col: 1, len: 30 }
                ],
                specials: Vec::new(),
            },
        ];
        &default_layouts
    } else {
        &spec.layouts
    };

    for (seq, lay) in layouts.iter().enumerate() {
        let seq_num = seq + 1;
        lines.push("  <Layout>".to_string());
        lines.push("    <PhysicalReportLayout>".to_string());
        lines.push("      <ReportLayoutText>".to_string());
        lines.push(format!("        <content>{DEFAULT_80COL_GRID_BASE64}</content>"));
        lines.push("        <position>1</position>".to_string());
        lines.push("      </ReportLayoutText>".to_string());

        // Output fields
        for (of_pos, of) in lay.output_fields.iter().enumerate() {
            let expr = &of.print_expression;
            let dom = of.domain.as_deref().unwrap_or("tcdsca");
            let row = of.row;
            let col = of.col;
            let plen = of.len;
            let pos = of_pos + 1;

            lines.push("      <ReportOutputField>".to_string());
            lines.push("        <barCode>0</barCode><font>0</font><maximumTextLines>0</maximumTextLines><minimumTextLines>0</minimumTextLines>".to_string());
            lines.push("        <underlined>false</underlined><reverse>false</reverse><bold>false</bold><color>8</color>".to_string());
            lines.push("        <aggregateFunction>0</aggregateFunction><aggregateExpression/><printCondition>1</printCondition>".to_string());
            lines.push("        <suppressIdenticalValues>false</suppressIdenticalValues><alignment>0</alignment>".to_string());
            lines.push(format!("        <printLength>{plen}</printLength><linkWithDomain>true</linkWithDomain>"));
            lines.push(format!("        <domain>{dom}</domain><printExpression>{expr}</printExpression>"));
            lines.push(format!("        <rowPosition>{row}</rowPosition><columnPosition>{col}</columnPosition>"));
            lines.push(format!("        <position>{pos}</position>"));
            lines.push("      </ReportOutputField>".to_string());
        }

        // Specials
        for (sp_pos, sp) in lay.specials.iter().enumerate() {
            let sp_type = sp.special_type;
            let lbl = &sp.label;
            let row = sp.row;
            let col = sp.col;
            let slen = sp.len;
            let pos = sp_pos + 1;

            lines.push("      <ReportSpecial>".to_string());
            lines.push("        <fillPrintEffect>false</fillPrintEffect><alignment>0</alignment><domainAdjustment>false</domainAdjustment><height>1</height>".to_string());
            lines.push(format!("        <label>{lbl}</label>"));
            lines.push("        <underlined>false</underlined><reverse>false</reverse><bold>true</bold><color>8</color>".to_string());
            lines.push(format!("        <length>{slen}</length><rowPosition>{row}</rowPosition><columnPosition>{col}</columnPosition>"));
            lines.push(format!("        <specialType>{sp_type}</specialType><position>{pos}</position>"));
            lines.push("      </ReportSpecial>".to_string());
        }

        lines.push("    </PhysicalReportLayout>".to_string());
        lines.push("    <positioningColumns>1</positioningColumns>".to_string());
        lines.push("    <extraNeed>0</extraNeed><newPage>false</newPage><lineFont>2</lineFont>".to_string());
        lines.push(format!("    <rows>{}</rows><columns>{}</columns>", lay.rows, lay.columns));
        lines.push(format!("    <outputExpression>{}</outputExpression>", lay.output_expression));
        lines.push(format!("    <sequence>{seq_num}</sequence>"));
        lines.push("    <inputField/>".to_string());
        lines.push(format!("    <layoutType>{}</layoutType>", lay.layout_type));
        lines.push("  </Layout>".to_string());
    }

    // Page Setup
    lines.push("  <PageSetup>".to_string());
    lines.push("    <repeatExpression>1</repeatExpression><nrColumns>0</nrColumns>".to_string());
    lines.push("    <Font><fixedFont>false</fixedFont><defaultFont>1</defaultFont></Font>".to_string());
    lines.push(format!("    <Paper><height>-1</height><width>{paper_width}</width></Paper>"));
    lines.push("    <Margins><footMargin>-1</footMargin><leftMargin>5</leftMargin><bottomMargin>2</bottomMargin><topMargin>2</topMargin></Margins>".to_string());
    lines.push("  </PageSetup>".to_string());

    // Script
    let script = script_override.or(spec.script.as_deref());
    if let Some(s) = script {
        if !s.is_empty() {
            lines.push("  <Source>".to_string());
            lines.push(format!("    <expression><![CDATA[{s}]]></expression>"));
            lines.push("    <sourceType>6</sourceType>".to_string());
            lines.push(format!("    <sourceName>{code}</sourceName>"));
            lines.push("  </Source>".to_string());
        }
    }

    lines.push(format!("  <application>{app}</application>"));
    lines.push("</DR_Report>".to_string());

    lines.join("\n") + "\n"
}
