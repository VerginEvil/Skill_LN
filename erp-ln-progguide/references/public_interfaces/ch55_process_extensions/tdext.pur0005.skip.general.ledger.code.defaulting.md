# tdext.pur0005.skip.general.ledger.code.defaulting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Procurement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2131-2132

```baan
Syntax: boolean tdext.pur0005.skip.general.ledger.code.defaulting(
boolean          i.user.interaction,
domain  tcmcs.tabl       i.from.table,
domain  tcsess           i.from.session,
domain  tcfieldname      i.table.field )
Usage:        Expl:   Use this method to skip the defaulting of the general ledger (GL)
code in Procurement processes.
The input arguments provided to this method depend on the
context from which it is invoked. There are two possible origins:
* DAL (Data Access Layer):
In this context, no user interaction is allowed. You can use
any table field from the given table to determine the output.
However, note that the session that triggered the defaulting
logic is not available in this context.
* UI (User Interface):
In this context, LN identifies the specific table field that
was modified and triggered the defaulting logic. It also knows
which session caused the trigger. You can use any table field
from the given table to determine the output.
Pre:    NA
Post:   NA
Input:  i.user.interaction                    - Indicates whether user interaction is
allowed in the current context.
i.from.table                                  - The table-code for which LN
is determining a default ledger code.
(Mandatory).
Supported Values:
tdpur201    Requisition Line
tdpur401    Purchase Order Line
i.from.session                                - The session that triggered the
defaulting. This field is empty when
called from the DAL or from a non                                                -UI
context.
Possible Values (among others):
tdpur2502m000
tdpur2502m100
tdpur4101m000
tdpur4101m100
i.table.field                                 - The table field that was modified and
triggered the defaulting logic. This
field is empty when called from the
DAL or from a non                                                -UI context.
Possible Values:
Any table field from <i.from.table>
that can trigger the general ledger
code defaulting logic.
Output: Not Applicable.
Return: true                                  - The extension has determined that
general ledger code defaulting
must be skipped for the given input.
false                                         - The standard logic for defaulting
applies.
```

## Process Extensions for ProductionOrder

The following process extension(s) is/are available: ProductionOrder.PrintCustomReports ProductionOrder.SkipCalculateIntermediateResults ProductionOrder.SkipClose ProductionOrder.SkipCreateOrderGroup ProductionOrder.SkipGenerateSubcDocuments ProductionOrder.SkipMaterialLineAggregation ProductionOrder.SkipPrintMaterialShortage ProductionOrder.SkipReportComplete ProductionOrder.SkipWarehouseForMaterialShortage
