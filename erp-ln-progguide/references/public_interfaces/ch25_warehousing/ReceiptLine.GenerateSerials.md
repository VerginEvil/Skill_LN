# ReceiptLine.GenerateSerials

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1243-1245

```baan
DLL:   whextinhapi
This function is available from     2021.04 (KB2182070  ).
Syntax: long ReceiptLine.GenerateSerials(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This function generates Serial(s) for the given receipt line.
Irrespective of 'Consolidate Stock Points in one Receipt Line'
parameter, the Serial is always present in the Receipt Line
Stock Point Details (whinh320), both for items set as
'Serial In Inventory' as well as items not set as 'Serial in
Inventory'. If applicable, existing records with empty serial
numbers will be filled. Otherwise, new records will be created.
If 'Serial In Inventory' and the Consolidate parameter is not
active seperate receipt line(s) (whinh312) will be created per
Serial.
Otherwise, Serial(s) will be generated in the Receipt Line
Stock Point Details(whinh320) for the same receipt line.
Example: Receipt line, 3 pcs (Consolidate = No)
Generate Serial:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    SERIAL1 1 pcs      |    SERIAL1 1 pcs
| 20    SERIAL2 1 pcs      |    SERIAL2 1 pcs
| 30    SERIAL3 1 pcs      |    SERIAL3 1 pcs
Example: Receipt line, 3 pcs (Consolidate = Yes)
Generate Serial:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 3 pcs      |    SERIAL1 1 pcs
|                          |    SERIAL2 1 pcs
|                          |    SERIAL3 1 pcs
Now suppose the item is Lot Controlled and Serialized:
Example: Receipt line, 3 pcs (Consolidate = No)
Current values:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    LOT1    3 pcs      |    LOT1    3 pcs
Generate Serials:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    SERIAL1 LOT1 1 pcs |    SERIAL1 LOT1 1 pcs
| 20    SERIAL2 LOT1 1 pcs |    SERIAL2 LOT1 1 pcs
| 30    SERIAL3 LOT1 1 pcs |    SERIAL3 LOT1 1 pcs
Example: Receipt line, 3 pcs (Consolidate = Yes)
Current values:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    LOT1    3 pcs      |    LOT1    3 pcs
Generate Serial:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    LOT1    3 pcs      |    SERIAL1 LOT1 1 pcs
|                          |    SERIAL2 LOT1 1 pcs
|                          |    SERIAL3 LOT1 1 pcs
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
