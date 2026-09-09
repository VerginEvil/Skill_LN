# JobShopBillOfMaterial.ValidateRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 655-656

```baan
DLL:   tiextbomapi
This function is available from 2020.12 (KB2163805).
Syntax: long JobShopBillOfMaterial.ValidateRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tibmdl           iBillOfMaterialCode,
domain  tibmrv           iRevision,
domain  tcyesno          iCheckUseUp,
domain  tcqiv1           iThresholdQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to validate the specified Job Shop
Bill of Material Revision.
Input:  iSite                   Site (mandatory).
iProduct                Main item (mandatory).
iBillOfMaterialCode     BOM Model (mandatory).
iRevision               Revision (mandatory).
iCheckUseUp             If yes, then the function checks
if the definitions of the Use Up Items
are:
- valid (last allowed order date vs
expiry date of the BOM) and
- useful (depending on the Inventory
level of the Use Up Item).
If not valid or not useful, then an error is
returned and if iRemoveUseUp = Yes, then
the Use Up item will be removed.
iThresholdQuantity      If the on-hand Inventory quantity of a
Use Up item is below iThresholdQuantity,
(or equal in case iThresholdQuantity = 0.0),
then the Use Up item is considered
as not useful.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       JS BOM Revision passed all the validation
checks.
<> 0                    JS BOM Revision did not pass all the
validation checks.
```
