# WhereUsedJobShopListOfMaterial.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for WhereUsedJobShopListOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 822-824

```baan
DLL:   tiextbomapi
This function is available from     2026.03 (KB3612917  ).
Syntax: long WhereUsedJobShopListOfMaterial.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterial,
domain  tibmrv           iRevision,
domain  tcpono           iPosition,
ref     domain  tcsite           oSite,
ref     domain  tcitem           oProduct,
ref     domain  tibmdl           oBillOfMaterial,
ref     domain  tibmrv           oRevision,
ref     domain  tcpono           oPosition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interfaces starts the session
Where                      -Used Job Shop List of Materials tibom3110m100.
Where                      -Used Job Shop List of Materials session can be used to
view where specific materials are used in the
Job Shop Bills of Material.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode              Specifies the start mode for the session.
Possible values are:
MODAL                                               - The parent session is blocked until
the child session exits, the session will
be started as a zoom session.
MODELESS                                               - Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iSessionIndex           Not used
iQueryExtend            A specific query to be used when starting the
session. Using the query extend may lead to a
data not found, session not started" situation.
iItem                   Item
iSite                   Site
iProduct                Product
iBillOfMaterialCode     Bill of material
iRevision               Revision
iPosition               Position
Output: if iStartMode MODAL and 1 record is selected
oSite                   Site
oProduct                Product
oBillOfMaterialCode     Bill of material
oRevision               Revision
oPosition               Position
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started successfully.
<> 0                    Errors occurred.
```

## Public Interfaces for ProductionPlanning

The following functions are available: ProductionPlanning.StartDetail ProductionPlanning.StartOverview
