# ReceiptLine.GenerateLots

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1242-1243

```baan
DLL:   whextinhapi
This function is available from     2021.04 (KB2182070  ).
Syntax: long ReceiptLine.GenerateLots(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will generate lot code(s) for a given
receipt line.
Irrespective of 'Consolidate Stock Points in one Receipt Line'
parameter, the lot is always present in the Receipt Line
Stock Point Details (whinh320), both for items set as 'Lot in
Inventory' as well as items not set as 'Lot in Inventory'.
If applicable, existing records with empty lot codes will be
filled with the generated Lot Code.
Unlike serials, the receipt line will never be split as a
result of lot generation (because a serial quantity is always 1)
Example: Receipt line, 3 pcs (Consolidate = No)
Generate Lot:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    LOT1    3 pcs      |    LOT1    3 pcs
Example: Receipt line, 3 pcs (Consolidate = Yes)
Generate Lot:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    LOT1    3 pcs      |    LOT1    3 pcs
Now suppose the item is Lot Controlled and Serialized:
Example: Receipt line, 3 pcs (Consolidate = No)
Current values:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    SERIAL1 1 pcs      |    SERIAL1 1 pcs
| 20    SERIAL2 1 pcs      |    SERIAL2 1 pcs
| 30    SERIAL3 1 pcs      |    SERIAL3 1 pcs
Generate Lot: (new lot per receipt line!)
| 10    SERIAL1 LOT1 1 pcs |    SERIAL1 LOT1    1 pcs
| 20    SERIAL2 LOT2 1 pcs |    SERIAL2 LOT2    1 pcs
| 30    SERIAL3 LOT3 1 pcs |    SERIAL3 LOT3    1 pcs
Example: Receipt line, 3 pcs (Consolidate = Yes)
current values:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 3 pcs      |    SERIAL1 1 pcs
|                          |    SERIAL2 1 pcs
|                          |    SERIAL3 1 pcs
Generate Lot:
| 10    (empty) LOT1 3 pcs |    SERIAL1 LOT1    1 pcs
|                          |    SERIAL2 LOT1    1 pcs
|                          |    SERIAL3 LOT1    1 pcs
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iReceipt                              - Mandatory
iReceiptLine                                  - Mandatory
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
