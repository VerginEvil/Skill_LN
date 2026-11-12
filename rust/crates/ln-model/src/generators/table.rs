use std::collections::HashMap;
use serde::{Deserialize, Serialize};

use crate::datatypes::{is_line_number_column, NativeDatatype};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TableFieldSpec {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub domain: Option<String>,
    #[serde(default)]
    pub native_datatype: Option<u32>,
    #[serde(default)]
    pub display_length: Option<usize>,
    #[serde(default)]
    pub default_value: Option<String>,
    #[serde(default)]
    pub is_primary_key: Option<bool>,
    #[serde(default)]
    pub is_mandatory: Option<bool>,
    #[serde(default)]
    pub is_nullable: Option<bool>,
    #[serde(default = "default_true")]
    pub active: Option<bool>,
    #[serde(default)]
    pub facets: HashMap<String, String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IndexColumnSpec {
    pub column: String,
    #[serde(default = "default_sort")]
    pub sorting_order: String, // "asc" or "desc"
}

fn default_sort() -> String {
    "asc".to_string()
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct IndexSpec {
    pub id: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub primary_key: Option<bool>,
    #[serde(default)]
    pub unique: Option<bool>,
    #[serde(default = "default_true")]
    pub active: Option<bool>,
    pub columns: Vec<IndexColumnSpec>,
}

fn default_true() -> Option<bool> {
    Some(true)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TableReferenceSpec {
    #[serde(alias = "to_table")]
    pub reference_table: String,
    #[serde(default)]
    pub name: Option<String>,
    #[serde(default)]
    pub delete_rule: Option<String>,
    #[serde(default)]
    pub update_rule: Option<String>,
    #[serde(default)]
    pub multiplicity: Option<String>,
    #[serde(default)]
    pub from_columns: Vec<String>,
    #[serde(default)]
    pub to_columns: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TableSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub package: Option<String>,
    #[serde(default)]
    pub fields: Vec<TableFieldSpec>,
    #[serde(default)]
    pub indices: Vec<IndexSpec>,
    #[serde(default)]
    pub references: Vec<TableReferenceSpec>,
}

/// Generates standard Infor LN Studio 10.8 `<DR_Table>` XML.
pub fn generate_table_xml(
    spec: &TableSpec,
    application: &str,
    default_version_id: &str,
    dal_code: Option<&str>,
    created_time: Option<&str>,
) -> String {
    let now_iso = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let name = &spec.code;

    let mut parts = Vec::new();
    parts.push(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#.to_string());
    parts.push("<DR_Table>".to_string());
    parts.push(format!("<description>{desc}</description>"));
    parts.push(format!("<versionID>{ver}</versionID>"));
    parts.push("<type>table</type>".to_string());
    parts.push(format!("<name>{name}</name>"));
    parts.push(format!(
        "<Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></Version>"
    ));
    parts.push(format!("<descriptionReference>{name}</descriptionReference>"));

    // Attachments
    parts.push(format!("<Attachment><type>relnotes</type><name>{name}</name></Attachment>"));
    parts.push(format!("<Attachment><type>techdoc</type><name>{name}</name></Attachment>"));
    for f in &spec.fields {
        let fname = &f.name;
        parts.push(format!("<Attachment><type>relnotes</type><name>{name}.{fname}</name></Attachment>"));
        parts.push(format!("<Attachment><type>techdoc</type><name>{name}.{fname}</name></Attachment>"));
    }

    // Indices
    for ind in &spec.indices {
        let idx_id = &ind.id;
        let idx_desc = ind.description.as_deref().unwrap_or(idx_id);
        let idx_label = ind.label_code.as_deref().unwrap_or(idx_id);
        let is_pk = if ind.primary_key.unwrap_or(false) { "true" } else { "false" };
        let is_unq = if ind.unique.unwrap_or(false) { "true" } else { "false" };
        let is_act = if ind.active.unwrap_or(true) { "true" } else { "false" };

        let mut idx_cols = String::new();
        for (c_pos, col) in ind.columns.iter().enumerate() {
            idx_cols.push_str(&format!(
                "<IndexColumn><sortingOrder>{}</sortingOrder><column>{}</column><position>{}</position></IndexColumn>",
                col.sorting_order, col.column, c_pos + 1
            ));
        }

        parts.push(format!(
            "<Index><descriptionReference>{idx_label}</descriptionReference><description>{idx_desc}</description>{idx_cols}<isActive>{is_act}</isActive><isPrimaryKey>{is_pk}</isPrimaryKey><isUnique>{is_unq}</isUnique><name>{idx_id}</name></Index>"
        ));
    }

    // Table Relationships
    for r in &spec.references {
        let to_tbl = &r.reference_table;
        let default_rel = format!("ref_{to_tbl}");
        let rel_name = r.name.as_deref().unwrap_or(&default_rel);
        let del_rule = r.delete_rule.as_deref().unwrap_or("not_delete_restricted");
        let upd_rule = r.update_rule.as_deref().unwrap_or("restrict");
        let mult = r.multiplicity.as_deref().unwrap_or("one_to_many");

        let mut col_rels = String::new();
        for (from_c, to_c) in r.from_columns.iter().zip(r.to_columns.iter()) {
            col_rels.push_str(&format!(
                "<TableRelationshipColumn><to>{to_c}</to><from>{from_c}</from></TableRelationshipColumn>"
            ));
        }

        parts.push(format!(
            "<TableRelationship><companyField/><toTable>{to_tbl}</toTable>{col_rels}<deleteRule>{del_rule}</deleteRule><updateRule>{upd_rule}</updateRule><referentialIntegrityCheck>true</referentialIntegrityCheck><multiplicity>{mult}</multiplicity><type>association</type><name>{rel_name}</name></TableRelationship>"
        ));
    }

    // Columns
    for (pos, f) in spec.fields.iter().enumerate() {
        let fname = &f.name;
        let fdesc = f.description.as_deref().unwrap_or(fname);
        let default_flabel = format!("{name}.{fname}");
        let flabel = f.label_code.as_deref().unwrap_or(&default_flabel);
        let c_null = if f.is_nullable.unwrap_or(false) { "true" } else { "false" };
        let c_act = if f.active.unwrap_or(true) { "true" } else { "false" };

        // Enforce Line Number Non-Mandatory Rule (TBL003 / ADR 0017)
        let is_mand = if let Some(m) = f.is_mandatory {
            if m { "true" } else { "false" }
        } else if is_line_number_column(fname) {
            "false"
        } else {
            "false"
        };

        let def_val_tag = if let Some(ref d) = f.default_value {
            format!("<defaultValue>{d}</defaultValue>")
        } else {
            String::new()
        };

        let c_domain = f.domain.as_deref().unwrap_or("tcdsca");
        let dt_code = f.native_datatype.unwrap_or_else(|| {
            NativeDatatype::from_str_hint(c_domain).as_u32()
        });

        let mut facets_xml = String::new();
        for (ftype, fval) in &f.facets {
            facets_xml.push_str(&format!("<Facet><value>{fval}</value><type>{ftype}</type></Facet>"));
        }

        parts.push(format!(
            "<Column><descriptionReference>{flabel}</descriptionReference><description>{fdesc}</description><additionalInstructions>columnDepth:0</additionalInstructions><isNullable>{c_null}</isNullable><isActive>{c_act}</isActive><isMandatory>{is_mand}</isMandatory>{def_val_tag}<position>{}</position><datatype>{facets_xml}<nativeDatatype>{dt_code}</nativeDatatype><name>{c_domain}</name></datatype><type>simple</type><name>{fname}</name></Column>",
            pos + 1
        ));
    }

    // Documentation
    parts.push("<documentation/>".to_string());

    // Embedded DAL script
    let dal_script = if let Some(dal) = dal_code {
        dal.to_string()
    } else {
        format!(
            "|*******************************************************************************\n\
            |* {name}  {ver}\n\
            |* {desc}\n\
            |* Script Type: DAL\n\
            |*******************************************************************************\n\n\
            #include <bic_dal2>\n\n\
            table t{name}\n\n\
            function extern boolean method.is.allowed(long i.method)\n\
            {{\n\
            \ton case i.method\n\
            \tcase DAL_NEW:\n\
            \t\tbreak\n\
            \tcase DAL_UPDATE:\n\
            \t\tbreak\n\
            \tcase DAL_DESTROY:\n\
            \t\tbreak\n\
            \tendcase\n\
            \treturn(true)\n\
            }}\n"
        )
    };

    let escaped_dal = dal_script
        .replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;");

    parts.push(format!(
        "<DR_Module><description>{desc}</description><versionID>{ver}</versionID><type>library</type><name>{name}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></Version><Source><sourceVersion><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></sourceVersion><sourceVersionID>{ver}</sourceVersionID><sourceObjectID>1</sourceObjectID><expression>{escaped_dal}</expression><expressionLanguageType>Baan4C</expressionLanguageType><sourceType>2</sourceType><sourceDescription>{desc}</sourceDescription><sourceName>{name}</sourceName></Source><documentation/><Attachment><type>techdoc</type><name>{name}</name></Attachment><application>{application}</application></DR_Module>"
    ));

    parts.push(format!("<application>{application}</application>"));
    parts.push("</DR_Table>".to_string());

    parts.join("")
}
