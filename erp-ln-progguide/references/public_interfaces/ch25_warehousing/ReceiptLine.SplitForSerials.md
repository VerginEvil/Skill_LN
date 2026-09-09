# ReceiptLine.SplitForSerials

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1259-1261

```baan
DLL:   whextinhapi
This function is available from 2022.05 (KB2237101).
Syntax: long ReceiptLine.SplitForSerials(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
boolean          iGenerateSerials,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This public interface splits the receipt line (or the stock
point details) into seperate lines for each serial.
Depending on the parameter 'Consolidate Stock Points in one
Receipt Line' this public interface has a different result.
If the parameter value is No and the item is 'Serialized in
Inventory', the receipt line will be split into seperate
receipt lines per piece.
If the parameter value is Yes, the receipt line stock point
details will be split into seperate sequences per piece.
If the option iGenerateSerials is True, the serial numbers will
be generated as well, in both situations.
If the item is not set as 'Serialized in inventory', this option
is not allowed.
For executing this public interface the same constraints apply
as for the corresponding option in the Infor LN Application.
If execution is not allowed a specified error message is returned.
Example:
- Receipt line, 3 pcs, Serial In Inventory
- Consolidate Stock Points in one Receipt Line = No
- iGenerateSerials = true
Split Line for Serials:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    SERIAL1 1 pcs      |    SERIAL1 1 pcs
| 20    SERIAL2 1 pcs      |    SERIAL2 1 pcs
| 30    SERIAL3 1 pcs      |    SERIAL3 1 pcs
Example:
- Receipt line, 3 pcs, Serial In Inventory
- Consolidate Stock Points in one Receipt Line = No
- iGenerateSerials = false
Split Line for Serials:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    " "     1 pcs      |    " "     1 pcs
| 20    " "     1 pcs      |    " "     1 pcs
| 30    " "     1 pcs      |    " "     1 pcs
Example:
- Receipt line, 3 pcs, Serial In Inventory
- Consolidate Stock Points in one Receipt Line = Yes
- iGenerateSerials = true
Split Line for Serials:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 3 pcs      |    SERIAL1 1 pcs
|                          |    SERIAL2 1 pcs
|                          |    SERIAL3 1 pcs
Example:
- Receipt line, 3 pcs, Serial In Inventory
- Consolidate Stock Points in one Receipt Line = Yes
- iGenerateSerials = false
Split Line for Serials:
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 3 pcs      |    ""      1 pcs
|                          |    ""      1 pcs
|                          |    ""      1 pcs
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
iGenerateSerials        - If true, (empty) serial numbers
will be generated per receipt line
and/or stock point detail split.
Output: oNumberOfReceiptLines   - Number of receipt lines in array
after split.
oReceiptLineArray       - Array of created receipt lines during
splitting (excluding iReceiptLine).
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
