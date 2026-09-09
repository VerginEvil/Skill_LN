# WarehouseOrder.CalculateDeliveryDate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1021-1022

```baan
DLL:   whextinhapi
This function is available from 2023.08 (KB2292294).
Syntax: long WarehouseOrder.CalculateDeliveryDate(
domain  whinh.oorg       iOrderOrigin,
domain  whinh.ittp       iTransactionType,
domain  tctyps           iShipFromType,
domain  tccshp           iShipFromCode,
domain  tccom.cadr       iShipFromAddress,
domain  tcncmp           iShipFromCompany,
domain  tccom.cadr       iShipToAddress,
domain  tcitem           iItem,
domain  tccfrw           iCarrier,
domain  tccrte           iRoute,
domain  tcmcs.serv       iServiceLevel,
domain  tccom.trmd       iTransportCategory,
domain  whinh.cmtg       iTransportMeansGroup,
domain  tctmcb           iTransportMeansCombination,
domain  tcdsca           iMeansOfTransport mb,
domain  tccdec           iDeliveryTerms,
domain  tcptpa           iPointOfTitlePassage,
domain  tcdate           iPlannedReceiptDate,
ref     domain  tcdate           oPlannedReceiptDate,
ref     domain  tcdate           oPlannedDeliveryDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the planned delivery date based on the
planned receipt date.
1. If the planned receipt date is not set (unknown) it will be
the current date.
2. The time needed for transportation is calculated backwards
from the planned receipt date. Except for the origins
production and production manual. Per definition the time
between planned delivery and planned receipt for production
is the routing time and not the transportation time. This
function does not do a routing calculation.
3. A calendar correction is done on the ship from site.
Pre:    N.a.
Post:   N.a.
Input:  iOrderOrigin - Order Origin; Mandatory
iTransactionType - Transaction Type; Mandatory
iShipFromType - Ship From Type; Mandatory
iShipFromCode - Ship From Code; Mandatory
iShipFromAddress - Ship From Address; Mandatory
iShipFromCompany - Ship From Company; Mandatory
iShipToAddress - Ship To Address; Mandatory
iItem - Item; Not Mandatory
iCarrier - Carrier; Not Mandatory
iRoute - Route; Not Mandatory
iServiceLevel - Service Level; Not Mandatory
iTransportCategory - Transport Category; Not Mandatory
iTransportMeansGroup - Transport Means Group; Not Mandatory
iTransportMeansCombination - Transport Mean Combination; Not
Mandatory
iMeansOfTransport - Means of Transport; Not Mandatory
iDeliveryTerms - Terms of Delivery; Not Mandatory
iPointOfTitlePassage - Point of title Passage; Not Mandatory
iPlannedReceiptDate - Planned Receipt Date; Not Mandatory
Output: oPlannedReceiptDate - Planned Receipt Date
oPlannedDeliveryDate - Planned Delivery Date
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Planned Dates calculated successfully
DALHOOKERROR - An error occurred when calculating Planned Dates
```
