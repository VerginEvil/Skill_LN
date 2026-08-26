# RemittanceAdvice.Apply

> Chapter: Chapter 37 Public Interfaces for Cash Management
>
> Group: Public Interfaces for RemittanceAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1791-1791

```baan
DLL:   tfextcmgapi
This function is available from     2025.04 (KB3568308  ).
Syntax: long RemittanceAdvice.Apply(
domain  tcncmp           iFinancialCompany,
const   domain  tfcmg.rcod       iRemittance,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function tries to apply all remittance advice lines
that have not been applied yet.
Pre:    db.retry.point() must be set.
Post:   abort/commit.transaction() must be done.
Input:
iFinancialCompany                             - Financial company for which the remittance
advice lines are to be applied.
Mandatory.
iRemittance                                   - Remittance code for which the remittance
advice lines are to be applied.
Mandatory.
Output:
oExceptionMessage                             - The last message if any message is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID                                  - An ID that refers to the exception information.
Use the functions in Exception to get
all relevant information.
Return:
0                                             - All remittance advice lines have been applied.
<> 0                                          - Error.
```
