# ProductVariant.ExecuteSubstitutionConstraint

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 677-678

```baan
DLL:   tiextpcfapi
This function is available from 2026.09 (KB3677048).
Syntax: long ProductVariant.ExecuteSubstitutionConstraint(
domain  tccpva           iProductVariant,
domain  tcolid           iOptionListID,
domain  tcitem           iItem,
domain  tccnsc           iConstraintCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   This public interface is used to execute the Substitution
Constraint for a Product Variant.
Note: This function uses variable arguments for both
input and output. Data is passed via triplets:
specify the field ID, the input value and the
output variable.
Example:
ret = ProductVariant.ExecuteSubstitutionConstraint(
|* Fixed arguments:
product.variant,                |* input
option.list.id,                 |* input
item,                           |* input
constraint.code,                |* input
exception.message,              |* output
exception.id,                   |* output
|* Variable arguments:
tipcf.flds.quantity,            |* input
|* field is of type tiqbm2
17.3,                           |* input
quantity,                       |* output
tipcf.flds.bom_warehouse,       |* input
input.warehouse,                |* input
output.warehouse)               |* output
Pre:    N.A.
Post:   N.A.
Input:  iProductVariant         - Product Variant. (Mandatory).
iOptionListID           - Option List ID.
iItem                   - Item.
iConstraintCode         - Constraint Code. (Mandatory).
...                     - A value of enum tipcf.flds that
refers to a user variable as
configured in tipcf0100m000.
The base type of the input/output
variables specified below must match
- Input variable: Value for the
specified Enum Constant
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
...                     - Output variable: Returns the executed
value corresponding to the
specified enum constant.
Return: 0                       - Substitution Constraint executed
successfully.
<> 0                    - Otherwise.
```
