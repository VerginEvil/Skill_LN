# IntercompanyTradeOrder.PostTransactionLine

> Chapter: Chapter 5 Public Interfaces for IntercompanyTrade
>
> Group: Public Interfaces for IntercompanyTradeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 161-161

```baan
DLL:   tcextitrapi
This function is available from 2025.05 (KB3568989).
Syntax: long IntercompanyTradeOrder.PostTransactionLine(
domain  tcncmp           iTradeOrderCompany,
domain  tcorno           iTradeOrder,
domain  tcpono           iTradeOrderLine,
domain  tcpono           iTradeOrderTransactionLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will post the transaction line for the
given intercompany trade order.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success.
Abort the transaction in case of failure.
Input:  iTradeOrderCompany      - Mandatory
iTradeOrder             - Mandatory
iTradeOrderLine         - Mandatory
iTradeOrderTransactionLine - Mandatory
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0 - Transaction line has been processed successfully
<> 0 - Error.
```
