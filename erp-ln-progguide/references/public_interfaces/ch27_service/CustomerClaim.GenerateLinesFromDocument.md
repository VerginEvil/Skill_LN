# CustomerClaim.GenerateLinesFromDocument

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1537-1537

```baan
DLL:   tsextcmmapi
This function is available from 2025.06 (KB3555637).
Syntax: long CustomerClaim.GenerateLinesFromDocument(
domain  tcorno           iCustomerClaim,
ref             boolean          oClaimLinesGenerated,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to generate Claim Lines under the given
Customer Claim based on the lines under the Sales Document
linked to this Customer Claim.
Pre:    db.retry.point set
Post:   commit/abort transaction
Input:  iCustomerClaim
Customer Claim: Mandatory
This Customer Claim must be linked to a Sales Document
and can not have any existing Claim Lines that were
copied from a Sales Document.
Output: oClaimLinesGenerated
When at least one new Claim Line has been generated this
flag is set to true.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0
No Error; transaction can be committed.
<> 0
Error situation; transaction should be aborted.
```
