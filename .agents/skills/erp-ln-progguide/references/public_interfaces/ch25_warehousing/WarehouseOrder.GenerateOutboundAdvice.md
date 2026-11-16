# WarehouseOrder.GenerateOutboundAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1026-1028

```baan
DLL:   whextinhapi
This function is available from 2026.04 (KB3665487).
Syntax: long WarehouseOrder.GenerateOutboundAdvice(
domain  whinh.btno       iRunNumber,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
boolean          iDirectRelease,
boolean          iCrossDock,
domain  tcyesno          iAlternativeItems,
domain  tcyesno          iAdviceDespiteShortage,
domain  tcyesno          iRecalculateExcessAtt,
domain  tcyesno          iOverdeliveryAllowed,
boolean          iStartAutomaticProcess,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate outbound advice for specific order(s)
or order ranges as provided in the i.processing.option.set.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
this function.
Input:  iRunNumber      - Run Number (Optional)
iOrderOrigin    - Specific order (Optional)
iOrder
iDirectRelease  - Direct Release generated advice
iCrossDock              - Create cross dock order for
shortage (True/False)
iAlternativeItems       - Alternative items handling (Yes/No)
iAdviceDespiteShortage  - Advice despite shortage (Yes/No)
iRecalculateExcessAtt   - Recalculate excess ATT (Yes/No)
iOverdeliveryAllowed    - Overdelivery allowed (Yes/No)
iStartAutomaticProcess
iProcessingOptionSet Optional, if 0, the default options
are applied.
In case iOrderOrigin/iOrder are filled then the following
options of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- OrderArray
In case option OrderArray is set then the selection range
fields (From/To) of the iProcessingOptionSet will be ignored.
Outbound advice will then be generated for the orders in the
array.
Processing Options have a direct relationship with the form fields
on session Generate Outbound Advice (whinh4201m000) and are not explained
in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
OrderOriginFrom oorg.f  domain  whinh.oorg      Minimum value
OrderOriginTo   oorg.t  domain  whinh.oorg      Maximum value
OrderFrom       orno.f  domain  tcorno          Minimum value
OrderTo         orno.t  domain  tcorno          Maximum value
SetFrom         oset.f  domain  tcwset          Minimum value
SetTo           oset.t  domain  tcwset          Maximum value
OrderLineFrom   pono.f  domain  tcpono          Minimum value
OrderLineTo     pono.t  domain  tcpono          Maximum value
SequenceFrom    seqn.f  domain  tcpono          Minimum value
SequenceTo      seqn.t  domain  tcpono          Maximum value
ReferenceFrom   refs.f  domain  tcrefs          Minimum value
ReferenceTo     refs.t  domain  tcrefs          Maximum value
CustomerOrderFr corn.f  domain  tccorn          Minimum value
CustomerOrderTo corn.t  domain  tccorn          Maximum value
ItemFrom        item.f  domain  tcpono          Minimum value
ItemTo          item.t  domain  tcpono          Maximum value
AttrSetFrom     atse.f  domain  tcatse          Minimum value
AttrSetTo       atse.t  domain  tcatse          Maximum value
DelDateFrom     dldt.f  domain  tcdate          Minimum value
DelDateTo       dldt.t  domain  tcdate          UTC:Current date
ShipTypeFrom    stty.f  domain  tctyps          Minimum value
ShipTypeTo      stty.t  domain  tctyps          Maximum value
ShipCodeFrom    stco.f  domain  tccshp          Minimum value
ShipCodeTo      stco.t  domain  tccshp          Maximum value
ShipAddrFrom    shpt.f  domain  tccom.cadr      Minimum value
ShipAddrTo      shpt.t  domain  tccom.cadr      Maximum value
RouteFrom       crte.f  domain  tccrte          Minimum value
RouteTo         crte.t  domain  tccrte          Maximum value
CarrierFrom     carr.f  domain  tccfrw          Minimum value
CarrierTo       carr.t  domain  tccfrw          Maximum value
SiteFrom        site.f  domain  tcsite          Minimum value
SiteTo          site.t  domain  tcsite          Maximum value
WarehouseFrom   cwar.f  domain  tccwar          Minimum value
WarehouseTo     cwar.t  domain  tccwar          Maximum value
OrderGroupFrom  grid.f  domain  tcpdno          Minimum value
OrderGroupTo    grid.t  domain  tcpdno          Maximum value
JSON Object OrderArray has the following structure:
"OutboundOrderArray": [
{
"OrderOrigin": 1,
"OrderNumber": "SLS000001",
},
{
"OrderOrigin": 50,
"OrderNumber": "JSC000001",
}
]
This structure can be created with the following code:
OutboundOrderArray = Json.newArray()
OutboundOrder = Json.newObject()
Json.setNumber(OutboundOrder, "OrderOrigin", 1)
Json.setString(OutboundOrder, "OrderNumber", "SLS000001")
Json.add(OutboundOrderArray, OutboundOrder)
OutboundOrder = Json.newObject()
Json.setNumber(OutboundOrder, "OrderOrigin", 50)
Json.setString(OutboundOrder, "OrderNumber", "JSC000001")
Json.add(OutboundOrderArray, OutboundOrder)
Output: oDataProcessed  - true:  Data Processed.
false: Nothing Selected.
Return: 0: OK, <> 0: Error
```
