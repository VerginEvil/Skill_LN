# ProductionOrder.GetInProcessQuantity

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 715-715

```baan
DLL:   tiextsfcapi
This function is available from     2024.04 (KB2300947  ).
Syntax: long ProductionOrder.GetInProcessQuantity(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iPosition,
domain  tcuef.effn       iUnit,
ref     domain  tcqst1           oQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to read the in-process
quantity for the Production Order's material line.
Pre:                  -
Post:                 -
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
iPosition               Position, if zero (0) is given, it refers
to produced end item, otherwise it refers
to the position of the order's material
line on the order.
iUnit                   Effectivity Unit (Optional).
Output:
oQuantity               The quantity that is in process for
this position.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successfully determined Quantity.
<> 0                    Quantity could not be determined.
```
