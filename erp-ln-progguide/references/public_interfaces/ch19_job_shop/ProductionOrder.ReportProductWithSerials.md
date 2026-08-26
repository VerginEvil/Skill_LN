# ProductionOrder.ReportProductWithSerials

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 762-764

```baan
DLL:   tiextsfcapi
This function is available from     2022.04 (KB2235599  ).
Syntax: long ProductionOrder.ReportProductWithSerials(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcclot           iLotCode,
domain  tiqep2           iProducedQuantity,
domain  tiqep2           iRejectedQuantity,
domain  tccdis           iRejectReason,
ref     domain  tcibd.sern       iSerialArrayProduced() fixed,
ref     domain  tcibd.sern       iSerialArrayRejected() fixed,
domain  tcutcs           iCompletionDate,
boolean          iSetStatusToCompleted,
ref     domain  tcclot           oLotCode,
ref             boolean          oOrderIsCompleted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a quantity can be reported complete
and/or rejected for a specific production order with serials,
as in session tisfc0120s000.
If the main item of the production order requires Backflushing,
then Backflushing will be executed, but only when the
company or site setting for the backflushing method is
'Automatic'. When the setting of the backflushing method
is 'Manual' or 'Interactive', then no Backflushing
will be done.
If iSetStatusToCompleted is true, the production
order status will be set to 'To be Completed' and
the required warehouse procedures will be executed,
but only if they have the setting 'Automatic'.
If all the warehouse procedures are executed, the
status of the production order will be changed from
'To be Completed' to 'Completed'.
The output argument oOrderIsCompleted will indicate
if the status is 'Completed'. When false,
additional processing of the warehouse orders
is required.
iSetStatusToCompleted is not allowed when:
-                       the production order requires backflushing and
-                       backflushing is not automatic and
-                       actual costing is used.
Printing labels is not supported in this Public Interface.
An error will be returned when the production order
requires label printing.
There should be no pending logical transactions before calling
this function.
Commit or abort transactions are handled within the function.
Pre:                  -
Post:                 -
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must
exist within iSite).
iLotCode                Code of existing or new lot or empty.
When empty and a lot is required, then
a new lot will be created.
When the specified lot does not exist,
then it will be created.
iProducedQuantity       The quantity that is reported as completed.
iRejectedQuantity       The quantity that is reported as rejected.
(Optional and can only be filled when
iProductionOrder does not have operations.)
iRejectReason           The reason for rejection.
iSerialArrayProduced    Array of Serial Numbers for the
quantity produced.
iSerialArrayRejected    Array of Serial Numbers for the
quantity rejected.
iCompletionDate         Date of completion.
iSetStatusToCompleted   If true then the status of the production
order will be set to 'To be Completed'
or 'Completed'; else the status
will not be changed.
Output:
oLotCode                Code of the lot that was actually used.
oOrderIsCompleted       If true when the production order
status was changed to Completed,
else false.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The reported quantities and / or
status change is succssfully processed.
<> 0                    Errors occurred.
```
