# Shipment.PrintPickAndLoadSheet

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1159-1161

```baan
DLL:   whextinhapi
This function is available from 2024.04 (KB2328091).
Syntax: long Shipment.PrintPickAndLoadSheet(
domain  whinh.shpm       iShipment,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the pick and load sheet
for the iShipment using the defaults or options as provided
in the iProcessingOptionSet.
Opening/Closing of the report(s) is handled by this function.
Pre:    N.a.
Post:   N.a.
Input:  iShipment               Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iShipment is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- ShipmentArray
The Pick and Load Sheet will then be printed for the given
iShipment.
In case option ShipmentArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
The Pick and Load Sheet will then be printed for the shipments
in the array.
Processing Options have a direct relationship with the form fields
on session Print Pick and Load Sheet (whinh4430m200) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
LoadFrom                domain whinh.load       Minimum Value
LoadTo                  domain whinh.load       Maximum Value
ShipmentFrom            domain whinh.shpm       Minimum Value
ShipmentTo              domain whinh.shpm       Maximum Value
ShipToTypeFrom          domain tctyps           Minimum Value
ShipToTypeTo            domain tctyps           Maximum Value
ShipToCodeFrom          domain tccshp           Minimum Value
ShipToCodeTo            domain tccshp           Maximum Value
RouteFrom               domain tccrte           Minimum Value
RouteTo                 domain tccrte           Maximum Value
PlannedDeliveryDateFrom domain tcdate           Minimum Value
PlannedDeliveryDateTo   domain tcdate           Maximum Value
ShipmentLineStatusFrom  domain whinh.shst       Minimum Value
ShipmentLineStatusTo    domain whinh.shst       Maximum Value
OrderOriginFrom         domain whinh.oorg       Minimum Value
OrderOriginTo           domain whinh.oorg       Maximum Value
OrderNumberFrom         domain tcorno           Minimum Value
OrderNumberTo           domain tcorno           Maximum Value
OrderLineFrom           domain tcpono           Minimum Value
OrderLineTo             domain tcpono           Maximum Value
WarehouseFrom           domain tccwar           Minimum Value
WarehouseTo             domain tccwar           Maximum Value
ItemFrom                domain tcitem           Minimum Value
ItemTo                  domain tcitem           Maximum Value
SortByReference         domain whinh.sssr       whinh.sssr.reference
SortByOrder             domain whinh.plss       whinh.plss.ascending
PrintShipmentAsBarcode  domain tcyesno          tcyesno.no
BarcodeType             domain tcbctype         tcbctype.not.appl
BarcodeHeight           tcmcs.byte1             0
ShipmentArray           domain ttjson           0
ReportNameAscending     domain tcmcs.str16      Empty String
ReportNameDescending    domain tcmcs.str16      Empty String
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
ReportNameAscending and ReportNameDescending only need to filled for
customized reports, otherwise the standard reports are used based on
the SortByOrder.
ReportNames must start with an "r", e.g. "rwhinh443011201"
Output: oDataProcessed          - true:  Pick and Load Sheet Printed.
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
