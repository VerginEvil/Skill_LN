# Call.ViewInvoice

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1393-1394

```baan
DLL:   tsextclmapi
This function is available from 2026.08 (KB3676476).
Syntax: long Call.ViewInvoice(
domain  tcorno           iCall,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Call Invoicing (tsclm1105s000)
for the invoice related to the given Call.
Input:
iCall
The Call to display the invoice for. (Mandatory)
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
