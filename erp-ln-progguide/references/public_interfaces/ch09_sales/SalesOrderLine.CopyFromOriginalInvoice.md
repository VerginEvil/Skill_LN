# SalesOrderLine.CopyFromOriginalInvoice

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 341-342

```baan
DLL:   tdextslsapi
This function is available from     2020.08 (KB2135988  ).
Syntax: long SalesOrderLine.CopyFromOriginalInvoice(
domain  tcorno           iSalesReturnOrder,
domain  tcncmp           iInvoiceCompany,
domain  tcttyp           iInvoiceTransactionType,
domain  tcinvn           iOriginalInvoiceNumber,
domain  tcyesno          iCopyAllLines,
long             iNrOfLinesToAdd,
const   domain  tcorno           iOriginalSalesOrderArray() fixed,
const   domain  tcpono           iOriginalLineArray(),
const   domain  tcpono           iOriginalSequenceArray(),
const   domain  tcpono           iOriginalActualDeliverySequenceArray(),
const   domain  tcpono           iOriginalInvoiceLineArray(),
domain  tcyesno          iCopyFromHistory,
ref             long             oNrOfLinesAdded,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will copy the given sales order invoice lines
to the sales return order (iSalesReturnOrder).
Pre:    The given return order must exist.
Post:   This function sets a retry              -point and will commit and/or abort
the transaction.
Input:  iSalesReturnOrder                     - The Sales Return Order to which the
order lines will be copied. Mandatory.
iInvoiceCompany                               - The company number of the invoice
iOriginalInvoiceNumber. Mandatory.
iInvoiceTransactionType                       - The transaction type of the invoice
iOriginalInvoiceNumber.
iOriginalInvoiceNumber                        - The invoice number from which part or all of
the lines are to be returned. Mandatory.
iCopyAllLines                                 - Yes: This will copy all the lines of
the original invoice.
No:  Only a selection of lines will be
copied. These lines are identified
by the arguments below.
iNrOfLinesToAdd                               - The number of lines that are to be
copied to the return order.
This argument is mandatory if
iCopyAllLines = No.
iOriginalSalesOrderArray                       - The sales order numbers from which the
lines will be copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalLineArray                            - The line numbers of the original invoice
lines that will be copied. The
number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalSequenceArray                        - The sequence numbers of the original
invoice lines that will be copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalActualDeliverySequenceArray
-                                               The actual delivery sequence numbers
of the original invoice lines
that will be copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iOriginalInvoiceLineArray
-                                               The invoice line numbers of the original
invoice lines that will be copied.
The number of entries in this array must
be equal to iNrOfLinesToAdd.
This array is allowed to be empty if
iCopyAllLines = Yes.
iCopyFromHistory                              - Not used
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
