# SalesOrderLine.GetComponentAndSalesSequence

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 348-349

```baan
DLL:   tdextslsapi
This function is available from     2025.04 (KB3568308  ).
Syntax: long SalesOrderLine.GetComponentAndSalesSequence(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequenceOrComponentSequence,
ref     domain  tcpono           oSalesOrderLineSequence,
ref     domain  tcpono           oSalesOrderLineComponentSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines sales order line- sequence and component
sequence based on the data in the given input fields.
Pre:    Not applicable
Post:   Not applicable
Input:  iSalesOrder                                   - Sales Order (mandatory)
iSalesOrderLine                                       - Sales Order Line (mandatory)
iSalesOrderLineSequenceOrComponentSequence
-                                                       Sales Order Line- Sequence Number
or Component Sequence Number
Output: oSalesOrderLineSequence                       - Sequence Number of the Sales
Order Line
oSalesOrderLineComponentSequence                      - Component Sequence Number of the
Sales Order Line
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - No error
<> 0                                                  - Error occurred
```
