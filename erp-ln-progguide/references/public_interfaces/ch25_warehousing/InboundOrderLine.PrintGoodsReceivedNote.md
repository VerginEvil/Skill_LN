# InboundOrderLine.PrintGoodsReceivedNote

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1088-1091

```baan
DLL:   whextinhapi
This function is available from 2024.03 (KB2322785).
Syntax: long InboundOrderLine.PrintGoodsReceivedNote(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This public interface will print the goods received note
using the defaults or options as provided in the
iProcessingOptionSet.
In case iOrderNumber is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- InboundOrderLineArray
The goods received note will then be printed for the given
iOrderOrigin, iOrderNumber, iOrderLine and iOrderSequence.
In case option InboundOrderLineArray is set then the
selection range fields (From/To) of the iProcessingOptionSet
will be ignored. The goods received note will then be printed
for the inbound order lines in the array.
Opening/Closing of the report is handled by this function.
Pre:    By default the transaction handling is done within this
function, so there should be no pending logical transaction
before calling this function.
This is not the case when IncludeTransactionHandling
(option of iProcessingOptionSet) is set to False.
Post:   By default the transaction handling is done within this
function, so there is no need to commit or abort the process.
That is handled within the function.
When IncludeTransactionHandling (option of iProcessingOptionSet)
is set to False then the calling process has to handle
abort/commit of the process.
Input:  iOrderOrigin            Mandatory
iOrderNumber            Optional
iOrderLine              Optional
iOrderSequence          Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Print Goods Received Note (whinh3412m100) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
ReceiptDateFrom                 domain tcdate           Minimum Value
ReceiptDateTo                   domain tcdate           Maximum Value
OrderOriginFrom                 domain whinh.oorg       Minimum Value
OrderOriginTo                   domain whinh.oorg       Maximum Value
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderSetFrom                    domain tcwset           Minimum Value
OrderSetTo                      domain tcwset           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
ReceiptFrom                     domain whinh.shpm       Minimum Value
ReceiptTo                       domain whinh.shpm       Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
ShipFromBusinessPartnerFrom     domain tccom.bpid       Minimum Value
ShipFromBusinessPartnerTo       domain tccom.bpid       Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
InOwnLanguage                   domain tcyesno          tcyesno.yes
AllOrders                       domain tcyesno          tcyesno.no
SortByOrderAndWarehouse         domain tcyesno          tcyesno.no
PrintLotsAndSerials             domain tcyesno          tcyesno.no
PrintHandlingUnits              domain tcyesno          tcyesno.no
PrintSpecification              domain tcyesno          tcyesno.no
PrintSpaceForNotes              domain tcyesno          tcyesno.no
PrintSubcontractingData         domain tcyesno          tcyesno.yes
PrintVariantOptionDescriptions  domain tcyesno          tcyesno.no
PrintStorageZone                domain tcyesno          tcyesno.no
NumberOfCopies                  domain tcsrno           0
ReprintAlreadyPrintedOrders     domain tcyesno          tcyesno.no
RePrintAllOpenLines             domain tcyesno          tcyesno.no
RePrintIncludeReceivedOrderLines domain tcyesno         tcyesno.no
IncludeTransactionHandling      boolean                 true
InboundOrderLineArray           domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
JSON Object InboundOrderLineArray has the following structure:
"InboundOrderLineArray": [
{
"OrderOrigin": 80,
"OrderNumber": "PUR000030",
"OrderLine": 10,
"OrderSequence": 0
},
{
"OrderOrigin": 50,
"OrderNumber": "JSC000012",
"OrderLine": 20,
"OrderSequence": 0
}
]
This structure can be created with the following code:
InboundOrderLineArray = Json.newArray()
InboundOrderLine = Json.newObject()
Json.setNumber(InboundOrderLine, "OrderOrigin", 80)
Json.setString(InboundOrderLine, "OrderNumber", "PUR000030")
Json.setNumber(InboundOrderLine, "OrderLine", 10)
Json.setNumber(InboundOrderLine, "OrderSequence", 1)
Json.add(InboundOrderLineArray, InboundOrderLine)
InboundOrderLine = Json.newObject()
Json.setNumber(InboundOrderLine, "OrderOrigin", 50)
Json.setString(InboundOrderLine, "OrderNumber", "JSC000012")
Json.setNumber(InboundOrderLine, "OrderLine", 10)
Json.setNumber(InboundOrderLine, "OrderSequence", 1)
Json.add(InboundOrderLineArray, InboundOrderLine)
ReportName only needs to filled for customized reports, otherwise
the report related to the SortOption is automatically used.
ReportName must start with an "r", e.g. "rwhinh341211101"
Output: oDataProcessed          - true:  Goods Received Note Printed.
false: Nothing Printed.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
