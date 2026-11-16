# ReceiptLine.GenerateHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1250-1251

```baan
DLL:   whextinhapi
This function is available from 2022.01 (KB2212523).
Syntax: long ReceiptLine.GenerateHandlingUnits(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This function generates handling units for the given receipt
line.
Generating handling units is allowed when:
- Receipt line is open or confirmed but not yet advised;
- No handling unit is present on the receipt line;
- Handling units are in use in the receipt area for the
combination of item and warehouse.
If receipt line package definition is known, generated handling
unit structure will follow this package definition.
Generated handling unit(s) will be stored in the entity Receipt
Line Handling Units (whinh324).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
