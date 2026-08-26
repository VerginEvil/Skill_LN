# CrossValidationRule.SetStatus

> Chapter: Chapter 40 Public Interfaces for General Ledger
>
> Group: Public Interfaces for CrossValidationRule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1813-1815

```baan
DLL:   tfextgldapi
This function is available from     2026.10 (KB3677891  ).
Syntax: long CrossValidationRule.SetStatus(
domain  tcncmp           iFinancialCompany,
domain  tcorno           iCrossValidationRule,
domain  tfgld.lino       iCrossValidationRuleVersion,
domain  tfgld.rl.stat    iStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface updates the status of the given
cross validation rule to the specified status.
Pre:    db.retry.point() must be set.
Post:   abort/commit.transaction() must be done.
Input:
iFinancialCompany                             - The financial company. (Mandatory)
iCrossValidationRule                          - The cross validation rule. (Mandatory)
iCrossValidationRuleVersion
-                                               The cross validation rule version.
(Mandatory)
iStatus                                       - The status. (Mandatory)
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                                             - The status of a cross validation rule
successfully set.
<> 0                                          - Error.
```

## Chapter 41 Public Interfaces for Fixed Assets

## Public Interfaces for Asset

The following functions are available: Asset.Adjust Asset.Dispose Asset.GetDefaultLedgerAccountAndDimensions Asset.StartAdjustAssets Asset.StartTransferAssets
