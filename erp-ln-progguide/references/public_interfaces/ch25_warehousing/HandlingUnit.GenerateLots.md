# HandlingUnit.GenerateLots

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1047-1047

```baan
DLL:   whextwmdapi
This function is available from 2022.01 (KB2212523).
Syntax: long HandlingUnit.GenerateLots(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will generate lot(s) for the handling
unit.
Generating lot code for the handling unit is allowed when:
- iHandlingUnit has status Inactive, Open or Receipt Open.
- iHandlingUnit contains lot-controlled item(s).
- iHandlingUnit does not contain lots.
- iHandlingUnit with a status Receipt Open is not in transit.
When handling unit has status Receipt Open, generated lots
will be also stored in the table Receipt Line Stock Point
Details (whinh320).
Example:
Handling Unit HU1 contains 3 pieces of item.
Item is lot-controlled and serialized.
Serials SER1, SER2 and SER3 are already stored in handling unit.
Lot LOT1 is generated.
---------------------------------------------------------------
| HU stock point details   |    Receipt Line
| (whwmd536)               |    Stock Point Details (whinh320)
---------------------------------------------------------------
| HU1 LOT1 SER1 1 pcs      |    LOT1    SER1    1 pcs
| HU1 LOT1 SER2 1 pcs      |    LOT1    SER2    1 pcs
| HU1 LOT1 SER3 1 pcs      |    LOT1    SER3    1 pcs
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - for this handling unit the lot code will
be generated (Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Lot is generated and linked to iHandlingUnit.
<> 0    - Error
```
