# ProductionOrder.SendHandlingUnitsToWarehouse

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 770-771

```baan
DLL:   tiextsfcapi
This function is available from     2025.07 (KB3567901  ).
Syntax: long ProductionOrder.SendHandlingUnitsToWarehouse(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
long             iNumberOfHandlingUnits,
ref     domain  tihuid           iHandlingUnitArray() fixed,
ref             boolean          oSomeHandlingUnitsSent,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be alike the form command Send to
Warehouse from session Production Order Handling Units
(tisfc0506m000).
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must
exist within iSite).
iNumberOfHandlingUnits  Number of Handling Units.
iHandlingUnitArray      Handling units to be sent to the
warehouse.
Output: oSomeHandlingUnitsSent  Indicates if one or more handling units
were sent to the warehouse.
oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Handling units sent to warehouse
successfully.
<> 0                    An error occurred while sending handling
units to the warehouse.
```
