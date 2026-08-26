# CrossDockOrderLines.Print

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for CrossDockOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1303-1306

```baan
DLL:   whextinhapi
This function is available from     2024.09 (KB3513678  ).
Syntax: long CrossDockOrderLines.Print(
domain  tcorno           iCrossDockOrder,
domain  tcpono           iCrossDockOrderLine,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the cross-dock order lines for
the iCrossDockOrder and iCrossDockOrderLine using the defaults
or options as provided in the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    N.a.
Post:   N.a.
Input:  iCrossDockOrder         Optional
iCrossDockOrderLine     Optional, ignored if iCrossDockOrder
is empty.
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iCrossDockOrder is filled then the following options
of the iProcessingOptionSet will be ignored:
-                       selection range fields (From/To)
-                       CrossDockOrderLineArray
The cross                      -dock order lines will then be printed for the given
iCrossDockOrder (and specific iCrossDockOrderLine, if filled).
In case option CrossDockOrderLineArray is set then the selection
range fields (From/To) of the iProcessingOptionSet will be
ignored.
The cross                      -dock order lines will then be printed for the
cross                      -dock order lines in the array.
Processing Options have a direct relationship with the form fields
on session Print Cross              -dock Order Lines (whinh6410m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
StagingLocationFrom             domain whloca           Minimum Value
StagingLocationTo               domain whloca           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
CrossDockOrderFrom              domain tcorno           Minimum Value
CrossDockOrderTo                domain tcorno           Maximum Value
CrossDockOrderTypeFrom          domain whinh.cdty       Minimum Value
CrossDockOrderTypeTo            domain whinh.cdty       Maximum Value
CrossDockOrderStatusFrom        domain whinh.cdos       Minimum Value
CrossDockOrderStatusTo          domain whinh.cdos       Maximum Value
OutboundOrderOriginFrom         domain whinh.oorg       Minimum Value
OutboundOrderOriginTo           domain whinh.oorg       Maximum Value
OutboundOrderNumberFrom         domain tcorno           Minimum Value
OutboundOrderNumberTo           domain tcorno           Maximum Value
OutboundOrderLineFrom           domain tcpono           Minimum Value
OutboundOrderLineTo             domain tcpono           Maximum Value
PlannedDeliveryDateFrom         domain tcdate           Minimum Value
PlannedDeliveryDateTo           domain tcdate           Current Date/Time
CrossDockOrderLineFrom          domain tcpono           Minimum Value
CrossDockOrderLineTo            domain tcpono           Maximum Value
InboundOrderOriginFrom          domain whinh.oorg       Minimum Value
InboundOrderOriginTo            domain whinh.oorg       Maximum Value
InboundOrderNumberFrom          domain tcorno           Minimum Value
InboundOrderNumberTo            domain tcorno           Maximum Value
InboundOrderLineFrom            domain tcpono           Minimum Value
InboundOrderLineTo              domain tcpono           Maximum Value
PlannedReceiptDateFrom          domain tcdate           Minimum Value
PlannedReceiptDateTo            domain tcdate           Maximum Value
CrossDockOrderLineStatusFrom    domain whinh.cdls       Minimum Value
CrossDockOrderLineStatusTo      domain whinh.cdls       Maximum Value
ReportNumber                    domain tcmcs.long       1
CrossDockOrderLineArray         domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
Possible values of ReportNumber are:
1                       - By Cross-dock Line
JSON Object CrossDockOrderLineArray has the following structure:
"CrossDockOrderLineArray": [
{
"OrderNumber": "COD000006"
"OrderLine": 10,
},
{
"OrderNumber": "COD000003"
"OrderLine": 20,
}
]
This structure can be created with the following code:
CrossDockOrderLineArray = Json.newArray()
CrossDockOrderLine = Json.newObject()
Json.setString(CrossDockOrderLine, "OrderNumber", "COD000006")
Json.setNumber(CrossDockOrderLine, "OrderLine", 10)
Json.add(CrossDockOrderLineArray, CrossDockOrderLine)
CrossDockOrderLine = Json.newObject()
Json.setString(CrossDockOrderLine, "OrderNumber", "COD000003")
Json.setNumber(CrossDockOrderLine, "OrderLine", 20)
Json.add(CrossDockOrderLineArray, CrossDockOrderLine)
ReportName only needs to filled for customized reports,
otherwise the standard report is used based on the ReportNumber.
ReportName must start with an "r", e.g. "rwhinh641001001"
Output: oDataProcessed                        - true:  Data Printed.
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

## Public Interfaces for Run

The following functions are available: Run.DetermineNumber
