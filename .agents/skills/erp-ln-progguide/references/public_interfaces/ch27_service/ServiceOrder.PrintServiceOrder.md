# ServiceOrder.PrintServiceOrder

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1436-1438

```baan
DLL:   tsextsocapi
This function is available from 2026.09 (KB3682934).
Syntax: long ServiceOrder.PrintServiceOrder(
domain  tcorno           iServiceOrder,
long             iProcessingOptionSet,
ref             boolean          oOrderPrinted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the printing of the Service Order for
the given Service Order.
Closing of reports:
During service order printing, one or more reports may be
opened. These reports are closed automatically unless the
Processing Option "KeepReportsOpen" is set to 'true'.
The public interface Printing.CloseOpenReports can be used to
close any remaining open reports if they were not closed
automatically.
Pre:    -
Post:   -
Input:  iServiceOrder           - Service Order (mandatory)
iProcessingOptionSet    - Processing Option Set (Optional).
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
PrintActivityLines              domain tcyesno          tcyesno.no
PrintAssignments                domain tcyesno          tcyesno.no
PrintBlockingReasons            domain tcyesno          tcyesno.no
PrintInterruptedOrders          domain tcyesno          tcyesno.no
PrintRequiredSkills             domain tcyesno          tcyesno.no
PrintEstimatedMaterial          domain tcyesno          tcyesno.no
PrintEstimatedLabor             domain tcyesno          tcyesno.no
PrintEstimatedOther             domain tcyesno          tcyesno.no
PrintActualMaterial             domain tcyesno          tcyesno.no
PrintActualLabor                domain tcyesno          tcyesno.no
PrintActualOther                domain tcyesno          tcyesno.no
PrintFailureAnalysis            domain tcyesno          tcyesno.no
PrintOptionSummarized           domain tcyesno          tcyesno.yes
--- Currency Options ---
PrintCurrency                   domain tcccur           ""
SalesCurrency                   domain tcccur           ""
RateType                        domain tcrtyp           ""
--- Text Attachments ---
PrintHeaderText                 domain tcyesno          tcyesno.no
PrintCancellationText           domain tcyesno          tcyesno.no
PrintInvoiceText                domain tcyesno          tcyesno.no
PrintActivityText               domain tcyesno          tcyesno.no
PrintCallText                   domain tcyesno          tcyesno.no
PrintSolutionText               domain tcyesno          tcyesno.no
PrintCostLineText               domain tcyesno          tcyesno.no
--- Device Options ---
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
The Processing Options correspond directly to the fields in the Print
Service Orders session (tssoc2400m000) and are therefore not all
described below. For additional information, refer to the session help.
- From the Report Options, only one type can be set to tcyesno.yes.
E.g. when Assigments are printed, Skills or cost lines can no
longer be selected. Or when one or more types of cost lines are
selected, e.g. the activity lines cannot be selected.
The Failure Analysis however, can only be selected simultaneously with
material cost lines.
- The Interrupted Orders flag of the session is not available, as the
requested order is printed, irrespective of interruption.
- The Currency Options 'Cost Currency' and 'Sales Currency' are only
applicable in case of a dependent currency system.
The defaults are determined the same way as in the session.
- PrintingFileoutPathAndName: Depending on the device this field can
be filled (if needed) with the output path and filename for
storing the file of the printed report.
Output: oOrderPrinted           - True: the service order has been printed.
False: the service order is not printed.
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
