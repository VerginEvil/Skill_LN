# ProductionOrderOperation.ResetStatus

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 801-802

```baan
DLL:   tiextsfcapi
This function is available from     2022.03 (KB2232034  ).
Syntax: long ProductionOrderOperation.ResetStatus(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
boolean          iResetPlannedQuantities,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to reset the status of a
completed Production Order Operation, as in
session tisfc0130m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
iOperation              Production Order Operation (mandatory,
its status must be blocked completed or
closed).
iResetPlannedQuantities Relevant if the reported quantities are
zero.
If true, resets the planned quantities
and material quantities to the estimated
values.
If false, the planned quantities are not
reset.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Operation is reset.
<> 0                    Operation could not be reset.
```
