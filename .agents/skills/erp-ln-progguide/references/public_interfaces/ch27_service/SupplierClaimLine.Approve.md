# SupplierClaimLine.Approve

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SupplierClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1550-1551

```baan
DLL:   tsextcmmapi
This function is available from 2022.10 (KB2262990).
Syntax: long SupplierClaimLine.Approve(
domain  tcorno           iSupplierClaim,
domain  tcpono           iClaimLine,
boolean          iAllowToUpdateHeaderStatus,
domain  tsmdm.text       iApprovalText,
domain  tccdis           iApprovalDecision,
domain  tscmm.actn       iApprovalAction,
domain  tclogn           iApprovedBy,
domain  tcdate           iApprovalDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Approve one specific Supplier Claim Line
(tscmm210 record). See functionality when a Supplier Claim
Line is Approved with session 'Supplier Claim Lines'
(tscmm2110m000).
Note that approval is not allowed on line level for the
scenarios below:
* If Supplier Claim Document Approval is set on the claim.
* If Workflow is active for supplier claims
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input   : iSupplierClaim                - The Supplier Claim
Mandatory
iClaimLine                    - The Claim Line
Mandatory
iAllowToUpdateHeaderStatus
- If true, and the approved
Claim Line is the last one,
the Claim header status is
set to Approved as well.
iApprovalText                 - The Approval Text,
A valid text number.
Not mandatory.
iApprovalDecision             - The Approval Decision.
Note that only a reason code of
type 'Claim Approval' which is
valid on the current date is
allowed.
Not mandatory.
iApprovalAction               - The Approval Action.
Not mandatory.
iApprovedBy                   - The login code of the user who
is approving the line.
Mandatory.
iApprovalDate                 - The Approval Date
Mandatory
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
