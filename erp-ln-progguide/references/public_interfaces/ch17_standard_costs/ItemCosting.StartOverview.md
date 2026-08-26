# ItemCosting.StartOverview

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for ItemCosting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 619-621

```baan
DLL:   tiextcprapi
This function is available from     2026.02 (KB3606237  ).
Syntax: long ItemCosting.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
ref     domain  tcitem           oItem,
ref     domain  tcemm.grid       oEnterpriseUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Item - Costing in overview
mode (ticpr0107m000).
Input:  iStartMode              Specifies the start mode for the
session. Possible values are:
MODAL                                               - The parent session is blocked
until the child session exits.
The session will be started as
a zoom session.
MODELESS                                               - Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Default value is 0 for which session
will start with index 1.
Supported values:
1: Sort by Item/Enterprise Unit
2: Sort by Enterprise Unit/Item
iQueryExtend            A specific query to be used when
zooming to this session.
iItem                   Item
iEnterpriseUnit         Enterprise Unit
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oItem           Item
oEnterpriseUnit Enterprise Unit
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

## Chapter 18 Public Interfaces for Manufacturing

## Master

## Public Interfaces for ProductionBillOfMaterial

The following functions are available: ProductionBillOfMaterial.ApproveRevision ProductionBillOfMaterial.CopyToJobShop ProductionBillOfMaterial.CreateNewRevision ProductionBillOfMaterial.ExpireRevision ProductionBillOfMaterial.Explode ProductionBillOfMaterial.GenerateProductSubcontractingModel ProductionBillOfMaterial.StartMultiMain ProductionBillOfMaterial.ValidateRevision
