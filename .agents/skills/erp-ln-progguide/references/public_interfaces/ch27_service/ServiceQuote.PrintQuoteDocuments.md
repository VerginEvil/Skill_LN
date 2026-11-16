# ServiceQuote.PrintQuoteDocuments

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1477-1479

```baan
DLL:   tsexteppapi
This function is available from 2026.10 (KB3682936).
Syntax: long ServiceQuote.PrintQuoteDocuments(
domain  tcorno           iQuote,
domain  tcpono           iRevision,
long             iProcessingOptionSet,
ref             boolean          oQuoteDocumentsPrinted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the printing of Quote Documents for
the given Quote.
Closing of reports:
During quote document printing, one or more reports may be
opened. These reports are closed automatically unless the
Processing Option "KeepReportsOpen" is set to 'true'.
The public interface Printing.CloseOpenReports can be used to
close any remaining open reports if they were not closed
automatically.
Database handling:
A db.retry.point() will be set and used if an external
document is printed or if text fields are printed.
Pre:    No open database transactions when external reports are printed.
Post:   Note that an abort.transaction() or commit.transaction() has
been executed.
Input:  iQuote                  - Quote (mandatory)
iRevision               - Revision (provide 0 if 'Revisions' is
not implemented, otherwise mandatory)
iProcessingOptionSet    - Processing Option Set (optional)
If set to 0, the default printing
options are applied.
A Processing Option Set can be created by calling
ProcessingOptionSet.Create() in the tcextextapi DLL. After use, the
option set can be deleted by calling ProcessingOptionSet.Delete().
Processing Options specified while a required Implemented Software
Component is not available are ignored.
NAME                            TYPE                    DEFAULT
KeepReportsOpen                 boolean                 false
--- Report Options ---
DocumentType                    domain tsmdm.prwh02     tsmdm.prwh02.internal
LineType                        domain tsepp.koql       5 (All Lines)
5 = All Lines
10 = New / Changed Lines
15 = Incl. Printed Lines
PrintLineAmounts                domain tcyesno          tcyesno.yes
PrintAlternatives               domain tcyesno          tcyesno.no
PrintTaxSummary                 domain tcyesno          tcyesno.no
IncludeQuoteText                domain tcyesno          tcyesno.no
PrintAdditionalInformation      domain tcyesno          tcyesno.no
--- Quote Cost Lines ---
QuoteCostLines                  domain tcyesno          tcyesno.no
CostTypeMaterial                domain tcyesno          tcyesno.no
CostTypeLabor                   domain tcyesno          tcyesno.no
CostTypeTooling                 domain tcyesno          tcyesno.no
CostTypeTraveling               domain tcyesno          tcyesno.no
CostTypeSubcontracting          domain tcyesno          tcyesno.no
CostTypeHelpDesk                domain tcyesno          tcyesno.no
CostTypeOther                   domain tcyesno          tcyesno.no
CostTypeFreight                 domain tcyesno          tcyesno.no
--- Currency Options ---
SalesCurrency                   domain tcccur           tsepp100.ccur
ExchangeRateType                domain tcrtyp           ""
--- Device Options ---
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
The Processing Options correspond directly to the fields in the Print
Quote Documents session (tsepp1400m000) and are therefore not all
described below. For additional information, refer to the session help.
- The Quote Cost Lines option enables/disables printing of cost lines.
When enabled, individual cost types can be selected. If the option
QuoteCostLines is set to no, all Cost Type options are ignored.
- The rate type is only applicable in case of a standard currency system.
- PrintingDevice: If no Printing Device is provided, a dialog will be
shown to enter the Device.
- PrintingFileoutPathAndName: Depending on the device this field can
be filled (if needed) with the output path and filename for
storing the file of the printed report.
Output: oQuoteDocumentsPrinted  - True: the quote document has been
printed.
False: the quote document is not
printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No problems have occurred. This does
not mean the document has been printed.
<> 0                    - An error occurred, but the document
might be printed anyways.
```
