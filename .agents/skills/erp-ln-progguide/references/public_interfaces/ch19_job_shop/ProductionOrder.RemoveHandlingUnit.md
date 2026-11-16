# ProductionOrder.RemoveHandlingUnit

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 753-754

```baan
DLL:   tiextsfcapi
This function is available from 2025.07 (KB3567400).
Syntax: long ProductionOrder.RemoveHandlingUnit(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tihuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public Interface can be used to remove a specific handling
unit from a production order.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must
exist within iSite).
iHandlingUnit           The Handling Unit to remove.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Removed handling unit successfully.
<> 0                    An error occurred in removing handling
unit.
```
