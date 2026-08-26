# ProductionOrder.ReportProductWithHandlingUnits

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 760-762

```baan
DLL:   tiextsfcapi
This function is available from     2024.02 (KB2310061  ).
Syntax: long ProductionOrder.ReportProductWithHandlingUnits(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tihuid           iHandlingUnit,
domain  tcpkdf           iAlternativePackageDefinition,
domain  tcclot           iLotCode,
domain  tiqep2           iQuantityToAdd,
domain  tcuef.effn       iEffectivityUnit,
ref     domain  tcibd.sern       iSerialArrayProduced() fixed,
ref     domain  tcclot           iLotCodeArrayProduced() fixed,
domain  tcutcs           iCompletionDate,
boolean          iSetStatusToCompleted,
boolean          iDirectlySendToWarehouse,
boolean          iAllowLessWhenDirectlySendToWarehouse,
boolean          iAllowReportMoreThanOrdered,
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
then Backflushing will be executed, but only when the
company or site setting for the backflushing method is
'Automatic'. When the setting of the backflushing method
is 'Manual' or 'Interactive', then no backflushing
will be done.
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
-                       the production order requires backflushing and
-                       backflushing is not automatic and
-                       actual costing is used.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:
iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iHandlingUnit           Handling Unit (Mandatory).
iAlternativePackageDefinition
May only be supplied when Alternative
Package Definition is allowed for the
production order.
iLotCode                Code of existing or new lot or empty.
When empty and a lot is required, then
a new lot will be created.
When the specified lot does not exist,
then it will be created.
iQuantityToAdd          Quantity to Add. Quantity that will be
added to the Handling Unit. A zero (0.0)
value is allowed in if either
iDirectlySendToWarehouse  or
iSetStautsToCompleted is set to True.
A negative quantity to add is allowed.
When the negative quantity is provided
quantity is subtracted from the handling
unit's produced quantity.
iEffectivityUnit        The Effectivity Unit. Not used when set
to 0.
iSerialArrayProduced    Array of Serial Numbers for the
quantity produced. May only be supplied
when the produced product is serialized.
iLotCodeArrayProduced   Array of Lot Code for the quantity
produced.Can only be provided only if
item is both serialized and lot
controlled.
iCompletionDate         Date of completion.
iSetStatusToCompleted   If true then the status of the production
order will be set to 'To be Completed'
or 'Completed'; else the status
will not be changed.
iDirectlySendToWarehouse
Directly Send to Warehouse.
iAllowLessWhenDirectlySendToWarehouse
Even when the produced quantity for the
Handling Unit is less than its label
quantity, still allow sending it to
warehouse directly.
iAllowReportMoreThanOrdered
If true then more can be reported as
complete than ordered.
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
status change is succssfully processed.
<> 0                    Errors occurred.
```
