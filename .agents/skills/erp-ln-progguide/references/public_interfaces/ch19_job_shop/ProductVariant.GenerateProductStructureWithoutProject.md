# ProductVariant.GenerateProductStructureWithoutProject

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 678-679

```baan
DLL:   tiextpcfapi
This function is available from 2024.01 (KB2295738).
Syntax: long ProductVariant.GenerateProductStructureWithoutProject(
domain  tccpva           iProductVariant,
domain  tcdate           iReferenceDate,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface generates a Product Structure based on a
configured Product Variant, without a Project. This can also be
done using session tipcs2220m000.
The configured Product Variant can be created using
ProductVariant.StartConfigurator or via the Product Configurator
(tipcf5120m000).
Pre:    Db.retry point must be set
Product Variant must be configured.
Post:   Transaction must be aborted or committed.
Input:  iProductVariant         - Product Variant (Mandatory). Cannot be
for an Assembly Item
iReferenceDate          - Reference Date (Optional). If empty,
the current date is used.
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
