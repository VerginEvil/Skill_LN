# Asset.GetDefaultLedgerAccountAndDimensions

> Chapter: Chapter 41 Public Interfaces for Fixed Assets
>
> Group: Public Interfaces for Asset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1818-1819

```baan
DLL:   tfextfamapi
This function is available from     2024.07 (KB2331941  ).
Syntax: long Asset.GetDefaultLedgerAccountAndDimensions(
domain  tcncmp           iAssetCompany,
domain  tffam.mcod       iAssetNumber,
domain  tffam.mcod       iAssetExtension,
domain  tffam.code       iAssetBook,
domain  tccom.bpid       iBusinessPartner,
const   domain  tffam.lcod       iLocationSegments() fixed,
domain  tcidty           iIntegrationDocumentType,
domain  tffam.dtty       iDepreciationType,
domain  tffam.dtyp       iDisposalType,
domain  tffam.code       iReason,
domain  tfgld.dbcr       iDebitCredit,
domain  tfgld.date       iTransactionDate,
long             iProcessingOptionSet,
ref     domain  tfgld.leac       oLedgerAccount,
ref     domain  tfgld.dimx       oDimensions() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function retrieves ledger account and dimensions from the
mapping scheme for a fixed asset.
Pre:                  -
Post:                 -
Input:  iAssetCompany                         - Asset Company: Mandatory
iAssetNumber                                  - Asset Number: Mandatory
iAssetExtension                               - Asset Extension: Mandatory
iAssetBook                                    - Asset Book: Mandatory
iBusinessPartner                              - Business Partner: Optional
iLocationSegments                             - Array with Location Segments: Optional
iIntegrationDocumentType
-                                               Integration Document Type: Mandatory
iDepreciationType                             - Depreciation Type: Optional
iDisposalType                                 - Disposal Type: Optional
iReason                                       - Reason: Optional
iDebitCredit                                  - Debit/Credit Indicator: Mandatory
iTransactionDate                              - Transaction Date: Mandatory
iProcessingOptionSet                          - Optional, if 0, the optional values
are retrieved from the asset and/or
asset book.
A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
NAME                            TYPE                    DEFAULT
OwningCompany                   domain  tcncmp          from Asset
OwningDepartment                domain  tccwoc          from Asset
Category                        domain  tffam.code      from Asset
Subcategory                     domain  tffam.code      from Asset
Group                           domain  tffam.code      from Asset
Frequency                       domain  tffam.code      from Asset Book
PropertyType                    domain  tffam.code      from Asset Book
DepreciationCode                domain  tffam.meth      from Asset Book
Output: oLedgerAccount                        - Ledger Account
oDimensions                                   - Array with Dimensions
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Data read
<> 0                                          - An error occurred
```
