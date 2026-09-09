# ProductionOrderOperation.Block

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 786-787

```baan
DLL:   tiextsfcapi
This function is available from 2023.09 (KB2299065).
Syntax: long ProductionOrderOperation.Block(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tisfc.blcd       iBlockingReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, the Production Order Operation
will be blocked with the given blocking reason.
ProductionOrderOperation.ResetStatus can be used to unblock an
Operation.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperation              Operation (mandatory)
iBlockingReason         Blocking Reason (mandatory)
Output:
oExceptionMessage       The last message if the return value
is not equal to 0. If more than one
message is given, these are present
in the oExceptionID.
oExceptionID            An ID that refers to all error
information.
Use the functions in Exception handling
to get all relevant information.
Return: 0                       The operation was blocked.
<> 0                    The operation was not blocked.
```
