# CrossValidationRule.Rebuild

> Chapter: Chapter 40 Public Interfaces for General Ledger
>
> Group: Public Interfaces for CrossValidationRule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1813-1813

```baan
DLL:   tfextgldapi
This function is available from     2026.10 (KB3677891  ).
Syntax: long CrossValidationRule.Rebuild(
domain  tcncmp           iFinancialCompany,
domain  tcorno           iCrossValidationRule,
domain  tfgld.lino       iCrossValidationRuleVersion,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface rebuilds the given cross validation rule.
(Note: Transaction handling is done within the public interface)
Pre:    N/A
Post:   N/A
Input:
iFinancialCompany                             - The financial company. (Mandatory)
iCrossValidationRule                          - The cross validation rule. (Mandatory)
iCrossValidationRuleVersion
-                                               The cross validation rule version.
(Mandatory)
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
0                                             - The rebuild of the given cross
validation rule was successful.
<> 0                                          - Error.
```
