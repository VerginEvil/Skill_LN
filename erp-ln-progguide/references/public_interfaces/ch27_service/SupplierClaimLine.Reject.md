# SupplierClaimLine.Reject

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SupplierClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1551-1552

```baan
DLL:   tsextcmmapi
This function is available from 2022.10 (KB2262990).
Syntax: long SupplierClaimLine.Reject(
domain  tcorno           iSupplierClaim,
domain  tcpono           iClaimLine,
boolean          iAllowToUpdateHeaderStatus,
domain  tclogn           iRejectedBy,
domain  tccdis           iRejectionReason,
domain  tcdate           iRejectionDate,
domain  tsmdm.text       iRejectionText,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Reject one specific Supplier Claim Line
(tscmm210 record). See functionality when a Supplier Claim
Line is Rejected with session Reject Supplier Claim
(tscmm2220m000).
When manually Rejecting the last claim line, a question is
asked whether to set the header status to Rejected as well.
This behavior can be controlled with the use of argument
iAllowToUpdateHeaderStatus.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   : iSupplierClaim                - The Supplier Claim
Mandatory
iClaimLine                    - The Claim Line
Mandatory
iAllowToUpdateHeaderStatus
- If true, and the rejected
Claim Line is the last one,
the Claim header status is
set to Rejected as well.
iRejectedBy                   - The login code of the user who
is rejecting.
Mandatory.
iRejectionReason              - The Rejection Reason.
Note that only a reason code of
type Claim Rejection which is
valid on the current date is
allowed.
Mandatory.
iRejectionDate                - The Rejection Date
Mandatory
iRejectionText                - The Rejection Text,
A valid text number.
Not mandatory.
Output  : oExceptionMessage             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                             - No error
<> 0                          - An error occurred
```
