# ItemWarehouseInventoryTransaction.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemWarehouseInventoryTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 924-926

```baan
DLL:   whextinrapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemWarehouseInventoryTransaction.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  tcdate           iTransactionDate,
domain  tcmcs.long       iSequence,
domain  tcncmp           iOrderCompany,
domain  tckoor           iTypeOfOrder,
domain  tcorno           iOrder,
domain  tccprj           iProject,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tcorno           iInventoryTransactionId,
domain  tcmcs.long       iInventoryTransactionIdSequence,
domain  tccom.bpid       iOwner,
domain  tccom.bpid       iBuyFromBusinessPartner,
ref     domain  tcitem           oItem,
ref     domain  tccwar           oWarehouse,
ref     domain  tcdate           oTransactionDate,
ref     domain  tcmcs.long       oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Item - Warehouse -
Inventory Transactions (whinr1510m000).
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byItemWarehouse":
data is displayed by item and warehouse
session will be started on index 1
view fields: Item and Warehouse
"byItem":
data is displayed by item
session will be started on session index 1
view fields: Item
"byOrder":
data is displayed by Order Company, and
Type of Order
session will be started on session index 2
view fields: Order Company, Type of Order
"byProjectOrder":
data is displayed by Project, Element, Activity,
Order Company and Type of Order
session will be started on session index 3
view fields: Project, Element, Activity
"byTransactionId"
data is displayed by Inventory Transaction ID
session will be started on session index 4
view fields: Inventory Transaction ID
"byOwner"
data is displayed by Owner
session will be started on session index 5
view fields: Owner
"byBuyFromBusinessPartner"
data is displayed by Buy-From Business Partner
session will be started on session index 6
view fields: Buy-From Business Partner
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iItem
Mandatory when iStartFilter "byItemWarehouse" or
"byItem" is used or iSessionIndex = 1 and iStartMode is
MODELESS
iWarehouse
Mandatory when iStartFilter "byItemWarehouse" is used
or iSessionIndex = 1 and iStartMode is MODELESS
iTransactionDate
Optional.
iSequence
Optional.
iOrderCompany
Mandatory when iStartFilter "byOrder" is used or
iSessionIndex = 2 and iStartMode is MODELESS
iTypeOfOrder
Mandatory when iStartFilter "byOrder" is used or
iSessionIndex = 2 is used and iStartMode is MODELESS
iOrder
Optional.
iProject
Optional.
iElement
Optional.
iActivity
Optional.
iInventoryTransactionId
Mandatory when iStartFilter "byTransactionId" is used or
iSessionIndex = 4 and iStartMode is MODELESS
iInventoryTransactionIdSequence
Optional.
iOwner
Optional.
iBuyFromBusinessPartner
Optional.
Output: for iStartMode MODAL:
oItem           - item of selected transaction
oWarehouse      - warehouse of selected transaction
oTransactionDate- transaction date of selected
transaction
oSequence       - sequence of selected transaction
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
