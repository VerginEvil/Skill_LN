# Asset.Adjust

> Chapter: Chapter 41 Public Interfaces for Fixed Assets
>
> Group: Public Interfaces for Asset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1815-1817

```baan
DLL:   tfextfamapi
This function is available from     2026.04 (KB3649252  ).
Syntax: long Asset.Adjust(
domain  tcncmp           iAssetCompany,
domain  tffam.mcod       iAssetNumber,
domain  tffam.mcod       iAssetExtension,
domain  tffam.date       iEffectiveFrom,
domain  tfgld.date       iAdjustmentDate,
domain  tffam.code       iReason,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function adjusts an asset.
Input:  iAssetCompany                         - Asset Company: Mandatory
iAssetNumber                                  - Asset Number: Mandatory
iAssetExtension                               - Asset Extension: Mandatory
iEffectiveFrom                                - Effective From: Mandatory
iAdjustmentDate                               - Adjustment Date: Mandatory if
iEffectiveFrom is Effective Date
iReason                                       - Reason: Mandatory
iProcessingOptionSet                          - Mandatory, a Processing Option Set
can be created via a call to
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Adjust Assets (tffam8220m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
Options which are not available as Processing Options will get
defaulted with the value in column DEFAULT below.
Processing Options that are set while a required Implemented
Software Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
Suppress                domain  tcyesno         tcyesno.no
ActionCategory          domain  tffam.oper2     tffam.oper2.no.change
Category                domain  tffam.code      minimum value
Subcategory             domain  tffam.code      minimum value
ActionGroup             domain  tffam.oper2     tffam.oper2.no.change
Group                   domain  tffam.code      minimum value
ActionInServiceDate     domain  tffam.oper      tffam.oper2.no.change
InServiceDate           domain  tfgld.date      minimum value
ActionOwner             domain  tffam.oper2     tffam.oper2.no.change
Owner                   domain  tffam.ownc      minimum value
ActionBusinessPercentage
domain  tffam.oper2     tffam.oper2.no.change
BusinessPercentage      domain  tffam.pcnt      minimum value
ActionITCMethod         domain  tffam.oper2     tffam.oper2.no.change
ITCMethod               domain  tffam.itcc      tffam.itcc.none
ActionAuto              domain  tffam.oper2     tffam.oper2.no.change
Auto                    domain  tffam.ajyn      tffam.ajyn.no
ActionListed            domain  tffam.oper2     tffam.oper2.no.change
Listed                  domain  tffam.ajyn      tffam.ajyn.no
ActionNew               domain  tffam.oper2     tffam.oper2.no.change
New                     domain  tffam.ajyn      tffam.ajyn.no
ActionAssetDistribtionBy
domain  tffam.oper2     tffam.oper2.no.change
AssetDistributionBy     domain  tffam.byqp      tffam.byqp.quantity
ActionVintageAccount    domain  tffam.vint.act  tffam.vint.act.nothing
VintageAccount          domain  tffam.lcod      minimum value
Location1From           domain  tffam.lcod      minimum value
Location1To             domain  tffam.lcod      maximum value
Location2From           domain  tffam.lcod      minimum value
Location2To             domain  tffam.lcod      maximum value
Location3From           domain  tffam.lcod      minimum value
Location3To             domain  tffam.lcod      maximum value
Location4From           domain  tffam.lcod      minimum value
Location4To             domain  tffam.lcod      maximum value
Location5From           domain  tffam.lcod      minimum value
Location5To             domain  tffam.lcod      maximum value
Location6From           domain  tffam.lcod      minimum value
Location6To             domain  tffam.lcod      maximum value
Location7From           domain  tffam.lcod      minimum value
Location7To             domain  tffam.lcod      maximum value
Location8From           domain  tffam.lcod      minimum value
Location8To             domain  tffam.lcod      maximum value
LocationChange          domain  tcyesno         tcyesno.no
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
