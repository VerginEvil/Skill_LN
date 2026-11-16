# ServiceOrderMaterialCosts.RecalculatePriceDiscounts

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderMaterialCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1468-1469

```baan
DLL:   tsextsocapi
This function is available from 2026.07 (KB3680879).
Syntax: long ServiceOrderMaterialCosts.RecalculatePriceDiscounts(
domain  tcorno           iServiceOrder,
domain  tcpono           iMaterialLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to recalculate the sales prices and discounts
for a Service Order Material line.
Pre:    db.retry.point must have been set.
Post:   Commit/abort the transaction.
Input:  iServiceOrder
Service Order
Mandatory
iMaterialLine
Service Order Material Line
Mandatory
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Not mandatory
NAME                    TYPE                    DEFAULT
================================================================
OverwriteManualPrice    domain  tcyesno         tcyesno.yes
OverwriteManualDiscounts
domain  tcyesno         tcyesno.yes
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No Error
<> 0                    - Error
```
