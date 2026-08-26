# JobShopBillOfMaterial.StartMultiMain

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 649-650

```baan
DLL:   tiextbomapi
This function is available from     2020.06 (KB2127704  ).
Syntax: long JobShopBillOfMaterial.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Job Shop Bill of Material
(tibom3600m000).
The session can only be started when:
1. the concept job shop by site is active or in preparation, and
2. a job shop bill of material exists for the specified
site / product / bill of material / revision
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
Not used
iSessionIndex
Not used
iQueryExtend
Optional
iSite
Optional
iProduct
Optional
iBillOfMaterialCode
Optional
iRevision
Optional
Output: oExceptionMessage                     - The last message if any message is
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
