# SalesOrderLine.ConfirmBackorderLine

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 341-342

```baan
DLL:   tdextslsapi
This function is available from 2020.11 (KB2151968).
Syntax: long SalesOrderLine.ConfirmBackorderLine(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcsite           iSite,
boolean          iManualConfirm,
ref             boolean          oBackorderLineConfirmed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This functions handles the confirmation of the backorder line.
When iManualConfirm is set to false the parameter
Confirm Back Orders Automatically is checked if the
backorder line should be processed automatically.
If Confirm Back Orders Automatically is not set to automatically
the process stops without error.
In case iManualConfirm is set to true, the parameter
Confirm Back Orders Automatically is not checked.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (Mandatory)
iSalesOrderLine         - Sales Order Line (Mandatory)
iSalesOrderSequence     - Sales Sequence number ( must be >= 0)
iSite                   - Site of the Sales Order Line
iManualConfirm          - Backorder line is manually confirmed
(True/False)
or via a process.
Output: oBackorderLineConfirmed - Backorder Line is confirmed
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Confirm successful or confirm not required.
<> 0                    Error during confirm occurred.
```
