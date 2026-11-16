# ProductionOrderOperation.ReportProduct

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 796-798

```baan
DLL:   tiextsfcapi
This function is available from 2021.04 (KB2178236).
Syntax: long ProductionOrderOperation.ReportProduct(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcclot           iLotCode,
domain  tiqep2           iProducedQuantity,
domain  tiqep2           iQuantityToInspect,
domain  tiqep2           iRejectedQuantity,
domain  tccdis           iRejectReason,
ref     domain  tcibd.sern       iSerialArrayProduced() fixed,
ref     domain  tcibd.sern       iSerialArrayToInspect() fixed,
ref     domain  tcibd.sern       iSerialArrayRejected() fixed,
domain  tcutcs           iCompletionDate,
boolean          iSetStatusToCompleted,
ref     domain  tcclot           oLotCode,
ref             boolean          oOperationIsCompleted,
ref             boolean          oErrorInReportProduct,
ref             boolean          oErrorInWarehousing,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a quantity on the specified
production order operation can be reported as complete,
rejected or sent to inspection, similar to session
tisfc0130m000.
This Public Interface consists of multiple transactions:
1. Report Product (including changing of status if requested)
2. Processing of the backflush transactions, including automatic
handling of the associated warehousing orders (if needed).
3. Processing WIP Transfers that were pending due to step 1.
4. Process the automatic activities on generated
warehousing orders related to the end item receipt (if needed).
This transaction will only be executed if:
- the previous actions are successfully completed and
committed(!), and
- several other detailed functional conditions are met (e.g.
the operation is the last operation, the end item has the
direct receipt setting, etc).
If the main item of the production order requires backflushing,
then Backflushing will be executed, but only when the
company or site setting for the backflushing method is
'Automatic'. When the setting of the backflushing method
is 'Manual' or 'Interactive', then no backflushing
will be done.
If iSetStatusToCompleted is true, then the operation
status will be set to 'Completed' (if possible).
The output argument oOperationIsCompleted will indicate
if it was possible change the status of the operation.
Use the serial array arguments to pass information about
serial numbers into this Public API. There is a separate
serial array for each of the 3 reported quantity types (produced,
to inspection and rejected).
If filled, then the length of the array must equal the
reported quantity.
The array can be static or dynamic.
Pass an empty array variable when no serial information must be
used for the quantity type.  Example of empty array variable
dummy.serials.produced,
which is defined as:
domain tcibd.sern dummy.serials.produced(1).
It is possible to use 1 and the same empty array variable for
all 3 array arguments.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled inside
the public interface.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperation              Operation (mandatory)
iLotCode                Code of existing or new lot or empty.
When empty and a lot is required, then
a new lot will be created.
When the specified lot does not exist,
then it will be created.
iProducedQuantity       The quantity that is reported as completed.
iQuantityToInspect      The quantity that is reported as send to
Inspection.
iRejectedQuantity       The quantity that is reported as rejected.
iRejectReason           The reason for rejection.
iSerialArrayProduced    Array of Serial Numbers for the
quantity produced.
iSerialArrayToInspect   Array of Serial Numbers for the
quantity to inspect.
iSerialArrayRejected    Array of Serial Numbers for the
quantity rejected.
iCompletionDate         Date of completion. Use zero to
specify the current date.
iSetStatusToCompleted   If true then the status of the production
order must be set to 'Completed'.
Output:
oLotCode                Code of the lot that was actually used.
oOperationIsCompleted   True when the status of the
operation was changed to Completed,
else false.
oErrorInReportProduct   If true, then an error occurred in the
Report Product transaction (see
above).
oErrorInWarehousing     If true, then an error occurred in the
Process Warehousing Orders transaction
(see above).
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The 2 transactions (see above) were
successfully completed.
<> 0                    Errors occurred in one of the two transactions.
Use oErrorInReportProduct and oErrorInWarehousing
to find out in which transaction the
error occurred.
If these are both false, then the error
occurred during checking the input
arguments.
```
