# ProductionOrderOperation.SetStatusCompleted

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 802-803

```baan
DLL:   tiextsfcapi
This function is available from 2021.04 (KB2178236).
Syntax: long ProductionOrderOperation.SetStatusCompleted(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcutcs           iCompletionDate,
boolean          iCheckFullReportedQuantity,
ref             boolean          oOperationIsCompleted,
ref             boolean          oErrorInChangeStatus,
ref             boolean          oErrorInWarehousing,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, the Production Order Operation
status of the specified Operation will be set to ›¼À˜Completed›¼À™.
This Public Interface consists of 2 transactions:
1. Change status.
2. Process the automatic activities on the generated
warehousing orders.
This transaction will only be executed when the first
action is successfully completed and committed and
only when handling the last operation and backflusing
was executed in the first transaction.
The output argument oOperationIsCompleted indicates
if the status of the operation was changed.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperation              Operation (mandatory)
iCompletionDate         Date of completion. Use zero to
specify the current date.
iCheckFullReportedQuantity If true, then the status change is
only done when the planned quantity
is produced.
Output:
oOperationIsCompleted   If true when the status of the
operation was successfully changed to
Completed else false.
oErrorInChangeStatus    If true, then an error occurred in the
Change Status transaction (see
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
Use oErrorInChangeStatus and oErrorInWarehousing
to find out in which transaction the
error occurred.
If these are both false, then the error
occurred during checking the input
arguments.
```
