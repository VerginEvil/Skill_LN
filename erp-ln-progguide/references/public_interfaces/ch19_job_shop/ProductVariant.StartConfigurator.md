# ProductVariant.StartConfigurator

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 687-688

```baan
DLL:   tiextpcfapi
This function is available from 2022.12 (KB2226156).
Syntax: long ProductVariant.StartConfigurator(
domain  tcitem           iGenericItem,
domain  tccprj           iProject,
domain  tccpva           iProductVariant,
domain  tcreft           iReferenceType,
domain  tcccur           iCurrency,
domain  tcqsl1           iOrderQuantity,
domain  tccwar           iShipFromWarehouse,
domain  tccuni           iSalesPriceUnit,
ref     domain  tccpva           oProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the Product Variant configurator.
Transaction management is handled by the Public Interface.
Pre:    None.
Post:   None.
Input:  iGenericItem            - Generic Item. (Mandatory)
iProject                - Project (Mandatory if the Generic Item
is With PCS).
iProductVariant         - Product Variant (Optional). The
Generic top-item for the Product
Variant should match iGenericItem.
iReferenceType          - Reference Type (Mandatory).
iCurrency               - Currency (Optional). If the project
type is standard, the default currency
is used. If the currency system is
dependent or standard, the currency of
the calculation office is used. In
these situations, this input is
ignored.
iOrderQuantity          - Order Quantity (Not used unless
iReferenceType is tcreft.sls.order or
tcreft.sls.quotation and
iProductVariant is not empty).
iShipFromWarehouse      - Ship from Warehouse (Not used unless
iReferenceType is tcreft.sls.order or
tcreft.sls.quotation and
iProductVariant is not empty).
iSalesPriceUnit         - Sales Price Unit (Not used unless
iReferenceType is tcreft.sls.order or
tcreft.sls.quotation and
iProductVariant is not empty).
Output: oProductVariant         - The created Product Variant.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Configurator started succesfully.
<> 0                    - Otherwise.
```
