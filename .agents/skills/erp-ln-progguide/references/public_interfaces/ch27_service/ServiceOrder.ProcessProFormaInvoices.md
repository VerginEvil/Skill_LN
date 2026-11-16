# ServiceOrder.ProcessProFormaInvoices

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1438-1439

```baan
DLL:   tsextsocapi
This function is available from 2026.10 (KB3699767).
Syntax: long ServiceOrder.ProcessProFormaInvoices(
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
long             iProcessingOptionSet,
ref             boolean          oProFormaInvoiceProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the Pro Forma Invoice for a Service
Order or a Service Order Activity.
The processing corresponds to the session Process Service Order
Pro Forma Invoices (tssoc2291m000).
Pre:    db.retry.point must have been set.
Post:   Commit/abort the transaction.
Input:  iServiceOrder           - Service Order (Mandatory).
iActivityLine           - Activity Line (Optional).
If set to 0, pro forma invoices will
be processed and printed for all
activity lines for the order.
iProcessingOptionSet    - Processing Option Set (Optional).
If set to 0, the default processing
options are applied.
A Processing Option Set can be created by calling
ProcessingOptionSet.Create() in the tcextextapi DLL. After use, the
option set can be deleted by calling ProcessingOptionSet.Delete().
Processing Options specified while a required Implemented Software
Component is not available, are ignored.
NAME                            TYPE                    DEFAULT
--- Cost Types ---
ProcessMaterialCosts            domain tcyesno          tcyesno.yes
ProcessLaborCosts               domain tcyesno          tcyesno.yes
ProcessOtherCosts               domain tcyesno          tcyesno.yes
ProcessSubcontractingCosts      domain tcyesno          tcyesno.yes
ProcessTravelCosts              domain tcyesno          tcyesno.yes
ProcessToolingCosts             domain tcyesno          tcyesno.yes
ProcessHelpdeskCosts            domain tcyesno          tcyesno.yes
ProcessFreightCosts             domain tcyesno          tcyesno.yes
ProcessRentalCosts              domain tcyesno          tcyesno.yes
ProcessFixedOrderPrice          domain tcyesno          tcyesno.yes
ProcessFixedActivityPrice       domain tcyesno          tcyesno.yes
ProcessQuoteInvoice             domain tcyesno          tcyesno.yes
--- Print Invoice As ---
TypeOfInvoice                   domain tcsli.tinv       tcsli.tinv.pro.forma
ProFormaInvoicingType           domain tcpitp           As defined in
Pro Forma
Invoicing Types
(tcmcs067).
--- Options ---
PrintErrors                     domain tcyesno          tcyesno.yes
--- Device Options ---
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
KeepReportsOpen                 boolean                 false
Reports are closed automatically unless the Processing Option
"KeepReportsOpen" is set to 'true'.
The public interface Printing.CloseOpenReports can be used to close any
remaining open reports if they were not closed automatically.
If the invoice is printed as a Customs Invoice, only the Cost Type
Material is applicable. In that case, all other Cost Types are ignored.
Output: oProFormaInvoiceProcessed - The Pro Forma Invoice is processed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Processing completed successfully
<> 0                    - An error occurred
```
