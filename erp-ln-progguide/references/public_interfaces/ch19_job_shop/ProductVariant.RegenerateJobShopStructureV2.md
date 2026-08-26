# ProductVariant.RegenerateJobShopStructureV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 682-683

```baan
DLL:   tiextpcfapi
This function is available from     2023.05 (KB2284269  ).
Syntax: long ProductVariant.RegenerateJobShopStructureV2(
domain  tccpva           iProductVariant,
boolean          iUpdateOrderPrice,
domain  tccwar           iShipFromWarehouse,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface regenerates a (Project) Structure for
a Product Variant based on a Job Shop Generic Item. Transaction
management is handled by the Public Interface.
Pre:    None.
Post:   None.
Input:  iProductVariant         Product Variant. (Mandatory)
iUpdateOrderPrice       Updates price in case reference type is
Sales Order / Sales Quotation.
iShipFromWarehouse      Warehouse for Project Part. This is
typically the Warehouse of the Sales
Order Line or Sales Quotation Line
from which the goods are shipped.
Output: oItem                                 - The created custom Item.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Structure regeneration completed.
<> 0                                          - Otherwise.
```
