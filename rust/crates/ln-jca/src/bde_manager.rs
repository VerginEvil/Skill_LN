use std::collections::HashMap;
use crate::client::{extract_tag, HttpClient};
use crate::error::JcaError;
use crate::filter::{BdeFilter, BdeSelection};
use crate::security::assert_not_prohibited_operation;

pub const DEFAULT_ITERATOR_FETCH_SIZE: usize = 250;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum BdeExecutionMode {
    List = 0,
    Show = 1,
    Bde = 2,
    SpecialList = 3,
    BrowseList = 4,
}

impl BdeExecutionMode {
    pub fn from_str(s: &str) -> Self {
        match s.trim().to_uppercase().as_str() {
            "LIST" | "0" => Self::List,
            "SHOW" | "1" => Self::Show,
            "SPECIALLIST" | "3" => Self::SpecialList,
            "BROWSELIST" | "4" => Self::BrowseList,
            _ => Self::Bde,
        }
    }
}

#[derive(Debug, Clone, Default)]
pub struct BdeParams {
    pub bde_name: String,
    pub method_name: String,
    pub mode: Option<BdeExecutionMode>,
    pub request_xml: Option<String>,
    pub context_xml: Option<String>,
    pub selection: Option<BdeSelection>,
    pub filter: Option<BdeFilter>,
    pub max_objects: Option<usize>,
    pub controlling_attributes: HashMap<String, String>,
}

pub struct JcaBdeManager<'a> {
    client: &'a HttpClient,
    conid: String,
}

impl<'a> JcaBdeManager<'a> {
    pub fn new(client: &'a HttpClient, conid: &str) -> Self {
        Self {
            client,
            conid: conid.to_string(),
        }
    }

    pub fn set_conid(&mut self, conid: &str) {
        self.conid = conid.to_string();
    }

    pub fn get_conid(&self) -> &str {
        &self.conid
    }

    /// Builds the ControlArea XML payload for a given BDE method call.
    pub fn build_control_area(
        &self,
        method_name: &str,
        selection: Option<&BdeSelection>,
        filter: Option<&BdeFilter>,
        context_xml: Option<&str>,
        max_objects: Option<usize>,
        iterator_id: Option<i64>,
        fetch_size: Option<usize>,
        controlling_attributes: &HashMap<String, String>,
    ) -> String {
        let mut xml = String::from("<ControlArea>");

        if let Some(sel) = selection {
            xml.push_str(&sel.to_xml());
        }

        if let Some(f) = filter {
            xml.push_str(&f.to_xml());
        }

        if let Some(ctx) = context_xml {
            if !ctx.trim().is_empty() {
                if ctx.trim().starts_with('<') {
                    xml.push_str(ctx.trim());
                } else {
                    xml.push_str(&format!("<ActivityID><activityUUID>{}</activityUUID></ActivityID>", ctx.trim()));
                }
            }
        }

        if let Some(max) = max_objects {
            if max > 0 {
                xml.push_str(&format!("<maxNumberOfObjects>{max}</maxNumberOfObjects>"));
            }
        }

        if let Some(iter_id) = iterator_id {
            xml.push_str(&format!("<iteratorID>{iter_id}</iteratorID>"));
        }

        if let Some(fs) = fetch_size {
            xml.push_str(&format!("<iteratorFetchSize>{fs}</iteratorFetchSize>"));
        }

        // Controlling Attributes matching methodName
        for (k, v) in controlling_attributes {
            let attr_name = if k.contains(';') {
                let parts: Vec<&str> = k.split(';').collect();
                if parts.len() >= 2 {
                    if !parts[0].is_empty() && parts[0] != method_name {
                        continue;
                    }
                    parts[1]
                } else {
                    k
                }
            } else if k.contains(':') {
                let parts: Vec<&str> = k.split(':').collect();
                if parts.len() >= 2 {
                    if !parts[0].is_empty() && parts[0] != method_name {
                        continue;
                    }
                    parts[1]
                } else {
                    k
                }
            } else {
                k.as_str()
            };

            let clean_attr = attr_name.trim();
            if !clean_attr.is_empty() {
                xml.push_str(&format!("<{clean_attr}>{}</{clean_attr}>", crate::filter::escape_xml(v)));
            }
        }

        xml.push_str("</ControlArea>");
        xml
    }

    /// Builds the full `<{methodName}Request>` XML envelope.
    pub fn build_request_envelope(
        &self,
        method_name: &str,
        control_area: &str,
        data_area: Option<&str>,
    ) -> String {
        let mut envelope = format!("<{method_name}Request>");
        envelope.push_str(control_area);
        if let Some(da) = data_area {
            if !da.trim().is_empty() {
                if da.trim().starts_with("<DataArea>") {
                    envelope.push_str(da.trim());
                } else {
                    envelope.push_str(&format!("<DataArea>{}</DataArea>", da.trim()));
                }
            }
        }
        envelope.push_str(&format!("</{method_name}Request>"));
        envelope
    }

    /// Executes a BDE call across any of the 5 modes.
    pub async fn execute(&self, params: &BdeParams) -> Result<String, JcaError> {
        let mode = params.mode.unwrap_or(BdeExecutionMode::Bde);
        let req_xml = params.request_xml.as_deref().unwrap_or("");

        // Safety check
        assert_not_prohibited_operation(&params.bde_name, &params.method_name, req_xml)?;

        match mode {
            BdeExecutionMode::List | BdeExecutionMode::BrowseList => {
                self.execute_list_with_pagination(params, None).await
            }
            BdeExecutionMode::SpecialList => {
                self.execute_list_with_pagination(params, Some(req_xml)).await
            }
            BdeExecutionMode::Show => {
                let ctrl_xml = self.build_control_area(
                    &params.method_name,
                    params.selection.as_ref(),
                    params.filter.as_ref(),
                    params.context_xml.as_deref(),
                    None,
                    None,
                    None,
                    &params.controlling_attributes,
                );
                let env_xml = self.build_request_envelope(&params.method_name, &ctrl_xml, Some(req_xml));
                let resp_xml = self.client.bde_call(&params.bde_name, &params.method_name, &self.conid, &env_xml).await?;
                Ok(extract_first_child_of_data_area(&resp_xml).unwrap_or(resp_xml))
            }
            BdeExecutionMode::Bde => {
                let ctrl_xml = self.build_control_area(
                    &params.method_name,
                    params.selection.as_ref(),
                    params.filter.as_ref(),
                    params.context_xml.as_deref(),
                    None,
                    None,
                    None,
                    &params.controlling_attributes,
                );
                let env_xml = if params.method_name == "DR_Create" && req_xml.starts_with("<DR_") {
                    // Send raw component root XML element directly (no <DR_CreateRequest> wrapper)
                    if !ctrl_xml.is_empty() && ctrl_xml != "<ControlArea></ControlArea>" && !req_xml.contains("<ControlArea>") {
                        if let Some(first_gt) = req_xml.find('>') {
                            let mut s = String::with_capacity(req_xml.len() + ctrl_xml.len() + 2);
                            s.push_str(&req_xml[..=first_gt]);
                            s.push('\n');
                            s.push_str(&ctrl_xml);
                            s.push_str(&req_xml[first_gt + 1..]);
                            s
                        } else {
                            req_xml.to_string()
                        }
                    } else {
                        req_xml.to_string()
                    }
                } else {
                    self.build_request_envelope(&params.method_name, &ctrl_xml, if req_xml.is_empty() { None } else { Some(req_xml) })
                };
                let resp_xml = self.client.bde_call(&params.bde_name, &params.method_name, &self.conid, &env_xml).await?;
                Ok(extract_first_child_of_data_area(&resp_xml).unwrap_or(resp_xml))
            }
        }
    }

    /// Implements 250-item `<iteratorID>` auto-pagination for LIST, BROWSELIST, and SPECIALLIST modes.
    async fn execute_list_with_pagination(
        &self,
        params: &BdeParams,
        initial_data_area: Option<&str>,
    ) -> Result<String, JcaError> {
        let mut accumulated_data_items = Vec::new();
        let mut current_iterator_id: Option<i64> = None;
        let fetch_size = DEFAULT_ITERATOR_FETCH_SIZE;

        let empty_ctrl_attrs = HashMap::new();
        loop {
            let ctrl_xml = self.build_control_area(
                &params.method_name,
                if current_iterator_id.is_none() { params.selection.as_ref() } else { None },
                if current_iterator_id.is_none() { params.filter.as_ref() } else { None },
                if current_iterator_id.is_none() { params.context_xml.as_deref() } else { None },
                if current_iterator_id.is_none() { params.max_objects } else { None },
                current_iterator_id,
                Some(fetch_size),
                if current_iterator_id.is_none() { &params.controlling_attributes } else { &empty_ctrl_attrs },
            );

            let data_area = if current_iterator_id.is_none() {
                initial_data_area
            } else {
                None
            };

            let envelope = self.build_request_envelope(&params.method_name, &ctrl_xml, data_area);
            let resp_xml = self.client.bde_call(
                &params.bde_name,
                &params.method_name,
                &self.conid,
                &envelope,
            ).await?;

            // Extract DataArea content
            if let Some(da_content) = extract_tag(&resp_xml, "DataArea") {
                let trimmed = da_content.trim();
                if !trimmed.is_empty() {
                    accumulated_data_items.push(trimmed.to_string());
                }
            }

            // Check ControlArea for iteratorID
            let iter_id = extract_tag(&resp_xml, "iteratorID")
                .and_then(|s| s.parse::<i64>().ok());

            match iter_id {
                Some(next_id) if next_id >= 0 => {
                    current_iterator_id = Some(next_id);
                }
                _ => break,
            }
        }

        let mut merged = String::from("<DataArea>");
        for items in accumulated_data_items {
            merged.push_str(&items);
        }
        merged.push_str("</DataArea>");

        Ok(merged)
    }
}

pub fn extract_first_child_of_data_area(xml: &str) -> Option<String> {
    let da_content = extract_tag(xml, "DataArea")?;
    let trimmed = da_content.trim();
    if trimmed.is_empty() {
        return Some("<Success/>".to_string());
    }
    Some(trimmed.to_string())
}
