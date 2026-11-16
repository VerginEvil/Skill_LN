# ConfigurableItemGenericPriceLists.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ConfigurableItemGenericPriceLists
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 695-696

```baan
DLL:   tiextpcfapi
This function is available from 2022.08 (KB2253191).
Syntax: long ConfigurableItemGenericPriceLists.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session Generic Price Lists
(tipcf4101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Not used.
iQueryExtend
A specific query to be used when zooming to this session.
iItem
The Configurable Item for which the session will be
started. Mandatory.
Output:
Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
- oItem                - Configurable Item.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started.
<> 0                    - Otherwise.
```
