# PurchaseOrder.PrintPurchaseOrder

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 445-447

```baan
DLL:   tdextpurapi
This function is available from 2024.08 (KB3511996).
Syntax: long PurchaseOrder.PrintPurchaseOrder(
domain  tcorno           iPurchaseOrder,
long             iProcessingOptionSet,
ref             boolean          oOrderPrinted,
ref             boolean          oProcessStopped,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the printing of the Purchase Order for
the given Purchase Order.
Closing of reports:
During the printing of the purchase order it is possible that
one or more reports will be opened. Reports are closed automatically
unless Processing Option "KeepReportsOpen" is passed as 'true' for
Processing Option "ReportType" is '1' (Purchase Order Acknowledgement).
The Public Interface 'Printing.CloseOpenReports' can be used to close
the reports afterwards if not done automatically.
Transaction handling:
Retry-point and commit/abort transaction is handled within
this function.
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'PurchaseOrder.StartAutomaticProcessing'
Pre:    -
Post:   -
Input:  iPurchaseOrder          - Purchase Order (Mandatory)
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default printing options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
- If Processing Option "ReportType" is '1' (Purchase Order Acknowledgement) the
other Processing Options have a direct relationship with the form fields on
session "Print Purchase Orders" (tdpur4401m000) and are not explained in further
detail here. Please refer to the session help for additional information.
Print options which are not available as Processing Options will get defaulted in
accordance with the session logic.
Processing Options which are set while a required Implemented Software Component
is not available are ignored.
- If Processing Option "ReportType" is '2' (Purchase Order Preview) the other
Processing Options are ignored. Printing is based on session "Preview Purchase
Orders" (tdpur4401m200).
NAME                                    TYPE                    DEFAULT
ReportType                              long                    1
KeepReportsOpen                         boolean                 false
Draft                                   boolean                 false
OrderLineTypesToPrint                   domain tdpur.kofl
tdpur.kofl.exc.printed
OnlyNewCanceledLines                    domain tcyesno          tcyesno.yes
ExcludeLinesWithChangeCodes             domain tcyesno          tcyesno.no
LinesToPrint                            domain tdsls.koqu
tdsls.koqu.ordered.quan
QuantitiesPrintedIn                     domain tdgen.utop
tdgen.utop.order.unit
PrintVariantOptions                     domain tcyesno          tcyesno.yes
PrintTaxText                            domain tcyesno          tcyesno.yes
PrintPrices                             domain tcyesno          tcyesno.yes
PrintCustomsValue                       domain tcyesno          tcyesno.no
PrintDeliveryAddressPerLine             domain tcyesno          tcyesno.no
PrintManufacturerPartNumbers            domain tcyesno          tcyesno.no
PrintLandedCosts                        domain tcyesno          tcyesno.no
PrintMaterialPriceInformation           domain tcyesno          tcyesno.no
PrintAppendixMaterialSupplyInformation  domain tcyesno          tcyesno.yes
PrintAppendixLandedCosts                domain tcyesno          tcyesno.yes
PrintAppendixConformanceReporting       domain tcyesno          tcyesno.yes
PrintAppendixAdditionalInformation      domain tcyesno          tcyesno.yes
PrintAppendixEndUserDeclarations        domain tcyesno          tcyesno.yes
PrintAppendixLicenses                   domain tcyesno          tcyesno.yes
PrintAppendixLettersOfCredit            domain tcyesno          tcyesno.no
PrintAppendixBankGuaranteeApplicant     domain tcyesno          tcyesno.yes
PrintAppendixBankGuaranteeBeneficiary   domain tcyesno          tcyesno.yes
PrintToPredefinedDevice                 domain tcyesno          tcyesno.yes
PrintingDevice                          domain tcmcs.str14      ""
PrintingFileoutPathAndName              domain tcmcs.str100     ""
- PrintingDevice: This field can be filled with the Device to were the
reports are printed. If not provided a dialog will be shown to
enter the Device or when PrintToPredefinedDevice is set to "Yes"
and defaults are present then printing will be done to the
default printing device(s).
- PrintingFileoutPathAndName: Depending on the device this field can be
be filled (if needed) with the output path and filename for
storing the file of the printed report.
Output: oOrderPrinted           - True: the purchase order has been printed.
False: the purchase order is not printed.
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
Return: 0                       - Possible that order has been printed
<> 0                    - An error occurred
```
