# InventoryCommitment.ConsumeFromBuffer

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 968-969

```baan
DLL:   whextinpapi
This function is available from 2025.07 (KB3568815).
Syntax: long InventoryCommitment.ConsumeFromBuffer(
domain  tcorno           iOrderNumberFrom,
domain  tcpono           iOrderLineFrom,
domain  whinp.corg       iOrderOriginTo,
domain  tcorno           iOrderNumberTo,
domain  tcpono           iOrderLineTo,
domain  tcpono           iOrderSequenceTo,
domain  tcpono           iBillOfMaterialLine,
domain  tcqiv1           iTransferQuantity,
domain  tccuni           iTransferUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function commits inventory that was previously reserved
in inventory buffers, to specific orders.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
Input:  iOrderNumberFrom        - Mandatory
iOrderLineFrom          - Optional
iOrderOriginTo          - Mandatory
The following values are allowed:
whinp.corg.sales
whinp.corg.production
whinp.corg.transfer
whinp.corg.transfer.man
whinp.corg.enterprise.plan
whinp.corg.prp
whinp.corg.schedule
whinp.corg.service
whinp.corg.maint.sales
whinp.corg.maint.work
whinp.corg.customer.claim
whinp.corg.supplier.claim
iOrderNumberTo          - Mandatory
iOrderLineTo            - Mandatory
iOrderSequenceTo        - Optional
iBillOfMaterialLine     - Optional
iTransferQuantity       - Mandatory
iTransferUnit           - Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No error has been detected.
Inventory Buffer is consumed.
<> 0                    - An Error is detected.
```
