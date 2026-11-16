# AssetBook.CalculateRemainingDepreciationLife

> Chapter: Chapter 41 Public Interfaces for Fixed Assets
>
> Group: Public Interfaces for AssetBook
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1844-1844

```baan
DLL:   tfextfamapi
This function is available from 2023.07 (KB2287701).
Syntax: long AssetBook.CalculateRemainingDepreciationLife(
domain  tcncmp           iAssetCompany,
domain  tffam.mcod       iAssetNumber,
domain  tffam.mcod       iAssetExtension,
domain  tffam.code       iAssetBook,
ref     domain  tcmcs.double     oRemainingDays,
ref     domain  tcmcs.double     oRemainingPeriods,
ref     domain  tffam.life       oRemainingLifeYears,
ref     domain  tffam.life       oRemainingLifePeriods,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function calculates the remaining depreciation life of
an asset book. The remaining depreciation life takes the
average convention of the used depreciation code into account.
Next output arguments are returned:
- oRemainingDays: Used for depreciation calculation when
depreciation mode in the FAM parameters is set to Daily.
- oRemainingPeriods: Unrounded value of remaining periods,
used for depreciation calculation when depreciation mode in
the FAM parameters is set to Periodically.
- oRemainingLifeYears / oRemainingLifePeriods:
Rounded number of entire years and periods, derived from
oRemainingPeriods and used for display purposes in several
sessions, because in fixed asset management it is common
practice to express the life in years and periods.
Pre:    -
Post:   -
Input:  iAssetCompany           - Asset Company: Mandatory
iAssetNumber            - Asset Number: Mandatory
iAssetExtension         - Asset Extension: Mandatory
iAssetBook              - Asset Book: Mandatory
Output: oRemainingDays          - Remaining days to be depreciated till
the end of the asset life.
oRemainingPeriods       - Remaining periods to be depreciated
till the end of the asset life.
oRemainingLifeYears     - Entire number of years still to be
depreciated.
oRemainingLifePeriods   - Rounded number of periods still to
be depreciated.
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
```
