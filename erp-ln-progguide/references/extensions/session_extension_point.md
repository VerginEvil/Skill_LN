# Session extension point

A session extension is used to add fields and commands to the session screen. This applies both to overview screens (grids) and detail screens.

For example to:

- Add the number of Purchase Orders for a Business Partner on the BP overview.

- Show the current weather for a Service Order location.

- Link a new developed print session to an overview session.

- Link a new developed report to a print session.

Fields and commands that are added by the session extension are automatically visible in the session. With the form personalization options, fields can be moved to the desired location and commands can be added to the toolbar.

For the session extension point, these extension types are available:

- Session

- Table selection

- Secondary Table

- Standard Linked Report

- Custom Linked Report

- Customer Defined Field

- Standard Field

- Custom Field

- Calculated field

- Standard Command

- Standard Form Command

- Custom Form Command

- Standard Context Message

- Custom Context Message

- Event

Note: The extension types that are available for a session extension depend on the type of session.

This diagram shows the position of the session extension: Note on filtering: You can filter on fields that are added by Table Selections. You can also filter on Calculated Fields, except the ones that are calculated with Expression Type “Function”.

## Session

With the properties and hooks that are defined for the extension type Session, you can change the behavior of the session.

This table shows the available properties:

Name

Include CDFs of Used Referenced Tables

This table shows the available hooks:

Name Signature

Declarations

Functions Before Context Send `void before.context.send(long i.msgs.node)` Session Extension LN Screen 4GL LN tables engine Session LN tables
4GL engine
LN Session
Session Extension
Screen

## Include CDFs of Used Referenced Tables property

If you select this property, all CDFs of tables, of which already fields are used in the session screen, are added to the form with the initial hidden state. With Personalize Form you can make those fields visible on the screen.

By default, this property is selected when you add a Session extension. Including CDFs of used referenced tables was the default behavior in Enterprise Server 10.4.1. If you clear the property check box, you can select the required individual CDFs at table level (in the Table Selection).

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension. Also, the references to include files and DLLs that are used by the extension must be coded in this hook with `#include` and `#pragma`.

Tables that are selected in the extension type Table Selection are implicitly declared, so they do not have to be added to this hook.

Example:

```baan
#include        <bic_text>
table   txprc100          |* Prices
string  date.string(14)
boolean retb
#pragma used dll "otxprcdll0001"
```

## Functions hook

Use this hook to code (common) functions to use in the other hooks of the session extension. This helps you in reusing code and to keep the other hooks small and clear.

Example:

```baan
function string format.date(long i.date)
{
return(utc.to.iso(i.date, UTC_ISO_DIFF))
}
```

## Before Context Send Hook

Use this hook to make changes to the context messages, before the message is sent through LN UI to Infor OS Portal or Infor Ming.le.

For more information about InContext messaging, see the Infor Enterprise Server InContext Modeling Development Guide. We recommend that you use the `After Mappings` hook of the individual context message, but use the `Before` `Context Send` hook in these cases:

- If you must make changes based on multiple context messages in the context.

- Infor LN does not have a template. To add a complete new message for which standard

The input argument of this hook is an XML node with the messages that are built by the standard session. Example XML:

```baan
<masterNode>
<message id="com.infor.ln.businesscontext" name="inforBusinessContext">
<entities>
<entityType>company</entityType>
<id1>1910</id1>
<visible>false</visible>
<readonly>true</readonly>
</entities>
<screenId>ln_tccom4500m000</screenId>
<logicalId>lid://infor.ln.701</logicalId>
<contextId>102320113837_33032_20</contextId>
<entities INFOR_CONTEXT_ARRAY="true">
<entityType>InforERPEnterpriseCommonInternalBusinessPartner</entityType>
<id1>TDCUS0016</id1>
<name>Acme Construction</name>
<readonly>false</readonly>
<accountingEntity>infor.ln.1910</accountingEntity>
<drillbackURL>?LogicalId=lid://infor.ln.701&amp;ICMDrillback=true&amp;Session=tccom4100s000&amp;Ses
sionIndex=1&amp;Filter=VERDVVMwMDE2&amp;Enc=1&amp;Mode=64</drillbackURL>
<visible>true</visible>
<lnTable>tccom100</lnTable>
</entities>
</message>
</masterNode>
```

How to investigate this XML, see Steps to investigate XML on page 68.

The example earlier has this equivalent in JSON:

```baan
{
"type": "inforBusinessContext",
"data": {
"screenId": "ln_tccom4500m000",
"logicalId": "lid://infor.ln.701",
"entities": [
{
"visible": false,
"readonly": true,
"entityType": "company",
"id1": 1910
},
{
"accountingEntity": "infor.ln.1910",
"visible": true,
"readonly": false,
"entityType": "InforERPEnterpriseCommonInternalBusinessPartner",
"id1": "TDCUS0016",
"name": "Acme Construction",
"drillbackURL": "?LogicalId=lid://infor.ln.701&ICMDrillback=true&Session=tccom4100s000&Ses
sionIndex=1&Filter=VERDVVMwMDE2&Enc=1&Mode=64",
"lnTable": "tccom100"
}
],
"contextId": "102320113837_33032_20"
}
}
```

An example to send an additional context message, in case you have a contextual application that listens to this message:

```baan
function extern void before.context.send(long i.msgs.node)
{
long    new.message
new.message = xmlNewNode("message", XML_ELEMENT, i.msgs.node)
xmlSetAttribute(new.message, "id", "com.acme.my.message")
xmlSetAttribute(new.message, "name", "acmeMyMessage")
xmlNewDataElement("user", logname$, new.message)
xmlNewDataElement("businessPartner", tccom100.bpid, new.message)
}
```

When this hook is executed, the values of (key) fields that are used to build up the standard part of the context message, are available. You can explore those fields by selecting the Standard Context Message extension type in the Extension Modeler and viewing the mapping. Ensure to delete that extension type again if you do not extend that particular message. You can use the available (key) fields to read additional data from the database, if required.

### Steps to investigate XML

To investigate the XML that is created by the session for which to change the context messages that must be sent:

1 Create the session extension. 2 Implement the `Before Context Send` hook. No additional code is required in the hook at this stage 3 Save the extension. 4 Start the Debugger from the Extensions (ttext1500m000) session for your session extension. 5 Add a breakpoint before “ `function extern void before.context.send(long i.msgs.node)` ” 6 Start the session and select a record. 7 The Debugger suspends in the `Before Context Send` hook. 8 Inspect the `i.msgs.node` variable.

Note: This XML is translated to JSON before it is sent to Infor OS Portal or Infor Ming.le. The Infor OS Portal context widgets or the Infor Ming.le contextual applications receive those JSON messages.

## Table Selection

Note: A Table Selection extension type is only possible for sessions of type `Display` and `Maintain`.

With the properties and hooks that are defined for the extension type Table Selection, you can include fields from the selected table. The included fields are displayed and read-only.

When you add a Table Selection, you have two options:

- Referenced Table

- Other Table

If you choose Referenced Table, you can select tables that are linked to the main table of the session. This can be a multilevel reference. For example, for a Business Partner, you can make a reference to the Language of the Country of the Address of the Business Partner.

You can select the same Referenced Table multiple times, but only if the reference path to that table is different. For example, you can reference to a Language from the Business Partner directly, but also by the Country of the Address of the Business Partner. In this case, automatically a new Sequence Number is assigned to the Table Selection.

If you choose Other Table, you can select any other table. In this case, you must specify the query part to join with this table yourself. Note that this is always handled as an inner join. Ensure that the record in the other table exists, otherwise the record of the main table is not displayed. If you cannot ensure that the record in the other table exists, do not use the Table Selection. Use a Calculated Field with the Nested Select option.

See Select property on page 86.

This table shows the available properties:

Name

Field List

Reference Type

Reference Path

Where Clause

## Field List property

The Field List property specifies the table fields to be displayed in the session. Click Details in the property value cell to get the list of available fields and select the ones to be displayed on the session’s screen.

You can leave the Field List blank, to add the Table Selection to be able to use the table fields in the expression for a Calculated Field.

See Table property on page 84.

## Reference Type property

This is a read-only property that indicates the reference type that is generated in the query of the session. For a Reference Table the property is `Refers`, for an Other Table it is `Where`.

## Reference Path property

This is a read-only property that shows the reference path to the table in the Table Selection of type Referenced Table. The starting point is the main table of the session; the end point is the table in the Table Selection. Click Details to see the detailed information of the reference path.

## Where Clause property

The Where Clause property can only be filled for Table Selections of type Other Table. This where clause is added to the query of the session to join the data. Click Details to specify the where clause in the window.

Example: `txprc001.pcod = tcibd001.cdf_pcod`

This example shows how data from another table is joined to the main table `tcibd001`. As described earlier, ensure that the data in the joined table exists, otherwise the record of the main table is not visible in the session.

Note: In the Where Clause you cannot use form fields.

## Secondary Table

Note: A Secondary Table extension type is used to refer to:

- Additional extension fields in an own extension table.

- Additional existing application fields in an extension session.

Use a Secondary Table extension type to maintain more tables in one view. You can add 20 secondary tables to a session.

This table shows the available properties with an example:

| Property | Example value | Explanation |
|---|---|---|
| Name | txest100 | Purchase Order extension table |
| Description | Purchase Order Extension |  |
| Field List | buyr,  badr | List of extension update fields. Here, buyer and buyer address. |
| Mapping List | otad<-->cadr | The link from the main table to the extension table. |

Here, the link from the buy-from address to the address code.

| Property | Example value | Explanation |
|---|---|---|
| Initially hidden in overview Cleared |  | By default not displayed in the overview session. |
| Initially hidden in detail | Selected | By default displayed in the detail session. |

Once the extension is activated, the fields will be available in the session and you can move them to the desired location by clicking Personalization > Personalize Form. The fields are then ready for input, taking into account the defined DAL functionality.

The same functionality is available through the function `sec.add.set.by.name()` in `before.program`. The function can be used in an extension session in combination with adding the secondary table fields to the form. The function cannot be used to extend an existing application session.

## Standard Linked Report

Use a Standard Linked Report extension type to code remove (conditionally) the report from the session.

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean <report>.is.visible()` |

## Is visible hook

Use this hook to remove standard linked reports from the session.

This hook can use actual values of the form fields. The availability of a certain report depends on the options chosen in the form.

Example:

```baan
function extern boolean tcibd040111000.is.visible()
{
if ext.details = tcyesno.yes then
return(true)
else
return(false)
endif
}
```

## Custom Linked Report

Use a Custom Linked Report extension type to add a report to a session.

For example, to add a report, you created in the `tx` package to print item data in a completely different layout.

These are the available properties:

- Report Group

- Sequence

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | boolean <report>.is.visible() |

## Report Group property

This property is used to set the report group to which the custom linked report must belong. At runtime the user must select which report from the report group must be printed. If the session does not have different report groups,you must add the report to the existing group. You can check this in the session definition to which you link the custom report. You cannot add report groups in the extension.

## Sequence property

This property is used to set the sequence of the report within the report group.

## Is Visible hook

This hook is used to conditionally add the custom linked report. This hook can use the actual values of the form fields. The availability of a report depends on the options selected in the form.

Example:

```baan
function extern boolean txcpr040111000.is.visible()
{
if ext.details = tcyesno.yes then
return(true)
else
return(false)
endif
}
```

## Customer Defined Field

Note: A Customer Defined Field extension type is only possible for sessions of type Display and Maintain.

Use a Customer Defined Field extension type in these cases:

- To link a zoom session to the CDF. Zooming is not possible for CDFs of type List.

- To control the input of a CDF.

Example:

- You have a custom table with Colors and want to zoom to the Colors session for a CDF in the Items table.

- You do not want to copy the CDF value of the previous record during the addition of a new record.

This table shows the available hooks:

| Name | Signature |
|---|---|
| Get Zoom Session | `string <CDF name>.get.zoom.session()` |
| Get Zoom Return Field | `string <CDF         name>.get.zoom.return.field()` |
| Selection Filter | `void <CDF name>.selection.filter()` |
| Before Zoom | `void <CDF name>.before.zoom()` |
| After Zoom | `void <CDF name>.after.zoom()` |
| Before Input | `void <CDF name>.before.input()` |

## Get Zoom Session hook

Use this hook to specify the zoom session for the customer defined field. To use a zoom session for a CDF, you must implement the Get Zoom Return Field hook.

Example:

```baan
function extern string tcibd001.cdf_colr.get.zoom.session()
{
return("txcom1500m000")
}
```

Note: This hook is called after the form is loaded in the session. If the zoom session depends on the data in the session, use this hook only to set the default zoom session. The specific zoom session based on the data must be set in the Before Zoom hook.

## Get Zoom Return Field hook

Specify the field that must be returned of the selected record in the zoom session and specified in the customer defined field. It must be one of the fields that are shown in the zoom session.

Example:

```baan
function extern string tcibd001.cdf_colr.get.zoom.return.field()
{
return("txcom100.colr")
}
```

Note: This hook is called after the form is loaded in the session. If the zoom return field depends on the data in the session, use this hook only to set the default zoom return field. The specific zoom return field that is based on the data must be set in the Before Zoom hook.

## Selection Filter hook

Use this hook to specify the query extension to filter the records that are shown in the zoom session.

Example:

```baan
function extern void tcibd001.cdf_colr.selection.filter()
{
on case tcibd001.citg
case "001":
query.extend.where.in.zoom("txcom100.ctyp = txctyp.hard")
break
case "002":
query.extend.where.in.zoom("txcom100.ctyp = txctyp.soft")
break
default:
|* no filter
endcase
}
```

## Before Zoom hook

Use this hook to instruct the zoom session to adapt its behavior. For example, the index the session should use or the record that should be shown as the first one. In the latter case, you must specify the key of that record. Note that standard sessions may not always show the desired behavior because of specific implementations.

Examples:

```baan
function extern void tcibd001.cdf_prbp.before.zoom()
{
attr.zoomindex = 2
}
function extern void tcibd001.cdf_prbp.before.zoom()
{
tccom100.bpid = tcibd001.cdf_prbp
}
function extern void tcibd001.cdf_prbp.before.zoom()
{
on case tcibd001.cdf_bunt
case txbunt.cons:
attr.zoomsession$ = "txcpr0501m000"
attr.zoomreturn$ = "txcpr001.prid"
break
case txbunt.b2b:
attr.zoomsession$ = "txcpr0502m000"
attr.zoomreturn$ = "txcpr002.prid"
break
default:
attr.zoomcode = 0
endcase
}
```

## After Zoom hook

Use this hook to react on the chosen entry in the zoom session.

Example:

```baan
function extern void tirou102.cdf_aitm.after.zoom()
{
if isspace(tirou102.cdf_aitm(1;9)) then
tirou102.cdf_aitm = tirou102.cdf_aitm(10)
endif
}
```

## Before Input hook

Use this hook to influence the standard behavior for input fields by setting predefined variables.

Examples:

```baan
function extern void tcibd001.cdf_prbp.before.input()
{
attr.dorp = DORP.DEFAULT
}
```

## Standard Field

Note: A Standard Field extension type is only valid for sessions of type `Print`, `Update` and `Update_print`.

Use a Standard Field extension type if additional validations of updating of related fields are required in the session’s screen.

Examples:

- If an option is selected, another option must be cleared automatically.

- To prevent a session running for a range. This table shows the available hooks:

| Name | Signature |
|---|---|
| When Field Changes | `void <field         name>.when.field.changes()` |
| Check Input | `void <field name>.check.input()` |

## When Field Changes hook

Use this hook to react on a change in a field. You can use and set the values of the form fields.

Note: To have the standard fields available for the hooks ensure you have at least Enterprise Server version 10.5.2 with KB 1923135 applied.

Example:

```baan
function extern void currency.when.field.changes()
{
if currency = "EUR" then
prnt.sellpr = tcyesno.yes
else
prnt.sellpr = tcyesno.no
endif
display("prnt.sellpr")
}
```

## Check Input hook

Use this hook to validate a field. You can use and set the values of the form fields. You can only use this hook to set additional restrictions on a field. The standard validations are also applied.

Example:

```baan
function extern void currency.check.input()
{
if txcomdll0001.is.currency.blocked.for.printing(currency) then
set.input.error("@" &
sprintf$("You cannot select currency %s; it is blocked",
currency))
endif
}
```

## Custom Field

A Custom Field extension type is only valid for sessions of these types:

- Print

- Update

- Update_print.

Use a Custom Field extension type if you must specify additional input on the session’s screen. A Custom Field can be inherited from a process extension or a new Custom Field can be specified in the session extension. The latter type of Custom Fields are applicable only in combination with a report extension. In the report extension you can import those Custom Fields, so that they are available as report input fields. In the report design you can filter on those fields.

Standard LN sessions can have the option to skip records based on conditions programmed in process extensions. In that case the Custom Fields are inherited from the process extension. You can use the Custom Field hooks to define the UI behavior of the fields.

This table shows the available properties:

Name

Name

Label

Description

Display Length

Domain

Process Type

Process Name

Is Mandatory

This table shows the available hooks:

| Name | Signature |
|---|---|
| Calculate Initial Value | `void <field name>.                 calculate.d` `efault.value()` |
| When Field Changes | `void <field name>.when.field.changes()` |
| Check Input | `void <field name>.check.input()` |
| Is Read-only | `boolean <field name>.is.readonly()` |
| Get Zoom Session | `string <field name>.get.zoom.session()` |
| Get Zoom Return Field | `string <field                 name>.get.zoom.r` `eturn.field()` |
| Selection Filter | `void <field name>.selection.filter()` |
| Before Zoom | `void <field name>.before.zoom()` |
| After Zoom | `void <field name>.after.zoom()` |

## Name property

The Name property is used for the variable name.

The property is prefixed with `ext.`. The maximum length of a variable name is 17, including the prefix. Use this variable name as the name in the hooks.

## Label property

Use this property if the field description must be displayed in different languages.

You can select an existing label or create a new label in the Extensions package. A label can have descriptions in different languages and multiple length variants. See the Infor LN Studio Application Development Guide.

See the Infor LN Studio Application Development Guide

The Label property cannot be filled if the Description property is used.

## Description property

The Description is displayed before the field.

If the descriptions must be available in multiple languages, based on user language, do not use the Description property. Link a label to the field with the Label property. The Description property cannot be specified if the Label property is used.

## Domain property

The Domain property is required to define the data type of the Custom Field.

You can select an existing domain or create a new domain in the Extensions package. The Domain property is read only for Custom Fields that are inherited from a process extension.

See the Infor LN Studio Application Development Guide

## Display Length property

Use this property to limit the display length of the field.

If you do not specify this property, the field is created on the screen with the length of the domain.

## Is Mandatory property

Use this property to indicate that the user must provide a value in this field.

Note: The check whether the field contains a value is executed when the user leaves the field. When the processing button is clicked, the field is only checked if the standard application calls the `check.all.input()` function. For screens without other fields to check, this call to `check.all.input()` can be absent. In that case you must extend the standard command or form command as well to call `check.all.input()` in the Before Command hook.

## Calculate Initial Value hook

Use this hook to set the initial value of the custom field. Note that this value is only applied if the form has no saved defaults for the current user.

Example:

```baan
function extern void ext.colr.t.calculate.default.value()
{
ext.colr.t = "ZZZZZZZZZZ"
}
```

## When Field Changes hook

Use this hook to react on a change in a field. You can use and set the values of the form fields.

Example:

```baan
function extern void ext.colr.f.when.field.changes()
{
ext.colr.t = ext.colr.f
display("ext.colr.t")
}
```

## Check Input hook

Use this hook to validate a custom field. You can use the values of the standard form fields and other custom fields.

Example:

```baan
function extern void ext.currency.check.input()
{
if txcomdll0001.is.currency.blocked.for.printing(ext.currency) then
set.input.error("@" &
sprint$("You cannot select currency %s; it is blocked",
ext.currency))
endif
}
```

## Is Read-only hook

Use this hook to set a custom field to read-only. This hook is executed only once at form initialization. To set a field read-only if other fields are changed, use the `When Field Changes` hook to set the custom field to read-only. You can use the `disable.fields()` function.

Example:

```baan
function extern boolean ext.currency.is.read.only()
{
return(txcomdll0001.is.currency.fixed(ext.currency))
}
```

## Get Zoom Session hook

Use this hook to specify the zoom session for the custom field. To use a zoom session, you must also implement the Get Zoom Return Field hook.

Example:

```baan
function extern string ext.colr.f.get.zoom.session()
{
return("txcpr0501m000") }
```

This hook is called after the form is loaded in the session. If the zoom session depends on the data in the session, use this hook to set the default zoom session. The specific zoom session that is based on the data must be set in the Before Zoom hook.

## Get Zoom Return Field hook

Use this hook to specify the field that must be returned of the selected record in the zoom session and specified in the custom field. It must be one of the fields that are shown in the zoom session.

Example:

```baan
function extern string ext.colr.f.get.zoom.return.field()
{
return("txcpr001.colr") }
```

This hook is called after the form is loaded in the session. If the zoom return field depends on the data in the session, use this hook to set the default zoom return field. The specific zoom return field that is based on the data must be set in the Before Zoom hook.

## Selection Filter hook

Use this hook to specify the query extension to filter the records that are shown in the zoom session.

Example:

```baan
function extern void ext.currency.selection.filter()
{
query.extend.where.in.zoom("tcmcs008.rapr = tcyesno.yes")
}
```

## Before Zoom hook

Use this hook to instruct the zoom session to adapt its behavior. For example, the index the session must use or the record that must be shown as the first one. In the latter case, you must specify the key of that record. Standard sessions do not always show the desired behavior because of specific implementations.

Examples:

```baan
function extern void ext.currency.before.zoom()
{
attr.zoomindex = 2
}
```

## After Zoom hook

Use this hook to react on the chosen entry in the zoom session.

Example:

```baan
function extern void ext.item.after.zoom()
{
if isspace(ext.item(1;9)) then
ext.item = ext.item(10)
endif
}
```

## Calculated Field

A Calculated Field extension type is only valid for sessions of type `Display` and `Maintain`.

Use a Calculated Field extension type if additional fields are required in the session’s screen. The added fields are always displayed as read-only.

Examples:

- Aggregations of table fields (average, sum, etc.)

- Fields of tables that cannot be joined, because the record to join might not exist.

- Results of calculations with standard main table fields or fields that are made available with the Table Selections.

- Results of called library functions.

- Graphs representing additional information that is related to the session’s data.

This table shows the available properties:

Name

Name

Label

Description

Control Type

Display Height

Display Length

View Field

Domain

Elements

Table

Expression Type

Simple Expression

Select

From

Where

This table shows the available hooks:

| Name | Signature |
|---|---|
| Calculate Value | `void <name>.calculate()` |

The Calculate Value hook is only available for Calculated Fields with Expression Type `Function`:

## Name property

The Name property is used for the variable name. It is always prefixed with `ext.`. The maximum length of a variable name is 17, including the prefix. This variable name is the name to be used in the Calculate Value hook.

## Label property

Use this property if the field description must be displayed in different languages. You can select an existing label, or create a new label in the Extensions package. A label can have descriptions in different languages and multiple length variants.

See the Infor LN Studio Application Development Guide.

The Label property cannot be filled if the Description property is used.

## Description property

The Description is displayed as column header in an overview session or before the field in a details session. If you require the descriptions in different languages (based on user language), do not use the Description property. Link a label to the field with the Label property.

The Description property cannot be specified the Label property is used.

## Control Type property

Select a Control Type to indicate the type of the Calculated Field.

This table shows the available Control Types:

| Control Type | Description |
|---|---|
| Normal | Use this Control Type to display the calculated value as a normal field. |

For a Normal field, you must specify the Domain property.

URL Area Use this Control Type if the calculated value is a URL and this URL must be em- bedded in the session. For a URL Area, use only Expression Type Function. URL Areas can be displayed only in MMT headers and detail sessions.

Picture Use this Control Type if the calculated value is a file name of a file containing a picture and this picture must be embedded in the session. For a Picture, use only Expression Type Function. Pictures can be displayed only in MMT headers and views of overview sessions. You can use static pictures or dynamic pictures, such as graphs, which you can generate in the Calculate Value hook. In case of static pictures you must make a copy to `${BSE}/tmp`. The static pictures are deleted by LN after it is shown.

## Display Heigth property

Use this property to specify the height of a URL Area or Picture.

This is the height in rows.

## Display Length property

Use this property to limit the display length of the field.

If you do not specify this property, the field is created on the screen with the length of the domain. For Calculated Fields of Control Type URL Area or Picture, it is also the width in characters. Space is reserved with a width of an average string with the given number of characters required.

## Domain property

The Domain property is required to define the data type of the Calculated Field with Control Type is Normal. You can select an existing domain or create a new domain in the Extensions package.

See the Infor LN Studio Application Development Guide.

## Elements property

Use the Elements property if more than one occurrence for the field is required.

The field becomes an array field. The default value is 1, specify a higher value if more occurrences are required. Array fields must be of Control Type Normal. The Expression Type Function is supported only.

Click Details for the labels / descriptions for the different occurrences of the field.

## Table property

This property is a link to a Table Selection of which to use fields in a Simple Expression.

## Expression Type property

Select an Expression Type to indicate how the value of the Calculated Field must be determined:

This table shows the available Expression Types:

| Expression Type | Description |
|---|---|
| Simple Expression | Use this Expression Type if the table data is already available. The data is available if the used table fields in the Simple Expression are part of: |

- The main table of the session.

- A table that is linked with the Table property For a Simple Expression, you must fill the Simple Expression property.

Query Extension Use this Expression Type if the table data is not yet available but can be added to the session’s query as an inner join. The complete query extension (`Selec` `t`, `From` and `Where` properties) must be specified to determine the value of the Calculated Field. Use this Expression Type if you are sure the data read by the query extension exists. If you cannot be sure that the data exists, use the `Nested Select` Expression Type. You cannot use this Expression Type if you need aggregated values (`count`, `a` `verage`, etc.). For aggregations, you must use the `Nested Select` Expression Type.

| Nested Select | Use this Expression Type if the data is not yet available and an inner join is not possible, because the data may not be present. This Expression Type is also required for aggregations of table data. The complete query (`Select`, `F` `rom` and `Where`) must be coded in the `Select` property. |
|---|---|
| Function | Use this Expression Type if the calculation of the field cannot be expressed in a query. For example, a complex calculation or a web service call. Note that Calculated Fields with Expression Type “Function” are not enabled for (easy) filtering. |

## Simple Expression property

A Simple Expression computes a value with table fields that are available in the main table of the session or are part of a table. This is added to the session by a Table Selection.

Examples:

```baan
tccom100.bpid(1;3) & "-" & tccom100.clan
case tccom100.clan
when "ARA" then "Arabic"
when "NLD" then "Dutch"
else "Other"
end
```

See the SQL chapter in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

Note: In the Simple Expression, you cannot use form fields.

## Select property

Use the `Select` property for Expression Type `Query Extension` or `Nested Select` to define the fields to add to the standard session query.

Expression Type Query Extension

The `Select` property must contain one single field or an expression that results in one value.

Examples:

```baan
tcmcs046.dsca
case tcmcs046.clan
when "ARA" then "Arabic"
when "NLD" then "Dutch"
else "Other"
end
```

Expression Type Nested Select

The `Select` property must contain a complete query to determine the value of the calculated Field.

Examples:

```baan
select  count(*)
from    tdpur400
where   tdpur400.otbp = tccom100.bpid
select  txprc001.pric
from    txprc001
where   txprc001.item = tcibd001.item
```

Note: In the `Where` Clause of the `Nested Select` you cannot use form fields.

## From property

Use the `From` property to specify the tables to be used for an Expression Type `Query Extension`.

## Where property

Use the `Where` property to join the tables for an Expression Type `Query Extension`.

Note: In the `Where` Clause you cannot use form fields.

## Calculate Value hook

Use this hook to calculate the value for the calculated field. The value must be assigned to the variable with the name of the `Name` property. You must implement this hook for Expression Type `Function`.

In this hook all fields of the main table are available. Those fields can be found in the Table Definitions session (ttadv4520m000). Additionally, all selected fields from the Table Selections and the Calculated Fields with other Expression Types than `Function` are available. You cannot use other Calculated Fields with Expression Type `Function`, because the order in which the Calculate Value hooks are executed is arbitrary.

Example for a field with Control Type Normal, no array field:

```baan
function extern void ext.price.calculate()
{
txprcdll0001.calculate.price(
tcibd001.item,
tcmcs023.catg,
utc.num(),
ext.price)
}
```

Example for a field with Control Type Normal, array field:

```baan
function extern void ext.turnover.calculate(i.elem.number)
{
long month
month = i.elem.number
txprcdll0001.calculate.turnover(tcibd001.item, month,
ext.turnover(i.elem.number))
}
```

Example for a field with Control Type URL Area:

```baan
function extern void ext.url.calculate()
{
ext.url = "https://www.infor.com"
}
```

Example for a field with Control Type Picture, graph:

```baan
function extern void ext.graph.calculate()
{
long    ch, sr, cnt, ret
domain  tccwoc  office
ch = chart.new(CHART_TYPE_BAR)
chart.set.title(ch, "Orders by Sales Office")
chart.set.axis.type(ch, CHART_XAXIS, DB.STRING)
chart.set.axis.type(ch, CHART_YAXIS, DB.LONG)
sr = chart.add.series(ch, "Orders")
select  tdsls400.cofc:office,count(tdsls400.orno):cnt
from    tdsls400
group by tdsls400.cofc
order by tdsls400.cofc
selectdo
chart.add.data.point(sr, office, cnt)
endselect
ext.graph = creat.tmp.file$(bse.tmp.dir$())
ret = chart.write(ch, ext.graph, 400, 400)
}
```

Example for a field with Control Type Picture, the image stored on the file system in a custom location:

```baan
function extern void ext.item.image.calculate()
{
long    ret
string  image.file(256)
image.file = sprintf$(
"{BSE}/AppData/images/items/%s",trim$(tcibd001.item))
ext.item.image = creat.tmp.file$(bse.tmp.dir$())
ret = file.cp(image.file, ext.item.image)
}
```

Example for a field with Control Type Picture, the image that is linked to an existing Infor LN object. In this case a Business Partner:

```baan
function extern void ext.image.calculate()
{
long    ret
ext.image = creat.tmp.file$(bse.tmp.dir$())
|* Field tccom100.imag included by Table Selection
ret = copy.image.to.file(get.compnr(), tccom100.imag,
"tccom100", ext.image)
}
```

## Standard Command

Use a Standard Command extension type to code additional logic around a session’s standard command, such as `mark. delete`, `print`, `edit. text`, etc.

Examples:

- To prevent Excel Import in a session.

- To run an own session after a standard command is executed.

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean <command>.is.visible()` |
| Is Enabled | `boolean <command.is.enabled()` |
| Before Command | `void <command>.before.command()` |
| After Command | `void <command>.after.command()` |

Do not use the hooks of the session extension to influence the behavior of updating tables. We recommend that you use the table extension, for example the `Method Is Allowed` and `Before Save` hooks. In an overview session with multiple records, you must be aware that multiple records are selected. The values available in the selection are the ones of the last (un)selected record. If the command disabling/enabling depends on all selected records, you must iterate over the selected records.

## Is Visible hook

Use this hook to remove standard commands from the session. Depending on the standard command, the command can remain visible but disabled. This is the case when removing the command would change the standard toolbar.

This hook should not use actual values of the form fields. The code in the hook is processed before actual data is read from the database or the form. To control the availability of the command based on data on the screen, you can use the `Is Enabled` hook. You can use data that is not related to actual contents of the screen, for example parameter data.

Example:

```baan
function extern boolean cmd.ssi.import.is.visible()
{
|* Don’t allow excel import
return(false)
}
```

## Is Enabled hook

Use this hook to disable standard commands in the session. This hook can use actual values of the form fields.

Note: This hook only applies to commands that use the actual data. Commands that are independent of actual data can only be disabled by the `Is Visible` hook. For example; Close (`abort.program`), New (`add.set`) in a type-2 form, an overview without view fields, etc.

Example:

```baan
function extern boolean dupl.occur.is.enabled()
{
|* Don’t allow copying purchased items
return(tcibd001.kitm <> tckitm.purchase)
}
```

## Before Command hook

Use this hook to perform additional actions before the command is executed. This hook can use actual values of the form fields. You can cancel the execution of the command by calling the `choice.again()` function.

If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `command.super()` function. Example:

```baan
function extern dupl.occur.before.command()
{
command.super()
|* Don’t allow copying purchased items
if tcibd001.kitm = tckitm.purchase then
message("It is not allowed to copy purchased items; " &
"add a new item to ensure actual defaults are applied.")
choice.again()
endif
}
```

This is an alternative for the `Is Enabled` hook. You can keep the command enabled and this hook gives a message why a record cannot be copied.

## After Command hook

Use this hook to perform additional actions after the command is executed. This hook can use actual values of the form fields.

If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `command.super()` function.

This example shows that the delete action is aborted if one of the selected records cannot be deleted.

```baan
function extern void mark.delete.after.command()
{
command.super()
|* Not allowed to delete if purchased item is in selection
g.pur.selected = false
do.selection(false, check.pur)
if g.pur.selected then
message("Not allowed to delete purchased item")
choice.again()
endif
}
```

In the `Function` hook:

```baan
function check.pur()
{
if tcibd001.kitm = tckitm.purchase then
g.pur.selected = true
endif
}
```

## Standard Form Command

Use a Standard Form Command extension type to code additional logic around a session’s standard form command.

Examples:

- To remove the standard form command.

- To run an own session after a standard form command is executed.

- To disable a standard form command in case a certain condition applies.

This table shows the available properties:

Name

Overwrite Description

Description Label

Short Description

Long Description

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean <command>.is.visible()` |
| Is Enabled | `boolean <command>.is.enabled()` |
| Before Command | `void <command>.before.command()` |
| After Command | `Void <command>.after.command()` |

In an overview session with multiple records, you must be aware that multiple records are selected. The values available in the selection are the ones of the last (un)selected record. If the form command disabling/enabling depends on all selected records, you must iterate over the selected records.

## Overwrite Description property

If you select this property check box, you can overwrite the standard description of the standard form command. In this case, you must either specify the Description Label property or the Description property.

## Description Label property

Use this property to have different descriptions for users that are working in different languages. You can select an existing label, or create a new label in the Extensions package. The label used must have the context `General use`. A label can have descriptions in different languages and multiple length variants; for the form command, you can specify two length variants. The one for the short description (used on text buttons) cannot be longer than 17 characters.

See the Infor LN Studio Application Development Guide.

The `Description Label` property cannot be filled if the Short/Long Description property is used.

## Short Description property

Use this property if your standard form command description is not language dependent. This is the description that is used if the form command is available as a button.

The `Short Description` is read-only in case the `Overwrite Description` property is not checked or the `Descrip` `tion Label` property is filled. In those cases, the `Short Description` shows the description that is used when the form command is displayed at runtime.

## Long Description property

Use this property if your standard form command description is not language dependent. This is the description that is used in the menus of the toolbar (Views, References, Actions or a session specific one).

The `Long Description` is read-only in case the `Overwrite Description` property is not checked or the `Description` `Label` property is filled. In those cases, the `Long Description` shows the description that is used when the form command is displayed at runtime.

## Is Visible hook

Use this hook to remove standard form commands from the session.

This hook should not use actual values of the form fields. The code in the hook is processed before actual data is read from the database or the form. If you must control the availability of the form command based on data on the screen, you can use the `Is Enabled` hook. You can use data that is not related to actual contents of the screen, for example parameter data.

Example:

```baan
function extern boolean function.create.bp.easy.is.visible()
{
|* Quick creation of business partners not allowed for users
|* of department 300
select  tccom001.cwoc
from    tccom001
where   tccom001.loco = :logname$
as set with 1 rows
selectdo
if strip$(tccom001.cwoc) = "300" then
return(false)
endif
endselect
return(true)
}
```

## Is Enabled hook

Use this hook to disable standard form commands in the session. This hook can use actual values of the form fields.

Example:

```baan
function extern boolean function.approve.order.line.is.enabled()
{
|* Check approval against company rules
if txpurdll0001.can.approve.line(tdpur401.orno, tdpur401.pono) then
return(true)
endif
return(false)
}
```

Note that this hook applies to standard form commands only that are enabled by the standard application if exactly one record is selected. In that case the extension can disable the command. In case the standard form command allows multiple records being selected, the command remains enabled. In that case, you must use the `Before Command` hook to skip the processing if required.

## Before Command hook

Use this hook to perform additional actions before the form command is executed. This hook can use actual values of the form fields. You can cancel the execution of the command by calling the `choice.again()` function.

If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `command.super()` function.

Example:

```baan
function extern function.approve.order.line.before.command()
{
command.super()
string l.mess(200) mb
|* Check approval against company rules
if not txpurdll0001.can.approve.line.with.mess(
tdpur401.orno, tdpur401.pono, l.mess) then
message(l.mess)
choice.again()
endif
}
```

Note: This is an alternative for the `Is Enabled` hook as described earlier. You can keep the command enabled and this hook gives a message that a line cannot be approved.

## After Command hook

Use this hook to perform additional actions after the form command is executed. This hook can use actual values of the form fields. If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `command.super()` function.

Example:

```baan
function extern void function.approve.order.line.after.command()
{
command.super()
txpurdll0001.publish.approval(tdpur401.orno, tdpur401.pono)
}
```

In the `After Command Hook` of a Standard Form Command you can use the function `command.repeat()`. This function executes the standard form command again, after the current execution has finished. The standard form command is not executed at the moment `command.repeat()` is called, but the function triggers re-execution after the current execution has finished.

In this example the `exec.cont.process()` form command prints a report. If the report is printed in another language than English (“2”), the command is repeated to print the report also in English.

```baan
function extern void function.exec.cont.process.after.command()
{
static string   save.language(1)
if language$ <> "2" then
save.language = language$
language$ = "2"
command.repeat()
else
if not isspace(save.language) then
language$ = save.language
save.language = ""
endif
endif
}
```

## Custom Form Command

Use a Custom Form Command extension type to add a form command to a session.

Examples:

- To add a form command to start an own session with the selection made in the standard session.

- To execute an own function to calculate a field value.

This table shows the available properties:

Name

Activation Type

Command Type

Field

Name Name

Description Label

Short Description

Long Description

Advanced Properties

This table shows the available hooks:

| Name | Signature |
|---|---|
| Is Visible | `boolean <command>.is.visible()` |
| Is Enabled | `boolean <command.is.enabled()` |
| Before Command | `void <command>.before.command()` |
| Command Executed | `void <command>.command.execute()` |
| After Command | `Void <command>.after.command()` |

In an overview session with multiple records, you must be aware that multiple records are selected. The values available in the selection are the ones of the last (un)selected record. If the form command disabling/enabling is dependent on all selected records, you must iterate over the selected records.

## Activation Type property

| The `Activation Type` is a read-only property that depends on the `Command Type`. |  |
|---|---|
| This table shows the possible Activation Types: |  |
| Activation Type | Description |
| session | This type applies to Command Type `Print`. In this case a print session is started. |
| function | This type applies to Command Type `Form` or `Field`. In this case the Command Execute hook is executed. |

## Command Type property

Use this property to indicate the type of the custom form command.

This table shows the possible Command Types:

| Command Type | Description |
|---|---|
| Form | Use this command type for custom form commands that must be added in the Views, References or Actions menu. |
| Field | Use this command type for custom form commands that must be linked to a specific field on the form. The Field property must be specified as well. |

## Field property

Use this property to specify the form field to which the custom form command with Command Type `Field` must be linked. Both standard form fields and fields that are added by the extension can be selected.

This property can only be specified for custom form commands with Command Type `Field`.

## Name property

Use this property to specify the function name for custom form commands with Activation Type `function`. For custom for commands with Activated Type `session` (for Command Type `Print`), the Name property holds the session code of the print session.

## Description Label property

Use this property to have different descriptions for users that are working in different languages. You can select an existing label, or create a new label in the Extensions package. The label used must have the context ‘General use’. A label can have descriptions in different languages and multiple length variants. For the form command, you can specify two length variants. The one for the short description (used on text buttons) must not be longer than 17 characters.

See the Infor LN Studio Application Development Guide.

The `Description Label` property cannot be filled if the Short/Long Description property is used.

## Short Description property

Use this property if your standard form command description is not language dependent. This is the description that is used if the form command is available as a button.

The Short Description is read-only in case the `Description Label` property is filled. In this case, the `Short De` `scription` shows the description that is used when the form command is displayed at runtime.

## Long Description property

Use this property if your standard form command description does is not language dependent. This is the description that is used in the menus of the toolbar (Views, References, Actions or a session specific one).

The `Long Description` is read-only in case the Overwrite Description check box is cleared or the Description Label property is specified. In those cases, the `Long Description` shows the description that is used when the form command is displayed at runtime.

## Advanced properties

Use the advanced properties to influence the appearance and behavior of the custom form command. The dialog box displays several properties that control the display, availability and execution of the custom form command.

See the Infor LN Studio Application Development Guide on docs.infor.com.

## Is Visible hook

Use this hook to remove custom form commands from the session.

This hook should not use actual values of the form fields. The code in the hook is processed before actual data is read from the database or the form. To control the availability of the form command that is based on data on the screen, you can use the `Is Enabled` hook. You can use data that is not related to actual contents of the screen, for example parameter data.

See this example:

```baan
function extern boolean function.publish.item.is.visible()
{
|* Publishing only available for production companies
return(get.compnr() >= 0100 and get.compnr() < 1000)
}
```

## Is Enabled hook

Use this hook to disable custom form commands in the session. This hook can use actual values of the form fields.

Example:

```baan
function extern boolean function.publish.item.is.enabled()
{
|* Publishing only enabled for manufactured items
if tcibd001.kitm = tckitm.manufacture then
return(true)
endif
return(false)
}
```

This hook only applies if the custom form command is defined with the `One Record Selected` option. In case the custom form command allows selecting multiple records, the command remains enabled. In that case, you must use the `Before Command` hook to skip the processing if required.

## Before Command hook

Use this hook to perform additional actions before the custom form command is executed. This hook can use actual values of the form fields. You can cancel the execution of the command by calling the `choice.again()` function. If multiple records can have been selected to be processed.

Example:

```baan
function extern function.publish.before.command()
{
|* Publishing only for manufactured items
if tcibd001.kitm <> tckitm.manufacture then
choice.again()
endif
}
```

Note: This is an alternative for the `Is Enabled` hook described earlier. You can keep the command enabled and this hook gives a message if an item should not be published.

## Command Execute hook

Use this hook to perform the real actions for the custom form command. This hook can use actual values of the form fields.

Example:

```baan
function extern function.publish.command.execute()
{
string l.mess(200) mb
|* Publish item
if not txdll0007.item.publish(tcibd001.item, l.mess)
message(l.mess)
choice.again()
endif
}
```

## After Command hook

Use this hook to perform additional actions after the custom form command is executed. This hook can use actual values of the form fields. Example:

```baan
function extern void function.publish.after.command()
{
message(sprint$("Item %s published", strip$(tcibd001.item))
}
```

## Standard Context Message

A context message is a message that is related to the current Infor LN object. This context message is sent to Infor OS Portal or Infor Ming.le and distributed to context widgets or contextual apps that are listening to those messages.

In this way the context widgets or contextual apps show relevant information that is related to the Infor LN object being worked on.

For more information about InContext messaging, see the Infor Enterprise Server InContext Modeling Development Guide.

Use a Standard Context Message extension type to code additional logic around a session’s standard context message.

For example in these situations:

- Infor LN Object. To prevent context being sent of a related

- Infor LN Object. To send additional attributes of an

This table shows the available properties:

Name

Mapping

This table shows the available hooks:

| Name | Signature |
|---|---|
| Before Mappings | `long before.mapping.hook<context_message_id>` |
| After Mappings | `long after.mapping.hook<context_message_id>` |
| Is Visible | `boolean <context_message_id>.is.visible()` |

## Mapping property

The Mapping property specifies the mapping between the elements of the context message and their values.

Those values can be table fields, literal, literal values or results of function calls. Click Details in the property value cell to show the list of the mappings. The standard mappings are shown on the left side. You can make changes to the standard mappings on the right side.

For the various mapping types and the helper functions, see "Model Editing" in the Infor Enterprise Server InContext Modeling Development Guide.

Note: In the current version of Infor LN and the Extension Modeler, changing the custom mapping type to None sends the element with an empty value. It does not omit the element. This issue will be solved in a next version of Infor LN. See the After Mappings hook on page 101 for an example how to remove an element from the context message.

Note: We recommend that you do not change the mapping of identifying fields in the `inforBusinessContext` message. The `inforBusinessContext` message is, amongst others, used by the Related Information contextual widget/application. This application is part of Infor Document Management (IDM). After changing the mapping, documents may not be found by IDM and thus not shown in the Related Information contextual widget/application. Changing `inforBusinessContext` must be done consequently for the different sessions where documents of the Infor LN object are shown. Ensure that the changes are also inline with changes to the Business Context Model in IDM. For more information about the Business Context Model, see the IDM documentation.

## Before Mappings hook

Use this hook to read additional data before the standard context message is built. This hook can use actual values of the selected Infor LN object.

As an alternative you can also read the data with a function mapped to an element in the field mapping. But in case you require multiple values of the same table, we recommend that you use this hook.

In this example, the Sales Office of the Sales Order is read. Then the `tdsls400.cofc` field can be used in the field mapping.

```baan
function extern long before.mapping.hook.com.infor.ln.businesscontext_tdsls400_1()
{
select  tdsls400.cofc
from    tdsls400
where   tdsls400.orno = :tdsls400.orno
as set with 1 rows
selectdo
endselect
return(0)
}
```

Use the `message.super()` function in this case:

- `before.mapping.hook()` and the values that are set by the The standard context message contains a standard hook are required in your logic.

## After Mappings hook

Use this hook to perform additional actions on the created XML, to make changes that cannot be achieved by changing the field mappings.

If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `message.super()` function.

This example shows the (conditional) deletion of an element.

```baan
function extern long after.mapping.hook.com.infor.ln.businesscontext_tsmdm200_1(long i.mes
sage.node)
{
|* Find the id2 element of tsmdm200 and remove it
long    all.id2s, one.id2, node
all.id2s = xmlFindMatch("?<entities>.<id2>", i.message.node)
if all.id2s <> 0 then
|* Now we have a node with an enumeration of all id2 nodes
node = xmlGetFirstChild(all.id2s)
while node <> 0
one.id2 = lval(xmlData$(node))
|* one.id2 now contains the xml node of an id2 element.
|* Belongs this id2 to LN table tsmdm200? Then delete it.
if xmlDataElement$(xmlGetParent(one.id2), "lnTable") = "tsmdm200" then
xmlDelete(one.id2)
break
endif
node = xmlGetRightSibling(node)
endwhile
xmlDelete(all.id2s)
endif
return(0)
}
```

## Is Visible hook

Use this hook to (conditionally) remove standard context messages.

See this example:

```baan
function extern boolean com.infor.ln.businesscontext_tcibd001_1.is.visible()
{
|* Don't send context in case of purchased item
select  tcibd001.kitm
from    tcibd001
where   tcibd001.item = :tcibd001.item
and     tcibd001.kitm = tckitm.purchase
selectdo
return(false)
endselect
return(true)
}
```

## Custom Context Message

A context message is a message that is related to the current Infor LN object. This context message is sent to Infor OS Portal or Infor Ming.le and distributed to context widgets or contextual apps that are listening to those messages.

In this way the context widgets or contextual apps show relevant information that is related to the Infor LN object being worked on.

For more information about InContext messaging, see the Infor Enterprise Server InContext Modeling Development Guide.

Use a Custom Context Message extension type to code and add context to a session’s standard context message.

For example, to send context of another related Infor LN Object. You can only send context messages of type `inforBusinessContext` or `contextualURL` with the Custom Context Message extension type. To send another context message type, you can use the `Before Context Send` hook to add this context message.

This table shows the available properties:

Name

Mapping

This table shows the available hooks:

| Name | Signature |
|---|---|
| Before Mappings | `long before.mapping.hook<context_message_id>` |
| After Mappings | `long after.mapping.hook<context_message_id>` |
| Is Visible | `boolean <context_message_id>.is.visible()` |

## Mapping property

The Mapping property specifies the mapping between the elements of the context message and their values.

Those values can be table fields, literal, literal values or results of function calls. Click Details in the property value cell to show the list of the mappings.

For the various mapping types and the helper functions, see "Model Editing" in the Infor Enterprise Server InContext Modeling Development Guide.

## Before Mappings hook

Use this hook to read data before the custom context message is built. This hook can use actual values of the (table) fields that are used in the standard context messages. As an alternative you can also read the data with a function mapped to an element in the field mapping. But in case you require multiple values of the same table, we recommend that you use this hook.

In this example, the Item Group of the Item is read. Then the `tcmcs023` fields can be used in the field mapping. In this way the contextual widgets/apps also have the information of the Item Group of an Item.

```baan
function extern long before.mapping.hook.com.infor.ln.businesscontext_1()
{
select  tcmcs023.*
from    tcmcs023, tcibd001
where   tcibd001.item = :tcibd001.item
and     tcibd001.citg refers to tcmcs023 unref clear
as set with 1 rows
selectdo
endselect
return(0)
}
```

## After Mappings hook

Use this hook to perform additional actions on the created XML, to make changes that cannot be achieved by changing the field mappings.

This example shows the addition of an element, that is not available in the context message type elements..

```baan
function extern long after.mapping.hook.com.infor.ln.businesscontext_1(long i.message.node)
{
|* Add element addition_1 (item group description) to the tcmcs023 entity
long    all.tables, one.table, node
all.tables = xmlFindMatch("?<entities>.<lnTable>", i.message.node)
if all.tables <> 0 then
|* Now we have a node with an enumeration of all lnTable nodes
node = xmlGetFirstChild(all.tables)
while node <> 0
one.table = lval(xmlData$(node))
|* one.table now contains the xml node of an lnTable element.
|* Is this LN table tcmcs023? If yes, add the element to its parent
if xmlData$(one.table) = "tcmcs023" then
xmlNewDataElement("addition_1", tcmcs023.dsca, xmlGetParent(one.ta
ble))
break
endif
node = xmlGetRightSibling(node)
endwhile
xmlDelete(all.tables)
endif
return(0)
}
```

## Is Visible hook

Use this hook to build the custom context message conditionally. See this example:

```baan
function extern boolean com.infor.ln.businesscontext_1.is.visible()
{
|* Don't send Item Group context for Item Group 001
select  tcibd001.citg
from    tcibd001
where   tcibd001.item = :tcibd001.item
as set with 1 rows
selectdo
endselect
return(strip$(tcibd001.citg) <> "001")
}
```

## Event

Use an Event extension type to code additional logic around a session’s standard events.

This is supported for these events:

- Before Program

- After Program

- After Form Read

- Before Display Object

- Before New Object, sessions of type ‘maintain’ only

- After Update DB Commit, sessions of type ‘maintain’ only

Event examples:

- To synchronize with a secondary table.

- To hide groups, fields, commands, total line, etc.

This table shows the available hooks:

| Name | Signature |
|---|---|
| Before Program | `void before.program()` |
| After Program | `void after.program()` |
| After Form Read | `void after.form.read()` |
| Before Display Object | `void before.display.object()` |
| Before New Object | `void before.new.object()` |
| After Update DB Commit | `void after.update.db.commit()` |

For more information about those hooks, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `event.super()` function. Examples:

```baan
function extern void before.program()
{
|* Don’t display a total line in the session
event.super()
fattr.total.line = false
change.done.in.session = false
}
function extern void after.program()
{
|* Build file with pricebooks when changes have been done during
|* this session. Flag has been set in after.update.db.commit hook.
if change.done.in.session then
txpcgdll0001.build.pricebook.file()
endif
}
function extern void after.read.form()
{
|* Remove the link to the DOM data
remove.form.commands("document.output.man")
}
function extern void before.display.object()
{
|* Handle disabling/enabling custom fields
if ext.print.detail = tcyesno.no then
disable.fields("ext.print.comp", "ext.print.mat")
else
enable.fields("ext.print.comp", "ext.print.mat")
endif
}
function extern void before.new.object()
{
|* Make a new description during copy
if choice = dupl.occur then
tcmcs045.dsca = strip$(tcmcs045.dsca) & " (copy)"
endif
}
function extern void after.update.db.commit()
{
|* Set the flag so that the after.program hook publishes the pricebook
change.done.in.session = true
}
```

## Functions

In the hooks of a session extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See Trusted / Untrusted concept on page 155 Embedded SQL and the `sql.*` functions are available to read additional data from the LN database.

Calling (own) DLL functions is also possible.

## Limitations and restrictions

- Transactions Transactions in a session extension are not supported, except for the Event hooks Before Program, After Program and After Update DB Commit.

- UI A session extension can add fields to the UI. Other UI actions, such as starting other sessions, is not supported in the hooks that calculate the values. Starting other sessions is supported in the hooks that are available for the session commands. In cloud-ready extensions you can only start own developed sessions in the Extensions package or by a Public Interface. See Governance on page 155

- Queries You can use queries within the hooks of the session extension to read data from the database. Note that the standard LN application and the extension share the same record buffers. This implies that when the extension reads data from the database into those record buffers, the functionality of the standard LN application may be disturbed. To prevent this, explicit binding of variables must be applied, or the record buffer must be saved before your query is executed and restored afterwards.
