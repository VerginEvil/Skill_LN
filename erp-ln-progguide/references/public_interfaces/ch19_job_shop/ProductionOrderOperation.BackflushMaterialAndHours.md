# ProductionOrderOperation.BackflushMaterialAndHours

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 786-787

```baan
DLL:   tiextsfcapi
This function is available from     2022.07 (KB2249872  ).
Syntax: long ProductionOrderOperation.BackflushMaterialAndHours(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tisfc.wybf       iSelectionMethod,
boolean          iCompletedOperationOnly,
domain  tcdate           iBackflushDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to perform the backflushing for one or
more Production Order Operations of a given Production Order.
Transaction management is handled by this Public Interface.
Pre:                  -
Post:                 -
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
iOperation              Production Order Operation (mandatory
if iSelectionMethod is not all).
iSelectionMethod        Operation(s) to handle:
all
upto
one
iCompletedOperationOnly Backflush Completed Operations only.
iBackflushDate          Backflush Date, cannot be in the
future (0 = current date).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Operation(s) have been backflushed.
<> 0                    Backflushing could not be completed.
```
