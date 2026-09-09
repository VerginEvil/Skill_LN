# CustomerClaim.Submit

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1541-1541

```baan
DLL:   tsextcmmapi
This function is available from 2023.09 (KB2295922).
Syntax: long CustomerClaim.Submit(
domain  tcorno           iCustomerClaim,
ref             boolean          oLinesForRMA,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to submit a Customer Claim.
Note that because of the automatic processing of warehousing
orders, the system commits the database transactions in this
function.
Therefore, it is not necessary to set a db.retry.point()
before calling this function, and abort/commit after this
function, because that is already handled within this function.
Pre:    -
Post:   This function sets a retry-point and will commit/abort
the transaction.
When oLinesForRMA is true, Customer Claim Acknowledgements
might be printed.
Input:  iCustomerClaim
Customer Claim: Mandatory
Output: oLinesForRMA
When lines are set to Pending Material Return this
flag is set to true.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No error
<> 0    - An error occurred
```
