# Call.CreateInvoice

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1376-1376

```baan
DLL:   tsextclmapi
This function is available from 2026.08 (KB3676476).
Syntax: long Call.CreateInvoice(
domain  tcorno           iCall,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates and creates an invoice line for the
given call.
Pre:    A db.retry.point() must have been specified.
Post:   An abort.transaction() or commit.transaction() must be executed.
Input:  iCall
The Call for which an invoice line must be created.
(Mandatory)
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                       - No error
<> 0                    - An error occurred.
```
