# Catalog.StartOverview

> Chapter: Chapter 11 Public Interfaces for Product Catalogs
>
> Group: Public Interfaces for Catalog
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 394-395

```baan
DLL:   tdextpctapi
This function is available from 2021.03 (KB2171713).
Syntax: long Catalog.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcmcs.str6       iCategory,
domain  tcseek           iSearchKey mb,
domain  tcyesno          iCatalog,
ref     domain  tcmcs.str6       oCategory,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Catalogs in overview
mode (tdpct0510m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by Category
2: sort by Search Key/Category
3: sort by Catalog/Category
iQueryExtend            A specific query to be used when zooming
to this session.
iCategory               Category
iSearchKey              Search Key
iCatalog                Catalog
Output: for iStartMode MODAL:
oCategory               Category of the selected line
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
