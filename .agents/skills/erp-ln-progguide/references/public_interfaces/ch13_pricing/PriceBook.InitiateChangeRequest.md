# PriceBook.InitiateChangeRequest

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for PriceBook
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 525-526

```baan
DLL:   tdextpcgapi
This function is available from 2026.08 (KB3683341).
Syntax: long PriceBook.InitiateChangeRequest(
domain  tdpcg.prbk       iPriceBook,
ref     domain  tdpcg.prbk       oChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function handles the initiation of a change request for the
given price book.
The initiation consists of two parts:
1. Determine if initiate change request is allowed.
2. Initiate the change request.
Pre:    Caller must set retry-point
Post:   Caller must set commit/abort transaction
Input:  iPriceBook              Price Book (Mandatory)
Output: oChangeRequest          New Change Request
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> The change request has been initiated
<> 0    -> An error occurred
```
