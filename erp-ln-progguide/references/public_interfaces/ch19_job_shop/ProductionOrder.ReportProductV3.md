# ProductionOrder.ReportProductV3

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 758-759

```baan
DLL:   tiextsfcapi
This function is available from 2026.01 (KB3644430).
Syntax: long ProductionOrder.ReportProductV3(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcclot           iLotCode,
domain  tiqep2           iProducedQuantity,
domain  tiqep2           iRejectedQuantity,
domain  tccdis           iRejectReason,
domain  tcuef.effn       iEffectivityUnit,
domain  tcutcs           iCompletionDate,
boolean          iSetStatusToCompleted,
boolean          iAllowReportMoreThanOrdered,
boolean          iDirectReceipt,
domain  tcutcs           iWarehouseReceiptDate,
domain  tcyesno          iDoBackflush,
ref     domain  tcclot           oLotCode,
ref             boolean          oOrderIsCompleted,
ref             boolean          oBackflushCompleted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a quantity can be reported complete
and or rejected for a specific production order, as in
session tisfc0120s000.
If the main item of the production order requires backflushing,
then Backflushing will be executed when the
company or site setting for the backflushing method is
'Automatic', or when iDoBackflush is 'Yes'.
If iSetStatusToCompleted is true, then the production
order status will be set to 'To be Completed' and
the required warehouse procedures will be executed,
but only if they have the setting 'automatic'.
If all the warehouse procedures are executed, then the
status of the production order will be changed from
'To be Completed' to 'Completed'.
The output argument oOrderIsCompleted will indicate
if the status is 'Completed'. When false, then
additional processing of the warehouse orders
is required.
iSetStatusToCompleted is not allowed when:
- the production order requires backflushing and
- backflushing is not automatic and
- actual costing is used.
Printing labels is not supported in this Public Interface.
An error will be returned when the production order
requires label printing.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iLotCode                Code of existing or new lot or empty.
When empty and a lot is required, then
a new lot will be created.
When the specified lot does not exist,
then it will be created.
iProducedQuantity       The quantity that is reported as completed.
iRejectedQuantity       The quantity that is reported as rejected.
Optional and can only be filled when
iProductionOrder does not have operations.
iRejectReason           The reason for rejection.
iEffectivityUnit        The Effectivity Unit. Not used when set
to 0.
iCompletionDate         Date of completion.
iSetStatusToCompleted   If true then the status of the production
order will be set to 'To be Completed'
or 'Completed'; else the status
will not be changed.
iAllowReportMoreThanOrdered
If true then more can be reported as
complete than ordered.
iDirectReceipt          Process inbound of the Item as soon as
the Order is reported complete.
iWarehouseReceiptDate   Receipt Date of associated Warehouse
receipt.
iDoBackflush            Execute backflushing even when
backflushing is not done automatically.
Output:
oLotCode                Code of the lot that was actually used.
oOrderIsCompleted       If true when the production order
status was changed to Completed,
else false.
oBackflushCompleted     If true when the backflush could be
executed, else false.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The reported quantities and / or
status change is successfully processed.
<> 0                    Errors occurred.
```
