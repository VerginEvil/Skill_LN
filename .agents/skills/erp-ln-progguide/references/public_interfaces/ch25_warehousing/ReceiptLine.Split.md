# ReceiptLine.Split

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1257-1257

```baan
DLL:   whextinhapi
This function is available from 2022.05 (KB2237101).
Syntax: long ReceiptLine.Split(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This public interface splits the given receipt line.
The given receipt line will be set to zero received quantity
and the existing details (like Stock Point Details and/or
Handling Units) will be moved to the next receipt line number
according to the step size defined in the master data set up.
For executing this public interface the same constraints apply
as for the corresponding option in the Infor LN Application.
If execution is not allowed a specified error message is returned.
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
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
