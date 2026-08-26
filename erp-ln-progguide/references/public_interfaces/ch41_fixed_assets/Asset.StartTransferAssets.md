# Asset.StartTransferAssets

> Chapter: Chapter 41 Public Interfaces for Fixed Assets
>
> Group: Public Interfaces for Asset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1821-1824

```baan
DLL:   tfextfamapi
This function is available from     2024.07 (KB2327954  ).
Syntax: long Asset.StartTransferAssets(
domain  tffam.mcod       iAssetNumber,
domain  tffam.mcod       iAssetExtension,
long             iStartMode,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session 'Transfer Assets' (tffam8211m000).
Input:  iAssetNumber                          - Asset Number: Mandatory
iAssetExtension                               - Asset Extension: Mandatory
iStartMode                                    - Specifies the start mode for the
session. Not used.
iProcessingOptionSet                          - Optional, if 0, the session is started
with regular defaulting logic (user
defaults or session defaults), except
selection ranges for Asset Number and
Asset Extension, which are defaulted
with iAssetNumber and iAssetExtension.
A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Transfer Assets (tffam8211m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
Options which are not available as Processing Options will get
defaulted with the value in column DEFAULT below.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
AssetNumberFrom                 domain  tffam.mcod      iAssetNumber
AssetNumberTo                   domain  tffam.mcod      iAssetNumber
AssetExtensionFrom              domain  tffam.mcod      iAssetExtension
AssetExtensionTo                domain  tffam.mcod      iAssetExtension
CategoryFrom                    domain  tffam.code      minimum value
CategoryTo                      domain  tffam.code      maximum value
SubcategoryFrom                 domain  tffam.code      minimum value
SubcategoryTo                   domain  tffam.code      maximum value
GroupFrom                       domain  tffam.code      minimum value
GroupTo                         domain  tffam.code      maximum value
ITCMethodFrom                   domain  tffam.itcc      minimum value
ITCMmethodTo                    domain  tffam.itcc      maximum value
VintageGroupAccountFrom         domain  tffam.lcod      minimum value
VintageGroupAccountTo           domain  tffam.lcod      maximum value
InServiceDateFrom               domain  tfgld.date      minimum value
InServiceDateTo                 domain  tfgld.date      current date
CurrentQuantityFrom             domain  tffam.pzlg      minimum value
CurrentQuantityTo               domain  tffam.pzlg      999999999
Automobile                      domain  tffam.aynb      tffam.aynb.both
Listed                          domain  tffam.aynb      tffam.aynb.both
New                             domain  tffam.aynb      tffam.aynb.both
Location1From                   domain  tffam.lcod      minimum value
Location1To                     domain  tffam.lcod      maximum value
Location2From                   domain  tffam.lcod      minimum value
Location2To                     domain  tffam.lcod      maximum value
Location3From                   domain  tffam.lcod      minimum value
Location3To                     domain  tffam.lcod      maximum value
Location4From                   domain  tffam.lcod      minimum value
Location4To                     domain  tffam.lcod      maximum value
Location5From                   domain  tffam.lcod      minimum value
Location5To                     domain  tffam.lcod      maximum value
Location6From                   domain  tffam.lcod      minimum value
Location6To                     domain  tffam.lcod      maximum value
Location7From                   domain  tffam.lcod      minimum value
Location7To                     domain  tffam.lcod      maximum value
Location8From                   domain  tffam.lcod      minimum value
Location8To                     domain  tffam.lcod      maximum value
EffectiveFrom                   domain  tffam.date      tffam.date.eff
TransferDate                    domain  tfgld.date      current date
Reason                          domain  tffam.code      minimum value
TransferPercentage              domain  tfgld.perc      100.0
TransferAmount                  domain  tfgld.amnt      0.0
TransferDistribution            domain  tcyesno         tcyesno.no
Suppress                        domain  tcyesno         tcyesno.no
PrintReport                     domain  tcyesno         tcyesno.yes
InServDateEqualToTransferDate   domain  tcyesno         tcyesno.no
TargetCompany                   domain  tcncmp          current company
BasedOnBookValue                domain  tcyesno         tcyesno.no
TargetVintageGroupAccount       domain  tffam.lcod      minimum value
TargetBusinessPartner           domain  tccom.bpid      minimum value
CopyAsset                       domain  tcyesno         tcyesno.yes
TargetAsset                     domain  tffam.mcod      minimum value
CopyExtension                   domain  tcyesno         tcyesno.no
TargetExtension                 domain  tffam.mcod      minimum value
FirstFreeAssetExtension         domain  tcyesno         tcyesno.no
CopyCategory                    domain  tcyesno         tcyesno.yes
TargetCategory                  domain  tffam.code      minimum value
TargetSubcategory               domain  tffam.code      minimum value
CopyGroup                       domain  tcyesno         tcyesno.yes
TargetGroup                     domain  tffam.code      minimum value
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for AssetBook

The following functions are available: AssetBook.CalculateRemainingDepreciationLife
