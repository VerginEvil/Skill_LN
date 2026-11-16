# SalesOrderLine.CopyFromOriginalScheduleShipment

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 345-346

```baan
DLL:   tdextslsapi
This function is available from 2023.06 (KB2278226).
Syntax: long SalesOrderLine.CopyFromOriginalScheduleShipment(
domain  tcorno           iSalesReturnOrder,
domain  tdshpm           iOriginalShipment,
domain  tcyesno          iCopyAllLines,
long             iNrOfLinesToAdd,
const   domain  tcorno           iOriginalScheduleArray() fixed,
const   domain  tcpono           iOriginalInvoiceLineArray(),
ref             long             oNrOfLinesAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will copy the given sales schedule actual
delivery lines (shipment lines) to the sales return
order (iSalesReturnOrder).
Pre:    The given return order must exist.
LN Application sets retry-point, so not by caller
Post:   LN Application sets commit/abort transaction, so not by caller
Input:  iSalesReturnOrder       - The Sales Return Order to which the
sales schedule actual lines delivery
lines (shipment lines) will be
copied. Mandatory.
iOriginalShipment       - The shipment from which part or all of
the lines are to be returned. Mandatory.
iCopyAllLines           - Yes: This will copy all the lines of
the original shipment.
No:  Only a selection of lines will be
copied. These lines are identified
by the arguments below.
iNrOfLinesToAdd         - The number of lines that are to be
copied to the return order.
This argument is mandatory if
iCopyAllLines = No.
iOriginalScheduleArray - The sales schedule numbers from which the
lines will be copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalInvoiceLineArray
- The invoice line numbers of the original
actual delivery lines that will be
copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd
This array is allowed to be empty if
iCopyAllLines = Yes.
Output: oNrOfLinesAdded         - The number of lines added to the order.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Copy was successful
<> 0                    An error occurred
```
