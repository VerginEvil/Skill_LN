# ReceiptLine.GenerateHandlingUnitsV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1241-1242

```baan
DLL:   whextinhapi
This function is available from     2022.08 (KB2233913  ).
Syntax: long ReceiptLine.GenerateHandlingUnitsV2(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  whhuid           iReceiptHandlingUnit,
domain  whhuid           iReceiptLineHandlingUnit,
domain  whwmd.pkdf       iPackageDefinition,
domain  tcitem           iPackagingItem,
domain  tcqiv1           iPackagingItemQuantity,
ref             long             oNumberReceiptLineHandlingUnits,
ref     domain  whhuid           oReceiptLineHandlingUnitsArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl  : This function generates handling units for the given receipt
line.
Generating handling units is allowed when:
-                       Receipt line is open or confirmed but not yet advised;
-                       No handling unit is present on the receipt line;
-                       Handling units are in use in the receipt area for the
combination of item and warehouse.
If iPackageDefinition is not empty handling unit will be
generated using this package definition; otherwise receipt line
package definition will be used.
Generated handling unit(s) will be stored in the entity Receipt
Line Handling Units (whinh324).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iReceipt                              - Mandatory
iReceiptLine                                  - Mandatory
iReceiptHandlingUnit                       - Receipt Header handling unit.
Optional
iReceiptLineHandlingUnit                       - Receipt Line handling unit.
Optional
iPackageDefinition                            - Package Definition Optional
iPackagingItem                                - Packaging Item Optional
iPackagingItemQuantity                        - Quantity of packaging items
Mandatory if packaging item is not empty
Output: oNumberReceiptLineHandlingUnits               - number of handling units which
are generated for Receipt Line.
oReceiptLineHandlingUnitsArray                       - array with generated handling
units.
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
