# Table extension point

A table extension is used to react on the table events such as insert, update and delete for standard LN tables.

You can also control whether those actions on the table are allowed. For CDFs, you can set defaults, add validations, etc. For standard fields, you can also add validations, etc.

Examples:

- When an Item is added to or updated in the Item table, to update a CDF that holds the last modification date.

- Make a CDF a required field if the Item is of a certain type.

- Block the adding of new Sales Order Lines for a Sales Order when a CDF on Sales Order level has a certain value.

- Do additional validation on a standard field.

A table extension is an extension to the Data Access Layer (DAL) of the table. Although for the table itself the DAL may not be implemented.

For background on hooks, validations, setting error messages, return values, etc. see the DAL chapters and functions in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

This diagram shows the position of the table extension: LN sessions manipulate data in the LN tables. The hooks of the table extension are executed both from the data access layer and the runtime layer. The latter happens in the case the data access layer has not been implemented or is bypassed (for performance reasons) for certain LN tables. The table extension is applied regardless of the techniques used in the standard application.

The Create/Convert to runtime process also invokes the table extension to determine whether custom indexes must be created, changed or deleted.

The table extension point, has these extension types:

- Table

- Customer defined field logic

- Standard field logic

- Custom index

- Calculated field

## Table

With the hooks defined for the extension type Table, you can react on events that occur on table level. This table shows the available hooks: Data runtime Access layer T LN LN Standard Runtime able LN table layer Session DAL Extension Create/Convert to table LN table
Runtime layer
Data Access layer
LN Session
Standard DAL
Table Extension Create/Convert to
runtime
LN table

| Name | Signature |
|---|---|
| Declarations |  |
| Functions |  |
| Before Open Object Set long `before.open.object.set()` |  |
| Set Object Defaults long `set.object.defaults()` |  |
| Method is Allowed | boolean `method.is.allowed(long method)` |
| Before Save | long `before.save.object(long mode)` |
| After Save | long `after.save.object(long mode)` |
| Before Destroy | long `before.destroy.object()` |
| After Destroy | long `after.destroy.object()` |

## Declarations hook

Use this hook to declare tables and variables that must be globally available in all hooks of the extension. Also, the references to include files and DLLs that are used by the extension must be coded in this hook with `#include` and `#pragma`.

Example:

```baan
#include        <bic_text>
table   tccom100          |* Business Partners
domain  tcnama  old.nama
string  date.string(14)
boolean retb
#pragma used dll "otxprcdll0001"
```

## Functions hook

Use this hook to code (common) functions to use in the other hooks of the table extension. This helps you in reusing code and to keep the other hooks small and clear.

Functions that are called through `with.old.object.values.do()` and `with.object.set.do()` in the other hooks of the extension must be coded in this hook.

Example:

```baan
function get.old.nama()
{
old.nama = tccom100.nama
}
function string format.date(long i.date)
{
return(utc.to.iso(i.date, UTC_ISO_DIFF))
}
```

## Before Open Object Set hook

Use this hook to initialize variables for this extension. You can also use this hook to disallow access to the table.

Example:

```baan
function extern long before.open.object.set()
{
if txprcdll0001.pricebooks.blocked() then
dal.set.error.message("@Pricebooks blocked for maintenance")
return(DALHOOKERROR)
endif
return(0)
}
```

For more information about `before.open.object.set()` of the standard Data Access Layer, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522). Extending the query is not supported in the extension.

## Set Object Defaults hook

Use this hook to set default values for CDFs.

Example:

```baan
function extern long set.object.defaults()
{
tcmcs004.cdf_date = utc.num()
return(0)
}
```

## Method is Allowed hook

Use this hook to control whether new records can be inserted, existing records can be updated or deleted. The input argument for this hook is the method.

This tables shows the Method values:

| Method | Description |
|---|---|
| `DAL_NEW` | The hook is called to know whether records can be added. There is no current record, but in case of a session with a view, the view fields are available. |
| `DAL_UPDATE` | The hook is called to know whether the current record can be updated. |
| `DAL_DESTROY` | The hook is called to know whether the current record can be deleted. |

Example:

```baan
function extern boolean method.is.allowed(long method)
{
on case method
case DAL_NEW:
select  tdsls400.cdf_blck
from    tdsls400
where   tdsls400.orno = :tdsls401.orno
as set with 1 rows
selectdo
if tdsls400.cdf_blck = tdcdf______chk.yes then
dal.set.error.message(
"@Order is blocked, you cannot add Lines to it.")
return(false)
endif
endselect
break
case DAL_UPDATE:
break
case DAL_DESTROY:
break
endcase
return(true)
}
```

See the Infor ES Programmers Guide (Infor Customer Portal KB2924522) for more information about `method.is.allowed()` of the standard Data Access Layer. Note that this hook can only be used to set more restrictions. If the standard functionality does not allow a certain action, the extension cannot allow it either.

## Before Save hook

Use this hook to perform additional actions before the current (new or existing) record is saved. Think of updating fields in other tables, validations that could not be done on field level, etc. The input argument for this hook is the mode.

This table shows the Mode values:

| Mode | Description |
|---|---|
| `DAL_NEW` | A new record is inserted. |
| `DAL_UPDATE` | An existing record is updated. |

This hook is executed before the `before.save.object()` hook of the standard Data Access Layer is executed. If the standard hook must be executed before the extension hook is executed, you can force the standard hook to execute anytime you prefer. This can be achieved by calling the `table.super()` function.

All field values of the current record of the table are available.

Example:

```baan
function extern long before.save.object(long mode)
{
table.super()
tcmcs004.cdf_lcdt = utc.num()
tcmcs004.cdf_user = logname$
return(0)
}
```

For more information about `before.save.object()` of the standard Data Access Layer, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522). For more information about using the `table.super()` function within hooks, see Using table.super() in hooks on page 36.

### Using table.super() in hooks

When using the `table.super()` function within hooks, developers should be aware that recursive calls may occur if the standard logic subsequently updates the same table.

To prevent this, it is recommended to declare the `mode` argument as optional and retrieve it dynamically using the `get.long.arg()` function. This pattern ensures compatibility with both `DAL_NEW` and `DAL_UPDATE` modes, while avoiding recursion or fatal errors during standard background updates.

Note: Declare all variables in this function as `static` to retain their values across recursive or repeated calls, avoid unintended side effects, and ensure stable behavior during hook execution.

Example:

```baan
function extern long after.save.object(...)
{
static    long     mode
static    long     ret
mode = 0
ret = 0
if get.argc() >= 1 then
mode = get.long.arg(1)
endif
table.super()
on case mode
case DAL_NEW:
break
case DAL_UPDATE:
with.old.object.values.do(get.old.values)
if tcmcs004.cdf_city <> old.city then
ret = txcomdll0001.log.city.change(old.city, tcmcs004.cdf_city)
if ret < 0 then
dal.set.error.message("@Error during logging city change")
return(DALHOOKERROR)
endif
endif
endcase
return(0)
}
```

This approach helps maintain stable behavior when the standard Data Access Layer logic re-triggers table updates internally.

## After Save hook

Use this hook to perform additional actions after the current (new or existing) record is saved. Think of updating fields in other tables, etc. The input argument for this hook is the mode. This table shows the Mode values:

| Mode | Description |
|---|---|
| `DAL_NEW` | A new record is inserted. |
| `DAL_UPDATE` | An existing record is updated. |

This hook is executed before the `after.save.object()` hook of the standard Data Access Layer is executed. If the standard hook must be executed before the extension hook is executed, you can force the standard hook being executed anytime you prefer. This can be achieved by calling the `table.super()` function.

All field values of the current record of the table are available.

Example:

```baan
function extern long after.save.object(long mode)
{
table.super()
with.old.object.values.do(get.old.values)
if tcmcs004.cdf_city <> old.city then
ret = txcomdll0001.log.city.change(
old.city, tcmcs004.cdf_city)
if ret < 0 then
dal.set.error.message(
"@Error during logging city change")
return(DALHOOKERROR)
endif
endif
return(0)
}
```

For more information about `after.save.object()` of the standard Data Access Layer, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

For more information about using the `table.super()` function within hooks, see Using table.super() in hooks on page 36.

## Before Destroy hook

Use this hook to perform additional actions before the current record is deleted. Think of updating fields in other tables, additional checks whether it can delete the record, etc.

This hook is executed before the `before.destroy.object()` hook of the standard Data Access Layer is executed. If the standard hook must be executed before the extension hook is executed, you can force the standard hook being executed anytime you prefer. This can be achieved by calling the `table.super()` function.

All field values of the current record of the table are available.

Example:

```baan
function extern long before.destroy.object()
{
table.super()
select  txcom001.*
from    txcom001
where   txcom001.crou = :tcmcs004.crou
as set with 1 rows
selectdo
dal.set.error.message(
"@Route still being used in Carrier Plan")
return(DALHOOKERROR)
endif
return(0)
}
```

For more information about `before.destroy.object()` of the standard Data Access Layer, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

For more information about using the `table.super()` function within hooks, see Using table.super() in hooks on page 36.

## After Destroy hook

Use this hook to perform additional actions after the current record is deleted. Think of updating fields in other tables, etc.

This hook is executed before the `after.destroy.object()` hook of the standard Data Access Layer is executed. If the standard hook must be executed before the extension hook is executed, you can force the standard hook being executed anytime you prefer. This can be achieved by calling the `table.super()` function.

All field values of the current record of the table are available.

Example:

```baan
function extern long after.destroy.object()
{
table.super()
txcomdll0001.log.deleted.sales.order(
tdsls400.orno, tdsls400.crep,
tdssl400.otbp, tdsls400.oamt)
return(0)
}
```

For more information about `after.destroy.object()` of the standard Data Access Layer, see the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

For more information about using the `table.super()` function within hooks, see Using table.super() in hooks on page 36.

## Customer defined field logic

With the hooks on CDF level you can let the CDFs behave like standard fields. This applies to making the field mandatory, update them automatically based on changes of other fields, validations, and so on.

This table shows the hooks that are available for each individual CDF:

| Name |  | Signature |
|---|---|---|
| Is Never Applicable |  | boolean `<cdf field>.is.never.applicable(long         mode)` |
| Is Applicable |  | boolean `<cdf field>.is.applicable(long mode)` |
| Is List Entry Applicable |  | boolean `<cdf         field>.<constantname>.is.applicable(long mode` `)` |
| Is Derived |  | boolean `<cdf field>.is.derived(long mode)` |
| Is Mandatory |  | boolean `<cdf field>.is.mandatory(long mode)` |
| Is Read-only |  | boolean `<cdf field>.is.readonly(long mode)` |
| Make Valid |  | long `<cdf field>.make.valid(long mode)` |
| Is Valid |  | boolean `<cdf field>.is.valid(long mode)` |
| Update |  | long `<cdf field>.update(long mode)` |
| The input argument for all hooks is the mode. |  |  |
| This table shows the Mode values: |  |  |
| Mode | Description |  |
| `DAL_NEW` | A new record is being inserted. |  |
| `DAL_UPDATE` | An existing record is being updated. |  |

In all hooks, except for the `<cdf field>.is.never.applicable()` hook, all field values of the current table record are available.

If CDFs are dependent on standard fields or other CDFs – in other words if in the hooks the values of other fields are used – the hooks are re-executed when the field(s) on which the CDF depends are changed. Those dependencies are registered automatically.

For more information about the hooks, see the corresponding - `field.<hook>()` of the standard Data Access Layer in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

## Is Never Applicable hook

Use this hook to indicate if the field is never applicable. If a field is never applicable the field is made invisible at startup of a session. A field can become never applicable based on a static constraint, such as a parameter setting.

Example:

```baan
function extern boolean tcmcs004.cdf_city.is.never.applicable(long mode)
{
select  txmcs000.icty
from    txmcs000
where   txmcs000.sequ = 0
as set with 1 rows
selectdo
if txmcs000.icty = tcyesno.no then
return(true)
endif
endselect
return(false)
}
```

## Is Applicable hook

Use this hook to indicate whether the field is applicable. If a field is not applicable, then the field is disabled and the field is cleared.

Example:

```baan
function extern boolean tcmcs004.cdf_city.is.applicable(long mode)
{
return(tcmcs004.crou(1;1) = "U")
}
```

## Is List Entry Applicable hook

Use this hook to indicate whether a certain list constant is applicable. If the list constant is not applicable it is not displayed in the field's drop down list box, so the end-user cannot select it.

The constant names to be used in the hooks are the constants that are defined in the CDF Lists (ttadv4592m000) session. If a standard enum domain is used for the CDF, instead of a List, the constant names can be found in the Domains (ttadv4500m000) session, Enum/Set data.

Example:

```baan
function extern boolean tdsls400.cdf_brsn.export.is.applicable(long mode)
{
if tdsls400.orno(1;3) = "EXP" or
tdsls400.orno(1;3) = "SLE" then
return(true)
endif
return(false)
}
```

## Is Derived hook

Use this hook to indicate whether the field is derived. If a field is derived, then the field is made read-only in the UI. The difference with the `<cdf field>.is.readonly()` hook is that the field value can be changed within other hooks of the extension, for example in the `<cdf field>.update()` hook. If a field is read-only, its value cannot be changed. Example:

```baan
function extern boolean tcmcs004.cdf_addr.is.derived(long mode)
{
if tcmcs004.crou(1;1) = "U" then
return(true)
endif
return(false)
}
function extern tcmcs004.cdf_addr.update(long mode)
{
if tcmcs004.crou(1;1) = "U" then
tcmcs004.cdf_addr = tcmcs004.cdf_zip & " " & tcmcs004.cdf_city
endif
}
```

## Is Mandatory hook

Use this hook to indicate whether the field is mandatory. If a field is mandatory then it must have a value other than `""`, `0.0`, `0` or blank.

Example:

```baan
function extern boolean tcmcs004.cdf_city.is.mandatory(long mode)
{
return(tcmcs004.crou(1;1) = "U")
}
```

## Is Read-only hook

Use this hook to indicate whether the field is read-only. If a field is read-only it is made read-only in the UI. The field however, still can have a value.

Example:

```baan
function extern boolean tdsls400.cdf_blck.is.readonly(long mode)
{
return(tdsls400.hdst = tdsls.hdst.closed)
}
```

## Make Valid hook

Use this hook to adjust the field's value before it is checked. You can use it for example to round a field's value.

Example:

```baan
function extern long tdsls401.cdf_mprc.make.valid(long mode)
{
tdsls401.cdf_mprc = round(tdsls401.cdf_mrpc, 2, 1)
return(0)
}
```

## Is Valid hook

Use this hook to perform any checks not already defined in one of the other field hooks.

Example:

```baan
function extern boolean tcibd001.cdf_colr.is.valid(long mode)
{
select  txcom002.colr
from    txcom002
where   txcom002.colr = :tcibd001.cdf_colr
as set with 1 rows
selectdo
return(true)
endselect
dal.set.error.message("txcomt002", tcibd001.cdf_colr)
|* Color %1$s not found
return(false)
}
```

## Update hook

Use this hook to (re) determine the value of the field based on the current record values. Think of determining defaults and calculating derived values.

Example:

```baan
function extern tcmcs004.cdf_addr.update(long mode)
{
if tcmcs004.crou(1;1) = "U" then
tcmcs004.cdf_addr = tcmcs004.cdf_zip & " " & tcmcs004.cdf_city
endif
}
```

## Standard field logic

With the hooks on standard field level you can influence the behavior of the standard application. This applies to making the field mandatory, update them automatically based on changes of other fields, validations, etc. For the standard fields, also hooks can be present in the standard Data Access Layer. If both hooks are present, in the DAL and in the table extension, the table extension can only restrict the data further. For example, data that cannot be entered because of an `is.valid()` hook in the standard DAL can still not be specified even if the table extension would allow it.

This table shows the hooks that are available for each standard table field:

| Name |  | Signature |
|---|---|---|
| Is List Entry Applicable |  | boolean `<table       field>.<constantname>.is.applicable(long mode` `[,long       element])` |
| Is Derived Name Signature |  | boolean `<table field>.is.derived(long mode [,long       element])` |
| Is Mandatory |  | boolean `<table field>.is.mandatory(long mode [,long       element]` `)` |
| Is Read-only |  | boolean `<table field>.is.readonly(long mode [,long       element])` |
| Make Valid |  | long `<table field>.make.valid(long mode [,long       element])` |
| Is Valid |  | boolean `<table field>.is.valid(long mode [,long       element])` |
| Update |  | long `<table field>.update(long mode [,long       element])` |
| The input argument for all hooks is the mode. Mode can have these values: |  |  |
| Mode | Description |  |
| `DAL_NEW` | A new record is being inserted. |  |
| `DAL_UPDATE` | An existing record is being updated. |  |

The argument `element` is available for all array table fields. The element points to the actual occurrence in the array that is being processed.

In all hooks, all field values of the current table record are available.

If standard fields are dependent on other standard fields or CDFs – in other words if in the hooks the values of other fields are used – the hooks are re-executed when the field(s) on which the field depends are changed. Those dependencies are registered automatically.

For more information about the hooks, see the corresponding `-field.<hook>()` of the standard Data Access Layer in the Infor ES Programmers Guide (Infor Customer Portal KB2924522).

## Is List Entry Applicable hook

Use this hook to indicate whether a certain list constant is applicable. If the list constant is not applicable it is not displayed in the field's drop down list box, so the end-user cannot select it.

The constant names to be used in the hooks are the constants that are defined for the domain of the table field. The constant names can be found in the Domains (ttadv4500m000) session, Enum/Set data.

Example:

```baan
function extern boolean tdsls400.osta.closed.is.applicable(long mode)
{
return(txcomdll0001.sales.order.can.be.closed())
}
```

## Is Derived hook

Use this hook to indicate whether the field is derived. If a field is derived, then the field is made read-only in the UI. The difference with the `<field>.is.readonly()` hook is that the field value can be changed within other hooks of the extension, for example in the `<field>.update()` hook. If a field is read-only, its value cannot be changed.

Example:

```baan
function extern boolean tdsls401.pric.is.derived(long mode)
{
select  txprc100.fixd
from    txprc100
where   txprc100.item = :tdsls401.item
as set with 1 rows
selectdo
|* Item price is fixed, user cannot change it
return(true)
endselect
return(false)
}
function extern tdsls401.pric.update(long mode)
{
select  txprc100.pric
from    txprc100
where   txprc100.item = :tdsls401.item
as set with 1 rows
selectdo
tdsls401.pric = txprc100.pric
endselect
}
```

## Is Mandatory hook

Use this hook to indicate whether the field is mandatory. If a field is mandatory then it must have a value other than `""`, `0.0`, `0` or blank.

Example:

```baan
function extern boolean tcmcs041.dsca.is.mandatory(long mode)
{
return(true)
}
```

## Is Read-only hook

Use this hook to indicate whether the field is read-only. If a field is read-only it is made read-only in the UI. The field however, still can have a value.

Example:

```baan
function extern boolean tcibd001.dsca.is.readonly(long mode)
{
if mode = DAL_UPDATE then
return(true)
endif
return(false)
}
```

## Make Valid hook

Use this hook to adjust the field's value before it is checked. You can use it for example to round a field's value.

Example:

```baan
function extern long tcibd001.dsca.make.valid(long mode)
{
|* Always start with capital
tcibd001.dsca(1;1) = toupper$(tcibd001.dsca(1;1))
return(0)
}
```

## Is Valid hook

Use this hook to perform any checks not already defined in one of the other field hooks.

Example:

```baan
function extern boolean tdsls401.item.is.valid(long mode)
{
if not txexpdll0001.item.allowed(tdsls401.ofbp, tdsls401.item) then
dal.set.error.message(
"@Item not allowed for this business partner”)
return(false)
endif
return(true)
}
```

## Update hook

Use this hook to (re) determine the value of the field based on the current record values. Think of determining defaults and calculating derived values.

Example:

```baan
function extern tdsls401.pric.update(long mode)
{
select  txprc100.pric
from    txprc100
where   txprc100.item = :tdsls401.item
as set with 1 rows
selectdo
tdsls401.pric = txprc100.pric
endselect
}
```

## Custom index

Use a custom index to create an additional index in a standard table. This index can be used in custom sessions to query the table in a more efficient way. You can use customer defined fields in a custom index.

This table shows the available properties:

Name

Sequence

Label

Description

Duplicates

When you defined a table extension with a custom index, the custom index remains active even if the table extension itself is de-activated. In case of de-activation, the hooks are not executed, but the custom index is not deleted.

## Sequence property

The Sequence property is a read-only property that is automatically generated. It starts with 99 and counts back in case of multiple custom indexes. If you remove a custom index, the others are not renumbered. During addition of a new custom index first the open number is reused.

In the hooks or other script components where to use the custom index, you can refer to it with this property: `<package><module><table number>._index<sequence>.`

We recommend that you use the individual fields in the queries. In case the standard table definition is modified and the custom index is also available as standard index, you can delete the custom index. Changing the scripts and hooks where you use the index is not required.

Example:

This example shows a validation check to prevent not unique values in a customer defined field.

```baan
function extern boolean tccom100.cdf_lnam.is.valid(long mode)
{
domain  tccom.bpid bpid
select  tccom100.bpid:bpid
from    tccom100
where   tccom100._index99 = {:tccom100.cdf_lnam}
and     tccom100.bpid <> :tccom100.bpid
as set with 1 rows
selectdo
dal.set.error.message(sprintf$("@Name used for BP %s", bpid))
return(false)
endselect
return(true)
}
```

## Label property

Use this property if the custom index description must be displayed in different languages. You can select an existing label, or create a new label in the Extensions package. A label can have descriptions in different languages.

For more information see the Infor LN Studio Application Development Guide.

The Label property cannot be filled if the Description property is used.

## Description property

Use this property if the custom index description is not language dependent.

The Description property cannot be filled if the Label property is used.

## Duplicates property

Use this property to indicate whether duplicates are allowed for this custom index.

Note: If you do not select this property you must ensure that the combination of the fields you defined in the custom index have unique values in the table. If there are duplicates and this property is not selected, you will lose data during the table reconfiguration process. The reconfiguration process takes place during the conversion to runtime of the table changes.

## Convert to Runtime

Before you can use the custom index, the table extension must be checked in and the table must be converted to runtime.

If you do not use the Extension Modeler to convert the table to runtime. Run the Create Runtime Data Dictionary (ttadv5210m000) session to convert the table to runtime. This session must also be used to remove the custom index after you deleted the table extension with the custom index.

## Calculated Field

Use a Calculated Field extension type if you require additional fields (non-table fields) in the data to be published to Data Lake.

Calculated Fields added as an extension to a table cannot be used in sessions, reports, etc.

Examples:

- Aggregations of table fields (average, sum, etc.)

- Results of called library functions

This table shows the available properties:

Name

Name

Description

Label

Domain

This table shows the available hooks:

| Name | Signature |
|---|---|
| Calculate Value | domain <domain> <name>.calculate() |

## Name property

The Name property is used for the variable name. It is prefixed with " `ext.` ". The maximum length of a variable name is 17, including the prefix.

## Label property

Use this property if the content of a label must be sent as field description in the metadata to Data Lake. The label in the language of the user that runs the publishing of the data sets, is used.

For more information about labels, see the Infor LN Studio Application Development Guide

The Label property cannot be specified if the Description property is used.

## Description property

Use this property if you require a hard-coded string to be sent as field description in the metadata to Data Lake.

The Description property cannot be specified if the Label property is used.

## Domain property

The Domain property is required to define the data type of the Calculated Field. You can select an existing domain or create a new domain in the Extensions package.

See the Infor LN Studio Application Development Guide

## Calculate Value hook

Use this hook to calculate the value for the calculated field. The calculated value must be the return value of the function.

In this hook, all fields of the current table record are available. The hook is called when the staged data is published.

In the code example, the Business Partner data of table tccom100 is published and requires the number of Purchase Orders for the Business Partner.

```baan
function extern domain tcmcs.long ext.no.po.calculate()
{
domain  tcmcs.long    retval
select  count(*):retval
from    tdpur400
where   tdpur400.otbp = :tccom100.bpid
selectdo
endselect
return(retval)
}
```

## Functions

In the hooks of a table extension you can use all trusted functions to do string manipulation, calculations, comparisons, etc.

See Trusted / Untrusted concept

Typical functions to be used in a table extension: • `with.old.object.values.do()` • `with.object.set.do()` • `dal.set.error.message()` • `disable.table.extension()` • `enable.table.extension()` • `ue.get.origin()`

Embedded SQL and the `sql.*` functions are available to read additional data from the LN database. You can also perform database changes with the `db.*` and `dal.*` functions.

## Limitations and restrictions

- Transactions All updates that are done in the table extension are part of the transaction that is started in the standard LN application. You cannot call `commit.transaction()`, `abort.transaction()` or `db.retry.point()` from within one of the extension hooks. Doing this can lead to fatal applications errors, or data corruption in the database.

- UI A table extension has no access to the UI. You cannot start sessions or reports.

- Queries You can use queries within the hooks of the table extension to read data from the database. Note that the standard LN application and the extension share the same record buffers. This implies that when the extension reads data from the database into those record buffers, the functionality of the standard LN application can be disturbed. To prevent this, explicit binding of variables must be applied, or the record buffer must be saved before your query is executed and restored afterwards.

## User Exit DLL

Older versions of Infor LN had the concept of User Exit DLLs. User Exit DLLs are similar to the extension scripts for table extensions, but are less rich in functionality. User Exit DLLs are still supported, but do not comply with cloud-ready extensions.

If a table extension is present, the User Exit DLL is ignored. If no table extension is present, the User Exit DLL is executed.
