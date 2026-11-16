# SalesQuote.Print

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 292-294

```baan
DLL:   tdextslsapi
This function is available from 2026.07 (KB3674553).
Syntax: long SalesQuote.Print(
domain  tcqono           iSalesQuote,
long             iProcessingOptionSet,
ref             boolean          oSalesQuotePrinted,
ref             boolean          oProcessStopped,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function handles the printing of the given sales quote.
Closing of reports:
During the printing of the sales quote, one or more reports may be
opened. This function also closes these reports.
Transaction handling:
Retry-point and commit/abort transaction are handled within
this function.
Pre:    NA
Post:   NA
Input:  iSalesQuote             - Sales Quote (Mandatory)
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields on session
"Print Sales Quotations" (tdsls1401m000) and are not explained in further
detail here. Please refer to the session help for additional information.
Print options which are not available as Processing Options are defaulted
in accordance with the session logic.
Processing Options which are set while a required Implemented Software
Component is not available are ignored.
Supported Processing Options and their defaults:
NAME                                    TYPE                    DEFAULT
Draft                                   boolean                 false
ExcludeCanceledAndLostLines             domain tcyesno          tcyesno.no
PrintMaterialPriceInformation           domain tcyesno          tcyesno.no
PrintAppendixVariantOptions             domain tcyesno          tcyesno.no
PrintAppendixUEFRequirements            domain tcyesno          tcyesno.no
PrintAppendixVariantSalesPriceStructure domain tcyesno          tcyesno.no
PrintAppendixAfterSalesService          domain tcyesno          tcyesno.no
PrintToPredefinedDevice                 domain tcyesno          tcyesno.yes
PrintingDevice                          domain tcmcs.str14      ""
PrintingFileoutPathAndName              domain tcmcs.str100     ""
- PrintingDevice: This field can be filled with the device to where the
reports are printed. If not provided, a dialog will be shown to
enter the device, or when PrintToPredefinedDevice is set to "Yes"
and defaults are present, printing will be done to the default
printing device(s).
- PrintingFileoutPathAndName: Depending on the device, this field can be
filled (if needed) with the output path and filename for
storing the file of the printed report.
Output: oSalesQuotePrinted      - True: the sales quote has been printed.
False: the sales quote is not printed.
oProcessStopped         - True: the printing process is stopped by
the user or due to an error.
False: the printing process was completed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The sales quote may have been printed.
<> 0                    - An error occurred.
```
