# SalesOrderInvoiceLine.ReleaseToInvoicing

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderInvoiceLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 368-369

```baan
DLL:   tdextslsapi
This function is available from 2021.01 (KB2162644).
Syntax: long SalesOrderInvoiceLine.ReleaseToInvoicing(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcpono           iInvoiceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the release of a sales order invoice line
to Invoicing.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (Mandatory)
iSalesOrderLine         - Sales Order Line (Mandatory)
iSalesOrderLineSequence - Sales Sequence number (must be >= 0)
iInvoiceLine            - Invoice Line (must be >= 0)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Release successful
<> 0                    - Error during release occurred
```
