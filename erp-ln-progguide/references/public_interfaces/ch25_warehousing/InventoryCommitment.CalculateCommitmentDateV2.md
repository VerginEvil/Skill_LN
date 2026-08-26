# InventoryCommitment.CalculateCommitmentDateV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 953-954

```baan
DLL:   whextinpapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long InventoryCommitment.CalculateCommitmentDateV2(
domain  whinp.corg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tctrns.date      iPlannedDeliveryDate,
ref     domain  tctrns.date      oCommitmentDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the commitment date.
If generation of inventory commitment is based on planned
delivery date (whinp000.icbo), then this function will return
zero as Commitment Date.
Input:  iOrderOrigin                          - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderLine                                    - Order Line
iWarehouse                                    - Warehouse (Mandatory)
iItem                                         - Item (Mandatory)
iPlannedDeliveryDate                          - PlannedDeliveryDate (Mandatory)
Output: oCommitmentDate                       - Commitment Date
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error has been detected.
<> 0                                          - An Error is detected.
```
