# ProductionOrders.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 782-783

```baan
DLL:   tiextsfcapi
This function is available from 2020.06 (KB2127770).
Syntax: long ProductionOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tccprj           iProject,
domain  tcitem           iItem,
domain  tcutcs           iActualDeliveryDate,
domain  tisfc.prcd       iPriority,
domain  tcpdno           iGroup,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Production Orders
(tisfc0501m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Optional. Allowed values:
showAll
showInUse (default)
iSessionIndex           Optional. The index that will be used.
Supported values:
1: sort by Production Order (default)
2: sort by Site, Production Order
3: sort by Project, Item
4: sort by Item, Delivery Date
5: sort by Priority
6: sort by Production Order Group
iQueryExtend            A specific query to be used when zooming
to this session.
iSite                   Site. Mandatory if iStartMode = MODELESS
and iSessionIndex = 2.
iProductionOrder        Production Order Number
iProject                Project
iItem                   Main Item
iActualDeliveryDate     Actual Delivery Date
iPriority               Priority
iGroup                  Production Order Group
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductionOrder        - Production Order Number
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
