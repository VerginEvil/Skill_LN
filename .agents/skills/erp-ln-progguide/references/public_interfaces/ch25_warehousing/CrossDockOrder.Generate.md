# CrossDockOrder.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for CrossDockOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1312-1314

```baan
DLL:   whextinhapi
This function is available from 2026.10 (KB3694663).
Syntax: long CrossDockOrder.Generate(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  whloca           iStagingLocation,
boolean          iPrintReport,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will generate cross-dock orders
for the given item/warehouse/staging location using
the defaults or options as provided in the
iProcessingOptionSet.
Transaction management is handled within this function.
Input:  iItem                   Optional. If filled, overrides
ItemFrom/ItemTo in option set.
iWarehouse              Optional. If filled, overrides
WarehouseFrom/WarehouseTo in option set.
iStagingLocation        Optional. If filled, overrides
StagingLocationFrom/StagingLocationTo
in option set.
iPrintReport            Determines whether reports will be
printed.
iDevice                 Mandatory if iPrintReport is true.
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Cross-dock Orders (whinh6200m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
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
InboundOrderOriginFrom          domain whinh.oorg       Minimum Value
InboundOrderOriginTo            domain whinh.oorg       Maximum Value
InboundOrderFrom                domain tcorno           Minimum Value
InboundOrderTo                  domain tcorno           Maximum Value
InboundLineFrom                 domain tcpono           Minimum Value
InboundLineTo                   domain tcpono           Maximum Value
InboundSequenceFrom             domain tcpono           Minimum Value
InboundSequenceTo               domain tcpono           Maximum Value
InboundBomLineFrom              domain tcpono           Minimum Value
InboundBomLineTo                domain tcpono           Maximum Value
InboundPegLineFrom              domain tcpono           Minimum Value
InboundPegLineTo                domain tcpono           Maximum Value
OutboundOrderOriginFrom         domain whinh.oorg       Minimum Value
OutboundOrderOriginTo           domain whinh.oorg       Maximum Value
OutboundOrderFrom               domain tcorno           Minimum Value
OutboundOrderTo                 domain tcorno           Maximum Value
OutboundLineFrom                domain tcpono           Minimum Value
OutboundLineTo                  domain tcpono           Maximum Value
OutboundSequenceFrom            domain tcpono           Minimum Value
OutboundSequenceTo              domain tcpono           Maximum Value
OutboundBomLineFrom             domain tcpono           Minimum Value
OutboundBomLineTo               domain tcpono           Maximum Value
OutboundPegLineFrom             domain tcpono           Minimum Value
OutboundPegLineTo               domain tcpono           Maximum Value
PlannedReceiptDateFrom          domain tcdate           Minimum Value
PlannedReceiptDateTo            domain tcdate           Maximum Value
PlannedDeliveryDateFrom         domain tcdate           Minimum Value
PlannedDeliveryDateTo           domain tcdate           Maximum Value
CrossDockOrderFrom              domain tcorno           Minimum Value
CrossDockOrderTo                domain tcorno           Maximum Value
CrossDockStatusFrom             domain whinh.cdos       whinh.cdos.open
CrossDockStatusTo               domain whinh.cdos       whinh.cdos.in.process
UserPriorityFrom                domain whinh.uspr       Minimum Value
UserPriorityTo                  domain whinh.uspr       Maximum Value
GenerateOrders                  domain tcyesno          tcyesno.yes
GenerateLines                   domain tcyesno          tcyesno.yes
DeleteExistingOrders            domain tcyesno          tcyesno.no
DeleteExistingLines             domain tcyesno          tcyesno.no
ApproveLines                    domain tcyesno          tcyesno.no
IncludePlannedOrders            domain tcyesno          tcyesno.yes
RushOrdersOnly                  domain tcyesno          tcyesno.no
GenerationType                  domain whinh.cdog       whinh.cdog.always
Series                          domain tcseri           Empty String
MinTimeTolerance                domain tcwttm           0
MaxTimeTolerance                domain tcwttm           0
MinTimeToleranceUnit            domain tctope           tctope.hours
MaxTimeToleranceUnit            domain tctope           tctope.hours
PrintGenerated                  domain tcyesno          tcyesno.yes
PrintDeleted                    domain tcyesno          tcyesno.no
PrintErrors                     domain tcyesno          tcyesno.yes
ReportNameGeneratedOrders       domain tcmcs.str16      Empty String
ReportNameDeletedOrders         domain tcmcs.str16      Empty String
Report Names only need to be filled in for customized reports, otherwise
the standard reports are used automatically.
ReportName must start with an "r", e.g. "rwhinh620021000"
Output: oDataProcessed          - true:  Cross-dock orders generated.
false: Nothing processed.
oExceptionMessage       - The last message if any.
oExceptionID            - Exception ID for details.
Return: 0                       - OK
<> 0                    - Error.
```
