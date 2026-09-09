# WarehouseReceipt.PrintReceipts

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 982-984

```baan
DLL:   whextinhapi
This function is available from 2024.06 (KB2327745).
Syntax: long WarehouseReceipt.PrintReceipts(
domain  whinh.shpm       iReceipt,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the receipt(s) for
the iReceipt using the defaults or options as
provided in the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Pre:    N.a.
Post:   N.a.
Input:  iReceipt                Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iReceipt is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- ReceiptArray
The Receipt will then be printed for the given iReceipt.
In case option ReceiptArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
The Receipt will then be printed for the receipts in the array.
Processing Options have a direct relationship with the form fields
on session Print Receipts (whinh3412m000) and are not explained in
further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
ReceiptFrom             domain whinh.shpm       Minimum Value
ReceiptTo               domain whinh.shpm       Maximum Value
ReceiptLineFrom         domain tcpono           Minimum Value
ReceiptLineTo           domain tcpono           Maximum Value
ReceiptDateFrom         domain tcdate           Minimum Value
ReceiptDateTo           domain tcdate           Current Date/Time
ShipFromTypeFrom        domain tctyps           Minimum Value
ShipFromTypeTo          domain tctyps           Maximum Value
ShipFromCodeFrom        domain tccshp           Minimum Value
ShipFromCodeTo          domain tccshp           Maximum Value
ShipToTypeFrom          domain tctyps           Minimum Value
ShipToTypeTo            domain tctyps           Maximum Value
ShipToCodeFrom          domain tccshp           Minimum Value
ShipToCodeTo            domain tccshp           Maximum Value
EffectivityUnitFrom     domain tcuef.effn       Minimum Value
EffectivityUnitTo       domain tcuef.effn       Maximum Value
OwnerFrom               domain tccom.bpid       Minimum Value
OwnerTo                 domain tccom.bpid       Maximum Value
ItemFrom                domain tcitem           Minimum Value
ItemTo                  domain tcitem           Maximum Value
OrderOriginFrom         domain whinh.oorg       Minimum Value
OrderOriginTo           domain whinh.oorg       Maximum Value
OrderNumberFrom         domain tcorno           Minimum Value
OrderNumberTo           domain tcorno           Maximum Value
OrderSetFrom            domain tcwset           Minimum Value
OrderSetTo              domain tcwset           Maximum Value
OrderLineFrom           domain tcpono           Minimum Value
OrderLineTo             domain tcpono           Maximum Value
PrintReceiptLines       domain whinh.prec       whinh.prec.all
PrintComponents         domain tcyesno          tcyesno.yes
PrintStockPointDetails  domain tcyesno          tcyesno.yes
PrintOwnership          domain tcyesno          tcyesno.no
PrintPegDistribution    domain tcyesno          tcyesno.no
PrintLandedCosts        domain tcyesno          tcyesno.no
PrintReceiptLineText    domain tcyesno          tcyesno.yes
PrintInspectionText     domain tcyesno          tcyesno.no
ReportNumber            domain tcmcs.long       1
ReceiptArray            domain ttjson           0
ReportName              domain tcmcs.str16      Empty String
Possible values of ReportNumber are:
1 - Receipts
2 - Receipt Lines by Order
3 - Receipt Lines by Item
4 - Receipt Lines by Receipt Number
5 - Receipt Lines by Business Partner
JSON Object ReceiptArray has the following structure:
"ReceiptArray": [
{
"Receipt": "REC000252"
},
{
"Receipt": "REC000119"
}
]
This structure can be created with the following code:
ReceiptArray = Json.newArray()
Receipt = Json.newObject()
Json.setString(Receipt, "Receipt", "REC000252")
Json.add(ReceipttArray, Receipt)
Receipt = Json.newObject()
Json.setString(Receipt, "Receipt", "REC000119")
Json.add(ReceiptArray, Receipt)
ReportName only needs to filled for customized reports,
otherwise the standard report is used based on the ReportNumber.
ReportName must start with an "r", e.g. "rwhinh341211001"
Output: oDataProcessed          - true:  Data Printed.
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
