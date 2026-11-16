# Item.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 189-190

```baan
DLL:   tcextibdapi
This function is available from 2020.06 (KB2127551).
Syntax: long Item.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tckitm           iItemType,
domain  tccpva           iProductVariant,
domain  tccprj           iPCSProject,
domain  tcosys           iOrderSystem,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Item General (tcibd0501m000) in overview mode.
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
Not used
iSessionIndex
Value:  1:  Item
6:  ItemType, Item
8:  ProductVariant, Project, Item
10: OderSystem, Item
Determines the sort order in the session.
E.g. if iSessionIndex = 6, then Items are sorted by
Item Type and Item, and the optional input arguments
iItemType and iItem can be used to execute an
automatic find action on start of the session.
iQueryExtend
A specific query to be used when starting the
session. Use this to specfiy a filter, e.g.
"tcibd001.kitm = tckitm.product"
Using the query extend may lead to a
"data not found, session not started" situation.
iItem
optional
iItemType
optional
iProductVariant
optional
iPCSProject
optional
iOrderSystem
optional
Output: for iStartMode MODAL:
oItem                   - item of the selected row
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
