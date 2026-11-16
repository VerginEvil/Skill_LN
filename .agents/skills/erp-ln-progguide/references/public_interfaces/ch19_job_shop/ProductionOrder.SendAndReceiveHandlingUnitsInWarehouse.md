# ProductionOrder.SendAndReceiveHandlingUnitsInWarehouse

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 769-770

```baan
DLL:   tiextsfcapi
This function is available from 2026.06 (KB3624546).
Syntax: long ProductionOrder.SendAndReceiveHandlingUnitsInWarehouse(
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
Transaction handling is handled in the public interface.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside Public Interface.
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
