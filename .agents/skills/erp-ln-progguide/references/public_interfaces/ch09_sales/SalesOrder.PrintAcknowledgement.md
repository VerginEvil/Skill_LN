# SalesOrder.PrintAcknowledgement

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 327-329

```baan
DLL:   tdextslsapi
This function is available from 2024.08 (KB3511996).
Syntax: long SalesOrder.PrintAcknowledgement(
domain  tcorno           iSalesOrder,
long             iProcessingOptionSet,
ref             boolean          oOrderPrinted,
ref             boolean          oProcessStopped,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the printing of the
Sales Order Acknowledgement for the given Sales Order.
Closing of reports:
During the printing of the sales order it is possible that
one or more reports will be opened. Closing of these reports
is also done within this function.
Transaction handling:
Retry-point and commit/abort transaction is handled within
this function.
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'SalesOrderLine.StartAutomaticProcessing'
Pre:    -
Post:   -
Input:  iSalesOrder             - Sales Order (mandatory)
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default printing options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Print Sales Order Acknowledgements/RMAs" (tdsls4401m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Print options which are not available as Processing Options
will get defaulted in accordance with the session logic.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
NAME                                    TYPE                    DEFAULT
Draft                                   boolean                 false
OrderLineTypesToPrint                   domain tdsls.kofl
tdsls.kofl.exc.printed
OnlyNewCanceledLines                    domain tcyesno          tcyesno.yes
DocumentsToPrint                        domain tdsls.docs       tdsls.docs.acks
QuantityToPrint                         domain tdsls.koqu
tdsls.koqu.ordered.quan
OrderAmountFrom                         domain tcamnt           0.0
OrderAmountFromCurrency                 domain tcccur           ""
DeliveryDateFrom                        domain tcdate           0
PrintVariantOptions                     domain tcyesno          tcyesno.yes
PrintVariantSalesPriceStructure         domain tcyesno          tcyesno.yes
PrintPromotions                         domain tcyesno          tcyesno.yes
PrintUEFRequirements                    domain tcyesno          tcyesno.yes
PrintComponentLines                     domain tcyesno          tcyesno.yes
PrintMaterialPriceInformation           domain tcyesno          tcyesno.no
PrintAppendixMaterialSupplyInformation  domain tcyesno          tcyesno.yes
PrintAppendixConformanceReporting       domain tcyesno          tcyesno.no
PrintAppendixAfterSalesService          domain tcyesno          tcyesno.no
PrintAppendixEndUserStatements          domain tcyesno          tcyesno.yes
PrintAppendixLicenses                   domain tcyesno          tcyesno.yes
PrintAppendixLettersOfCredit            domain tcyesno          tcyesno.no
PrintAppendixBankGuaranteeApplicant     domain tcyesno          tcyesno.yes
PrintAppendixBankGuaranteeBeneficiary   domain tcyesno          tcyesno.yes
PrintToPredefinedDevice                 domain tcyesno          tcyesno.yes
PrintingDevice                          domain tcmcs.str14      ""
PrintingFileoutPathAndName              domain tcmcs.str100     ""
- PrintingDevice: This field can be filled with the Device to where the
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
