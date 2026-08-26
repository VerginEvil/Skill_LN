# ItemRoutings.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ItemRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 665-667

```baan
DLL:   tiextrouapi
This function is available from     2023.12 (KB2307645  ).
Syntax: long ItemRoutings.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iMainItem,
domain  tirou.opro       iRouting,
ref     domain  tcitem           oMainItem,
ref     domain  tirou.opro       oRouting,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Item Routings
in overview mode (tirou1101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           1                       - The session will start with
the first session index:
Manufactured Item, Routing.
2                                               - The session will start with
the second session index:
Manufactured Item, Up to Order Quantity,
Routing.
3                                               - The session will start with
the third session index:
Standard Routing, Manufactured Item,
Routing.
iQueryExtend            A specific query to be used when zooming
to this session.
Primary Key fields:
iMainItem               Main Item                       - Optional
iRouting                Routing                       - Optional
Output: for iStartMode MODAL:
oMainItem       Main Item of selected line
oRouting        Routing of selected line
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```

## Public Interfaces for ProductVariant

The following functions are available: ProductVariant.CreateWithFeaturesOptions ProductVariant.CreateWithOptions ProductVariant.ExecuteSubstitutionConstraint ProductVariant.GenerateProductStructureWithoutProject ProductVariant.GenerateProductStructureWithoutProjectV2 ProductVariant.GenerateStructure ProductVariant.GenerateStructureV2 ProductVariant.InitializeOptionSet ProductVariant.InitializeVariant ProductVariant.ProcessSalesConfiguration ProductVariant.RegenerateJobShopStructure ProductVariant.RegenerateJobShopStructureV2 ProductVariant.ReprocessCPQConfiguration ProductVariant.StartConfigurator ProductVariant.StartMultiMain ProductVariant.StartOverview ProductVariant.StartValidateProductVariants ProductVariant.Validate ProductVariant.ValidateConstraint
