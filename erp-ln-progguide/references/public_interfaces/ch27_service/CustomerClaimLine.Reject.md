# CustomerClaimLine.Reject

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1531-1533

```baan
DLL:   tsextcmmapi
This function is available from     2023.06 (KB2288749  ).
Syntax: long CustomerClaimLine.Reject(
domain  tcorno           iCustomerClaim,
domain  tcpono           iClaimLine,
domain  tccdis           iRejectionReason,
domain  tcdate           iRejectionDate,
domain  tsmdm.text       iRejectionText,
domain  tscmm.actn       iRejectionAction,
domain  tclogn           iRejectedBy,
domain  tcyesno          iUpdateHeaderStatus,
domain  tcyesno.c        iReleaseMaterials,
domain  tcyesno          iSolveRelatedCall,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Reject one specific Customer Claim Line.
See functionality when a Customer Claim Line is Rejected with
session Reject Customer Claim (tscmm1220m000).
On rejecting the last claim line, the header status can be
set to Rejected as well. This behavior can be controlled with
the use of argument iUpdateHeaderStatus.
Pre:                  -
Post:   This function sets a retry              -point and will commit and/or abort
the transaction.
Input:  iCustomerClaim
Customer Claim: Mandatory
iClaimLine
Claim Line: Mandatory
iRejectionReason
Rejection Reason. Note that only a reason code of
type Claim Rejection which is valid on the current
date is allowed: Mandatory.
iRejectionDate
Rejection Date: Mandatory
iRejectionText
Rejection Text; A valid text number: Not mandatory.
iRejectionAction
Rejection Action: Mandatory
iRejectedBy
Login code of the user rejecting the line: Mandatory.
iUpdateHeaderStatus
If Yes, and the rejected Claim Line is the last one,
the Claim header status is set to Rejected too.
Mandatory (Yes/No)
iReleaseMaterials
When not all materials have been released for approval,
they are released when iReleaseMaterials is Yes.
When not all materials have been released for approval,
and iReleaseMaterials is Cancel, Approval is stopped.
When iReleaseMaterials is No, approval continues but
unreleased materials are not released.
Mandatory (Yes/No/Cancel)
iSolveRelatedCall
When header status is set to Rejected, and there is a
related Call, the Call is set to Solved when
iSolveRelatedCall is Yes.
Mandatory (Yes/No)
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                           - No error
<> 0                                  - An error occurred
```

## Public Interfaces for SupplierClaim

The following functions are available: SupplierClaim.GenerateSerializedItem SupplierClaim.SetRMAReceived
