# SalesOrderLine.RecalculatePriceAndDiscounts

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 353-354

```baan
DLL:   tdextslsapi
This function is available from     2024.06 (KB3500234  ).
Syntax: long SalesOrderLine.RecalculatePriceAndDiscounts(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will handle the recalculation of prices and
discounts and the redetermination of material price
information for the given sales order line.
Pre:    Caller must set the retry              -point
Post:   Caller must commit/abort the transaction.
Input:  iSalesOrder                           - Sales Order (Mandatory)
iSalesOrderLine                               - Sales Order Line (Mandatory)
iSalesOrderSequence                           - Sales Sequence number ( must be >= 0)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default recalculate options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Price and Discount Recalculation Parameters" (tdpcg0240s000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Recalculate options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
NAME                                    TYPE                    DEFAULT
RecalculatePrice                        domain tcyesno          tcyesno.yes
RecalculateProductVariantPrice          domain tcyesno          tcyesno.no
RecalculateEffectivityUnitPrice         domain tcyesno          tcyesno.no
RecalculateDiscount                     domain tcyesno          tcyesno.yes
RedetermineMaterialPriceInformation     domain tcyesno          tcyesno.yes
RedetermineMaterialPriceAgreement       domain tcyesno          tcyesno.yes
OverwriteManualMaterialPriceAgreement   domain tcyesno          tcyesno.no
RedetermineMaterialLines                domain tcyesno          tcyesno.yes
OverwriteManualMaterialLines            domain tcyesno          tcyesno.no
OverwriteIgnoredMaterialLines           domain tcyesno          tcyesno.no
RedetermineMaterialActualPrices         domain tcyesno          tcyesno.yes
OverwriteManualMaterialActualPrices     domain tcyesno          tcyesno.no
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Recalculation was successful, or
no recalculation needed to be done.
<> 0                                          - An error occurred
```
