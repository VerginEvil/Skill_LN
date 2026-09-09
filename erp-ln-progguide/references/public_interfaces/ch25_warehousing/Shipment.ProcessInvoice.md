# Shipment.ProcessInvoice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1161-1164

```baan
DLL:   whextinhapi
This function is available from 2025.12 (KB3621390).
Syntax: long Shipment.ProcessInvoice(
domain  whinh.shpm       iShipment,
domain  tcsli.tinv       iTypeOfInvoice,
domain  tcpitp           iInvoiceType,
boolean          iProcessInvoice,
domain  tcmcs.str15      iInvoiceDevice,
domain  tcmcs.str15      iErrorDevice,
long             iProcessingOptionSet,
ref             boolean          oSetNewRetryPoint,
ref             boolean          oErrorFound,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will process the invoice for the iShipment
using the defaults or options as provided in the
i.processing.option.set.
If the i.type.of.invoice = Standard a real (definitive) invoice
will created.
Roughly this function comprises of two steps:
1) For each billable order origin the corresponding source
package is called for creating the billable lines in CI.
2) Finally, CI is called for composing and printing the invoice.
Step 2 is only performed when iProcessInvoice is true.
Opening/Closing of the report(s) is handled by this function.
Pre:    Shipment(s) are Frozen / Confirmed.
db.retry.point must be set when iProcessInvoice is false.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iShipment               Optional
iTypeOfInvoice          Pro Forma Invoice, Customs Invoice,
Consigment Invoice or Standard Invoice.
iInvoiceType            Mandatory when iTypeOfInvoice is
Pro Forma Invoice, Customs Invoice or
Consigment Invoice.
Ignored for Standard Invoice.
iProcessInvoice         Mandatory,
true  - Step 2 is performed.
false - Step 2 is not performed.
iInvoiceDevice          Mandatory but will be overruled with
predefined device if
PrintToPredefinedDevice has value
tcyesno.yes.
iErrorDevice            Mandatory when PrintErrors has value
tcyesno.yes.
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iShipment is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- ShipmentArray
The invoice will then be processed for the given iShipment.
In case option ShipmentArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
The invoice will then be processed for the shipments in the
array.
Processing Options have a direct relationship with the form fields
on session Process Pro Forma Invoices (whinh4279m000)/ Process Invoices
(whinh4279m100) and are not explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
ShipmentFrom            domain whinh.shpm       Minimum Value
ShipmentTo              domain whinh.shpm       Maximum Value
LoadFrom                domain whinh.load       Minimum Value
LoadTo                  domain whinh.load       Maximum Value
ShipFromTypeFrom        domain tctyps           Minimum Value
ShipFromTypeTo          domain tctyps           Maximum Value
ShipFromCodeFrom        domain tccshp           Minimum Value
ShipFromCodeTo          domain tccshp           Maximum Value
ShipToTypeFrom          domain tctyps           Minimum Value
ShipToTypeTo            domain tctyps           Maximum Value
ShipToCodeFrom          domain tccshp           Minimum Value
ShipToCodeTo            domain tccshp           Maximum Value
AllShipments            domain tcyesno          tcyesno.no
PrintToPredefinedDevice domain tcyesno          tcyesno.yes
PrintErrors             domain tcyesno          tcyesno.yes
ShipmentArray           domain ttjson           0
ReportName              domain tcmcs.str16      Empty String
JSON Object ShipmentArray has the following structure:
"ShipmentArray": [
{
"Shipment": "SHP008448"
},
{
"Shipment": "SHP008428"
}
]
This structure can be created with the following code:
ShipmentArray = Json.newArray()
Shipment = Json.newObject()
Json.setString(Shipment, "Shipment", "SHP008448")
Json.add(ShipmentArray, Shipment)
Shipment = Json.newObject()
Json.setString(Shipment, "Shipment", "SHP008428")
Json.add(ShipmentArray, Shipment)
ReportName only needs to filled for customized error report, otherwise
the report related to the session is automatically used.
ReportName must start with an "r", e.g. "rwhinh427901001"
Output: oSetNewRetryPoint       - true:  New db.retry.point needs to be
set.
false: No new db.retry.point needs to
be set.
oErrorFound             - Error found
oDataProcessed          - true:  Invoice data is processed.
false: Nothing Printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
