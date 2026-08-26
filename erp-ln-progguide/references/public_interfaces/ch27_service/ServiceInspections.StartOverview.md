# ServiceInspections.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceInspections
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1362-1364

```baan
DLL:   tsextcfgapi
This function is available from     2023.06 (KB2293111  ).
Syntax: long ServiceInspections.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcitem           iItem fixed,
domain  tcibd.sern       iSerial fixed,
domain  tcorno           iOrder,
domain  tcpono           iActivity,
domain  tcorno           iClaim,
domain  tcpono           iClaimLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function starts the overview session Inspections
(tscfg3100m000).
Pre     :               -
Post    :               -
Input   : iStartMode: Not used; Not mandatory
Session is always started MODELESS. That means that
parent and child are parallel sessions that can be
manipulated simultaneously.
iStartFilter: Not mandatory
iStartFilter determines the View fields when the
session is started.
Possible values         | View fields
------------------------                              |------------------------
""                      | No view fields
"SerializedItem"        | Item, Serial
"ServiceOrderActivity"  | Service Order, Activity
"WorkOrder"             | Work Order, Activity (0)
"WorkOrderActivity"     | Work Order, Activity
"CustomerClaim"         | Customer Claim, Line (0)
"CustomerClaimLine"     | Customer Claim, Line
"SupplierClaim"         | Supplier Claim, Line (0)
"SupplierClaimLine"     | Supplier Claim, Line
iQueryExtend: Not used; Not mandatory
A specific query to be used when zooming to this
session.
iItem
Item. Mandatory when iStartFilter is SerializedItem.
iSerial
Serial Number. Mandatory when iStartFilter is
SerializedItem.
iOrder
Order Number. Mandatory when iStartFilter is
ServiceOrderActivity, WorkOrder, or WorkOrderActivity.
iActivity
Activity. Mandatory when iStartFilter is
ServiceOrderActivity, or WorkOrderActivity.
iClaim
Claim. Mandatory when iStartFilter is
CustomerClaim, CustomerClaimLine, SupplierClaim, or
SupplierClaimLine.
iClaimLine
Claim Line. Mandatory when iStartFilter is
CustomerClaimLine, or SupplierClaimLine.
Output  : ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0             Session started
<> 0          An error occurred
```

## Public Interfaces for Call

The following functions are available: Call.CreateInvoice Call.GenerateSerializedItem Call.SetStatusToInProcess Call.StartOverview Call.TransferToCustomerClaim Call.TransferToMaintenanceSalesOrderPartLine Call.TransferToPlannedActivity Call.TransferToServiceOrder Call.TransferToServiceOrderV2 Call.TransferToServiceQuote Call.TransferToWorkOrder Call.ViewInvoice
