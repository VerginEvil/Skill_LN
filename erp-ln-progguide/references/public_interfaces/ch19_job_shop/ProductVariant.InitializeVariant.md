# ProductVariant.InitializeVariant

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 679-680

```baan
DLL:   tiextpcfapi
This function is available from     2026.09 (KB3673834  ).
Syntax: long ProductVariant.InitializeVariant(
domain  tccpva           iProductVariant,
domain  tcdate           iReferenceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   The public interface will initialize the product variant,
replicating the behavior of the form command Initialize Variant
in session tipcf5120m000.
When this public interface is called,
all option sets and their related configurable options of
input product variant are initialized.
Pre:    db.retry.point must be set.
Post:   Commit or abort the transaction.
Input:  iProductVariant                       - Product Variant (Mandatory).
iReferenceDate                                - Reference Date. If the user does not
provide a value, then the value is
defaulted with date from reference
order of the product variant
(Optional).
Output: oExceptionMessage                     - The last error message found
during the execution of public
interface. If multiple error messages
are found, by using ›¼ÀœoExceptionID›¼À                                                ,
messages can be retrieved.
oExceptionID                                  - An ID that refers to the exception
information. Use ›¼ÀœException›¼À                                                 related
functions to retrieve related
information.
Return: 0                                     - Success.
<> 0                                          - Error occurred during Initializing
the product variant.
```
