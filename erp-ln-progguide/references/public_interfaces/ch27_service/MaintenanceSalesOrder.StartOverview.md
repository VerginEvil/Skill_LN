# MaintenanceSalesOrder.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1491-1492

```baan
DLL:   tsextmscapi
This function is available from 2026.05 (KB3663572).
Syntax: long MaintenanceSalesOrder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iMaintenanceSalesOrder,
long             iViewFieldSet,
ref     domain  tcorno           oMaintenanceSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Maintenance Sales Orders
Overview (tsmsc1100m000).
Before calling MaintenanceSalesOrder.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the iViewFieldSet can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the table index that is to be used. (Optional)
Supported values:
1: sort by Maintenance Sales Order
2: sort by Sold-to Business Partner
3: sort by Service Office
4: sort by Order Status
5: sort by Order Date
6: sort by Customer Order
7: sort by Description
8: sort by (serialized) Item
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on the main
table tsmsc100 are supported. (Optional)
iMaintenanceSalesOrder
The Maintenance Sales Order to display at the top of the
grid if present in the chosen view. (Optional)
iViewFieldSet
A Set to set the view fields when the index used is not
index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       SoldToBusinessPartner   domain  tccom.bpid      empty
3       ServiceOffice           domain  tccwoc          empty
4       OrderStatus             domain  tsmsc.stat      empty
5       OrderDate               domain  tsmdm.utct      empty
6       CustomerOrder           domain  tccorn          empty
7       Description             domain  tsmdm.dscb      empty
8       Item                    domain  tcitem          empty
8       SerialNumber            domain  tcibd.sern      empty
Output:
oMaintenanceSalesOrder
The selected MaintenanceSalesOrder if iStartMode is
MODAL and the session is closed with a single selection.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
