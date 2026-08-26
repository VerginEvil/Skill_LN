# RequestForQuote.PrintRequestForQuote

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for RequestForQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 408-410

```baan
DLL:   tdextpurapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long RequestForQuote.PrintRequestForQuote(
domain  tcqono           iRequestForQuote,
long             iProcessingOptionSet,
ref             boolean          oRequestForQuotePrinted,
ref             boolean          oProcessStopped,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the printing of the Request for Quote
for the given Request for Quote.
Closing of reports:
During the printing of the Request for Quote it is
possible that one or more reports will be opened. Closing
of these reports is also done within this function.
Transaction handling:
Retry                         -point and commit/abort transaction is handled within
this function.
Pre:                  -
Post:                 -
Input:  iRequestForQuote                      - Request for Quote (mandatory)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default printing options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
-               Processing Options have a direct relationship with the form fields
on session "Print Requests for Quotation" (tdsls1401m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Print options which are not available as Processing Options
will get defaulted in accordance with the session logic.
-               Processing Options which are set while a required Implemented
Software Component is not available are ignored.
NAME                                    TYPE                    DEFAULT
Draft                                   boolean                 false
IncludePrintedRFQs                      domain tcyesno          tcyesno.no
TaxText                                 domain tcyesno          tcyesno.yes
RFQLineText                             domain tcyesno          tcyesno.no
ManufacturerPartNumbers                 domain tcyesno          tcyesno.no
ApprovedManufacturerPartNumbersOnly     domain tcyesno          tcyesno.no
MaterialSupplyInformation               domain tcyesno          tcyesno.yes
DetailLines                             domain tcyesno          tcyesno.no
ReceiptAddressPerLine                   domain tcyesno          tcyesno.no
Alternatives                            domain tcyesno          tcyesno.yes
Documents                               domain tcyesno          tcyesno.no
Questions                               domain tcyesno          tcyesno.no
AdditionalInformation                   domain tcyesno          tcyesno.yes
ConformanceReporting                    domain tcyesno          tcyesno.yes
PrintToPredefinedDevice                 domain tcyesno          tcyesno.yes
PrintingDevice                          domain tcmcs.str14      ""
PrintingFileoutPathAndName              domain tcmcs.str100     ""
-               PrintingDevice: This field can be filled with the Device to were the
reports are printed. If not provided a dialog will be shown to
enter the Device or when PrintToPredefinedDevice is set to "Yes"
and defaults are present then printing will be done to the
default printing device(s).
-               PrintingFileoutPathAndName: Depending on the device this field can be
be filled (if needed) with the output path and filename for
storing the file of the printed report.
Output: oRequestForQuotePrinted                       - True: the request for quote has
been printed.
False: the request for quote is
not printed.
oProcessStopped                                       - True: the printing process is stopped
by the user or due to an error.
False: the printing process was
completed.
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Possible that request for quote has
been printed
<> 0                                          - An error occurred
```
