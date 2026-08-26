# CustomerClaim.Close

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaim
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1521-1522

```baan
DLL:   tsextcmmapi
This function is available from     2023.01 (KB2267965  ).
Syntax: long CustomerClaim.Close(
const   domain  tcorno           iCustomerClaim fixed,
const   domain  tcyesno          iMoveClaimToHistory,
const   domain  tcyesno          iDeleteClaim,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Close one specific Customer Claim
(tscmm100 record). See functionality when a Customer Claim
is Closed with session 'Close Customer Claims' (tscmm1250m000).
Note that even if the iCustomerClaim already has the status
'Closed', this function can still be called because of the fact
that the claim still needs to be moved to the history or
should be deleted.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iCustomerClaim
The customer claim which needs to be closed, moved to
history or needs to be deleted.
(mandatory)
iMoveClaimToHistory
Indicator whether the claim should be moved to history
after its status is changed to 'Closed'. Note that if
customer claim history is not implemented, then the
claim cannot be moved to history, so in that situation
when iMoveClaimToHistory is set to 'tcyesno.yes', the
claim will not be moved to the history tables.
(mandatory)
iDeleteClaim
Indicator whether the claim should be deleted after its
status is changed to 'Closed'.
Note that if customer claim history is implemented and
if the iMoveClaimToHistory is set to 'tcyesno.no' and
the iDeleteClaim is set to 'tcyesno.yes', then the
claim will not be deleted. This is in line with how the
session tscmm1250m000 is handling this.
(mandatory)
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Customer Claim status is set to 'Closed' or the
status was already 'Closed', but the claim is moved
to history and/or is deleted without errors.
<> 0                          - Error during closing the claim.
```
