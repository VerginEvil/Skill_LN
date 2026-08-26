# ConfigurableItemSettingsForDataGeneration.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableItemSettingsForDataGeneration
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 700-701

```baan
DLL:   tiextpcfapi
This function is available from     2022.08 (KB2253191  ).
Syntax: long ConfigurableItemSettingsForDataGeneration.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tckoid           iItemField,
ref     domain  tcitem           oItem,
ref     domain  tckoid           oItemField,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session Generic Item - Settings for
Data Generation (tipcf3101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Specifies the sort order of the records being  displayed.
Possible values are:
1                               -             Session is sorted by Item, Item Field,
Sequence Number.
3                               -             Session is sorted by Item, Item Field,
Sequence Number, Text Block.
iQueryExtend
A specific query to be used when zooming to this session.
iItem
The Configurable Item for which the session will be
started. Mandatory.
iItemField
The Item Field for which the session will be started.
Mandatory if iSessionIndex is 1.
Output:
Variables below contain the values of the selected record.
They are only filled if iStartMmode is MODAL and 1 record has
been selected.
-                        oItem                - Configurable Item.
-                        oItemField           - Item Field.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```

## Public Interfaces for

## StandardItemConfigurationsOptions

The following functions are available: StandardItemConfigurationsOptions.StartOverview
