# ProjectPCS.StartCopyCustomizedProductStructureToCustomizedStructure

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 891-892

```baan
DLL:   tiextpcsapi
This function is available from     2026.06 (KB3642321  ).
Syntax: long ProjectPCS.StartCopyCustomizedProductStructureToCustomizedStructure(
long             iStartMode,
domain  tcsite           iSite,
domain  tcitem           iSourceCustomizedItem,
domain  tcitem           iTargetCustomizedIem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to start session Copy Customized Product
Structure to Customized Structure (tipcs2231m000)
If input arguments are specified as "", then screen defaults
apply if they are set                      -up.
The same holds for options in the processing option set;
and screen defaults also apply when options are left out.
Otherwise, screen defaults are ignored.
Input:  iStartMode                            - Specifies the start mode for the
session (Mandatory). Possible values:
MODAL                                                 - The parent session is blocked
until the child session exits. The
session will be started as a zoom
session.
MODELESS_ALWAYS                                                 - Parent and child are
parallel sessions that can be
manipulated simultaneously, even if
the session is a Dialog.
iSite                                         - Site. Only applicable when
Job Shop by Site is active for
operations. (Optional).
iSourceCustomizedItem                         - Source Customized Item. (Optional).
iTargetCustomizedItem                         - Target Customized Item. (Optional).
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
NAME                                         TYPE         DEFAULT
UseProjectReferenceDate               domain tcyesno      tcyesno.no
ReferenceDate                         domain tiutcs       utc()
CopyAllComponentsAndEffectivityUnits  domain tcyesno      tcyesno.yes
EffectivityUnit                       domain tcuef.effn   0
CopyMethod                            domain ticpst       ticpst.single
CopyEitemRelationships                domain tcyesno      tcyesno.yes
CopyProductVariantStructure           domain tcyesno      tcyesno.yes
IncludeAlternatives                   domain tcyesno      tcyesno.no
IncludeUseUpMaterials                 domain tcyesno      tcyesno.no
GenerateNewItemCodes                  domain tcyesno      tcyesno.yes
AskBeforeGeneratingNewItemCode        domain tcyesno      tcyesno.yes
ApproveConversionFactors              domain tcyesno      tcyesno.yes
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Copy Customized Product Structure
to Customized Structure is started
successfully.
<> 0                                          - Copy Customized Product Structure
to Customized Structure is not started
successfully.
Return: long
```
