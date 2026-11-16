# Call.TransferToServiceQuote

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Call
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1390-1391

```baan
DLL:   tsextclmapi
This function is available from 2025.09 (KB3614350).
Syntax: long Call.TransferToServiceQuote(
domain  tcorno           iCall,
long             iProcessingOptionSet,
ref     domain  tcyesno          oCallIsBlocked,
ref     domain  tcorno           oQuote,
ref     domain  tcpono           oQuoteRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to:
- Transfer a Call to a Quote for a Service Order
- Transfer a Call to a Quote for Part Maintenance
This function handles the transfer of a call to a service quote.
Before transferring the call, based on the blocking settings
defined in the Call Management parameters, it is checked if the
call must be blocked. When the call is set to blocked, the call
cannot be transferred and output argument oCallIsBlocked will
be set to Yes.
Pre:    Call ProcessingOptionSet.Create() to obtain iProcessingOptionSet.
Post:   Delete the option set by calling ProcessingOptionSet.Delete()
This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iCall
Call Number: Mandatory
iProcessingOptionSet
Processing Option Set: Mandatory, a processing option
set number, referring to a processing option set
containing at least one valid option.
NAME                           TYPE            DEFAULT
================================================================
QuoteType                       long            1
This defines to which type of Service Quote the Call
should be transferred to. When no correct value is
provided, the default value is 1.
Allowed values:
1 : Quote for a Service Order
2 : Quote for Part Maintenance
Output: oCallIsBlocked
Indicates if the call is set to blocked.
oQuote
The quote number to which the call is transferred.
oQuoteRevision
The quote revision to which the call is transferred.
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
