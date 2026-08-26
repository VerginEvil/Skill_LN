# HandlingUnit.Transfer

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1057-1058

```baan
DLL:   whextwmdapi
This function is available from     2024.09 (KB3518395  ).
Syntax: long HandlingUnit.Transfer(
domain  tcseri           iSeries,
domain  tccopt           iOrderType,
domain  whhuid           iHandlingUnit,
domain  tcncmp           iShipToCompany,
domain  tctyps           iShipToType,
domain  tccshp           iShipToCode,
domain  whloca           iShipToLocation,
domain  tccprj           iProject,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will support direct transfer of handling
unit from one warehouse/location to another.
Both intra                      - and inter warehouse transfers are supported.
Handling unit must have status In Stock.
Pre:    NA
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSeries               - Series for transfer order to be created (Optional)
iOrderType                       - Order  type for transfer order to be created
(Optional)
iHandlingUnit                       - Handling Unit (Mandatory)
iShipToCompany                       - Transfer To Company (Optional, current
company will used if 0)
iShipToType                       - Transfer To Type (Mandatory, only value
tctyps.warehouse is allowed)
iShipToCode                       - Transfer To Code (Mandatory)
iShipToLocation                       - Transfer To Location (Mandatory if
iShipToCode is warehouse with locations and
iHandlingUnit contains location                               -controlled item)
iProject                       - Project (Must be empty when project pegging is
not implemented)
iElement                       - Project Element (Must be empty when project pegging
is not implemented)
iActivity                       - Project Activity (Must be empty when project pegging
is not implemented)
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0               - Handling Unit has been transferred successfully
DALHOOKERROR                       - Otherwise.
```
