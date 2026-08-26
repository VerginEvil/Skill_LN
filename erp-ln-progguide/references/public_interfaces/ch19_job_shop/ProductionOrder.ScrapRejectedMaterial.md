# ProductionOrder.ScrapRejectedMaterial

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 769-770

```baan
DLL:   tiextsfcapi
This function is available from     2021.12 (KB2198728  ).
Syntax: long ProductionOrder.ScrapRejectedMaterial(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iMaterialPosition,
domain  tiqep2           iQuantityToScrap,
domain  tcibd.sern       iSerialNumber,
domain  tcuef.effn       iEffectivityUnit,
domain  tcclot           iLotCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to scrap a quantity of rejected
material of an operation, as in session tisfc0213m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory and must be
in iSite).
iMaterialPosition       MaterialPosition (Mandatory).
iQuantityToScrap        Quantity to Scrap (Mandatory).
When the Serial Number is not empty,
this value must be 1.0.
iSerialNumber           The Serial Number (Optional).
Should exist if given.
iEffectivityUnit        Effectivity Unit (Optional).
iLotCode                Lot Code (Optional).
Should exist if given.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Rejected quantity is scrapped.
<> 0                    Rejected quantity was not scrapped.
```
