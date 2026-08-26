# SalesOrder.Cancel

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 314-315

```baan
DLL:   tdextslsapi
This function is available from     2026.08 (KB3687527  ).
Syntax: long SalesOrder.Cancel(
domain  tcorno           iSalesOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function cancels the given sales order.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (Mandatory)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default cancel options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Cancel Sales Order" (tdsls4201s300) and are
not explained in further detail here.
Supported Processing Options and their defaults:
NAME                                      TYPE                  DEFAULT
------------------------------------------------------------------------
SalesOrderAcknowledgement                 domain tcmcs.str2     ""
SalesOrderChangeOrderSequence             domain tcmcs.str8     ""
SalesOrderChangeReason                    domain tccdis         ""
SalesOrderChangeType                      domain tccdis         ""
SalesOrderLineAcknowledgement             domain tcmcs.str2     ""
SalesOrderLineChangeOrderSequence         domain tcmcs.str8     ""
SalesOrderLineChangeReason                domain tccdis         ""
SalesOrderLineChangeType                  domain tccdis         ""
PurchaseOrderAcknowledgement              domain tcmcs.str2     ""
PurchaseOrderChangeOrderSequence          domain tcmcs.str8     ""
PurchaseOrderChangeReason                 domain tccdis         ""
PurchaseOrderChangeType                   domain tccdis         ""
PurchaseOrderLineAcknowledgement          domain tcmcs.str2     ""
PurchaseOrderLineChangeOrderSequence      domain tcmcs.str8     ""
PurchaseOrderLineChangeReason             domain tccdis         ""
PurchaseOrderLineChangeType               domain tccdis         ""
CancelCrossDockOrderLine                  domain tcyesno        tcyesno.no
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Sales Order has been canceled
<> 0                    An error occurred
```
