# SalesOrderInvoiceLine.ReadInvoicingStatusDescription

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderInvoiceLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 365-366

```baan
DLL:   tdextslsapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long SalesOrderInvoiceLine.ReadInvoicingStatusDescription(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcpono           iSalesActualDeliverySequence,
domain  tcpono           iInvoiceLine,
ref     domain  tcdsca           oDescription mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the description of the status in
Invoicing for the given sales order line/sales order invoice
line.
Note: The returned value in oDescription is intended for
feedback to a user, not for decision making within the software
itself.
Pre:    None
Post:   None
Input:  iSalesOrder                           - Sales Order (Mandatory)
iSalesOrderLine                               - Sales Order Line (Mandatory)
iSalesOrderLineSequence                       - Sales Sequence number (must be >= 0)
iSalesActualDeliverySequence
-                                               Sales Actual Delivery Sequence number
(Optional)
If iSalesActualDeliverySequence and
iInvoiceLine are both 0, then the
output will be based on all actual
delivery lines/invoice lines that
have been released to invoicing.
iInvoiceLine                                  - Invoice Line (Optional)
If iSalesActualDeliverySequence and
iInvoiceLine are both 0, then the
output will be based on all actual
delivery lines/invoice lines that
have been released to invoicing.
Output: oDescription                          - The description of the status in
Invoicing.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Function was executed successful
<> 0                                          - An error occurred during execution of
the function.
```
