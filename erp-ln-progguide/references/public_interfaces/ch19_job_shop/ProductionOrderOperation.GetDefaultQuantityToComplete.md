# ProductionOrderOperation.GetDefaultQuantityToComplete

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 791-792

```baan
DLL:   tiextsfcapi
This function is available from     2025.11 (KB3564185  ).
Syntax: long ProductionOrderOperation.GetDefaultQuantityToComplete(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
boolean          iQuantityOfSemiFinished,
ref     domain  tiqep2           oDefaultQuantityToComplete,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface calculates the default quantity to
complete for the given Production Order Operation.
Input:  iSite                   Site.
iProductionOrder        Production Order (mandatory).
iOperation              Operation(mandatory).
iQuantityOfSemiFinished The default quantity to complete of the
semi                                              -finished product will be returned.
Default value false.
Output:
oDefaultQuantityToComplete
Default Quantity Completed.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Calculated Default Quantity Completed.
<> 0                    Otherwise.
```
