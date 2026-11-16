use crate::error::BdeExecutionError;

pub const PROHIBITED_BDE_METHODS: &[&str] = &[
    "endactivity",
    "closetask",
    "finalizeactivity",
    "deliveractivity",
    "commitactivity",
    "completeactivity",
];

pub const PROHIBITED_XML_TAGS: &[&str] = &[
    "<endactivity",
    "<closetask",
    "<finalizeactivity",
    "<deliveractivity",
    "<end/>",
    "<end>",
    "<deliver/>",
    "<deliver>",
];

/// Protocol-level safety check (ADR 0007 / ADR 0008 / ADR 0021):
/// Physically rejects any attempt to invoke EndActivity, CloseTask, FinalizeActivity, or Deliver.
pub fn assert_not_prohibited_operation(
    bde_name: &str,
    method_name: &str,
    request_xml: &str,
) -> Result<(), BdeExecutionError> {
    let b_low = bde_name.trim().to_lowercase();
    let m_low = method_name.trim().to_lowercase();

    for forbidden in PROHIBITED_BDE_METHODS {
        if m_low == *forbidden || m_low.contains(forbidden) || b_low.contains(forbidden) {
            return Err(BdeExecutionError {
                message: format!(
                    "[PROHIBITED_OPERATION] Protocol-level guardrail (ADR 0008): '{}.{}' \
                    (EndActivity/CloseTask) is physically prohibited. Use 'prepare-end-activity' for read-only \
                    verification and complete the activity manually in LN Studio.",
                    bde_name, method_name
                ),
                bde: bde_name.to_string(),
                method: method_name.to_string(),
                status_code: None,
                exception_code: None,
                raw_response: String::new(),
            });
        }
    }

    if !request_xml.is_empty() {
        let xml_low = request_xml.to_lowercase();
        for tag in PROHIBITED_XML_TAGS {
            if xml_low.contains(tag) {
                return Err(BdeExecutionError {
                    message: format!(
                        "[PROHIBITED_OPERATION] Protocol-level guardrail (ADR 0008): XML payload containing '{}' \
                        is physically prohibited from executing activity closure.",
                        tag
                    ),
                    bde: bde_name.to_string(),
                    method: method_name.to_string(),
                    status_code: None,
                    exception_code: None,
                    raw_response: String::new(),
                });
            }
        }
    }

    Ok(())
}
