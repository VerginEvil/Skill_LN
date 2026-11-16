# InventoryCommitment.CalculateCommitmentDate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 963-963

```baan
DLL:   whextinpapi
This function is available from 2023.12 (KB2310180).
Syntax: long InventoryCommitment.CalculateCommitmentDate(
domain  whinp.corg       iOrderOrigin,
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
Note: In order to calculate the commitment date related to
Rental Orders correctly version 2 of this function is created.
For new implementations it is recommended to always use this
new function. For existing implementations it is only required
to switch to this new version when Rental Order functionality
in combination with item type Rental Product is used.
Input:  iOrderOrigin            - Order Origin (Mandatory)
iWarehouse              - Warehouse (Mandatory)
iItem                   - Item (Mandatory)
iPlannedDeliveryDate    - PlannedDeliveryDate (Mandatory)
Output: oCommitmentDate         - Commitment Date
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No error has been detected.
<> 0                    - An Error is detected.
```
