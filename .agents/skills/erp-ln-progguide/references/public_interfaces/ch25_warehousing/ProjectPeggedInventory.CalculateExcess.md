# ProjectPeggedInventory.CalculateExcess

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectPeggedInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1229-1229

```baan
DLL:   whextwmdapi
This function is available from 2026.08 (KB3685005).
Syntax: long ProjectPeggedInventory.CalculateExcess(
domain  tccwar           iWarehouseFrom,
domain  tccwar           iWarehouseTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will calculate the excess for the
project pegged inventory.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iWarehouseFrom          - Optional
iWarehouseTo            - Mandatory
iItemFrom               - Optional
iItemTo                 - Mandatory
Output: oDataProcessed          - true:  Excess Calculated.
false: Nothing Calculated.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
