# CustomerClaimLine.ApproveForInvoiceLinking

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for CustomerClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1528-1529

```baan
DLL:   tsextcmmapi
This function is available from     2023.10 (KB2295974  ).
Syntax: long CustomerClaimLine.ApproveForInvoiceLinking(
domain  tcorno           iCustomerClaim,
domain  tcpono           iClaimLine,
domain  tclogn           iApprovedBy,
domain  tcdate           iApprovalDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function approves a Customer Claim Line for Invoice
Linking.
Approve for Invoice Linking is only applicable when
the Customer Claim Invoice Procedure is Invoice Based.
Approve for Invoice Linking is allowed when:
-                       Customer Claim Status is Pending Approval, or Approved.
-                       Customer Claim Line has been Approved.
-                       Customer Claim Line Claim Method is Reimburse Costs.
When one of these conditions is not met, an error is returned.
Pre:    db.retry.point set
Post:   commit/abort transaction
Input:  iCustomerClaim
Customer Claim: Mandatory
iClaimLine
Claim Line: Mandatory
iApprovedBy
Login code of the user approving the line: Mandatory.
iApprovalDate
Approval Date: Mandatory
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No error
<> 0                          - An error occurred
```
