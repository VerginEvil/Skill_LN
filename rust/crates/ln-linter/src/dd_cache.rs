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

                self.tables.insert(
                    t_key.clone(),
                    TableMeta {
                        name: t_key,
                        description: desc,
                        fields: fields_map,
                        indices: Vec::new(),
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
            },
        );
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
