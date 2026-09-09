# ProductVariant.ReprocessCPQConfiguration

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 686-687

```baan
DLL:   tiextpcfapi
This function is available from 2025.04 (KB3561937).
Syntax: long ProductVariant.ReprocessCPQConfiguration(
domain  tccpva           iProductVariant,
long             iProcessingOptionSet,
ref             boolean          oProductVariantProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to reprocess a Product Variant
which is configured using CPQ. Any changes in the CPQ model are
applied to the configuration. Product variants with a product
structure will have the product structure regenerated.
Transaction management is handled by the Public Interface.
Pre:    N.A.
Post:   N.A.
Input:  iProductVariant         Product Variant. (Mandatory).
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields
on session Reprocess CPQ Configurations (tipcf2221m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Reprocess CPQ Configurations options which are not available as
Processing Options will get defaulted in accordance with the session
logic.
NAME                            TYPE                    DEFAULT
UpdatePCSProjectReferenceDate   domain  tcyesno         tcyesno.no
PCSProjectReferenceDate         domain  tcdate          Current date
CheckStandardItemInventory      domain  tcyesno         tcyesno.yes
UpdatePricesQuotationLines      domain  tcyesno         tcyesno.yes
UpdatePricesSalesOrderLines     domain  tcyesno         tcyesno.yes
Output: oProductVariantProcessed
- True, If Product Variant is
reprocessed successfully.
False, If  Product Variant is
not reprocessed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Reprocessed CPQ configuration
successfully.
<> 0                    - Otherwise.
```
