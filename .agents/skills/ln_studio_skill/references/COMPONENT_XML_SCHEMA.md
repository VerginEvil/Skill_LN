# Infor LN Studio Component XML Schema Reference

This reference documents the official XML schema structures required by **Infor LN Studio 10.8** (April 2026 tree) for software components across all managed extensions:
- Tables (`.tbl`)
- Domains (`.dmn`)
- Labels (`.lbl`)
- Sessions (`.ses` / `<DR_Controller>`)
- Libraries (`.lib` — DLL, Session Extensions `ess`, Table Extensions `est`)
- Menus (`.mnu`)
- Reports (`.rpt`, `.rptdsrc`)

---

## 1. Table Schema (`.tbl`)

Root element is `<DR_Table>`. Note the Workbench column label convention: `<package><table_code>.<column>` (e.g. `txtxcmg010.user` for package `tx` and table `txcmg010`).

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Batch Header</description>
  <versionID>B61O_a_ext</versionID>
  <type>table</type>
  <name>txcmg011</name>
  <Version>
    <ObjectID/><classID/><checkInLabel/><documentation/>
    <isExpired>no</isExpired>
    <isCheckedOutParallel>no</isCheckedOutParallel>
    <isCheckedOut>no</isCheckedOut>
    <modificationDateTime>2026-10-22T05:00:00Z</modificationDateTime>
    <modifiedBy>agent</modifiedBy>
    <creationDateTime>2026-10-22T05:00:00Z</creationDateTime>
    <createdBy>agent</createdBy>
  </Version>
  <descriptionReference>txcmg011</descriptionReference>
  <Attachment><type>relnotes</type><name>txcmg011</name></Attachment>
  <Attachment><type>techdoc</type><name>txcmg011</name></Attachment>

  <!-- Indices -->
  <Index>
    <descriptionReference>txcmg01101</descriptionReference>
    <description>Batch No</description>
    <IndexColumn>
      <sortingOrder>asc</sortingOrder>
      <name>btno</name>
      <position>1</position>
    </IndexColumn>
    <isActive>true</isActive>
    <isPrimaryKey>true</isPrimaryKey>
    <isUnique>true</isUnique>
    <name>1</name>
  </Index>

  <!-- Columns -->
  <!-- Long integer Column -->
  <Column>
    <descriptionReference>txtxcmg011.btno</descriptionReference>
    <description>Batch No</description>
    <isNullable>false</isNullable>
    <isActive>true</isActive>
    <isMandatory>true</isMandatory>
    <position>1</position>
    <datatype>
      <Facet><value>9</value><type>totalDigits</type></Facet>
      <nativeDatatype>3</nativeDatatype>
      <name>tcmcs.long</name>
    </datatype>
    <type>simple</type>
    <name>btno</name>
  </Column>

  <!-- String Column with min/maxLength -->
  <Column>
    <descriptionReference>txtxcmg011.cdec</descriptionReference>
    <description>Description</description>
    <isNullable>true</isNullable>
    <isActive>true</isActive>
    <isMandatory>false</isMandatory>
    <position>2</position>
    <datatype>
      <Facet><value>30</value><type>maxLength</type></Facet>
      <Facet><value>1</value><type>minLength</type></Facet>
      <nativeDatatype>6</nativeDatatype>
      <name>tcdsca</name>
    </datatype>
    <type>simple</type>
    <name>cdec</name>
  </Column>

  <!-- Date Column -->
  <Column>
    <descriptionReference>txtxcmg011.bild</descriptionReference>
    <description>Billing Date</description>
    <isNullable>true</isNullable>
    <isActive>true</isActive>
    <isMandatory>false</isMandatory>
    <position>3</position>
    <datatype>
      <Facet><value>Date</value><type>DateFacet</type></Facet>
      <nativeDatatype>9</nativeDatatype>
      <name>tfgld.date</name>
    </datatype>
    <type>simple</type>
    <name>bild</name>
  </Column>

  <!-- Numeric / Amount Column with fractionDigits -->
  <Column>
    <descriptionReference>txtxcmg011.tamt</descriptionReference>
    <description>Total Amount</description>
    <isNullable>true</isNullable>
    <isActive>true</isActive>
    <isMandatory>false</isMandatory>
    <position>4</position>
    <datatype>
      <Facet><value>15</value><type>totalDigits</type></Facet>
      <Facet><value>2</value><type>fractionDigits</type></Facet>
      <nativeDatatype>5</nativeDatatype>
      <name>tcamnt</name>
    </datatype>
    <type>simple</type>
    <name>tamt</name>
  </Column>

  <!-- Embedded DAL 2 Script -->
  <DR_Module>
    <description>Billing Batch Header</description>
    <versionID>B61O_a_ext</versionID>
    <type>library</type>
    <name>txcmg011</name>
    <Source>
      <expression>| DAL 2 script content here...</expression>
      <expressionLanguageType>Baan4C</expressionLanguageType>
      <sourceType>12</sourceType>
      <sourceDescription>Billing Batch Header</sourceDescription>
      <sourceName>txcmg011</sourceName>
    </Source>
    <application>EXTce01107</application>
  </DR_Module>

  <application>EXTce01107</application>
</DR_Table>
```

---

## 2. Domain Schema (`.dmn`)

Root element is `<DR_Domain>`.
Ecore native datatype codes:
- `1` = Byte
- `2` = Double / Float
- `3` = Long / Integer
- `5` = Numeric / Amount
- `6` = String
- `7` = Enum / Boolean
- `9` = Date
- `14` = UTC DateTime

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Domain xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Remarks</description>
  <versionID>B61O_a_ext</versionID>
  <type>domain</type>
  <name>txcmg.remk</name>
  <descriptionReference>txcmg.remk</descriptionReference>
  <nativeDatatype>6</nativeDatatype>
  <Facet>
    <value>100</value>
    <type>maxLength</type>
  </Facet>
  <Facet>
    <value>1</value>
    <type>minLength</type>
  </Facet>
  <application>EXTce01107</application>
</DR_Domain>
```

---

## 3. Label Schema (`.lbl`)

Root element is `<DR_Label>`. Language `2` is standard English:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Label xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Remarks</description>
  <versionID>B61O_a_ext</versionID>
  <type>label</type>
  <name>txcmg.remk</name>
  <helpText>Billing Remarks</helpText>
  <language>2</language>
  <length>30</length>
  <application>EXTce01107</application>
</DR_Label>
```

---

## 4. Session Schema (`.ses` / `<DR_Controller>`)

Root element is `<DR_Controller>`. Supports:
- Single-occurrence / List / Details (`windowType`: `1` for Details, `2` for Multi-occurrence Overview)
- MMT Controllers (`type`: `mmt_controller`, with `<ControllerSatelliteRelationship>`)
- Form Commands (`<FormCommand>` declaring standard or custom user choices)
- Form Groups (`<FormGroup>` building the visual group tree)

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Controller xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Batch MMT Controller</description>
  <versionID>B61O_a_ext</versionID>
  <type>session</type>
  <name>txcmg0110m100</name>
  <descriptionReference>txcmg0110m100</descriptionReference>
  <windowType>2</windowType>

  <!-- Controller Table Relationship -->
  <ControllerTableRelationship>
    <showView>false</showView>
    <dynIndexSwitching>1</dynIndexSwitching>
    <toTable>txcmg011</toTable>
    <position>1</position>
    <descriptionReference>txcmg011</descriptionReference>
    <description>Billing Batch Header</description>
    <name>txcmg011</name>
  </ControllerTableRelationship>

  <!-- Satellite Sessions for MMT -->
  <ControllerSatelliteRelationship>
    <name>txcmg0510m000</name>
    <description>Billing Batch Lines</description>
    <satellite>txcmg0510m000</satellite>
    <position>1</position>
  </ControllerSatelliteRelationship>

  <!-- Form Commands -->
  <FormCommand>
    <name>exec.user.0</name>
    <function>generate.billing</function>
    <descriptionReference>txcmg0110m100.cmd1</descriptionReference>
    <description>Generate Billing</description>
    <commandType>1</commandType>
    <position>10</position>
  </FormCommand>

  <!-- Form Group Tree -->
  <Form>
    <FormGroup>
      <groupNumber>1</groupNumber>
      <parentGroup>0</parentGroup>
      <firstChildGroup>2</firstChildGroup>
      <nextGroup>0</nextGroup>
      <previousGroup>0</previousGroup>
      <name>Main</name>
    </FormGroup>
    <FormGroup>
      <groupNumber>2</groupNumber>
      <parentGroup>1</parentGroup>
      <firstChildGroup>0</firstChildGroup>
      <nextGroup>0</nextGroup>
      <previousGroup>0</previousGroup>
      <name>HeaderGroup</name>
      <FormField>
        <fieldName>txcmg011.btno</fieldName>
        <fieldLabel>txtxcmg011.btno</fieldLabel>
        <position>10</position>
      </FormField>
    </FormGroup>
  </Form>

  <!-- Embedded UI Script -->
  <DR_Module>
    <name>txcmg0110m100</name>
    <Source>
      <expression>| UI 4GL script content here...</expression>
      <sourceType>4</sourceType>
    </Source>
  </DR_Module>

  <application>EXTce01107</application>
</DR_Controller>
```

---

## 5. Library Schema (`.lib`)

Root element is `<DR_Module>`.
Source types:
- General DLL: `sourceType=6` in `<pkg>/library/<mod>/`
- Session Extension (`ess`): `sourceType=8` in `<pkg>/library/ess/`
- Table Extension (`est`): `sourceType=6` in `<pkg>/library/est/`

Table Extension seeding official `#context_on` / `#context_off` blocks:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Module xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Table Extension for whinh312</description>
  <versionID>B61O_a_ext</versionID>
  <type>library</type>
  <name>txestwhinh312</name>
  <Source>
    <expression><![CDATA[
| Hook declarations
#context_on "declarations"
table twhltc100
#context_off

table twhinh312
#include <bic_dal2>
#include <bic_tableext>

| Hook functions
#context_on "functions"
#context_off

| Hook method.is.allowed
#context_on "method.is.allowed"
function extern boolean method.is.allowed(long method)
{
	on case method
	case DAL_NEW:
		break
	endcase
	return(true)
}
#context_off
]]></expression>
    <sourceType>6</sourceType>
    <sourceName>txestwhinh312</sourceName>
  </Source>
  <application>EXTce01107</application>
</DR_Module>
```

---

## 6. Menu Schema (`.mnu`)

Root element is `<DR_Menu>`.
`<MenuChoice>` defines entries (`menuFieldType`: `1` for session, `2` for submenu):

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Menu xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Enhancements</description>
  <versionID>B61O_a_ext</versionID>
  <type>menu</type>
  <name>txgld0000m001</name>
  <MenuChoice>
    <descriptionReference/>
    <description>Withholding Tax Parameter</description>
    <initialHidden>false</initialHidden>
    <filterFunction/><filterLibrary/>
    <isActive>true</isActive>
    <processInfo/>
    <menuFieldName>txcmg9000m000</menuFieldName>
    <menuFieldType>1</menuFieldType>
    <descriptionIsLinked>true</descriptionIsLinked>
    <position>10</position>
  </MenuChoice>
  <application>EXTce01107</application>
</DR_Menu>
```

---

## 7. Report Schema (`.rpt`, `.rptdsrc`)

Root element is `<DR_Report>`. Contains `<InputField>`, `<Layout>`, `<PhysicalReportLayout>` (with base64 `<ReportLayoutText>`), `<ReportOutputField>`, `<ReportSpecial>`, `<PageSetup>`, and 4GL report `<Source>`:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Report xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Batch Summary Report</description>
  <versionID>B61O_a_ext</versionID>
  <type>report</type>
  <name>txcmg04010100</name>
  <Version>
    <ObjectID/><classID/><checkInLabel/><documentation/>
    <isExpired>no</isExpired>
    <isCheckedOutParallel>no</isCheckedOutParallel>
    <isCheckedOut>no</isCheckedOut>
    <modificationDateTime>2026-10-27T05:00:00Z</modificationDateTime>
    <modifiedBy>agent</modifiedBy>
    <creationDateTime>2026-10-27T05:00:00Z</creationDateTime>
    <createdBy>agent</createdBy>
  </Version>
  <descriptionReference>txcmg04010100</descriptionReference>
  <Attachment><type>relnotes</type><name>txcmg04010100</name></Attachment>
  <Attachment><type>techdoc</type><name>txcmg04010100</name></Attachment>
  <language>2</language>

  <InputField>
    <isTableField>false</isTableField>
    <sortSequence>1</sortSequence>
    <sortMode>1</sortMode>
    <datatype>
      <Facet><value>9</value><type>totalDigits</type></Facet>
      <nativeDatatype>3</nativeDatatype>
      <name>tcmcs.long</name>
    </datatype>
    <fieldname>btno</fieldname>
    <name>btno</name>
  </InputField>

  <Layout>
    <type>4</type>
    <sequenceNumber>1</sequenceNumber>
    <PhysicalReportLayout>
      <ReportLayoutText>AQgBjDoBEwGMWwEZAYwsAR4BjF0BSwGMOgJLAYs6/yAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA=</ReportLayoutText>
      <width>80</width>
      <height>2</height>
      <ReportOutputField>
        <printCondition/>
        <suppressEmptyField>false</suppressEmptyField>
        <printExpression>btno</printExpression>
        <row>1</row>
        <column>1</column>
        <length>9</length>
        <datatype>
          <Facet><value>9</value><type>totalDigits</type></Facet>
          <nativeDatatype>3</nativeDatatype>
          <name>tcmcs.long</name>
        </datatype>
      </ReportOutputField>
    </PhysicalReportLayout>
  </Layout>

  <PageSetup>
    <paperWidth>80</paperWidth>
    <pageLength>66</pageLength>
    <linesPerPage>60</linesPerPage>
  </PageSetup>

  <Source>
    <expression><![CDATA[
before.program:
	| Report initialization
detail.1:
	layout.1()
]]></expression>
    <sourceType>7</sourceType>
    <sourceName>txcmg04010100</sourceName>
  </Source>
  <application>EXTce01107</application>
</DR_Report>
```

---

## 8. Message Schema (`.msg`)

Root element is `<DR_Message>`. Defines runtime dialog and error messages with severity levels (`1`=Info, `2`=Warning, `3`=Error):

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Message xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Batch Closed</description>
  <versionID>B61O_a_ext</versionID>
  <type>message</type>
  <name>txcmg0001</name>
  <descriptionReference>txcmg0001</descriptionReference>
  <messageCode>txcmg0001</messageCode>
  <severity>3</severity>
  <text>Billing batch %1$s has already been finalized and cannot be modified.</text>
  <application>EXTce01107</application>
</DR_Message>
```

---

## 9. Question Schema (`.qst`, `.que`)

Root element is `<DR_Question>`. Defines interactive user prompt dialogs with question text, domain, and default answer:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Question xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Confirm Batch Finalization</description>
  <versionID>B61O_a_ext</versionID>
  <type>question</type>
  <name>txcmg0002</name>
  <descriptionReference>txcmg0002</descriptionReference>
  <questionCode>txcmg0002</questionCode>
  <severity>2</severity>
  <domain>tcyesno</domain>
  <defaultAnswer>yes</defaultAnswer>
  <text>Do you want to finalize billing batch %1$s now?</text>
  <application>EXTce01107</application>
</DR_Question>
```

---

## 10. Include Function Schema (`.fnc`, `.fun`)

Root element is `<DR_Module>` with `<type>function</type>`. Represents reusable 4GL include function source definitions:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Module xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Tax Calculation Function</description>
  <versionID>B61O_a_ext</versionID>
  <type>function</type>
  <name>txcmgf001</name>
  <Source>
    <expression><![CDATA[
function extern double txcmgf001.calculate_tax(double amount, double rate)
{
	return(amount * (rate / 100.0))
}
]]></expression>
    <sourceType>8</sourceType>
    <sourceName>txcmgf001</sourceName>
  </Source>
  <application>EXTce01107</application>
</DR_Module>
```

---

## 11. Additional File Schema (`.add`)

Root element is `<DR_AdditionalFile>`. Represents non-4GL configuration, schema, or asset files packaged in activities:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_AdditionalFile xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <description>Billing Configuration JSON</description>
  <versionID>B61O_a_ext</versionID>
  <type>additional_file</type>
  <name>txcmgcfg</name>
  <keyword1>billing</keyword1>
  <keyword2>config</keyword2>
  <keyword3>tax</keyword3>
  <content><![CDATA[{"taxRate": 7.0, "currency": "THB", "autoFinalize": true}]]></content>
  <application>EXTce01107</application>
</DR_AdditionalFile>
```
