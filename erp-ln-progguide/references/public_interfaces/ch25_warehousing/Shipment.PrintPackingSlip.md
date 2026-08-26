# Shipment.PrintPackingSlip

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1147-1149

```baan
DLL:   whextinhapi
This function is available from     2024.03 (KB2320617  ).
Syntax: long Shipment.PrintPackingSlip(
domain  whinh.shpm       iShipment,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the packing slip for the
iShipment using the defaults or options as provided
in the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success.
Abort the transaction in case of failure.
Input:  iShipment               Optional
iDevice                 Mandatory
iProcessingOptionSet Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iShipment is filled then the following options
of the iProcessingOptionSet will be ignored:
-                       selection range fields (From/To)
-                       ShipmentArray
The Packing Slip will then be printed for the given iShipment.
In case option ShipmentArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
The Packing Slip will then be printed for the shipments in the
array.
Processing Options have a direct relationship with the form fields
on session Print Packing Slips (whinh4475m000) and are not explained
in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ShipmentFrom                    domain whinh.shpm       Minimum Value
ShipmentTo                      domain whinh.shpm       Maximum Value
LoadFrom                        domain whinh.load       Minimum Value
LoadTo                          domain whinh.load       Maximum Value
ShippingContainerFrom           domain whinh.cntr       Minimum Value
ShippingContainerTo             domain whinh.cntr       Maximum Value
ShipFromTypeFrom                domain tctyps           Minimum Value
ShipFromTypeTo                  domain tctyps           Maximum Value
ShipFromCodeFrom                domain tcshpm           Minimum Value
ShipFromCodeTo                  domain tcshpm           Maximum Value
ShipToTypeFrom                  domain tctyps           Minimum Value
ShipToTypeTo                    domain tctyps           Maximum Value
ShipToCodeFrom                  domain tcshpm           Minimum Value
ShipToCodeTo                    domain tcshpm           Maximum Value
CarrierFrom                     domain tccfrw           Minimum Value
CarrierTo                       domain tccfrw           Maximum Value
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
ShipmentConfirmDateFrom         domain tcdate           Minimum Value
ShipmentConfirmDateTo           domain tcdate           Maximum Value
AllShipments                    domain tcyesno          tcyesno.no
UseOrderLanguage                domain tcyesno          tcyesno.yes
NumberOfCopies                  domain tcsrno           0
Reprint                         domain tcyesno          tcyesno.no
PrintDetailedReport             domain tcyesno          tcyesno.no
PrintOwnership                  domain tcyesno          tcyesno.no
PrintApprovalInformation        domain tcyesno          tcyesno.no
PrintVariantOptionDescription   domain tcyesno          tcyesno.no
ShipmentArray                   domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
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
Json.setString(Shipment, "shipment", "SHP008448")
Json.add(ShipmentArray, Shipment)
Shipment = Json.newObject()
Json.setString(Shipment, "shipment", "SHP008428")
Json.add(ShipmentArray, Shipment)
ReportName only needs to filled for customized reports, otherwise
the standard report is automatically used.
ReportName must start with an "r", e.g. "rwhinh447501001"
Output: oDataProcessed                        - true:  Packing Slip Printed.
false: Nothing Printed.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
