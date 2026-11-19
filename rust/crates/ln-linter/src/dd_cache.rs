use regex::Regex;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};

pub const BSHELL_PSEUDO_FIELDS: &[&str] = &[
    "_compnr", "record_len", "_index1", "_index2", "_index3", "_index4",
    "_index5", "_index6", "_index7", "_index8", "_index9", "_index10",
    "_index11", "_index12",
];

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct FieldMeta {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub domain: Option<String>,
    #[serde(default)]
    pub datatype: Option<serde_json::Value>,
    #[serde(rename = "isMandatory", alias = "mandatory", default)]
    pub is_mandatory: Option<bool>,
    #[serde(rename = "maxLength", alias = "length", default)]
    pub max_length: Option<serde_json::Value>,
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct TableMeta {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub fields: HashMap<String, FieldMeta>,
    #[serde(default)]
    pub indices: Vec<serde_json::Value>,
    #[serde(skip)]
    pub index_columns: HashMap<String, Vec<String>>,
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct DomainMeta {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub datatype: Option<serde_json::Value>,
    #[serde(default)]
    pub length: Option<usize>,
    #[serde(default)]
    pub constants: Option<HashMap<String, serde_json::Value>>,
}

#[derive(Debug, Clone, Default)]
pub struct DataDictionaryCache {
    pub cache_path: Option<PathBuf>,
    pub tables: HashMap<String, TableMeta>,
    pub domains: HashMap<String, DomainMeta>,
}

impl DataDictionaryCache {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn from_path(path: impl AsRef<Path>) -> Self {
        let p = path.as_ref().to_path_buf();
        let mut cache = Self {
            cache_path: Some(p.clone()),
            tables: HashMap::new(),
            domains: HashMap::new(),
        };
        if p.exists() {
            if let Ok(content) = fs::read_to_string(&p) {
                if let Ok(val) = serde_json::from_str::<serde_json::Value>(&content) {
                    cache.ingest_json(&val);
                }
            }
        }
        cache
    }

    pub fn from_json_value(val: &serde_json::Value) -> Self {
        let mut cache = Self::default();
        cache.ingest_json(val);
        cache
    }

    pub fn has_data(&self) -> bool {
        !self.tables.is_empty() || !self.domains.is_empty()
    }

    pub fn ingest_json(&mut self, data: &serde_json::Value) {
        if let Some(raw_tables) = data.get("tables").and_then(|t| t.as_object()) {
            for (tbl_name, tbl_info) in raw_tables {
                let t_key = tbl_name.trim().to_lowercase();
                let mut fields_map = HashMap::new();
                let mut desc = None;

                if let Some(list) = tbl_info.as_array() {
                    for f in list {
                        if let Some(fname) = f.as_str() {
                            let fn_lower = fname.trim().to_lowercase();
                            fields_map.insert(
                                fn_lower.clone(),
                                FieldMeta {
                                    name: fn_lower,
                                    ..Default::default()
                                },
                            );
                        }
                    }
                } else if let Some(obj) = tbl_info.as_object() {
                    desc = obj.get("description").and_then(|d| d.as_str()).map(ToString::to_string);
                    let raw_fields = obj.get("fields").or_else(|| obj.get("columns"));

                    if let Some(f_arr) = raw_fields.and_then(|f| f.as_array()) {
                        for item in f_arr {
                            if let Ok(fmeta) = serde_json::from_value::<FieldMeta>(item.clone()) {
                                fields_map.insert(fmeta.name.to_lowercase(), fmeta);
                            } else if let Some(fname) = item.as_str() {
                                let fn_lower = fname.trim().to_lowercase();
                                fields_map.insert(
                                    fn_lower.clone(),
                                    FieldMeta {
                                        name: fn_lower,
                                        ..Default::default()
                                    },
                                );
                            }
                        }
                    } else if let Some(f_obj) = raw_fields.and_then(|f| f.as_object()) {
                        for (fname, fmeta_val) in f_obj {
                            let fn_lower = fname.trim().to_lowercase();
                            if let Ok(mut fmeta) = serde_json::from_value::<FieldMeta>(fmeta_val.clone()) {
                                if fmeta.name.is_empty() {
                                    fmeta.name = fn_lower.clone();
                                }
                                fields_map.insert(fn_lower, fmeta);
                            } else {
                                fields_map.insert(
                                    fn_lower.clone(),
                                    FieldMeta {
                                        name: fn_lower,
                                        ..Default::default()
                                    },
                                );
                            }
                        }
                    }
                }

                let mut index_columns: HashMap<String, Vec<String>> = HashMap::new();
                let mut indices_vec: Vec<serde_json::Value> = Vec::new();
                if let Some(obj) = tbl_info.as_object() {
                    if let Some(raw_idx) = obj.get("indices") {
                        if let Some(idx_obj) = raw_idx.as_object() {
                            for (idx_k, cols_val) in idx_obj {
                                if let Some(arr) = cols_val.as_array() {
                                    let cols: Vec<String> = arr
                                        .iter()
                                        .filter_map(|v| v.as_str().map(|s| s.trim().to_lowercase()))
                                        .filter(|s| !s.is_empty())
                                        .collect();
                                    if !cols.is_empty() {
                                        index_columns.insert(idx_k.clone(), cols);
                                    }
                                }
                            }
                        } else if let Some(idx_arr) = raw_idx.as_array() {
                            indices_vec = idx_arr.clone();
                            for item in idx_arr {
                                if let Some(m) = item.as_object() {
                                    let idx_name = m
                                        .get("name")
                                        .and_then(|v| v.as_str())
                                        .unwrap_or("")
                                        .trim()
                                        .to_string();
                                    if !idx_name.is_empty() {
                                        if let Some(cols_arr) = m.get("columns").and_then(|v| v.as_array()) {
                                            let cols: Vec<String> = cols_arr
                                                .iter()
                                                .filter_map(|v| v.as_str().map(|s| s.trim().to_lowercase()))
                                                .filter(|s| !s.is_empty())
                                                .collect();
                                            if !cols.is_empty() {
                                                index_columns.insert(idx_name, cols);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                self.tables.insert(
                    t_key.clone(),
                    TableMeta {
                        name: t_key,
                        description: desc,
                        fields: fields_map,
                        indices: indices_vec,
                        index_columns,
                    },
                );
            }
        }

        if let Some(raw_domains) = data.get("domains") {
            if let Some(d_arr) = raw_domains.as_array() {
                for item in d_arr {
                    if let Some(dname) = item.as_str() {
                        let d_lower = dname.trim().to_lowercase();
                        self.domains.insert(
                            d_lower.clone(),
                            DomainMeta {
                                name: d_lower,
                                ..Default::default()
                            },
                        );
                    }
                }
            } else if let Some(d_obj) = raw_domains.as_object() {
                for (dname, dmeta_val) in d_obj {
                    let d_lower = dname.trim().to_lowercase();
                    if let Ok(mut dmeta) = serde_json::from_value::<DomainMeta>(dmeta_val.clone()) {
                        if dmeta.name.is_empty() {
                            dmeta.name = d_lower.clone();
                        }
                        self.domains.insert(d_lower, dmeta);
                    } else {
                        self.domains.insert(
                            d_lower.clone(),
                            DomainMeta {
                                name: d_lower,
                                ..Default::default()
                            },
                        );
                    }
                }
            }
        }
    }

    pub fn has_table(&self, table_name: &str) -> bool {
        self.tables.contains_key(&table_name.trim().to_lowercase())
    }

    pub fn has_field(&self, table_name: &str, field_name: &str) -> bool {
        let t_key = table_name.trim().to_lowercase();
        let f_key = field_name.trim().to_lowercase();

        if BSHELL_PSEUDO_FIELDS.contains(&f_key.as_str()) {
            return true;
        }

        let re_idx = Regex::new(r"^_index\d+$").unwrap();
        if re_idx.is_match(&f_key) {
            return true;
        }

        if let Some(tbl) = self.tables.get(&t_key) {
            tbl.fields.contains_key(&f_key)
        } else {
            false
        }
    }

    pub fn has_domain(&self, domain_name: &str) -> bool {
        self.domains.contains_key(&domain_name.trim().to_lowercase())
    }

    pub fn get_field(&self, table_name: &str, field_name: &str) -> Option<&FieldMeta> {
        let t_key = table_name.trim().to_lowercase();
        let f_key = field_name.trim().to_lowercase();
        self.tables.get(&t_key).and_then(|t| t.fields.get(&f_key))
    }

    pub fn get_domain(&self, domain_name: &str) -> Option<&DomainMeta> {
        let d_key = domain_name.trim().to_lowercase();
        self.domains.get(&d_key)
    }

    pub fn update_table(
        &mut self,
        table_name: &str,
        fields: HashMap<String, FieldMeta>,
        indices: Option<Vec<serde_json::Value>>,
        description: Option<String>,
    ) {
        let t_key = table_name.trim().to_lowercase();
        let mut fields_map = HashMap::new();
        for (k, mut v) in fields {
            let f_key = k.to_lowercase();
            v.name = f_key.clone();
            fields_map.insert(f_key, v);
        }
        self.tables.insert(
            t_key.clone(),
            TableMeta {
                name: t_key,
                description,
                fields: fields_map,
                indices: indices.unwrap_or_default(),
                index_columns: HashMap::new(),
            },
        );
    }

    pub fn get_index_columns(&self, table_name: &str, index_name: &str) -> Option<Vec<String>> {
        let t_key = table_name.trim().to_lowercase();
        let i_key = index_name.trim().to_lowercase();
        self.tables
            .get(&t_key)
            .and_then(|t| t.index_columns.get(&i_key).cloned())
    }

    pub fn save_to_path(&self, path: impl AsRef<Path>) -> std::io::Result<()> {
        let target = path.as_ref();
        if let Some(parent) = target.parent() {
            if !parent.as_os_str().is_empty() {
                fs::create_dir_all(parent)?;
            }
        }

        let mut tables_json = serde_json::Map::new();
        let mut tbl_keys: Vec<_> = self.tables.keys().cloned().collect();
        tbl_keys.sort();
        for t_key in tbl_keys {
            let tbl = &self.tables[&t_key];
            let mut fields_json = serde_json::Map::new();
            let mut f_keys: Vec<_> = tbl.fields.keys().cloned().collect();
            f_keys.sort();
            for f_key in f_keys {
                let f = &tbl.fields[&f_key];
                let mut f_obj = serde_json::Map::new();
                f_obj.insert("name".into(), serde_json::Value::String(f.name.clone()));
                if let Some(ref dmn) = f.domain {
                    f_obj.insert("domain".into(), serde_json::Value::String(dmn.clone()));
                }
                if let Some(ref dt) = f.datatype {
                    f_obj.insert("datatype".into(), dt.clone());
                }
                if let Some(mand) = f.is_mandatory {
                    f_obj.insert("mandatory".into(), serde_json::Value::Bool(mand));
                }
                if let Some(ref desc) = f.description {
                    f_obj.insert("description".into(), serde_json::Value::String(desc.clone()));
                }
                fields_json.insert(f_key, serde_json::Value::Object(f_obj));
            }

            let mut t_obj = serde_json::Map::new();
            t_obj.insert("name".into(), serde_json::Value::String(tbl.name.clone()));
            if let Some(ref desc) = tbl.description {
                t_obj.insert("description".into(), serde_json::Value::String(desc.clone()));
            }
            t_obj.insert("fields".into(), serde_json::Value::Object(fields_json));
            if !tbl.index_columns.is_empty() {
                let mut idx_obj = serde_json::Map::new();
                let mut idx_keys: Vec<_> = tbl.index_columns.keys().cloned().collect();
                idx_keys.sort();
                for ik in idx_keys {
                    let cols = tbl.index_columns[&ik]
                        .iter()
                        .map(|c| serde_json::Value::String(c.clone()))
                        .collect();
                    idx_obj.insert(ik, serde_json::Value::Array(cols));
                }
                t_obj.insert("indices".into(), serde_json::Value::Object(idx_obj));
            } else {
                t_obj.insert("indices".into(), serde_json::Value::Object(serde_json::Map::new()));
            }
            tables_json.insert(t_key, serde_json::Value::Object(t_obj));
        }

        let mut domains_json = serde_json::Map::new();
        let mut d_keys: Vec<_> = self.domains.keys().cloned().collect();
        d_keys.sort();
        for d_key in d_keys {
            let d = &self.domains[&d_key];
            if let Ok(val) = serde_json::to_value(d) {
                domains_json.insert(d_key, val);
            }
        }

        let root = serde_json::json!({
            "version": "1.0",
            "tables": serde_json::Value::Object(tables_json),
            "domains": serde_json::Value::Object(domains_json),
        });
        fs::write(target, serde_json::to_string_pretty(&root).unwrap_or_else(|_| "{}".into()))
    }

    fn map_dd_txt_datatype(raw_dt: &str) -> String {
        let dt = raw_dt.split_whitespace().collect::<Vec<_>>().join(" ").to_ascii_lowercase();
        if dt.starts_with("utc") {
            "14".to_string()
        } else if dt == "date" {
            "9".to_string()
        } else if dt.starts_with("double") {
            "2".to_string()
        } else if dt == "long" || dt == "integer" {
            "3".to_string()
        } else if dt == "numeric" || dt == "float" {
            "5".to_string()
        } else if dt.starts_with("enum") {
            "7".to_string()
        } else if dt == "byte" {
            "1".to_string()
        } else if dt == "string" || dt == "multibyte" || dt == "multibyte string" || dt == "text" {
            "6".to_string()
        } else {
            raw_dt.trim().to_string()
        }
    }

    fn merge_table_entry(
        &mut self,
        tbl_name: &str,
        fields_map: HashMap<String, FieldMeta>,
        indices_map: HashMap<String, Vec<String>>,
        description: Option<String>,
    ) {
        let t_key = tbl_name.trim().to_lowercase();
        if let Some(existing) = self.tables.get_mut(&t_key) {
            if existing.description.as_deref().unwrap_or("").is_empty() {
                if let Some(d) = description {
                    if !d.is_empty() {
                        existing.description = Some(d);
                    }
                }
            }
            for (f_key, f_meta) in fields_map {
                if let Some(cur) = existing.fields.get_mut(&f_key) {
                    if cur.domain.as_deref().unwrap_or("").is_empty() && f_meta.domain.is_some() {
                        cur.domain = f_meta.domain;
                    }
                    if cur.datatype.is_none() && f_meta.datatype.is_some() {
                        cur.datatype = f_meta.datatype;
                    }
                    if cur.is_mandatory.is_none() && f_meta.is_mandatory.is_some() {
                        cur.is_mandatory = f_meta.is_mandatory;
                    }
                    if cur.description.as_deref().unwrap_or("").is_empty() && f_meta.description.is_some() {
                        cur.description = f_meta.description;
                    }
                } else {
                    existing.fields.insert(f_key, f_meta);
                }
            }
            for (idx_k, cols) in indices_map {
                if !existing.index_columns.contains_key(&idx_k) || existing.index_columns[&idx_k].is_empty() {
                    existing.index_columns.insert(idx_k, cols);
                }
            }
        } else {
            self.tables.insert(
                t_key.clone(),
                TableMeta {
                    name: t_key,
                    description,
                    fields: fields_map,
                    indices: Vec::new(),
                    index_columns: indices_map,
                },
            );
        }
    }

    fn merge_domain_if_missing(&mut self, domain_name: &str, datatype: &str, length: Option<usize>) {
        let d_key = domain_name.trim().to_lowercase();
        if d_key.is_empty() || d_key == "not applicab" {
            return;
        }
        if let Some(existing) = self.domains.get_mut(&d_key) {
            if existing.datatype.is_none() && !datatype.is_empty() {
                existing.datatype = Some(serde_json::Value::String(datatype.to_string()));
            }
            if existing.length.is_none() && length.is_some() {
                existing.length = length;
            }
        } else {
            self.domains.insert(
                d_key.clone(),
                DomainMeta {
                    name: d_key,
                    description: None,
                    datatype: Some(serde_json::Value::String(datatype.to_string())),
                    length,
                    constants: None,
                },
            );
        }
    }

    pub fn ingest_dd_txt_content(&mut self, text: &str, source_name: &str) -> Option<(String, usize)> {
        let lines: Vec<&str> = text.lines().collect();
        let is_cdf = text.to_ascii_lowercase().contains("customer defined fields")
            || source_name.to_ascii_lowercase().ends_with("-cdf.txt");

        if is_cdf {
            let re_cdf_tbl = Regex::new(r"(?i)^\s*Table\s*:\s*([a-z]{5}\d{3})\b\s*(.*)$").unwrap();
            let re_cdf_row = Regex::new(
                r"(?i)^\s*([a-z][a-z0-9_]*)\s*\[\s*\d+\s*\]\s+.*?\s+(Yes|No)\s+(Yes|No)\s+(Yes|No)\s+(Yes|No)\s+(String|Date|UTC\s*Date(?:/Time|/)?|Numeric|Double|Long|Integer|Enumerate|Text|Multibyte(?:\s+String)?|Boolean)\s+([a-z]{2})\s+([a-z0-9_.]+)\s+(Yes|No)\s+(Yes|No)\s+(Yes|No)\b"
            ).unwrap();
            let mut tbl_name = String::new();
            let mut tbl_desc = String::new();
            let mut fields_map = HashMap::new();
            for line in &lines {
                if let Some(c) = re_cdf_tbl.captures(line) {
                    tbl_name = c[1].to_lowercase();
                    tbl_desc = c[2].trim().to_string();
                    continue;
                }
                if let Some(c) = re_cdf_row.captures(line) {
                    let raw_field = c[1].to_lowercase();
                    let f_name = if raw_field.starts_with("cdf_") { raw_field } else { format!("cdf_{raw_field}") };
                    let dt_code = Self::map_dd_txt_datatype(&c[6]);
                    let dmn = format!("{}{}", c[7].to_lowercase(), c[8].to_lowercase());
                    self.merge_domain_if_missing(&dmn, &dt_code, None);
                    fields_map.insert(
                        f_name.clone(),
                        FieldMeta {
                            name: f_name,
                            description: None,
                            domain: Some(dmn),
                            datatype: Some(serde_json::Value::String(dt_code)),
                            is_mandatory: Some(false),
                            max_length: None,
                        },
                    );
                }
            }
            if tbl_name.is_empty() || fields_map.is_empty() {
                return None;
            }
            let count = fields_map.len();
            self.merge_table_entry(&tbl_name, fields_map, HashMap::new(), Some(tbl_desc));
            return Some((tbl_name, count));
        }

        let re_tbl_hdr = Regex::new(r"(?i)^\s*Table\s*:\s*([a-z]{2})\s+([a-z]{3})\s+(\d{3})\b\s*(.*)$").unwrap();
        let re_upd_ref = Regex::new(r"(?i)\s+Update\s+Reference\s+Message.*$").unwrap();
        let re_field_row = Regex::new(
            r"(?i)^\s*\d+\s+([a-z][a-z0-9_]*)\s+(.*?)\s+([a-z]{2}[a-z0-9_.]+)\s+(UTC\s*Date(?:/Time|/)?|Multibyte(?:\s+String)?|Integer|String|Enumerate|Double|Long|Text|Date|Byte|Numeric|Float|Boolean)\s+(?:\d+\s+)?(\d+)\s+(Yes|No)\s+(Yes|No)\b"
        ).unwrap();
        let re_combined_row = Regex::new(r"(?i)^\s*\d+\s+(cmb[a-z0-9_]*)\s+Not\s+applicab").unwrap();
        let re_child_row = Regex::new(r"(?i)^\s+([a-z][a-z0-9_]*)\s+Child\s+Field\b").unwrap();
        let re_idx_hdr = Regex::new(r"(?i)^\s*Index\s+Description\s+Index\s+Parts\b").unwrap();
        let re_idx_row = Regex::new(r"(?i)^\s*(\d+)\s+(.+?)\s+(Yes|No)\s+(Yes|No)\s*$").unwrap();

        let mut tbl_name = String::new();
        let mut tbl_desc = String::new();
        let mut fields_map: HashMap<String, FieldMeta> = HashMap::new();
        let mut combined_children: HashMap<String, Vec<String>> = HashMap::new();
        let mut indices_map: HashMap<String, Vec<String>> = HashMap::new();
        let mut current_combined: Option<String> = None;
        let mut in_index_section = false;

        for line in &lines {
            if tbl_name.is_empty() {
                if let Some(c) = re_tbl_hdr.captures(line) {
                    tbl_name = format!("{}{}{}", &c[1], &c[2], &c[3]).to_lowercase();
                    tbl_desc = re_upd_ref.replace(c[4].trim(), "").trim().to_string();
                    continue;
                }
            }
            if re_idx_hdr.is_match(line) {
                in_index_section = true;
                current_combined = None;
                continue;
            }
            if in_index_section {
                if let Some(c) = re_idx_row.captures(line) {
                    let idx_num = c[1].to_string();
                    let mid_tokens: Vec<&str> = c[2].trim().split_whitespace().collect();
                    let mut parts_rev: Vec<String> = Vec::new();
                    for tok in mid_tokens.iter().rev() {
                        let t_low = tok.to_lowercase();
                        if fields_map.contains_key(&t_low) || combined_children.contains_key(&t_low) {
                            parts_rev.push(t_low);
                        } else {
                            break;
                        }
                    }
                    let mut expanded = Vec::new();
                    for part in parts_rev.into_iter().rev() {
                        if let Some(children) = combined_children.get(&part) {
                            expanded.extend(children.iter().cloned());
                        } else {
                            expanded.push(part);
                        }
                    }
                    if !expanded.is_empty() {
                        indices_map.insert(idx_num, expanded);
                    }
                }
                continue;
            }
            if let Some(ref cmb) = current_combined {
                if let Some(c) = re_child_row.captures(line) {
                    combined_children.entry(cmb.clone()).or_default().push(c[1].to_lowercase());
                    continue;
                }
            }
            if let Some(c) = re_combined_row.captures(line) {
                let cmb = c[1].to_lowercase();
                combined_children.entry(cmb.clone()).or_default();
                current_combined = Some(cmb);
                continue;
            }
            if let Some(c) = re_field_row.captures(line) {
                current_combined = None;
                let f_name = c[1].to_lowercase();
                let f_desc = c[2].trim().to_string();
                let dmn = c[3].to_lowercase();
                let dt_code = Self::map_dd_txt_datatype(&c[4]);
                let phys_len_str = c[5].trim();
                let phys_len_num = phys_len_str.parse::<usize>().ok();
                let mand = c[6].eq_ignore_ascii_case("yes");
                self.merge_domain_if_missing(&dmn, &dt_code, phys_len_num);
                fields_map.insert(
                    f_name.clone(),
                    FieldMeta {
                        name: f_name,
                        description: Some(f_desc),
                        domain: Some(dmn),
                        datatype: Some(serde_json::Value::String(dt_code)),
                        is_mandatory: Some(mand),
                        max_length: Some(serde_json::Value::String(phys_len_str.to_string())),
                    },
                );
            }
        }

        if tbl_name.is_empty() || fields_map.is_empty() {
            return None;
        }
        let count = fields_map.len();
        self.merge_table_entry(&tbl_name, fields_map, indices_map, Some(tbl_desc));
        Some((tbl_name, count))
    }

    pub fn ingest_dd_txt_dir(&mut self, dir: &Path) -> std::io::Result<usize> {
        if !dir.exists() || !dir.is_dir() {
            return Ok(0);
        }
        let mut files: Vec<PathBuf> = fs::read_dir(dir)?
            .flatten()
            .map(|e| e.path())
            .filter(|p| p.is_file() && p.extension().and_then(|s| s.to_str()).map_or(false, |e| e.eq_ignore_ascii_case("txt")))
            .collect();
        files.sort_by_key(|p| {
            let name = p.file_name().and_then(|s| s.to_str()).unwrap_or("").to_ascii_lowercase();
            (if name.ends_with("-cdf.txt") { 1 } else { 0 }, name)
        });
        let mut imported = 0usize;
        for f in files {
            if let Ok(content) = fs::read_to_string(&f) {
                let sname = f.file_name().and_then(|s| s.to_str()).unwrap_or("");
                if self.ingest_dd_txt_content(&content, sname).is_some() {
                    imported += 1;
                }
            }
        }
        Ok(imported)
    }

    pub fn update_domain(
        &mut self,
        domain_name: &str,
        datatype: Option<&str>,
        length: Option<usize>,
        constants: Option<Vec<String>>,
    ) {
        let d_key = domain_name.trim().to_lowercase();
        let consts_map = constants.map(|list| {
            let mut map = HashMap::new();
            for c in list {
                map.insert(c.clone(), serde_json::Value::String(c));
            }
            map
        });
        self.domains.insert(
            d_key.clone(),
            DomainMeta {
                name: d_key,
                description: None,
                datatype: datatype.map(|s| serde_json::Value::String(s.to_string())),
                length,
                constants: consts_map,
            },
        );
    }
}
