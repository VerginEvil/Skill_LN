# JobShopBillOfMaterial.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 650-651

```baan
DLL:   tiextbomapi
This function is available from     2020.06 (KB2127704  ).
Syntax: long JobShopBillOfMaterial.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
domain  tcsite           oSite,
domain  tcitem           oProduct,
domain  tibmdl           oBillOfMaterialCode,
domain  tibmrv           oRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Job Shop Bill of Material
(tibom3600m000).
The session can only be started when:
1. the concept job shop by site is active or in preparation, and
2. a job shop bill of material exists for the specified
site / product / bill of material / revision / query extend
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session. Optional.
Possible values are:
"showAll": All BOM lines are displayed
"showEffective": Only effective lines are shown (default)
"showCurrent": Only lines whiche are Approved an Effective
When empty: "showEffective" is applied
iSessionIndex
Not used
iQueryExtend
A specific query to be used when starting the
session. Using the query extend may lead to a
"data not found, session not started" situation.
Optional
iSite
Mandatory if i.mode = MODELESS, else optional
iProduct
Optional
iBillOfMaterialCode
Optional
iRevision
Optional
Output: if iStartMode MODAL and 1 record is selected
oSite
oProduct
oBillOfMaterialCode
oRevision
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```
