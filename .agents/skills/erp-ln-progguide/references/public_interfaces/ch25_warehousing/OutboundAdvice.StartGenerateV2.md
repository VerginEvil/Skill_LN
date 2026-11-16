# OutboundAdvice.StartGenerateV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1200-1202

```baan
DLL:   whextinhapi
This function is available from 2025.12 (KB3612207).
Syntax: long OutboundAdvice.StartGenerateV2(
long             iStartMode,
boolean          iIgnoreSelectionFields,
domain  whinh.oorg       iFromOrderOrigin,
domain  tcorno           iFromOrderNumber,
domain  tcwset           iFromOrderSet,
domain  tcpono           iFromOrderLine,
domain  whinh.oorg       iToOrderOrigin,
domain  tcorno           iToOrderNumber,
domain  tcwset           iToOrderSet,
domain  tcpono           iToOrderLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Generate Outbound Advice
(whinh4201m000). Depending on the main table of the calling
session, Non-Consecutive Record Selection (NCRS) is used.
When the main table is:
Warehousing Orders      (whinh200) or
Outbound Order Lines    (whinh220) or
Planned Loads/Shipments (whinh480) then
the range selections will be imported based on the selected
records in the parent session and the selection related fields
will be ignored.
Input:  iStartMode
Not Used.
iIgnoreSelectionFields
If true, (empty) From/To selection fields will not be
filled in the session.
iFromOrderOrigin
From Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderNumber
From Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderSet
From Order Set selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iFromOrderLine
From Order Line selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderOrigin
To Order Origin selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderNumber
To Order Number selection field is filled with this
value. (when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderSet
To Order Set selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iToOrderLine
To Order Line selection field is filled with this value.
(when iIgnoreSelectionFields is false and NCRS
is not applicable)
iProcessingOptionSet
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a call to
function ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Outbound Advice (whinh4201m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
OrderOriginFrom                 domain whinh.oorg       Minimum Value
OrderOriginTo                   domain whinh.oorg       Maximum Value
OrderGroupFrom                  domain tcpdno           Minimum Value
OrderGrouprTo                   domain tcpdno           Maximum Value
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderSetFrom                    domain tcwset           Minimum Value
OrderSetTo                      domain tcwset           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
OrderSequenceFrom               domain tcpono           Minimum Value
OrderSequenceTo                 domain tcpono           Maximum Value
ShipmentReferenceFrom           domain tcrefs           Minimum Value
ShipmentReferenceTo             domain tcrefs           Maximum Value
CustomerOrderFrom               domain tccorn           Minimum Value
CustomerOrderTo                 domain tccorn           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
AttributeSetFrom                domain tcatse           Minimum Value
AttributeSetTo                  domain tcatse           Maximum Value
IncludeReturnOrders             domain tcyesno          tcyesno.no
IncludeReturnRejects            domain tcyesno          tcyesno.no
RushOrdersOnly                  domain tcyesno          tcyesno.no
CommittedInventoryOnly          domain tcyesno          tcyesno.no
UseLoadPlan                     domain tcyesno          tcyesno.no
LoadFrom                        domain whinh.load       Minimum Value
LoadTo                          domain whinh.load       Maximum Value
ShipmentFrom                    domain whinh.shpm       Minimum Value
ShipmentTo                      domain whinh.shpm       Maximum Value
PrintErrors                     domain tcyesno          tcyesno.yes
UseProjectedShipments           domain tcyesno          tcyesno.no
ProjectedLoadFrom               domain whinh.load       Minimum Value
ProjectedLoadTo                 domain whinh.load       Maximum Value
ProjectedShipmentFrom           domain whinh.shpm       Minimum Value
ProjectedShipmentTo             domain whinh.shpm       Maximum Value
DMSItems                        domain whinh.dmsr       whinh.dmsr.excluded
ApplyDMS                        domain tcyesno          tcyesno.no
UseCluster                      domain tcyesno          tcyesno.no
ClusterCompany                  domain tcncmp           Current company
ClusterFrom                     domain tcorno           Minimum Value
ClusterTo                       domain tcorno           Maximum Value
DeliveryDateFrom                domain tcdate           Minimum Value
DeliveryDateTo                  domain tcdate           Current Date/Time
SiteFrom                        domain tcsite           Minimum Value
SiteTo                          domain tcsite           Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
ShipToTypeFrom                  domain tctyps           Minimum Value
ShipToTypeTo                    domain tctyps           Maximum Value
ShipToCodeFrom                  domain tcshpm           Minimum Value
ShipToCodeTo                    domain tcshpm           Maximum Value
ShipToAddressFrom               domain tccom.cadr       Minimum Value
ShipToAddressTo                 domain tccom.cadr       Maximum Value
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
CarrierFrom                     domain tccfrw           Minimum Value
CarrierTo                       domain tccfrw           Maximum Value
CreateCrossDockOrders           domain tcyesno          tcyesno.yes
HandleAlternativeItems          domain tcyesno          tcyesno.no
CreateAdviceDespiteShortage     domain tcyesno          tcyesno.no
RecalculateExcessAndATT         domain tcyesno          tcyesno.no
OverdeliveryAllowed             domain tcyesno          tcyesno.no
AdviceLog                       domain whinh.oalg       whinh.oalg.no
PrintAdvice                     domain tcyesno          tcyesno.yes
PrintShortage                   domain tcyesno          tcyesno.yes
PrintProjectCostPegTransfers    domain tcyesno          tcyesno.no
PrintOwnership                  domain tcyesno          tcyesno.no
PrintItemStorageConditions      domain tcyesno          tcyesno.no
PrintLocationStorageConditions  domain tcyesno          tcyesno.no
PrintToPredefinedDevice         domain tcyesno          tcyesno.yes
PrintDimensionsOnAppendix       domain tcyesno          tcyesno.no
SortByOption                    domain whsb.oslsosc     whsb.oslsosc.order
LabelPrinting                   domain whinh.plbs       whinh.plbs.order.settings
LabelPrintedBy                  domain whwmd.lbpb       whwmd.lbpb.internal
LabelLayout                     domain tclabl           empty string
LabelCopies                     domain tcmcs.long       0
HandlingUnitsOnly               domain tcyesno          tcyesno.no
LabelPrintingMethod             domain whinh.prmt       whinh.prmt.not.appl
Output: oExceptionMessage       - The last message if any message is
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
