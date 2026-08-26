# SalesOrderLine.CopyFromOriginalOrder

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 342-343

```baan
DLL:   tdextslsapi
This function is available from     2020.08 (KB2135988  ).
Syntax: long SalesOrderLine.CopyFromOriginalOrder(
domain  tcorno           iSalesReturnOrder,
domain  tcorno           iOriginalSalesOrder,
domain  tcyesno          iCopyAllLines,
long             iNrOfLinesToAdd,
const   domain  tcpono           iOriginalLineArray(),
const   domain  tcpono           iOriginalSequenceArray(),
domain  tcyesno          iCopyFromHistory,
ref             long             oNrOfLinesAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will copy the given sales order lines to the
sales return order (iSalesReturnOrder).
Pre:    The given return order must exist.
Post:   This function sets a retry              -point and will commit and/or abort
the transaction.
Input:  iSalesReturnOrder                     - The Sales Return Order to which the
order lines will be copied. Mandatory.
iOriginalSalesOrder                           - The sales order from which the lines
will be copied. Mandatory.
iCopyAllLines                                 - Yes: This will copy all the lines of
the original sales order.
(Note that Total lines and
backorder lines are excluded from
this.)
No:  Only a selection of lines will be
copied. These lines are identified
by the arguments below.
iNrOfLinesToAdd                               - The number of lines that are to be
copied to the return order.
This argument is mandatory if
iCopyAllLines = No.
iOriginalLineArray                            - The line numbers of the original order
lines that will be copied. The
number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalSequenceArray                        - The sequence numbers of the original
order lines that will be copied. The
number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iCopyFromHistory                              - Yes: Copies the lines from the sales
order line history table.
No:  Copies the lines from the actual
sales order line table.
Output: oNrOfLinesAdded                       - The number of lines added to the order.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Copy was successful
<> 0                    An error occurred
```
