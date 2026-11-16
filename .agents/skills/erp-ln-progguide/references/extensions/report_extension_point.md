# Report extension point

A report extension is used to enrich the data that is used as input for the report.

This applies to reports for which a design is present in Infor Reporting and reports that are personalized with Infor LN Report Designer. A report extension can also be used to redirect the data to an alternative report.

Examples:

- To add the CDFs of the Purchase Order Header to the Purchase Order report.

- To write additional rows with data from one of your own tables.

- To run an own Sales Order Acknowledgment report, that deviates completely from the standard one.

When the report is printed data is sent by the LN session to the native LN report. In case of Infor Reporting, the unformatted data of this native LN report serves as a data source. The report extension adds the fields and the rows to this data source.

In case of Infor LN Report Designer, the added fields by the report extension are available as report input fields to be used in the report layouts.

For the report extension point, these extension types exist:

- Report

- Table selection

- Dataset

- Calculated field

This diagram shows the position of the report extension: When the Report Extension is created, you must change the report design with Infor Reporting ’s Report Studio. Or you can use Infor LN Report Designer to add the new fields to the report.

See these guides:

- Development Guide Infor Enterprise Server Connector for Infor Reporting

- Report Designer Development Guide Infor LN

## Report

The properties and hooks that are defined for the Report extension type can intervene in writing data rows in the XML file. This XML file is used as input for the reporting tools.

This table shows the available properties:

Name

Include all CDFs

This table shows the available hooks:

Name Signature

Declarations Infor XML file LN Report Report LN Report LN engine Session Extension native report LN Designer tables Infor Reporting Report engine
LN Session
Report Extension
LN native report
XML file
LN tables
Infor LN Report
Designer Infor Reporting

| Name | Signature |
|---|---|
| Functions |  |
| Write Row | void write.row() |
| Get Alternative Report string get.alternative.report() |  |

## Include all CDFs property

If you check this property, all CDFs of tables, of which already fields are used in the report, are added to the data rows in the XML file. Those tables can be found in the list of tables that is displayed to add a Table Selection for the report.

By default, this property check box is selected when you add a Report extension. Including all CDFs was the default behavior in ES 10.4.2. If you clear this property check box, you can include all CDFs at table level (in the Table Selection) or select individual CDFs or ignore all CDFs.

If the report has linked tables with a lot of CDFs and you do not need most of them, for performance reasons we recommend that you uncheck this property and select the individual CDFs at table level.

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension. Also, the references to include files and DLLs that are used by the extension must be coded in this hook with #include and #pragma.

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

Use this hook to code (common) functions to use in the other hooks of the report extension. This helps you in reusing code and to keep the other hooks small and clear.

Example:

```baan
function string format.date(long i.date)
{
return(utc.to.iso(i.date, UTC_ISO_DIFF))
}
function string get.item.description(domain tcitem i.item)
{
domain  tcdesc     dsca
select  tcibd001.dsca:dsca
from    tcibd001
where   tcibd001.item = :i.item
as set with 1 rows
selectdo
return(dsca)
endselect
return("???????????????")
}
```

## Write Row hook - Infor Reporting only

You can use this hook in these situations:

- Writing additional rows to the XML file.

- Calculating values for Calculated Fields.

The Write Row hook is executed before the standard row is written to the XML file. If the standard row must be written before the hook is executed, you can force the standard row being written anytime you prefer. This can be achieved by calling the report.super() function.

Example:

```baan
function extern void write.row()
{
ext.alternative = tcyesno.no
report.super()
ext.alternative = tcyesno.yes
select  tcibd005.*
from    tcibd005
where   tcibd005.item = :tdpur401.item
selectdo
rpi.write.additional.row()
endselect
}
```

In this example there is also an `ext.alternative` Calculated Field. To filter to distinguish the standard rows and the additional rows in the Infor Reporting design, this field is added. It must have the value `no` for the standard rows and value `yes` for the additional rows. The additional rows are written for each record found in `tcibd005` for the current Item.

For `tcibd005` there must be a Table Selection to select the individual fields, but that Table Selection does not require a Table Read hook. The `ext.alternative` Calculated Field does not require a Calculate Value hook, because the value is calculated here.

## Get Alternative Report hook

Use this hook to specify an alternative report for the current one. When the current report (the report for which the extension has been created) is opened by a print session, not this report will be opened, but the one returned by this hook. This is useful when the standard LN application opens a report which has not been linked to a session; in case a report is linked to a session, it can be made invisible with the session extension and the alternative one can be added as a custom linked report.

Example:

```baan
function extern string get.alternative.report()
{
domain  tcyesno   ext.spec.report
import("ext.spec.report", ext.spec.report)
if ext.spec.report = tcyesno.yes then
return("txibd040114000")
else
return("")
endif
}
```

In this example the alternative report is opened if the session field, custom fields can be added in the session extension, `ext.spec.report` is set to the value “yes”.

## Table Selection

With the properties and hooks that are defined for the extension type Table Selection, you can include fields from the selected table in the XML.

Use this extension type if there is a 1-to-1 relationship between the data already in the report and the additional data you require. Use the Dataset extension type when there is a 1-to-n relationship and you must print multiple occurrences of the data.

When you add a Table Selection, the tables that are already linked to the report are displayed. If the table of which to add fields is not in the list, specify `Other Table` and you can select any table.

This table shows the available properties:

Name

All Customer Defined Fields

All Standard Fields

Field List

This table shows the available hooks:

| Name | Signature |
|---|---|
| Table Read | void <table>.read() |

## All Customer Defined Fields property

If you select this property check box, all CDFs if the selected table are included in the XML. Note that if you checked the Include All CDFs property on Report level, this property is checked and cannot be changed.

If the table has a lot of CDFs and you do not need them all, for performance reasons we recommend that you clear this property check box and select the individual CDFs in the Field List property.

## All Standard Fields property

If you check this property, all standard fields of the selected table are included in the XML.

If the table has a lot of fields and you do not need them all, for performance reasons we recommend that you clear this property check box and select the individual fields in the Field List property.

## Field List property

The Field List property can be filled only if not all CDFs and standard fields of the table are already selected with the All Customer Defined Fields and All Standard Fields properties. Click Details in the property value cell to get the list of available fields. Select the ones you require in the XML data source.

## Table Read hook

Use this hook to write the SQL query to read the data of the table. There are two cases for which it is not required to implement this hook for a Table Selection:

- The table is already linked to the report. However, it can be that not all fields of the table are available; in that case, still a Table Read hook is required to read those additional fields.

- The table data is read in the Write Row hook at report level. This is mandatory if you need data of multiple table records being sent in the XML file.

To select the correct data from the tables, all fields that are sent from the print session to the native report are available. Those fields can be found in the Reports session (ttadv3530m000), option Report Input Fields.

Example:

```baan
function extern void tccom100.read()
{
select tccom100.*
from   tccom100
where  tccom100.bpid = :tdpur400.otbp
as set with 1 rows
selectdo
endselect
}
```

## Dataset - Infor LN Report Designer only

Use this extension type when there is a 1-to-n relationship between the existing report data and printing multiple occurrences of the data.

In Infor LN Report Designer, you can create new layouts that are linked to the Dataset to print the fields. The Dataset extension type is supported only for Infor LN Report Designer. To achieve the same for Infor Reporting, use the Write Row hook to add data to the data source.

This table shows the available properties:

Name

Name

Label

Description

Type

Selection

Where Clause

This table shows the available hooks:

| Name | Signature |
|---|---|
| Read dataset | void<dataset>.read() |

## Name property

The Name property is used for the dataset name.

## Label property

Use this property if the Dataset description must be available in multiple languages.

The description is visible at design time in the Infor LN Report Designer. You can select an existing label, or create a new label in the Extensions package. A label can have descriptions in different languages and multiple length variants.

See the Infor LN Studio Application Development Guide

The Label property cannot be filled if the Description property is used.

## Description property

The description is visible at design time in the Infor LN Report Designer.

If the Dataset description must be available in multiple languages, do not use the Description property, but link a label to the field with the Label property. The Description property cannot be filled if the Label property is used.

## Type property

This tables shows the Dataset types:

| Dataset type | Description |
|---|---|
| Query | Use this Type if the retrieval of the data can be expressed in a database query. Click Details to select the main table of the query and the fields that must be added to the report. You can add also fields of referenced tables (multi-level). |
| Other | Use this Type if the data retrieval cannot be expressed in a database query. For example, when data must be retrieved by calling a Public Interface of LN. Or reading data on the file system or calling a web service that returns the data. |

You must implement the Read Dataset hook to retrieve the data. The fields of the Dataset must be added as Calculated Fields.

## Where Clause property

The Where Clause property is used to select records from the main table of the dataset query.

In this Where Clause you can use the fields that are already present as report input fields.

An example: `tdsls401.item = :tcibd001.item`

In this example a dataset is created with the Order Lines (tdsls401) for the Item (tcibd001) that is already printed on the report.

## Read Dataset hook

Use this hook to write the code to specify the Dataset fields.

The Dataset fields must be defined as Calculated Fields and linked to the Dataset. For each row that must be written in the Dataset, the function `write.additional.row()` is called. In this example a function is called to build an array with drawing files that must be printed for the specified Item:

```baan
function extern void dataset.read()
{
long
nr.of.drawings, i
string
drawing.files(1,1) based
txibddll0001.get.drawing.file
s(tcibd001.item,
drawing.files, nr.of.drawings)
for i = 1 to nr.of.drawings
ext.drawing.file = drawing.files(1,
i)                 write.additional.row()
endfor
free.mem(drawing.files)
}
```

## Calculated Field

Use a Calculated Field extension type if you need additional fields (non-table fields) in the XML data source.

Examples:

- Aggregations of table fields (average, sum, etc.)

- Results of calculations with standard report fields or fields made available with the Table Selections

- Results of called library functions

This table shows the available properties:

Name

Name

Description

Label

Domain

Elements

Dataset

This table shows the available hooks:

| Name | Signature |
|---|---|
| Calculate Value | void <name>.calculate() |

## Name property

The Name property is used for the variable name. It is prefixed with "ext.". The maximum length of a variable name is 17, including the prefix. This variable name is the name to be used in the Calculate Value hook or the Write Row hook. This is also the name of the field in the XML data source and available at design time in Infor Reporting’s Report Studio and Infor LN Report Designer.

## Label property

Use this property if the report must be printed in different languages. You can select an existing label, or create a new label in the Extensions package. A label can have descriptions in different languages and multiple length variants.

See the Infor LN Studio Application Development Guide.

The Label property cannot be filled if the Description property is used.

## Description property

The Description is sent in the XML data source and available at design time in Infor Reporting’s Report Studio.

If you must print the reports in different languages that are based on user language or the recipient language, do not use the Description property, but link a label to the field with the Label property.

The Description property cannot be filled if the Label property is used.

## Domain property

The Domain property is required to define the data type of the Calculated Field. You can select an existing domain or create a new domain in the Extensions package.

See the Infor LN Studio Application Development Guide.

## Elements property

Use the Elements property if you require more than one occurrence for the field.

The field becomes an array field. The default value is 1. Specify a higher value if you need more occurrences.

## Dataset property

Use this property if the Calculated Field is connected to a Dataset.

## Calculate Value hook

Use this hook to calculate the value for the calculated field. The value must be assigned to the variable with the name of the Name property. In case of an array field, when the Elements property is greater than 1.

In this hook, all fields are available that are sent from the print session to the native report. Those fields can be found in the Reports (ttadv3530m000) session, option Report Input Fields. Additionally, all fields are available of the tables read in the Table Read hooks of the Table Selections.

This hook is called by the report engine before the row of data is written to the XML data source. If the calculated field values are required in the Write Row hook, do not use the Calculate Value hook. You must calculate the value in the Write Row hook itself.

Example, no array field:

```baan
function extern void ext.no.po.calculate()
{
ext.no.po = 0
select  count(tdpur400.orno):ext.no.po
from    tdpur400
where   tdpur400.otbp = :tccom100.bpid
selectdo
endselect
}
```

For performance reasons, you can decide to calculate multiple fields in one Calculate Value hook; in that case, you can omit the hooks for the other fields. You can also calculate the values in the Write Row hook. Note that the order in which the Calculate Value hooks are executed is arbitrary.

Example, array field:

```baan
function extern void ext.turnover.calculate(i.elem.number)
{
long month
month = i.elem.number
txprcdll0001.calculate.turnover(tcibd001.item, month,
ext.turnover(i.elem.number))
}
```

## Text Line Filter - Infor LN Report Designer only

This extension type is used for all Report input fields, Calculated fields, Datasets, and Table selections that have fields of data type Text. For these text fields, a Text Line Filter can be configured. In Infor LN Report Designer, you can configure text line filters with various values, including Custom Filter. When this value is selected, the custom filter can be developed in the Extension Modeler by creating a Text Line Filter hook for the related text field configured with the Custom Filter property in Report Designer. Consequently, for the custom text line filter to work correctly, it must be configured in both Report Designer and Extension Modeler.

This table shows the available properties:

Name

Name

Description

This table shows the available hooks:

| Name | Signature |
|---|---|
| Text Line Filter | void <text field name>.filter.text.line() |

## Name property

The Name property is used for the text field name and is read-only.

## Description property

The Description property is used for the text field description and is read-only.

## Text Line Filter hook

Use this hook to define the text line filter of the specified text field.

Example: skip text lines with the text '<Internal>':

```baan
function extern tdsls400.txta.filter.text.line()
{
| Set lattr.print to true or false and/or adjust lattr.prline.
| By default lattr.print = true
if pos(lattr.prline, "<Internal>") > 0 then
lattr.print = false
endif
}
```

Example: replace the text '<BPN>' with the name of the business partner

```baan
function extern tdsls400.txta.filter.text.line()
{
| Set lattr.print to true or false and/or adjust lattr.prline.
| By default lattr.print = true
lattr.prline = str.replace$(lattr.prline, "<BPN>", tccom100.nama)
}
```

## Functions

In the hooks of a report extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See Trusted / Untrusted concept

Typical function to be used in a report extension:

- rpi.write.additional.row()

This function can be used in the Write Row hook to write additional rows in the XML data source.

Embedded SQL and the sql.* functions are available to read additional data from the LN database.

## Limitations and restrictions

- Transactions Transactions in a report extension are not supported.

- UI A report extension has no access to the UI. You cannot start sessions or (other) reports.

- Printing The report extension is meant only for reading or calculating additional data to be printed in the reports. You cannot control the printing itself by manipulating the predefined variables for report scripts. The `lattr.*` variables may not reflect the correct values. The moment of reading the additional data and the real printing is different. The variable `lattr.language$` can be used to check the language in which the report is printed. To have access to this variable, you can use this line in the Declaration hook:

`#include <bic_repgen>`
