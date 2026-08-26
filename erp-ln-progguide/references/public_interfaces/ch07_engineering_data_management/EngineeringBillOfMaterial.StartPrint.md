# EngineeringBillOfMaterial.StartPrint

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 262-265

```baan
DLL:   tiextedmapi
This function is available from     2026.06 (KB3628866  ).
Syntax: long EngineeringBillOfMaterial.StartPrint(
long             iStartMode,
domain  tcitem           iEngineeringItem,
domain  tiedm.prt.bom    iPrintOptions,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to Print Engineering BOMs
(tiedm1410m000), the purpose of this session is to print the
single level and multi                      -level BOM structure.
Pre:    NA
Post:   NA
Input:  iStartMode (Mandatory Input)
Specifies the start mode for the session.
Possible values are:
MODAL
The parent session is blocked until the
child session exits, the session will be
started as a Zoom session.
MODELESS
Parent and child are parallel
sessions that can be manipulated
simultaneously.
MODELESS_ALWAYS
Parent and child are parallel
sessions that can be manipulated
simultaneously.
iEngineeringItem (Optional)
Engineering Item.
iPrintOptions (Mandatory Input)
Print Options
(Single level, Multi                                              -level or Summarized)
iProcessingOptionSet (Optional)
Processing Option Set.
If 0, then user default/session default
values are applied. A Processing Option
Set can be created via a call to
ProcessingOptionSet.Create() in DLL
tcextextapi. After the call the option
set can be deleted by calling
ProcessingOptionSet.Delete().
NAME                            TYPE                    DEFAULT
FromEngineeringItem             domain tcitem           ""
ToEngineeringItem               domain tcitem           Max. Value of Domain
RevisionDate                    domain tcdate           utc.num()
OrderQuantity                   domain tiqep1           1
Configuration                   domain ticonfig         ticonfig.all
EffectivityUnit                 domain tcuef.effn       0
PrintReferenceDesignators       domain tcyesno          tcyesno.no
AlternativeItems                domain tcyesno          tcyesno.no
UseUpMaterial                   domain tcyesno          tcyesno.no
PrintEItemTextsAndItemTexts     domain tcyesno          tcyesno.no
PrintEBOMTexts                  domain tcyesno          tcyesno.no
LanguageForTexts                domain tclan            empty
SortByComponentDimension        domain tcyesno          tcyesno.no
Default Values:
FromEngineeringItem
If input variable field "FromEngineeringItem" is given, it will
be used as default value. Otherwise, it will be defaulted with
BLANK.
ToEngineeringItem
If input variable field "ToEngineeringItem" is given, it
will be used as default value. Otherwise, it will be defaulted
with maximum value of its Domain.
RevisionDate
If input variable field "RevisionDate" is given, it will be
used as default value. Otherwise, it will be defaulted with
utc.num().
OrderQuantity
It is valid only if Summarized Print Type is selected. If input
variable field "OrderQuantity" is given, it will be used as
default value. Otherwise, it will be defaulted with 1.
Configuration
If input variable field "Configuration" is given, it will be
used as default value. Otherwise, it will be defaulted with
ticonfig.all.
EffectivityUnit
It is valid only if Configuration is selected as Specific. If
input variable field "EffectiveUnit" is given, it will be used
as default value. Otherwise, it will be defaulted with 0.
PrintReferenceDesignators
It is not Valid if Summarized Print Type is selected. If input
variable field "PrintReferenceDesignators" is given, it will
be used as default value. Otherwise, it will be defaulted with
tcyesno.no.
AlternativeItems
It is not Valid if Summarized Print Type is selected. If input
variable field "AlternativeItems" is given, it will be used as
default value. Otherwise, it will be defaulted with tcyesno.no.
UseUpMaterial
It is not Valid if Summarized Print Type is selected. If input
variable field "UseUpMaterial" is given, it will be used as
default value. Otherwise, it will be defaulted with tcyesno.no.
PrintEItemTextsAndItemTexts
It is always enabled. If input variable field
"PrintEitemTextsAndItemTexts" is given, it will be used as
default value. Otherwise, it will be defaulted with tcyesno.no.
PrintEBOMTexts
It is not Valid if Summarized Print Type is selected. If input
variable field "PrintEbomTexts" is given, it will be used as
default value. Otherwise, it will be defaulted with tcyesno.no.
LanguageForTexts
It is valid, only if any of the texts are selected to be
printed. If input variable field "LanguageforTexts" is given,
it will be used as default value. Otherwise, it will be
defaulted with EN.
SortByComponentDimension
It is valid only if Summarized Print Type is selected. If input
variable field "SortByComponentDimension" is given, it will be
used as default value. Otherwise, it will be defaulted with
tcyesno.no.
Return:
0                 Success. Session Started.
DALHOOKERROR
Error. Starting Session.
```

## Public Interfaces for EngineeringItem

The following functions are available: EngineeringItem.GenerateByMBC EngineeringItem.StartDetail EngineeringItem.StartOverview
