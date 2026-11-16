use serde::{Deserialize, Serialize};

pub const STANDARD_COMMANDS: &[(&str, bool, usize)] = &[
    ("start.set", false, 1),
    ("first.view", false, 2),
    ("next.view", false, 3),
    ("prev.view", false, 4),
    ("last.view", false, 5),
    ("def.find", true, 6),
    ("find.data", true, 7),
    ("first.set", true, 8),
    ("next.set", true, 9),
    ("display.set", false, 10),
    ("prev.set", true, 11),
    ("rotate.curr", false, 12),
    ("last.set", true, 13),
    ("add.set", true, 14),
    ("update.db", true, 15),
    ("dupl.occur", true, 16),
    ("recover.set", true, 17),
    ("mark.delete", true, 18),
    ("mark.occur", false, 19),
    ("change.order", false, 20),
    ("modify.set", true, 21),
    ("print.data", false, 23),
    ("create.job", false, 24),
    ("change.frm", true, 25),
    ("first.frm", true, 26),
    ("next.frm", true, 27),
    ("prev.frm", true, 28),
    ("last.frm", true, 29),
    ("resize.frm", false, 31),
    ("cust.grid", false, 32),
    ("cmd.options", false, 33),
    ("zoom", false, 34),
    ("interrupt", false, 35),
    ("end.program", true, 36),
    ("abort.program", true, 37),
    ("text.manager", false, 39),
    ("run.job", false, 40),
    ("global.delete", false, 41),
    ("global.copy", false, 42),
    ("save.defaults", false, 43),
    ("get.defaults", false, 44),
    ("start.chart", false, 45),
    ("start.query", true, 46),
    ("select.all", false, 47),
];

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SessionFormFieldSpec {
    pub name: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub mandatory: Option<bool>,
    #[serde(default)]
    pub native_datatype: Option<u32>,
    #[serde(default)]
    pub length: Option<usize>,
    #[serde(default)]
    pub zoom_program: Option<String>,
    #[serde(default)]
    pub zoom_return_field: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FormCommandSpec {
    pub name: String,
    #[serde(default)]
    pub function: Option<String>,
    #[serde(default)]
    pub label_code: Option<String>,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub position: Option<String>,
    #[serde(default)]
    pub sequence: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SatelliteSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SessionSpec {
    pub code: String,
    #[serde(default)]
    pub description: Option<String>,
    #[serde(default)]
    pub version_id: Option<String>,
    #[serde(default)]
    pub application: Option<String>,
    #[serde(default = "default_window_type")]
    pub window_type: usize, // 1 = Dynamic, 2 = Standard, 3 = MMTController, 4 = Dialog
    #[serde(default = "default_sub_type")]
    pub sub_type: usize,    // 1 = Maintain, 2 = Display, 3 = Process, 4 = Print
    #[serde(default)]
    pub table: Option<String>,
    #[serde(default)]
    pub table_description: Option<String>,
    #[serde(default)]
    pub satellites: Vec<SatelliteSpec>,
    #[serde(default)]
    pub form_commands: Vec<FormCommandSpec>,
    #[serde(default)]
    pub fields: Vec<SessionFormFieldSpec>,
    #[serde(default)]
    pub script: Option<String>,
}

fn default_window_type() -> usize {
    2
}

fn default_sub_type() -> usize {
    1
}

pub fn generate_form_field_xml(
    f: &SessionFormFieldSpec,
    table_code: &str,
    seq: usize,
    group_id: usize,
) -> String {
    let full_name = if table_code.is_empty() {
        f.name.clone()
    } else {
        format!("{table_code}.{}", f.name)
    };
    let f_lbl = f.label_code.clone().unwrap_or_else(|| full_name.clone());
    let is_mand = if f.mandatory.unwrap_or(false) { "true" } else { "false" };
    let f_len = f.length.unwrap_or(20);
    let f_dt = f.native_datatype.unwrap_or(6);
    let zoom_prog = f.zoom_program.as_deref().unwrap_or("");
    let zoom_ret = f.zoom_return_field.as_deref().unwrap_or("");
    let zoom_type = if !zoom_prog.is_empty() { "2" } else { "1" };
    let disp_format = if f_dt == 3 { "ZZZZZ9" } else { "" };
    let format_linked = "true";
    let desc_len = f.description.as_ref().map(|d| d.len()).unwrap_or(f.name.len());
    let u_id = format!("uuid-field-{seq}");

    format!(
        "<FormField><uuid>{u_id}</uuid><textDirection>10</textDirection><fieldAlignment>5</fieldAlignment><indexZoomSession>0</indexZoomSession><iconName/><additionalProperties2>0</additionalProperties2><additionalProperties1>1</additionalProperties1><autoEnableDisable>false</autoEnableDisable><behindEnumConstant>0</behindEnumConstant><hyperlink>false</hyperlink><searchDescription/><constantValueForYes>0</constantValueForYes><viewField>false</viewField><displayHeight>1</displayHeight><columnID>1</columnID><endXPosition>50</endXPosition><parentField>0</parentField><labelHeightOverview>1</labelHeightOverview><labelLengthOverview>999</labelLengthOverview><labelHeightDetail>1</labelHeightDetail><labelLengthDetail>{desc_len}</labelLengthDetail><labelPosition>1</labelPosition><dependentOnParentField>false</dependentOnParentField><xPositionLabel>1</xPositionLabel><followUpField>0</followUpField><labelAlignment>2</labelAlignment><windowsControl>0</windowsControl><fieldBelowGrid>false</fieldBelowGrid><overviewSession>true</overviewSession><detailsSession>true</detailsSession><childFieldsBehind>false</childFieldsBehind><followUp>false</followUp><nextField>0</nextField><groupID>{group_id}</groupID><synchronizedField>false</synchronizedField><defaultValue/><inputReferenceExpression>1</inputReferenceExpression><fieldLabel>{f_lbl}</fieldLabel><languageUnitExpression/><mandatoryInput>{is_mand}</mandatoryInput><sequenceMode>{}</sequenceMode><fieldLength>{f_len}</fieldLength><echoField>true</echoField><message/><defaultExpression>false</defaultExpression><zoomReturnField>{zoom_ret}</zoomReturnField><zoomProgram>{zoom_prog}</zoomProgram><zoomType>{zoom_type}</zoomType><startPositionString>1</startPositionString><linkInputDigitsBefore>true</linkInputDigitsBefore><inputDigitsBefore>{f_len}</inputDigitsBefore><linkDisplayDigitsBefore>true</linkDisplayDigitsBefore><displayDigitsBefore>{f_len}</displayDigitsBefore><minimumInputLength>0</minimumInputLength><displayFormatLinked>{format_linked}</displayFormatLinked><displayFormat>{disp_format}</displayFormat><fieldType>2</fieldType><domain/><element>1</element><fieldName>{full_name}</fieldName><rowScreenPosition>1</rowScreenPosition><columnScreenPosition>44</columnScreenPosition><sequenceNumber>{seq}</sequenceNumber></FormField>",
        seq * 10
    )
}

/// Generates standard Infor LN Studio 10.8 `<DR_Controller>` XML.
pub fn generate_session_xml(
    spec: &SessionSpec,
    application: &str,
    default_version_id: &str,
    ui_script_code: Option<&str>,
    created_time: Option<&str>,
) -> String {
    let now_iso = created_time.unwrap_or("1970-01-01T00:00:00Z");
    let desc = spec.description.as_deref().unwrap_or(&spec.code);
    let ver = spec.version_id.as_deref().unwrap_or(default_version_id);
    let app = spec.application.as_deref().unwrap_or(application);
    let code = &spec.code;

    let mut parts = Vec::new();
    parts.push(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#.to_string());
    parts.push("<DR_Controller>".to_string());
    parts.push(format!("<description>{desc}</description>"));
    parts.push(format!("<versionID>{ver}</versionID>"));
    parts.push("<type>session</type>".to_string());
    parts.push(format!("<name>{code}</name>"));
    parts.push(format!(
        "<Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></Version>"
    ));
    parts.push(format!("<descriptionReference>{code}</descriptionReference>"));
    parts.push(format!("<windowType>{}</windowType>", spec.window_type));

    // Linked Table Relationship
    if let Some(ref tcode) = spec.table {
        let t_desc = spec.table_description.as_deref().unwrap_or(tcode);
        let index_usage = "<IndexUsage><nrGroupFields>0</nrGroupFields><sequence>0</sequence><active>false</active><position>1</position></IndexUsage>";
        parts.push(format!(
            "<ControllerTableRelationship><showView>false</showView><dynIndexSwitching>1</dynIndexSwitching>{index_usage}<toTable>{tcode}</toTable><position>1</position><descriptionReference>{tcode}</descriptionReference><description>{t_desc}</description><name>{tcode}</name></ControllerTableRelationship>"
        ));
    }

    // Satellites
    for (sat_pos, sat) in spec.satellites.iter().enumerate() {
        let s_code = &sat.code;
        let s_desc = sat.description.as_deref().unwrap_or(s_code);
        parts.push(format!(
            "<ControllerSatelliteRelationship><name>{s_code}</name><description>{s_desc}</description><descriptionReference>{s_code}</descriptionReference><position>{}</position><documentation/><versionID>{ver}</versionID><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></Version><toSession>{s_code}</toSession><initialHidden>false</initialHidden></ControllerSatelliteRelationship>",
            sat_pos + 1
        ));
    }

    // Form Commands
    for cmd in &spec.form_commands {
        let c_name = &cmd.name;
        let c_fn = cmd.function.as_deref().unwrap_or(c_name);
        let default_lbl = format!("{code}.{c_name}");
        let c_lbl = cmd.label_code.as_deref().unwrap_or(&default_lbl);
        let c_desc = cmd.description.as_deref().unwrap_or(c_name);
        let c_pos = cmd.position.as_deref().unwrap_or("1");
        let c_seq = cmd.sequence.as_deref().unwrap_or("10");

        parts.push(format!(
            "<FormCommand><name>{c_name}</name><description>{c_desc}</description><descriptionReference>{c_lbl}</descriptionReference><type>user</type><position>{c_pos}</position><sequence>{c_seq}</sequence><defaultcommand>false</defaultcommand><activationType>function</activationType><activationName>{c_fn}</activationName><parent/><shortcut/><separator>false</separator><showAsButton>true</showAsButton><showOnMenu>true</showOnMenu><initialHidden>false</initialHidden><commandAvailability>1</commandAvailability><multipleExecution>false</multipleExecution><saveBeforeExecution>false</saveBeforeExecution><refreshParent>false</refreshParent><category>1</category></FormCommand>"
        ));
    }

    // UI Methods
    parts.push("<UIMethod><status>allowed</status><description>Webtop Enabled</description><name>webtop</name></UIMethod>".to_string());
    parts.push("<UIMethod><status>notchecked</status><description>Workflow Enabled</description><name>workflow</name></UIMethod>".to_string());

    // Standard Commands
    for &(cmd_name, is_act, pos) in STANDARD_COMMANDS {
        let act_str = if is_act { "true" } else { "false" };
        parts.push(format!(
            "<StandardCommand><active>{act_str}</active><defaultcommand>false</defaultcommand><startcommand>false</startcommand><position>{pos}</position><description/><name>{cmd_name}</name></StandardCommand>"
        ));
    }
    parts.push("<defaultStartCommand>false</defaultStartCommand>".to_string());

    // Form & Form Fields Layout
    let mut fields_xml = String::new();
    let t_code = spec.table.as_deref().unwrap_or("");
    for (seq, f) in spec.fields.iter().enumerate() {
        fields_xml.push_str(&generate_form_field_xml(f, t_code, seq + 1, 2));
    }

    let form_groups_xml = "<FormGroup><selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous><nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly><formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage><nrSubGroups>1</nrSubGroups><firstChildGroup>2</firstChildGroup><virtualGroup>true</virtualGroup><groupAlignment>1</groupAlignment><firstField>0</firstField><nextGroup>0</nextGroup><previousGroup>0</previousGroup><parentGroup>0</parentGroup><overviewSession>true</overviewSession><detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/><level>0</level><repeating>false</repeating><groupID>1</groupID></FormGroup><FormGroup><selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous><nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly><formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage><nrSubGroups>1</nrSubGroups><firstChildGroup>0</firstChildGroup><virtualGroup>false</virtualGroup><groupAlignment>-2</groupAlignment><firstField>10</firstField><nextGroup>3</nextGroup><previousGroup>0</previousGroup><parentGroup>1</parentGroup><overviewSession>true</overviewSession><detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/><level>1</level><repeating>true</repeating><groupID>2</groupID></FormGroup><FormGroup><selectionGroup>false</selectionGroup><parentTable/><miscellaneous>0</miscellaneous><nextToOtherGroup>false</nextToOtherGroup><checkBoxesOnly>false</checkBoxesOnly><formFormat>13</formFormat><subGroupOnNewPage>false</subGroupOnNewPage><nrSubGroups>1</nrSubGroups><firstChildGroup>0</firstChildGroup><virtualGroup>false</virtualGroup><groupAlignment>-3</groupAlignment><firstField>20</firstField><nextGroup>0</nextGroup><previousGroup>2</previousGroup><parentGroup>1</parentGroup><overviewSession>true</overviewSession><detailsSession>true</detailsSession><showGroupBox>false</showGroupBox><groupHeader/><level>1</level><repeating>false</repeating><groupID>3</groupID></FormGroup>";

    parts.push(format!(
        "<Form><PhysicalFormLayout>{fields_xml}{form_groups_xml}</PhysicalFormLayout><description>{desc}</description><name>{code}d</name><horizontal>true</horizontal><custProhibited>false</custProhibited><additionalConstraints>1</additionalConstraints><documentation/><application>{app}</application></Form>"
    ));

    // Embedded UI Script
    let default_script;
    let s = if let Some(s) = ui_script_code.or(spec.script.as_deref()) {
        s
    } else {
        let t_code = spec.table.as_deref().unwrap_or("");
        let t_desc = spec.table_description.as_deref().unwrap_or(t_code);
        default_script = format!(
            "|*******************************************************************************\n\
            |* {code}  {ver}\n\
            |* {desc}\n\
            |* Script Type: 123\n\
            |*******************************************************************************\n\n\
            #include <bic_dam>\n\n\
            declaration:\n\n\
            \ttable\tt{t_code} |* {t_desc}\n\n\
            main.table.io:\n\
            before.write:\n\n\
            before.rewrite:\n\n\
            choice.update.db:\n\
            before.choice:\n\
            \tcheck.all.input()\n"
        );
        &default_script
    };

    let escaped = s.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;");
    parts.push(format!(
        "<DR_Module><description>{desc}</description><versionID>{ver}</versionID><type>library</type><name>{code}</name><Version><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></Version><Source><sourceVersion><ObjectID/><classID/><checkInLabel/><documentation/><isExpired>no</isExpired><isCheckedOutParallel>no</isCheckedOutParallel><isCheckedOut>no</isCheckedOut><modificationDateTime>{now_iso}</modificationDateTime><modifiedBy>agent</modifiedBy><creationDateTime>{now_iso}</creationDateTime><createdBy>agent</createdBy></sourceVersion><sourceVersionID>{ver}</sourceVersionID><sourceObjectID>1</sourceObjectID><expression>{escaped}</expression><expressionLanguageType>Baan4C</expressionLanguageType><sourceType>1</sourceType><sourceDescription>{desc}</sourceDescription><sourceName>{code}</sourceName></Source><documentation/><Attachment><type>relnotes</type><name>{code}</name></Attachment><Attachment><type>techdoc</type><name>{code}</name></Attachment><additionalConstraints>1</additionalConstraints><additionalInstructions/><keyword>||</keyword><application>{app}</application></DR_Module>"
    ));

    parts.push("</DR_Controller>".to_string());
    parts.join("")
}
