# ProductVariant.Validate

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 688-689

```baan
DLL:   tiextpcfapi
This function is available from     2026.01 (KB3602361  ).
Syntax: long ProductVariant.Validate(
domain  tccpva           iProductVariant,
domain  tcyesno          iRevalidateVariant,
domain  tcyesno          iOverwriteSalesPrice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to validate a Product Variant.
In case the product variant is validated, the required option
sets are created.
Pre:    db.retry point must be set.
Post:   Transaction must be aborted or committed.
Input:  iProductVariant                       - Product Variant. (Mandatory)
iRevalidateVariant                            - Control for revalidating a validated
product variant.
iOverwriteSalesPrice                          - Control for overwriting sales price.
Output: oExceptionMessage                     - The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Product Variant is validated and
Option Set is created.
<> 0                                          - Otherwise.
```
