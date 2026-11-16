# ReceiptLine.SplitForLotsBatches

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1257-1259

```baan
DLL:   whextinhapi
This function is available from 2022.05 (KB2237101).
Syntax: long ReceiptLine.SplitForLotsBatches(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
boolean          iGenerateLots,
domain  tcqiv1           iSplitSize,
domain  tcpono           iSplitNumber,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This public interface splits the receipt line (or the stock
point details) into seperate lines for each lot / batch size.
Dependent on the 'Consolidate Stock Points in one Receipt Line'
parameter, this public interface has a different result.
If the parameter value is No this function splits the receipt
line and creates seperate receipt lines according to the Split
Size and Split Number.
If the parameter value is Yes, it does not split the receipt
line but splits the related Stock Point Details accordingly.
Optionally, if the iGenerateLots is True lot codes will be
generated for each created receipt line or detail line.
The Split Size and Split Number are optional arguments and
either one can be calculated based on the receipt quantity and
the value of the other argument.
If both Split Size and Split Number are empty, the default Size
is determined from the Default Lot Size defined in session
"Item-Warehousing" (whwmd4600m000) or
"Items-Warehousing by Site" (whwmd4604m000).
But in the end both variables are needed for executing the split
If it is not possible to determine the Split Size and Number
an error message will be returned.
For executing this public interface the same constraints apply
as for the corresponding option in the Infor LN Application.
If execution is not allowed a specified error message is returned.
Example:
- Receipt Quantity = 30
- Consolidate Stock Points in one Receipt Line = Yes
- iGenerateLots = True, iSplitSize = 10, iSplitNumber = 3
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 30 pcs     |    LOT1    10 pcs
|                          |    LOT2    10 pcs
|                          |    LOT3    10 pcs
Example:
- Receipt Quantity = 30
- Consolidate Stock Points in one Receipt Line = No
- iGenerateLots = False, iSplitSize = 10, iSplitNumber = 3
---------------------------------------------------------------
| Receipt Line (whinh312)  |    Stock Point Details (whinh320)
---------------------------------------------------------------
| 10    (empty) 10 pcs   |      (empty) 10 pcs
| 20    (empty) 10 pcs   |      (empty) 10 pcs
| 30    (empty) 10 pcs   |      (empty) 10 pcs
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
iGenerateLots           - - If true and the item is defined as
'Lot in Inventory', lot codes will be
generated per receipt line and/or
stock point detail split.
iSplitSize              - The lot/batch size of the split
(optional).
If empty, Split Size is determined via
receipt quantity and Split Number.
If both split size and number are empty,
the default Size is determined from the
Item-Warehousing.
iSplitNumber            - The number of lots/batches to be split
(optional)
If empty, Split Number is determined via
receipt quantity and Split Size.
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
