# PurchaseOrderLine.RecalculatePriceAndDiscounts

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 461-463

```baan
DLL:   tdextpurapi
This function is available from     2026.07 (KB3675187  ).
Syntax: long PurchaseOrderLine.RecalculatePriceAndDiscounts(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iPurchaseOrderLineSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function handles the recalculation of prices and discounts,
and the redetermination of material price information for the given
purchase order line.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder                                - Purchase Order (Mandatory)
iPurchaseOrderLine                                    - Purchase Order Line (Mandatory)
iPurchaseOrderLineSequence                            - Purchase Order Line Sequence
iProcessingOptionSet                                  - Processing Option Set (Optional).
If 0, the default recalculate options
are applied.
A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Price and Discount Recalculation Parameters" (tdpcg0240s000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Recalculate options which are not available as Processing Options
are defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
Supported Processing Options and their defaults:
NAME                                            TYPE                    DEFAULT
RecalculatePrice                                domain tcyesno
tcyesno.yes
RecalculateDiscount                             domain tcyesno
tcyesno.yes
RedetermineMaterialPriceAgreement               domain tcyesno
tcyesno.yes
OverwriteManualMaterialPriceAgreement           domain tcyesno          tcyesno.no
RedetermineMaterialLines                        domain tcyesno
tcyesno.yes
OverwriteManualMaterialLines                    domain tcyesno          tcyesno.no
OverwriteIgnoredMaterialLines                   domain tcyesno          tcyesno.no
RedetermineMaterialActualPrices                 domain tcyesno
tcyesno.yes
OverwriteManualMaterialActualPrices             domain tcyesno          tcyesno.no
Output: oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Recalculation was successful, or
no recalculation needed to be done.
<> 0                                                  - An error occurred.
```
