# WarehouseOrder.CalculateReceiptDate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1022-1023

```baan
DLL:   whextinhapi
This function is available from 2026.01 (KB3644645).
Syntax: long WarehouseOrder.CalculateReceiptDate(
domain  whinh.oorg       iOrderOrigin,
domain  whinh.ittp       iTransactionType,
domain  tccom.cadr       iShipFromAddress,
domain  tctyps           iShipToType,
domain  tccshp           iShipToCode,
domain  tccom.cadr       iShipToAddress,
domain  tcncmp           iShipToCompany,
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
domain  tcdate           iPlannedDeliveryDate,
ref     domain  tcdate           oPlannedDeliveryDate,
ref     domain  tcdate           oPlannedReceiptDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the planned receipt date
based on the planned delivery date:
1. If planned delivery date is unknown it will be the
current date.
2. The time needed for transportation is calculated forwards
from the planned delivery date. Except for the origins
production and production manual. Per definition the time
between planned delivery and planned receipt for production
is the routing time and not the transportation time.
3. A calendar correction is done on the ship to site.
Pre:    .a.
Post:   N.a.
Input:  iOrderOrigin - Order Origin; Mandatory
iTransactionType - Transaction Type; Mandatory
iShipFromAddress - Ship From Address; Mandatory
iShipToType - Ship To Type; Mandatory
iShipToCode - Ship To Code; Mandatory
iShipToAddress - Ship To Address; Mandatory
iShipToCompany - Ship To Company; Not Mandatory
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
iPlannedDeliveryDate - Planned Delivery Date; Not Mandatory
Output: oPlannedDeliveryDate - Planned Delivery Date
oPlannedReceiptDate - Planned Receipt Date
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Planned Dates calculated successfully
DALHOOKERROR - An error occurred when calculating Planned Dates
```
