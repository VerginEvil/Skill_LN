# Account.CrossValidateDimensions

> Chapter: Chapter 40 Public Interfaces for General Ledger
>
> Group: Public Interfaces for Account
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1832-1832

```baan
DLL:   tfextgldapi
This function is available from 2024.12 (KB3525960).
Syntax: long Account.CrossValidateDimensions(
domain  tcncmp           iFinancialCompany,
domain  tcdate           iDateForCheck,
domain  tfgld.leac       iLedgerAccount,
domain  tfgld.dimn       iDimensionNumber,
const   domain  tfgld.dimx       iDimensionArray() fixed,
ref             boolean          oValidDimensions,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function checks whether the dimensions are valid
according to the cross validation rules.
Pre:    -
Post:   -
Input:  iFinancialCompany       - Financial Company: Mandatory
iDateForCheck           - Date for check in UTC format:
Mandatory
iLedgerAccount          - Ledger Account: Mandatory
iDimensionNumber        - Until (and including) which dimension
of the array is to be checked:
Mandatory
iDimensionArray         - Array with dimensions
Output: oValidDimensions        - Dimensions are valid according to
cross validation rules
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Data read
<> 0                    - An error occurred
Return: 0/DALHOOKERROR
```
