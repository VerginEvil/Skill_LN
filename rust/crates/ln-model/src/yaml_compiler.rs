use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use thiserror::Error;

use ln_eclipse_compat::admin::AdminFile;

use crate::datatypes::NativeDatatype;
use crate::generators::*;
use crate::path_resolver::{
    split_component_name, validate_no_legacy_plural, TdePathError,
};

#[derive(Debug, Error)]
pub enum CompileError {
    #[error("Failed to parse YAML schema: {0}")]
    YamlParseError(#[from] serde_yaml::Error),
    #[error("Path error: {0}")]
    PathError(#[from] TdePathError),
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
    #[error("Admin file error: {0}")]
    AdminError(#[from] ln_eclipse_compat::admin::AdminError),
    #[error("Validation error: {0}")]
    ValidationError(String),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawEnumItem {
    pub name: Option<String>,
    pub description: Option<String>,
    pub position: Option<usize>,
    pub value: Option<usize>,
    pub label: Option<String>,
    pub label_code: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum RawEnumOrString {
    Item(RawEnumItem),
    Str(String),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawDomainSpec {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub package: Option<String>,
    #[serde(alias = "datatype", default)]
    pub r#type: Option<String>,
    #[serde(default)]
    pub length: Option<usize>,
    #[serde(default)]
    pub display_length: Option<usize>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub constants: Vec<RawEnumOrString>,
    #[serde(default)]
    pub enums: Vec<RawEnumOrString>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawFieldSpec {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub domain: Option<String>,
    #[serde(alias = "datatype", default)]
    pub r#type: Option<String>,
    #[serde(default)]
    pub native_datatype: Option<u32>,
    #[serde(default)]
    pub length: Option<usize>,
    #[serde(default)]
    pub display_length: Option<usize>,
    #[serde(default)]
    pub default_value: Option<String>,
    #[serde(default)]
    pub is_primary_key: Option<bool>,
    #[serde(alias = "mandatory", default)]
    pub is_mandatory: Option<bool>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawIndexSpec {
    pub id: serde_yaml::Value,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub primary_key: Option<bool>,
    #[serde(default)]
    pub unique: Option<bool>,
    #[serde(default)]
    pub active: Option<bool>,
    #[serde(default)]
    pub columns: Vec<serde_yaml::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawReferenceSpec {
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
    #[serde(alias = "from_fields", default)]
    pub from_columns: Vec<String>,
    #[serde(alias = "to_fields", default)]
    pub to_columns: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawTableSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub package: Option<String>,
    #[serde(default)]
    pub module: Option<String>,
    #[serde(default)]
    pub fields: Vec<RawFieldSpec>,
    #[serde(default)]
    pub indices: Vec<RawIndexSpec>,
    #[serde(default)]
    pub references: Vec<RawReferenceSpec>,
    #[serde(alias = "script", default)]
    pub dal_code: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum RawSatellite {
    Str(String),
    Obj(SatelliteSpec),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawSessionSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default)]
    pub r#type: Option<String>,
    #[serde(default)]
    pub window_type: Option<usize>,
    #[serde(default)]
    pub sub_type: Option<usize>,
    #[serde(default)]
    pub table: Option<String>,
    #[serde(default)]
    pub table_description: Option<String>,
    #[serde(default)]
    pub satellites: Vec<RawSatellite>,
    #[serde(default)]
    pub form_commands: Vec<FormCommandSpec>,
    #[serde(default)]
    pub fields: Vec<SessionFormFieldSpec>,
    #[serde(default)]
    pub script: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeclarativeSchema {
    #[serde(default = "default_version_id")]
    pub version_id: String,
    #[serde(default = "default_application")]
    pub application: String,
    #[serde(default)]
    pub domains: Vec<RawDomainSpec>,
    #[serde(default)]
    pub tables: Vec<RawTableSpec>,
    #[serde(default)]
    pub sessions: Vec<RawSessionSpec>,
    #[serde(default)]
    pub libraries: Vec<LibrarySpec>,
    #[serde(default)]
    pub menus: Vec<MenuSpec>,
    #[serde(default)]
    pub reports: Vec<ReportSpec>,
    #[serde(default)]
    pub messages: Vec<MessageSpec>,
    #[serde(default)]
    pub questions: Vec<QuestionSpec>,
    #[serde(default)]
    pub functions: Vec<FunctionSpec>,
    #[serde(default)]
    pub additionals: Vec<AdditionalFileSpec>,
    #[serde(default)]
    pub business_objects: Vec<BusinessObjectSpec>,
    #[serde(default)]
    pub labels: Vec<LabelSpec>,
}

fn default_version_id() -> String {
    "B61O_a_ext".to_string()
}

fn default_application() -> String {
    "EXTce01107".to_string()
}

#[derive(Debug, Clone)]
pub struct GeneratedFile {
    pub component_type: String,
    pub name: String,
    pub relative_path: String,
    pub absolute_path: PathBuf,
    pub content: String,
}

#[derive(Debug, Clone)]
pub struct CompileResult {
    pub generated_files: Vec<GeneratedFile>,
    pub admin_updated: bool,
    pub admin_path: Option<PathBuf>,
}

/// Parses and compiles a declarative YAML schema into Single-XML TDE workspace layout.
pub fn compile_schema_to_tde(
    schema_yaml: &str,
    output_root: &Path,
    update_admin: bool,
    created_time: Option<&str>,
) -> Result<CompileResult, CompileError> {
    let schema: DeclarativeSchema = serde_yaml::from_str(schema_yaml)?;
    let ver = &schema.version_id;
    let app = &schema.application;

    let mut generated_files = Vec::new();

    // 1. Tables & Table Labels
    for raw_t in &schema.tables {
        let tcode = raw_t.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&tcode);
        let eff_pkg = raw_t.package.clone().unwrap_or(pkg);
        let eff_mod = raw_t.module.clone().unwrap_or(if mod_code.is_empty() { "gen".to_string() } else { mod_code });
        let desc = raw_t.description.clone().unwrap_or_else(|| tcode.clone());
        let t_ver = raw_t.version_id.as_deref().unwrap_or(ver);
        let t_app = raw_t.application.as_deref().unwrap_or(app);

        let mut fields = Vec::new();
        for f in &raw_t.fields {
            let fname = f.name.to_lowercase();
            let flabel = f.label_code.clone().unwrap_or_else(|| format!("{tcode}.{fname}"));
            let fdesc = f.description.clone().unwrap_or_else(|| fname.clone());
            let dt = f.native_datatype.unwrap_or_else(|| {
                if let Some(ref d) = f.domain {
                    NativeDatatype::from_str_hint(d).as_u32()
                } else if let Some(ref t) = f.r#type {
                    NativeDatatype::from_str_hint(t).as_u32()
                } else {
                    6
                }
            });

            fields.push(TableFieldSpec {
                name: fname,
                description: Some(fdesc),
                label_code: Some(flabel),
                domain: f.domain.clone(),
                native_datatype: Some(dt),
                display_length: f.display_length.or(f.length),
                default_value: f.default_value.clone(),
                is_primary_key: f.is_primary_key,
                is_mandatory: f.is_mandatory,
                is_nullable: None,
                active: Some(true),
                facets: std::collections::HashMap::new(),
            });
        }

        let mut indices = Vec::new();
        for ind in &raw_t.indices {
            let idx_id = match &ind.id {
                serde_yaml::Value::Number(n) => n.to_string(),
                serde_yaml::Value::String(s) => s.clone(),
                other => format!("{other:?}"),
            };
            let idx_desc = ind.description.clone().unwrap_or_else(|| idx_id.clone());
            let idx_label = ind.label_code.clone().unwrap_or_else(|| format!("{tcode}.{idx_id}"));

            let mut cols = Vec::new();
            for c in &ind.columns {
                let (col_name, sort) = match c {
                    serde_yaml::Value::String(s) => (s.clone(), "asc".to_string()),
                    serde_yaml::Value::Mapping(m) => {
                        let c_name = m.get(&serde_yaml::Value::String("column".to_string()))
                            .or_else(|| m.get(&serde_yaml::Value::String("name".to_string())))
                            .and_then(|v| v.as_str())
                            .unwrap_or("")
                            .to_string();
                        let s_ord = m.get(&serde_yaml::Value::String("sorting_order".to_string()))
                            .and_then(|v| v.as_str())
                            .unwrap_or("asc")
                            .to_string();
                        (c_name, s_ord)
                    }
                    _ => (String::new(), "asc".to_string()),
                };
                if !col_name.is_empty() {
                    cols.push(IndexColumnSpec { column: col_name, sorting_order: sort });
                }
            }

            indices.push(IndexSpec {
                id: idx_id,
                description: Some(idx_desc),
                label_code: Some(idx_label),
                primary_key: ind.primary_key,
                unique: ind.unique,
                active: ind.active,
                columns: cols,
            });
        }

        let mut references = Vec::new();
        for r in &raw_t.references {
            references.push(TableReferenceSpec {
                reference_table: r.reference_table.to_lowercase(),
                name: r.name.clone(),
                delete_rule: r.delete_rule.clone(),
                update_rule: r.update_rule.clone(),
                multiplicity: r.multiplicity.clone(),
                from_columns: r.from_columns.clone(),
                to_columns: r.to_columns.clone(),
            });
        }

        let table_spec = TableSpec {
            code: tcode.clone(),
            description: Some(desc.clone()),
            version_id: Some(t_ver.to_string()),
            package: Some(eff_pkg.clone()),
            fields: fields.clone(),
            indices: indices.clone(),
            references,
        };

        let tbl_xml = generate_table_xml(&table_spec, t_app, t_ver, raw_t.dal_code.as_deref(), created_time);
        let tbl_rel = format!("{eff_pkg}/table/{eff_mod}/{tcode}.tbl");
        let tbl_abs = output_root.join(&tbl_rel);
        generated_files.push(GeneratedFile {
            component_type: "table".to_string(),
            name: tcode.clone(),
            relative_path: tbl_rel,
            absolute_path: tbl_abs,
            content: tbl_xml,
        });

        // Table Label
        let tbl_lbl_xml = generate_label_xml(&tcode, &desc, t_ver, t_app, None, created_time);
        let tbl_lbl_rel = format!("{eff_pkg}/label/{tcode}.lbl");
        let tbl_lbl_abs = output_root.join(&tbl_lbl_rel);
        generated_files.push(GeneratedFile {
            component_type: "label".to_string(),
            name: tcode.clone(),
            relative_path: tbl_lbl_rel,
            absolute_path: tbl_lbl_abs,
            content: tbl_lbl_xml,
        });

        // Field Labels
        for f in &fields {
            let lbl_code = f.label_code.as_ref().unwrap();
            let lbl_desc = f.description.as_deref().unwrap_or(lbl_code);
            let lbl_xml = generate_label_xml(lbl_code, lbl_desc, t_ver, t_app, f.display_length, created_time);
            let lbl_rel = format!("{eff_pkg}/label/{lbl_code}.lbl");
            let lbl_abs = output_root.join(&lbl_rel);
            generated_files.push(GeneratedFile {
                component_type: "label".to_string(),
                name: lbl_code.clone(),
                relative_path: lbl_rel,
                absolute_path: lbl_abs,
                content: lbl_xml,
            });
        }

        // Index Labels
        for ind in &indices {
            let lbl_code = ind.label_code.as_ref().unwrap();
            let lbl_desc = ind.description.as_deref().unwrap_or(lbl_code);
            let lbl_xml = generate_label_xml(lbl_code, lbl_desc, t_ver, t_app, None, created_time);
            let lbl_rel = format!("{eff_pkg}/label/{lbl_code}.lbl");
            let lbl_abs = output_root.join(&lbl_rel);
            generated_files.push(GeneratedFile {
                component_type: "label".to_string(),
                name: lbl_code.clone(),
                relative_path: lbl_rel,
                absolute_path: lbl_abs,
                content: lbl_xml,
            });
        }
    }

    // 2. Domains & Enum Labels
    for raw_d in &schema.domains {
        let dname = raw_d.name.to_lowercase();
        let (pkg, _, _) = split_component_name(&dname);
        let eff_pkg = raw_d.package.clone().unwrap_or(pkg);
        let desc = raw_d.description.clone().unwrap_or_else(|| dname.clone());
        let d_ver = raw_d.version_id.as_deref().unwrap_or(ver);
        let d_app = raw_d.application.as_deref().unwrap_or(app);

        let dt = if let Some(ref t) = raw_d.r#type {
            NativeDatatype::from_str_hint(t).as_u32()
        } else if !raw_d.constants.is_empty() || !raw_d.enums.is_empty() {
            7 // Enum
        } else {
            6
        };

        let raw_enum_items = if !raw_d.enums.is_empty() {
            &raw_d.enums
        } else {
            &raw_d.constants
        };

        let mut enums = Vec::new();
        for (idx, e) in raw_enum_items.iter().enumerate() {
            let pos = (idx + 1) * 10;
            match e {
                RawEnumOrString::Str(s) => {
                    enums.push(EnumItem {
                        name: s.clone(),
                        description: s.replace('.', " ").to_string(),
                        position: pos,
                        label_code: Some(format!("{dname}{pos:03}")),
                    });
                }
                RawEnumOrString::Item(item) => {
                    let e_pos = item.position.unwrap_or(pos);
                    let e_name = item.name.clone().unwrap_or_else(|| format!("val_{e_pos}"));
                    let e_desc = item.description.clone().or_else(|| item.label.clone()).unwrap_or_else(|| e_name.clone());
                    let e_lbl = item.label_code.clone().unwrap_or_else(|| format!("{dname}{e_pos:03}"));
                    enums.push(EnumItem {
                        name: e_name,
                        description: e_desc,
                        position: e_pos,
                        label_code: Some(e_lbl),
                    });
                }
            }
        }

        let domain_spec = DomainSpec {
            name: dname.clone(),
            description: desc,
            native_datatype: dt,
            display_length: raw_d.display_length.or(raw_d.length).unwrap_or(20),
            version_id: Some(d_ver.to_string()),
            application: Some(d_app.to_string()),
            enums: enums.clone(),
            facets: std::collections::HashMap::new(),
        };

        let dmn_xml = generate_domain_xml(&domain_spec, d_ver, d_app);
        let dmn_rel = format!("{eff_pkg}/domain/{dname}.dmn");
        let dmn_abs = output_root.join(&dmn_rel);
        generated_files.push(GeneratedFile {
            component_type: "domain".to_string(),
            name: dname.clone(),
            relative_path: dmn_rel,
            absolute_path: dmn_abs,
            content: dmn_xml,
        });

        // Enum Constant Labels
        for e in &enums {
            let lbl_code = e.label_code.as_ref().unwrap();
            let lbl_xml = generate_label_xml(lbl_code, &e.description, d_ver, d_app, None, created_time);
            let lbl_rel = format!("{eff_pkg}/label/{lbl_code}.lbl");
            let lbl_abs = output_root.join(&lbl_rel);
            generated_files.push(GeneratedFile {
                component_type: "label".to_string(),
                name: lbl_code.clone(),
                relative_path: lbl_rel,
                absolute_path: lbl_abs,
                content: lbl_xml,
            });
        }
    }

    // 3. Sessions & Session Labels
    for raw_s in &schema.sessions {
        let scode = raw_s.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&scode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let desc = raw_s.description.clone().unwrap_or_else(|| scode.clone());
        let s_ver = raw_s.version_id.as_deref().unwrap_or(ver);
        let s_app = raw_s.application.as_deref().unwrap_or(app);

        // Archetype mapping
        let (w_type, s_type) = if let Some(ref stype) = raw_s.r#type {
            match stype.to_lowercase().as_str() {
                "maintain_details" => (1, 1),
                "mmt_controller" => (3, 1),
                "satellite" => (1, 1),
                "display" => (1, 2),
                "process" => (1, 3),
                "print" => (1, 4),
                _ => (2, 1),
            }
        } else {
            (raw_s.window_type.unwrap_or(2), raw_s.sub_type.unwrap_or(1))
        };

        let mut satellites = Vec::new();
        for sat in &raw_s.satellites {
            match sat {
                RawSatellite::Str(s) => satellites.push(SatelliteSpec { code: s.clone(), description: None }),
                RawSatellite::Obj(obj) => satellites.push(obj.clone()),
            }
        }

        let session_spec = SessionSpec {
            code: scode.clone(),
            description: Some(desc.clone()),
            version_id: Some(s_ver.to_string()),
            application: Some(s_app.to_string()),
            window_type: w_type,
            sub_type: s_type,
            table: raw_s.table.clone(),
            table_description: raw_s.table_description.clone(),
            satellites,
            form_commands: raw_s.form_commands.clone(),
            fields: raw_s.fields.clone(),
            script: raw_s.script.clone(),
        };

        let ses_xml = generate_session_xml(&session_spec, s_app, s_ver, None, created_time);
        let ses_rel = format!("{pkg}/session/{eff_mod}/{scode}.ses");
        let ses_abs = output_root.join(&ses_rel);
        generated_files.push(GeneratedFile {
            component_type: "session".to_string(),
            name: scode.clone(),
            relative_path: ses_rel,
            absolute_path: ses_abs,
            content: ses_xml,
        });

        // Session Label
        let ses_lbl_xml = generate_label_xml(&scode, &desc, s_ver, s_app, None, created_time);
        let ses_lbl_rel = format!("{pkg}/label/{scode}.lbl");
        let ses_lbl_abs = output_root.join(&ses_lbl_rel);
        generated_files.push(GeneratedFile {
            component_type: "label".to_string(),
            name: scode.clone(),
            relative_path: ses_lbl_rel,
            absolute_path: ses_lbl_abs,
            content: ses_lbl_xml,
        });

        // Form Command Labels
        for cmd in &raw_s.form_commands {
            let cmd_lbl = cmd.label_code.clone().unwrap_or_else(|| format!("{scode}.{}", cmd.name));
            let cmd_desc = cmd.description.as_deref().unwrap_or(&cmd.name);
            let cmd_lbl_xml = generate_label_xml(&cmd_lbl, cmd_desc, s_ver, s_app, None, created_time);
            let cmd_lbl_rel = format!("{pkg}/label/{cmd_lbl}.lbl");
            let cmd_lbl_abs = output_root.join(&cmd_lbl_rel);
            generated_files.push(GeneratedFile {
                component_type: "label".to_string(),
                name: cmd_lbl,
                relative_path: cmd_lbl_rel,
                absolute_path: cmd_lbl_abs,
                content: cmd_lbl_xml,
            });
        }
    }

    // 4. Libraries
    for lib in &schema.libraries {
        let lcode = lib.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&lcode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let l_ver = lib.version_id.as_deref().unwrap_or(ver);
        let l_app = app;

        let lib_xml = generate_library_xml(lib, l_app, l_ver, created_time);
        let lib_rel = format!("{pkg}/library/{eff_mod}/{lcode}.lib");
        let lib_abs = output_root.join(&lib_rel);
        generated_files.push(GeneratedFile {
            component_type: "library".to_string(),
            name: lcode.clone(),
            relative_path: lib_rel,
            absolute_path: lib_abs,
            content: lib_xml,
        });
    }

    // 5. Menus & Menu Labels
    for mnu in &schema.menus {
        let mcode = mnu.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&mcode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let desc = mnu.description.clone().unwrap_or_else(|| mcode.clone());
        let m_ver = mnu.version_id.as_deref().unwrap_or(ver);
        let m_app = mnu.application.as_deref().unwrap_or(app);

        let mnu_xml = generate_menu_xml(mnu, m_app, m_ver, created_time);
        let mnu_rel = format!("{pkg}/menu/{eff_mod}/{mcode}.mnu");
        let mnu_abs = output_root.join(&mnu_rel);
        generated_files.push(GeneratedFile {
            component_type: "menu".to_string(),
            name: mcode.clone(),
            relative_path: mnu_rel,
            absolute_path: mnu_abs,
            content: mnu_xml,
        });

        // Menu Label
        let mnu_lbl_xml = generate_label_xml(&mcode, &desc, m_ver, m_app, None, created_time);
        let mnu_lbl_rel = format!("{pkg}/label/{mcode}.lbl");
        let mnu_lbl_abs = output_root.join(&mnu_lbl_rel);
        generated_files.push(GeneratedFile {
            component_type: "label".to_string(),
            name: mcode.clone(),
            relative_path: mnu_lbl_rel,
            absolute_path: mnu_lbl_abs,
            content: mnu_lbl_xml,
        });
    }

    // 6. Reports
    for rpt in &schema.reports {
        let rcode = rpt.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&rcode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let r_ver = rpt.version_id.as_deref().unwrap_or(ver);
        let r_app = rpt.application.as_deref().unwrap_or(app);

        let rpt_xml = generate_report_xml(rpt, r_app, r_ver, None);
        let rpt_rel = format!("{pkg}/report/{eff_mod}/{rcode}.rpt");
        let rpt_abs = output_root.join(&rpt_rel);
        generated_files.push(GeneratedFile {
            component_type: "report".to_string(),
            name: rcode.clone(),
            relative_path: rpt_rel,
            absolute_path: rpt_abs,
            content: rpt_xml,
        });
    }

    // 7. Messages
    for msg in &schema.messages {
        let mcode = msg.code.to_lowercase();
        let (pkg, _, _) = split_component_name(&mcode);
        let m_ver = msg.version_id.as_deref().unwrap_or(ver);
        let m_app = msg.application.as_deref().unwrap_or(app);

        let msg_xml = generate_message_xml(msg, m_app, m_ver);
        let msg_rel = format!("{pkg}/message/{mcode}.msg");
        let msg_abs = output_root.join(&msg_rel);
        generated_files.push(GeneratedFile {
            component_type: "message".to_string(),
            name: mcode.clone(),
            relative_path: msg_rel,
            absolute_path: msg_abs,
            content: msg_xml,
        });
    }

    // 8. Questions
    for qst in &schema.questions {
        let qcode = qst.code.to_lowercase();
        let (pkg, _, _) = split_component_name(&qcode);
        let q_ver = qst.version_id.as_deref().unwrap_or(ver);
        let q_app = qst.application.as_deref().unwrap_or(app);

        let qst_xml = generate_question_xml(qst, q_app, q_ver);
        let qst_rel = format!("{pkg}/question/{qcode}.qst");
        let qst_abs = output_root.join(&qst_rel);
        generated_files.push(GeneratedFile {
            component_type: "question".to_string(),
            name: qcode.clone(),
            relative_path: qst_rel,
            absolute_path: qst_abs,
            content: qst_xml,
        });
    }

    // 9. Functions
    for fnc in &schema.functions {
        let fcode = fnc.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&fcode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let f_ver = fnc.version_id.as_deref().unwrap_or(ver);
        let f_app = fnc.application.as_deref().unwrap_or(app);

        let fnc_xml = generate_function_xml(fnc, f_app, f_ver);
        let fnc_rel = format!("{pkg}/function/{eff_mod}/{fcode}.fnc");
        let fnc_abs = output_root.join(&fnc_rel);
        generated_files.push(GeneratedFile {
            component_type: "function".to_string(),
            name: fcode.clone(),
            relative_path: fnc_rel,
            absolute_path: fnc_abs,
            content: fnc_xml,
        });
    }

    // 10. Additionals
    for add in &schema.additionals {
        let acode = add.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&acode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let a_ver = add.version_id.as_deref().unwrap_or(ver);
        let a_app = add.application.as_deref().unwrap_or(app);

        let add_xml = generate_additional_xml(add, a_app, a_ver);
        let add_rel = format!("{pkg}/additional/{eff_mod}/{acode}.add");
        let add_abs = output_root.join(&add_rel);
        generated_files.push(GeneratedFile {
            component_type: "additional".to_string(),
            name: acode.clone(),
            relative_path: add_rel,
            absolute_path: add_abs,
            content: add_xml,
        });
    }

    // 11. Business Objects
    for bo in &schema.business_objects {
        let bcode = bo.code.to_lowercase();
        let (pkg, mod_code, _) = split_component_name(&bcode);
        let eff_mod = if mod_code.is_empty() { "gen".to_string() } else { mod_code };
        let b_ver = bo.version_id.as_deref().unwrap_or(ver);
        let b_app = bo.application.as_deref().unwrap_or(app);

        let bo_xml = generate_business_object_xml(bo, b_app, b_ver, created_time);
        let bo_rel = format!("{pkg}/businessobject/{eff_mod}/{bcode}.bus");
        let bo_abs = output_root.join(&bo_rel);
        generated_files.push(GeneratedFile {
            component_type: "businessobject".to_string(),
            name: bcode.clone(),
            relative_path: bo_rel,
            absolute_path: bo_abs,
            content: bo_xml,
        });
    }

    // 12. Custom Labels declared explicitly
    for lbl in &schema.labels {
        let lcode = lbl.name.to_lowercase();
        let (pkg, _, _) = split_component_name(&lcode);
        let l_ver = lbl.version_id.as_deref().unwrap_or(ver);
        let l_app = lbl.application.as_deref().unwrap_or(app);
        let l_desc = &lbl.description;

        let lbl_xml = generate_label_xml(&lcode, l_desc, l_ver, l_app, lbl.length, created_time);
        let lbl_rel = format!("{pkg}/label/{lcode}.lbl");
        let lbl_abs = output_root.join(&lbl_rel);
        generated_files.push(GeneratedFile {
            component_type: "label".to_string(),
            name: lcode.clone(),
            relative_path: lbl_rel,
            absolute_path: lbl_abs,
            content: lbl_xml,
        });
    }

    // Write all files to disk (ensuring directory structure & blocking legacy plural folders)
    for f in &generated_files {
        validate_no_legacy_plural(&f.absolute_path)?;
        if let Some(parent) = f.absolute_path.parent() {
            std::fs::create_dir_all(parent)?;
        }
        std::fs::write(&f.absolute_path, &f.content)?;
    }

    // Check if .admin sync should happen
    let admin_path = output_root.join(".admin");
    let should_sync = update_admin || admin_path.exists();
    let mut admin_done = false;

    if should_sync {
        let mut admin = AdminFile::load_from_path(&admin_path)?;
        for f in &generated_files {
            admin.after_create(&f.relative_path);
        }
        admin.save_to_path(&admin_path)?;
        admin_done = true;
    }

    Ok(CompileResult {
        generated_files,
        admin_updated: admin_done,
        admin_path: if admin_done { Some(admin_path) } else { None },
    })
}
