# Infor LN Studio Component XML Schema Reference

This reference documents the XML tag structures required by Infor LN Studio 10.8 for tables (`.tbl`), sessions (`.ses`), domains (`.dmn`), and labels (`.lbl`).

---

## 1. Table Schema (`.tbl`)

The root element is `<DR_Table>`:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<DR_Table>
  <description>Inspection Skipping Method</description>
  <versionID>B61O_a_ext</versionID>
  <type>table</type>
  <name>txptc100</name>
  <Version>
    <ObjectID/><classID/><checkInLabel/><documentation/>
    <isExpired>no</isExpired>
    <isCheckedOutParallel>no</isCheckedOutParallel>
    <isCheckedOut>no</isCheckedOut>
    <modificationDateTime>2026-08-14T10:50:50Z</modificationDateTime>
    <modifiedBy>agent</modifiedBy>
    <creationDateTime>2026-08-14T10:50:50Z</creationDateTime>
    <createdBy>agent</createdBy>
  </Version>
  <descriptionReference>txptc100</descriptionReference>
  <Attachment><type>relnotes</type><name>txptc100</name></Attachment>
  <Attachment><type>techdoc</type><name>txptc100</name></Attachment>

  <!-- Indices -->
  <Index>
    <descriptionReference>txptc10001</descriptionReference>
    <description>Seq.</description>
    <IndexColumn>
      <sortingOrder>asc</sortingOrder>
      <column>seqn</column>
      <position>1</position>
    </IndexColumn>
    <isActive>true</isActive>
    <isPrimaryKey>true</isPrimaryKey>
    <isUnique>true</isUnique>
    <name>1</name>
  </Index>

  <!-- Table Relationships -->
  <TableRelationship>
    <companyField/>
    <toTable>tcmcs060</toTable>
    <TableRelationshipColumn>
      <to>cmnf</to>
      <from>cmnf</from>
    </TableRelationshipColumn>
    <deleteRule>cascade</deleteRule>
    <updateRule>cascade</updateRule>
    <referentialIntegrityCheck>true</referentialIntegrityCheck>
    <multiplicity>oneToOne</multiplicity>
    <type>association</type>
    <name>tcmcs060</name>
  </TableRelationship>

  <!-- Columns -->
  <Column>
    <descriptionReference>txtxptc100.seqn</descriptionReference>
    <description>Seq.</description>
    <additionalInstructions>columnDepth:0</additionalInstructions>
    <isNullable>true</isNullable>
    <isActive>true</isActive>
    <isMandatory>true</isMandatory>
    <defaultValue>$__unique</defaultValue>
    <position>1</position>
    <datatype>
      <Facet><value>6</value><type>maxLength</type></Facet>
      <Facet><value>1</value><type>minLength</type></Facet>
      <nativeDatatype>3</nativeDatatype>
      <name>tcpono</name>
    </datatype>
    <type>simple</type>
    <name>seqn</name>
  </Column>

  <!-- Embedded DAL -->
  <DR_Module>
    <description>Inspection Skipping Method</description>
    <versionID>B61O_a_ext</versionID>
    <type>library</type>
    <name>txptc100</name>
    <Source>
      <expression>| 4GL DAL Code here...</expression>
      <expressionLanguageType>Baan4C</expressionLanguageType>
      <sourceType>12</sourceType>
      <sourceDescription>Inspection Skipping Method</sourceDescription>
      <sourceName>txptc100</sourceName>
    </Source>
    <application>EXTce01105</application>
  </DR_Module>

  <application>EXTce01105</application>
</DR_Table>
```

---

## 2. Session Schema (`.ses`)

The root element is `<DR_Controller>`:

- `<ControllerTableRelationship>`: Links the session to its primary table.
- `<StandardCommand>`: Enables or disables standard toolbar buttons (`def.find`, `first.set`, `add.set`, `update.db`, etc.).
- `<Form><PhysicalFormLayout>`: Defines dynamic form fields (`<FormField>`) and container groupings (`<FormGroup>`).
- `<DR_Module>`: Contains embedded UI script with `sourceType=1`.

---

## 3. Label Schema (`.lbl`)

Root element is `<DR_Label>`:

```xml
<DR_Label>
  <description>By Needed Quantity</description>
  <versionID>B61O_a_ext</versionID>
  <type>label</type>
  <name>txoutm010</name>
  <LabelVariant>
    <keyword>BY NEEDED</keyword>
    <isActive>1</isActive>
    <description>By Needed Quantity</description>
    <height>1</height>
    <length>18</length>
    <context>3</context>
    <language>2</language>
  </LabelVariant>
  <application>EXTce01105</application>
</DR_Label>
```

---

## 4. Domain Schema (`.dmn`)

Root element is `<DR_Domain>`:

- `<datatype><nativeDatatype>`:
  - `3`: Long / Integer
  - `6`: String / Text
  - `7`: Enumeration
  - `14`: Date / Time
- `<Enumeration>`: List of enum constants with `<descriptionReference>`, `<description>`, `<name>`, and `<position>`.
