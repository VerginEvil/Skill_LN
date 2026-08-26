# ProductionOrder.RemoveUnusedHandlingUnits

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 754-755

```baan
DLL:   tiextsfcapi
This function is available from     2025.07 (KB3567400  ).
Syntax: long ProductionOrder.RemoveUnusedHandlingUnits(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref             boolean          oSomeRemoved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public Interface can be used to remove the unused handling
units from a production order. This is equivalent to the
execution of the form command Remove Handling Units from session
Report Orders Completed (tisfc0120s000).
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must
exist within iSite).
Output: oSomeRemoved            Indicates if one or more unused Handling
Units were removed.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Removed unused handling units
successfully.
<> 0                    An error occurred in removing unused
handling units.
```
