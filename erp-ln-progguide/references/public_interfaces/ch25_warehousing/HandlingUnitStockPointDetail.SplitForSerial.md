# HandlingUnitStockPointDetail.SplitForSerial

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStockPointDetail
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1289-1289

```baan
DLL:   whextwmdapi
This function is available from 2025.02 (KB3541323).
Syntax: long HandlingUnitStockPointDetail.SplitForSerial(
domain  whhuid           iHandlingUnit,
domain  tcmcs.long       iDistributionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface splits handling unit stock point detail
with serialized item in multiple stock point details.
Split is allowed when:
Serial is empty and Stock Point Detail quantity is greater than
1.0.
Handling Unit Status is equal to:
- ToInspect and inspection is not yet started;
- Staged and expected not shipped quantity is 0.0;
- Allocated, Partial Allocated, Partial Released or
Released and handling unit is linked to the one order line only.
- All other statuses except Shipment Frozen, Partial Frozen,
Confirming, Shipped, Closed and Inactive.
Handling unit with serial in inventory item must be generated
according to the package definition template
which allows multiple stock points at the bottom level.
In case multiple stock points are not allowed a separate handling
unit must be generated for each serial number.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iHandlingUnit           - Handling Unit (mandatory)
iDistributionSequence   - Handling Unit Stock Point Detail
Distribution Sequence (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
