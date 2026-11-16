# JobShopBillOfMaterial.RemoveUseUp

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 649-650

```baan
DLL:   tiextbomapi
This function is available from 2021.04 (KB2181351).
Syntax: long JobShopBillOfMaterial.RemoveUseUp(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
domain  tcqiv1           iThresholdQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to remove Use Up Materials that are
not valid or not useful anymore from the specified BOM revision.
A Use Up Material is not valid if its last allowed order date
is after the expiry date of the BOM revision.
A Use Up Material is not useful if its on-hand inventory quantity
is lower than iThresholdQuantity or zero (when iThresholdQuantity
is not specified).
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point must be set.
Post:   Abort or commit the transaction.
Input:  iSite                   Site (mandatory).
iProduct                Main item (mandatory).
iBillOfMaterialCode     BOM Model (mandatory).
iRevision               Revision (mandatory).
The status of the specified BOM
revision must be New.
iThresholdQuantity      Threshold quantity for inventory
check (optional).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - no use up materials were found, or
- all found use up materials are valid
and usefull, or
- all invalid or not useful
use up materials were succesfully
removed.
<> 0                    An invalid or not useful material
could not be removed.
```
