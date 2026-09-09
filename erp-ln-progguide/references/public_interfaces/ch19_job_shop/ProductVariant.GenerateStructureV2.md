# ProductVariant.GenerateStructureV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 680-681

```baan
DLL:   tiextpcfapi
This function is available from 2024.11 (KB3500971).
Syntax: long ProductVariant.GenerateStructureV2(
domain  tccprj           iProject,
domain  tccpva           iProductVariant,
domain  tcdate           iReferenceDate,
domain  tcyesno          iRegenerate,
domain  tcyesno          iUpdateReferenceDate,
domain  tcyesno          iCheckStock,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface generates a Product Structure based on a
configured Product Variant, similar to tipcs2220m000.
The configured Product Variant can be created using
ProductVariant.StartConfigurator or via the Product Configurator
(tipcf5120m000).
Existing Sales Order lines and Quotation Order lines belonging
to the Product Variant are updated.
Transaction management is handled by the Public Interface.
Pre:    None.
Post:   None.
Input:  iProject                - Project (Mandatory, if the Generic
top item for the Product Variant is
With PCS).
iProductVariant         - Product Variant (Mandatory). Cannot be
for an Assembly Item
iReferenceDate          - Reference Date. If empty,
the Reference Date for the given
Project is taken. If Reference Date
for the Project is empty, the current
date is used.
iRegenerate             - If yes, the Product Variant is also
Regenerated.
iUpdateReferenceDate    - Update the Project Reference Date.
iCheckStock             - Check the Standard Item Inventory.
Output: oItem                   - The created custom Item.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Structure generation completed.
<> 0                    - Otherwise.
```
