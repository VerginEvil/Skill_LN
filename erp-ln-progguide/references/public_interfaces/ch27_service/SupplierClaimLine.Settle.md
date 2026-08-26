# SupplierClaimLine.Settle

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SupplierClaimLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1537-1538

```baan
DLL:   tsextcmmapi
This function is available from     2025.03 (KB3554806  ).
Syntax: long SupplierClaimLine.Settle(
domain  tcorno           iSupplierClaim,
domain  tcpono           iClaimLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Settle one specific Supplier Claim Line
(tscmm210 record). See functionality when a Supplier Claim
Line is Settled with Form Command 'Settle' via a Supplier Claim
Line(s) session (tscmm2110m000 etc.).
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be executed.
Input:  iSupplierClaim                - The Supplier Claim number, Mandatory
iClaimLine                            - The Claim Line number, Mandatory
Output: oExceptionMessage
-                                       The last message if any message is found.
If more than one message is given, these are
present in the oExceptionID.
oExceptionID                          - An ID that refers to the exception
information. Use the functions in Exception
to get all relevant information.
Return: 0                             - No error
<> 0                                  - An error occurred
```

## Public Interfaces for OrderRelation

The following functions are available: OrderRelation.GetLatestSequenceNumber
