# CustomerClaimLine.Approve

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1542-1543

```baan
DLL:   tsextcmmapi
This function is available from 2023.06 (KB2288749).
Syntax: long CustomerClaimLine.Approve(
domain  tcorno           iCustomerClaim,
domain  tcpono           iClaimLine,
domain  tccdis           iApprovalReason,
domain  tcdate           iApprovalDate,
domain  tsmdm.text       iApprovalText,
domain  tscmm.actn       iApprovalAction,
domain  tclogn           iApprovedBy,
domain  tcyesno          iUpdateHeaderStatus,
domain  tcyesno.c        iReleaseMaterials,
domain  tcyesno          iIgnoreCanceledSupplierClaim,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this function to Approve one specific Customer Claim Line.
See functionality when a Customer Claim Line is Approved with
session Customer Claim Lines (tscmm1110m000).
Note that approval is not allowed on line level for the
following scenarios:
* If Customer Claim Document Approval is set on the claim;
* If Workflow is active for Customer Claims.
Pre:    -
Post:   This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iCustomerClaim
Customer Claim: Mandatory
iClaimLine
Claim Line: Mandatory
iApprovalReason
Approval Reason. Note that only a reason code of
type Claim Approval which is valid on the current
date is allowed.
Mandatory when Customer Claim Document Approval is Yes,
or when Workflow is active for Customer Claims.
Otherwise, not mandatory.
iApprovalDate
Approval Date: Mandatory
iApprovalText
Approval Text; A valid text number: Not mandatory
iApprovalAction
Approval Action: Not mandatory.
iApprovedBy
Login code of the user approving the line: Mandatory.
iUpdateHeaderStatus
If Yes, and the approved Claim Line is the last one,
the Claim header status is set to Approved too.
Mandatory (Yes/No)
iReleaseMaterials
When not all materials have been released for approval,
they are released when iReleaseMaterials is Yes.
When not all materials have been released for approval,
and iReleaseMaterials is Cancel, Approval is stopped.
When iReleaseMaterials is No, approval continues but
unreleased materials are not released.
Mandatory (Yes/No/Cancel)
iIgnoreCanceledSupplierClaim
Continue approving when the Supplier Claim for the
Claim Line has been canceled. Otherwise, approval stops.
Mandatory (Yes/No)
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No error
<> 0    - An error occurred
```
