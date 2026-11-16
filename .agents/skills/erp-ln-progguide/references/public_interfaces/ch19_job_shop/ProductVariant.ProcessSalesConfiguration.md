# ProductVariant.ProcessSalesConfiguration

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 683-684

```baan
DLL:   tiextpcfapi
This function is available from 2025.03 (KB3536251).
Syntax: long ProductVariant.ProcessSalesConfiguration(
domain  tccpva           iProductVariant,
long             iProcessingOptionSet,
ref             long             oNumberOfProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to Process Sales
Configurations. The executed process is similar to the process
that is performed when tipcf5205m000 is used via the standard
interface.
Pre:    N.A.
Post:   N.A.
Input:  iProductVariant         Product Variant. (Optional).
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields
on session Process Sales Configurations (tipcf5205m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Process Sales Configurations options which are not available as
Processing Options will get defaulted in accordance with the session
logic.
NAME                            TYPE                    DEFAULT
ProductVariantFrom              domain  tccpva          iProductVariant
ProductVariantTo                domain  tccpva          999999999
ConfigurationStatusFrom         domain  tipcf.acfs      empty
ConfigurationStatusTo           domain  tipcf.acfs      empty
ConfigurationDateFrom           domain  tiutcs          0
ConfigurationDateTo             domain  tiutcs          max value of domain
RequestedOfflineDateFrom        domain  tiutcd          0
RequestedOfflineDateTo          domain  tiutcd          max value of domain
ItemFrom                        domain  tcitem          ""
ItemTo                          domain  tcitem          max value of domain
PrintReport                             boolean         false
PrintingDevice                  domain  tcmcs.str14     ""
PrintingFileoutPathAndName      domain  tcmcs.str100    ""
Default values:
ProductVariantFrom              - If the input variable field
ProductVariantFrom is given, it will
be used as the default value,
otherwise it will be defaulted with 0.
*To                             - If the "*From" field is provided then
"*To" field will be defaulted with
"*From" field, otherwise the "*To"
fields will be defaulted to their
maximum domain value.
Output: oNumberOfProcessed      - The number of Product Variants that
were successfully processed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Processed Sales configuration
successfully.
<> 0                    - Otherwise.
```
