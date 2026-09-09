# ProductVariant.InitializeOptionSet

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 681-682

```baan
DLL:   tiextpcfapi
This function is available from 2026.09 (KB3673834).
Syntax: long ProductVariant.InitializeOptionSet(
domain  tccpva           iProductVariant,
domain  tcopts           iOptionSet,
domain  tcdate           iReferenceDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   The public interface will initialize the product variant
option sets, replicating the behavior of the form command
Initialize Option Set in session tipcf5120m000.
When this public interface is called, all option sets
with values greater than or equal to the specified input
option set are initialized, along with their related
configurable options.
Pre:    db.retry.point must be set.
Post:   Commit or abort the transaction.
Input:  iProductVariant         - Product Variant (Mandatory).
iOptionSet              - Option Set. Option set of the product
variant that need to be initialized.
All option sets with values greater
than or equal to the specified input
option set are initialized, along with
their related configurable options
(Mandatory).
iReferenceDate          - Reference Date. If the user does not
provide a value, then the value is
defaulted with date from reference
order of the product variant
(Optional).
Output: oExceptionMessage       - The last error message found
during the execution of public
interface. If multiple error messages
are found, by using ›¼ÀœoExceptionID›¼À•,
messages can be retrieved.
oExceptionID            - An ID that refers to the exception
information. Use ›¼ÀœException›¼À• related
functions to retrieve related
information.
Return: 0                       - Success.
<> 0                    - Error occurred during Initializing
the option sets.
```
