# ConfigurableStructures.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableStructures
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 818-819

```baan
DLL:   tiextpcfapi
This function is available from     2026.10 (KB3684755  ).
Syntax: long ConfigurableStructures.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iProduct,
domain  tibmrv           iVersion,
ref     domain  tcitem           oProduct,
ref     domain  tibmrv           oVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Configurable
Structures (tipcf3150m000) in overview mode. Use this session
to view and maintain the Configurable Structures.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel sessions
that can be manipulated simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
Started session. Optional.
Possible values are:
"showAll":      All Configurable BOMS are displayed
"showCurrent":  Only Actual and New versions are
displayed
When empty:     "showEffective" is applied
iSessionIndex           Specifies the table                      -index that is to be
used.
Standard supported values:
1: sort by Product,
Version (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iProduct                Product (Optional).
iVersion                Version (Optional).
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProduct                Product.
oVersion                Version.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for

## MaterialToIssueForProductionOrders

The following functions are available: MaterialToIssueForProductionOrders.StartOverview
