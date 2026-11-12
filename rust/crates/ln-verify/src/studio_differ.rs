use std::collections::HashMap;
use std::fs::File;
use std::io::{Cursor, Read};
use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use zip::ZipArchive;

use crate::class_parser::{parse_class_bytes, ParsedClass};
use crate::fallback::VerifyError;

pub const BASELINE_MANIFEST_JSON: &str = include_str!("../../../schemas/build_0640_manifest.json");
pub const BASELINE_OWTEMPLATES_JSON: &str = include_str!("../../../schemas/owtemplates_0640.json");
pub const BASELINE_TDE_SCHEMA_JSON: &str = include_str!("../../../schemas/tde_schema_0640.json");

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClassDiff {
    pub class_name: String,
    pub issue: String,
    pub expected_fields: usize,
    pub actual_fields: usize,
    pub expected_uid: Option<i64>,
    pub actual_uid: Option<i64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct StudioBuildDiffReport {
    pub studio_home: String,
    pub baseline_build_id: String,
    pub target_build_id: String,
    pub total_classes_checked: usize,
    pub matched_classes: usize,
    pub diff_classes: Vec<ClassDiff>,
    pub owtemplates_checked: usize,
    pub matched_owtemplates: usize,
    pub diff_owtemplates: Vec<String>,
    pub admin_component_verified: bool,
    pub is_100_percent_match: bool,
    pub summary_markdown: String,
}

/// In-memory diff comparing parsed classes and XML templates against the Build 0640 baseline.
pub fn diff_studio_artifacts(
    classes: &[ParsedClass],
    templates: &HashMap<String, Vec<u8>>,
    studio_home_label: &str,
) -> Result<StudioBuildDiffReport, VerifyError> {
    let manifest: serde_json::Value = serde_json::from_str(BASELINE_MANIFEST_JSON)?;
    let owtemplates_val: serde_json::Value = serde_json::from_str(BASELINE_OWTEMPLATES_JSON)?;

    let baseline_build_id = manifest["build_id"].as_str().unwrap_or("10_8_0_build0640-x86_64").to_string();
    let baseline_classes = manifest["classes"].as_object();
    let baseline_templates = owtemplates_val["owtemplates"].as_object();

    let mut diff_classes = Vec::new();
    let mut matched_classes = 0;
    let mut total_classes = 0;
    let mut admin_verified = false;

    for cls in classes {
        let c_name = &cls.class_name;

        // AdministrationComponent check
        if c_name == "com.infor.ln.studio.common.core.cm.administration.AdministrationComponent" {
            total_classes += 1;
            let uid_ok = cls.serial_version_uid == Some(2);
            let instance_fields = cls.fields.iter().filter(|f| !f.is_static).count();
            let fields_ok = instance_fields == 7;
            if uid_ok && fields_ok {
                admin_verified = true;
                matched_classes += 1;
            } else {
                diff_classes.push(ClassDiff {
                    class_name: c_name.clone(),
                    issue: "AdministrationComponent serialVersionUID or field count mismatch".to_string(),
                    expected_fields: 7,
                    actual_fields: instance_fields,
                    expected_uid: Some(2),
                    actual_uid: cls.serial_version_uid,
                });
            }
            continue;
        }

        // Only inspect TDE model classes or classes indexed in baseline manifest
        let is_tde_model = c_name.starts_with("com.infor.ln.studio.common.core.model.tde")
            || c_name.starts_with("com.infor.ln.studio.apps.core.model.additional");

        let in_baseline = baseline_classes.map(|bc| bc.contains_key(c_name)).unwrap_or(false);

        if !is_tde_model && !in_baseline {
            continue; // Skip general runtime studio classes (ast.*, bseruntime.*, etc.)
        }

        total_classes += 1;
        let actual_instance_fields = cls.fields.iter().filter(|f| !f.is_static).count();

        if let Some(b_classes) = baseline_classes {
            if let Some(expected_meta) = b_classes.get(c_name) {
                let exp_sha = expected_meta["sha256"].as_str().unwrap_or("");
                let exp_fields = expected_meta["field_count"].as_u64().unwrap_or(0) as usize;
                let exp_uid = expected_meta["serial_version_uid"].as_i64();

                let sha_matched = !exp_sha.is_empty() && exp_sha == cls.sha256;
                let fields_matched = exp_fields == actual_instance_fields && exp_uid == cls.serial_version_uid;

                if sha_matched || fields_matched {
                    matched_classes += 1;
                } else {
                    diff_classes.push(ClassDiff {
                        class_name: c_name.clone(),
                        issue: format!("Instance field count difference or serialVersionUID mismatch (expected {} fields, got {})", exp_fields, actual_instance_fields),
                        expected_fields: exp_fields,
                        actual_fields: actual_instance_fields,
                        expected_uid: exp_uid,
                        actual_uid: cls.serial_version_uid,
                    });
                }
            } else {
                // New model class not in baseline
                diff_classes.push(ClassDiff {
                    class_name: c_name.clone(),
                    issue: "Model class not present in Build 0640 baseline".to_string(),
                    expected_fields: 0,
                    actual_fields: actual_instance_fields,
                    expected_uid: None,
                    actual_uid: cls.serial_version_uid,
                });
            }
        } else {
            matched_classes += 1;
        }
    }

    let mut diff_owtemplates = Vec::new();
    let mut matched_templates = 0;
    let mut total_templates = 0;

    if let Some(b_tmpl) = baseline_templates {
        for (tmpl_name, tmpl_meta) in b_tmpl {
            total_templates += 1;
            if let Some(target_bytes) = templates.get(tmpl_name) {
                let exp_hash = tmpl_meta["sha256"].as_str().unwrap_or("");
                let mut hasher = Sha256::new();
                hasher.update(target_bytes);
                let actual_hash = format!("{:x}", hasher.finalize());

                if exp_hash.is_empty() || exp_hash == actual_hash {
                    matched_templates += 1;
                } else {
                    diff_owtemplates.push(format!("{tmpl_name} (hash mismatch: expected {exp_hash}, got {actual_hash})"));
                }
            } else {
                diff_owtemplates.push(format!("{tmpl_name} (missing in target build)"));
            }
        }
    }

    let is_100_percent = diff_classes.is_empty() && diff_owtemplates.is_empty() && admin_verified;

    let mut md = String::new();
    md.push_str("# Studio Build Verification Report\n\n");
    md.push_str(&format!("- **Studio Home**: `{studio_home_label}`\n"));
    md.push_str(&format!("- **Baseline Build**: `{baseline_build_id}`\n"));
    md.push_str(&format!("- **Classes Checked**: {matched_classes} / {total_classes} matched\n"));
    md.push_str(&format!("- **OWTemplates Checked**: {matched_templates} / {total_templates} matched\n"));
    md.push_str(&format!("- **AdministrationComponent (serialVersionUID=2L, 7 fields)**: {}\n", if admin_verified { "VERIFIED" } else { "FAILED" }));

    if is_100_percent {
        md.push_str("\n### Result: 100% Match with Build 0640 Baseline (0 diffs)\n");
    } else {
        md.push_str("\n### Result: Differences Detected\n");
        if !diff_classes.is_empty() {
            md.push_str("\n#### Class Differences:\n");
            for cd in &diff_classes {
                md.push_str(&format!("- `{}`: {}\n", cd.class_name, cd.issue));
            }
        }
        if !diff_owtemplates.is_empty() {
            md.push_str("\n#### Template Differences:\n");
            for td in &diff_owtemplates {
                md.push_str(&format!("- `{td}`\n"));
            }
        }
    }

    Ok(StudioBuildDiffReport {
        studio_home: studio_home_label.to_string(),
        baseline_build_id,
        target_build_id: "Target LN Studio Installation".to_string(),
        total_classes_checked: total_classes,
        matched_classes,
        diff_classes,
        owtemplates_checked: total_templates,
        matched_owtemplates: matched_templates,
        diff_owtemplates,
        admin_component_verified: admin_verified,
        is_100_percent_match: is_100_percent,
        summary_markdown: md,
    })
}

/// Opens an Infor LN Studio installation directory and compares JAR bytecode and owtemplates.
pub fn verify_studio_build(studio_home: &Path) -> Result<StudioBuildDiffReport, VerifyError> {
    if !studio_home.exists() {
        return Err(VerifyError::General(format!("Studio home directory does not exist: {}", studio_home.display())));
    }

    let plugins_dir = studio_home.join("plugins");
    if !plugins_dir.exists() {
        return Err(VerifyError::General(format!("Plugins directory not found in {}", studio_home.display())));
    }

    let mut common_core_jar: Option<PathBuf> = None;
    let mut apps_core_jar: Option<PathBuf> = None;

    if let Ok(entries) = std::fs::read_dir(&plugins_dir) {
        for entry in entries.flatten() {
            let p = entry.path();
            let fname = p.file_name().and_then(|n| n.to_str()).unwrap_or("");
            if fname.starts_with("com.infor.ln.studio.common.core_") && fname.ends_with(".jar") {
                common_core_jar = Some(p);
            } else if fname.starts_with("com.infor.ln.studio.apps.core_") && fname.ends_with(".jar") {
                apps_core_jar = Some(p);
            }
        }
    }

    let common_jar_path = common_core_jar.ok_or_else(|| {
        VerifyError::General(format!("com.infor.ln.studio.common.core_*.jar not found in {}", plugins_dir.display()))
    })?;

    let mut parsed_classes = Vec::new();
    let mut extracted_templates: HashMap<String, Vec<u8>> = HashMap::new();

    // 1. Inspect common.core jar
    let f = File::open(&common_jar_path)?;
    let mut zip = ZipArchive::new(f)?;

    let mut nested_jars: Vec<(String, Vec<u8>)> = Vec::new();

    for i in 0..zip.len() {
        let mut entry = zip.by_index(i)?;
        let name = entry.name().to_string();

        if name.ends_with(".jar") {
            let mut jar_bytes = Vec::new();
            entry.read_to_end(&mut jar_bytes)?;
            nested_jars.push((name, jar_bytes));
        } else if name.starts_with("owtemplates/") && name.ends_with(".xml") {
            let tmpl_name = Path::new(&name).file_name().unwrap().to_string_lossy().to_string();
            let mut t_bytes = Vec::new();
            entry.read_to_end(&mut t_bytes)?;
            extracted_templates.insert(tmpl_name, t_bytes);
        } else if name.ends_with(".class") {
            let mut class_bytes = Vec::new();
            entry.read_to_end(&mut class_bytes)?;
            if let Ok(parsed) = parse_class_bytes(&class_bytes) {
                parsed_classes.push(parsed);
            }
        }
    }

    // Process nested jars (e.g. lnstudio_commoncore.jar)
    for (n_name, jar_bytes) in nested_jars {
        if n_name.contains("commoncore") || n_name.contains("core") {
            let cur = Cursor::new(jar_bytes);
            if let Ok(mut inner_zip) = ZipArchive::new(cur) {
                for i in 0..inner_zip.len() {
                    if let Ok(mut inner_entry) = inner_zip.by_index(i) {
                        let inner_name = inner_entry.name().to_string();
                        if inner_name.ends_with(".class") {
                            let mut class_bytes = Vec::new();
                            if inner_entry.read_to_end(&mut class_bytes).is_ok() {
                                if let Ok(parsed) = parse_class_bytes(&class_bytes) {
                                    parsed_classes.push(parsed);
                                }
                            }
                        } else if inner_name.starts_with("owtemplates/") && inner_name.ends_with(".xml") {
                            let tmpl_name = Path::new(&inner_name).file_name().unwrap().to_string_lossy().to_string();
                            let mut t_bytes = Vec::new();
                            if inner_entry.read_to_end(&mut t_bytes).is_ok() {
                                extracted_templates.insert(tmpl_name, t_bytes);
                            }
                        }
                    }
                }
            }
        }
    }

    // 2. Inspect apps.core jar if present
    if let Some(apps_path) = apps_core_jar {
        if let Ok(f_apps) = File::open(&apps_path) {
            if let Ok(mut zip_apps) = ZipArchive::new(f_apps) {
                for i in 0..zip_apps.len() {
                    if let Ok(mut entry) = zip_apps.by_index(i) {
                        let name = entry.name().to_string();
                        if name.starts_with("owtemplates/") && name.ends_with(".xml") {
                            let tmpl_name = Path::new(&name).file_name().unwrap().to_string_lossy().to_string();
                            let mut t_bytes = Vec::new();
                            if entry.read_to_end(&mut t_bytes).is_ok() {
                                extracted_templates.insert(tmpl_name, t_bytes);
                            }
                        } else if name.ends_with(".jar") && name.contains("fourgl") {
                            let mut inner_bytes = Vec::new();
                            if entry.read_to_end(&mut inner_bytes).is_ok() {
                                let cur = Cursor::new(inner_bytes);
                                if let Ok(mut inner_zip) = ZipArchive::new(cur) {
                                    for j in 0..inner_zip.len() {
                                        if let Ok(mut e) = inner_zip.by_index(j) {
                                            let ename = e.name().to_string();
                                            if ename.starts_with("owtemplates/") && ename.ends_with(".xml") {
                                                let tmpl_name = Path::new(&ename).file_name().unwrap().to_string_lossy().to_string();
                                                let mut t_bytes = Vec::new();
                                                if e.read_to_end(&mut t_bytes).is_ok() {
                                                    extracted_templates.insert(tmpl_name, t_bytes);
                                                }
                                            } else if ename.ends_with(".class") {
                                                let mut class_bytes = Vec::new();
                                                if e.read_to_end(&mut class_bytes).is_ok() {
                                                    if let Ok(parsed) = parse_class_bytes(&class_bytes) {
                                                        parsed_classes.push(parsed);
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // 3. Scan exploded bundle directories in plugins/ (e.g. com.infor.ln.studio.apps.ui_*/owtemplates/)
    if let Ok(entries) = std::fs::read_dir(&plugins_dir) {
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                let ow_dir = p.join("owtemplates");
                if ow_dir.exists() && ow_dir.is_dir() {
                    if let Ok(tmpl_entries) = std::fs::read_dir(&ow_dir) {
                        for te in tmpl_entries.flatten() {
                            let tp = te.path();
                            if tp.is_file() && tp.extension().and_then(|e| e.to_str()) == Some("xml") {
                                if let Ok(t_bytes) = std::fs::read(&tp) {
                                    let tmpl_name = tp.file_name().unwrap().to_string_lossy().to_string();
                                    extracted_templates.insert(tmpl_name, t_bytes);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    diff_studio_artifacts(&parsed_classes, &extracted_templates, &studio_home.to_string_lossy())
}
