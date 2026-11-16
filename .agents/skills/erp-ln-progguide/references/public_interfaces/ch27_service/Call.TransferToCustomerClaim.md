# Call.TransferToCustomerClaim

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1381-1381

```baan
DLL:   tsextclmapi
This function is available from 2024.12 (KB3542116).
Syntax: long Call.TransferToCustomerClaim(
domain  tcorno           iCall,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oCustomerClaim,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the transfer of a call to a customer claim.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked
will be set to Yes.
Pre:    None.
Post:   This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iCall
Call Number: Mandatory
Output: oCallIsBlocked
Indicates if the call is set to blocked.
oCustomerClaim
The customer claim number to which the call is
transferred.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0    :  Transfer successful or Call is Blocked
<> 0 :  Error occurred
```
