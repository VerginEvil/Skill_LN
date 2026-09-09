# ProductionOrder.CalculateStartDate

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 706-706

```baan
DLL:   tiextsfcapi
This function is available from 2024.12 (KB3541196).
Syntax: long ProductionOrder.CalculateStartDate(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcutcs           iRequestedDeliveryDate,
ref     domain  tcutcs           oProductionStartDate,
ref     domain  tcutcs           oPlannedDeliveryDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to calculate the Production Start Date
based on the given Requested Delivery Date. The planning method
of the production order must be set to "Backward". The planning
information for the Production Order as well its operation
planning is adjusted.
Pre:    transaction started
Post:   abort or commit
Input:
iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory and must be
in the given Site).
iRequestedDeliveryDate  Requested Delivery Date.
Output:
oProductionStartDate    Production Start Date.
oPlannedDeliveryDate    Planned Delivery Date.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Calculated the planned delivery date and
Production Start date successfully.
<> 0                    Errors occurred.
```
