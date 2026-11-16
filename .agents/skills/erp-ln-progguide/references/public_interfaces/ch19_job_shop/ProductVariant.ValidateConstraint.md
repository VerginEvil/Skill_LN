# ProductVariant.ValidateConstraint

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 692-692

```baan
DLL:   tiextpcfapi
This function is available from 2026.05 (KB3649794).
Syntax: long ProductVariant.ValidateConstraint(
domain  tccpva           iProductVariant,
domain  tcolid           iOptionListID,
domain  tcitem           iItem,
domain  tccnsc           iConstraintCode,
ref             boolean          oConstraintsValidationResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to validate the constraint of a
product variant.
Pre:    N.A.
Post:   N.A.
Input:  iProductVariant         - Product Variant. (Mandatory).
iOptionListID           - OptionList ID.
iItem                   - Item.
iConstraintCode         - Constraint Code. (Mandatory).
Output: oConstraintsValidationResult
- Constraints Validation Result.
oExceptionMessage       - The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Constraint is validated.
<> 0                    - Otherwise.
```
