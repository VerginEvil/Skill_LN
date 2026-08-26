# ProductionOrders.ProcessMaterialShortages

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 782-783

```baan
DLL:   tiextsfcapi
This function is available from     2024.12 (KB3530049  ).
Syntax: long ProductionOrders.ProcessMaterialShortages(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iMaterialPosition,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface processes Material shortages for a given
range of Production Orders. This is similar to the form command
"Process Shortages Directly" of session Material to Issue for
Production Orders (ticst0101m100).
Transaction management is handled by this Public Interface.
Input:
iSite                   Site. Mandatory if the Sites concept is active.
When selecting a range of production Orders,
only orders in the given site are considered.
Mandatory if iProductionOrder is not empty.
iProductionOrder        Production Order.
iMaterialPosition       Material Position.
iProcessingOptionSet    A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create(). If 0, then
defaults are applied.
NAME                  TYPE                DEFAULT
ProductionOrderFrom     domain  tcpdno  iProductionOrder
ProductionOrderTo       domain  tcpdno  ProductionOrderFrom when set,
Otherwise max domain value
MaterialPositionFrom    domain  cpono   iMaterialPositionFrom
MaterialPositionTo      domain  tcpono  MaterialPositionFrom when set,
Otherwise max domain value
ProjectFrom             domain  ccprj   ""
ProjectTo               domain  tccprj  ProjectFrom when set,
Otherwise max domain value
WarehouseFrom           domain  tccwar  ""
WarehouseTo             domain  tccwar  WarehouseFrom when set,
Otherwise max domain value
ItemFrom                domain  tcitem  ""
ItemTo                  domain  tcitem  ItemFrom when set,
Otherwise max domain value
AllocationDate          domain  tcutcs  Current date
BackflushMaterialsOnly  domain  tcyesno tcyesno.no
IssueDate               domain  tcutcs  Current date
WayOfOperationSelection domain  tisfc.wybf
tisfc.wybf.all
Operation               domain  tcopno  0
GroupSelection          domain  tcyesno tcyesno.no
OrderGroupFrom          domain  tcpdno  ""
OrderGroupTo            domain  tcpdno  OrderGroupFrom when set,
Otherwise max domain value
IssueSequence           domain  tisfc.issq
tisfc.issq.pdno›¼                                                      
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Sucessfull
<> 0                    Otherwise.
```
