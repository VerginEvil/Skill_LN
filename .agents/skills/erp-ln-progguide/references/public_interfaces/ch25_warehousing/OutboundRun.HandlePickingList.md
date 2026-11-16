# OutboundRun.HandlePickingList

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundRun
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1205-1208

```baan
DLL:   whextinhapi
This function is available from 2024.03 (KB2325172).
Syntax: long OutboundRun.HandlePickingList(
domain  whinh.btno       iOutboundRun,
domain  whinh.spla       iAction,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will handle the picking list for the
iOutboundRun and iAction using the defaults or options as
provided in the iProcessingOptionSet.
The opening/closing of the related report is handled within
this public interface.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iOutboundRun            Mandatory
iAction                 Mandatory
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Picking List (whinh4415m000) and are not explained
in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Extended:
Since 2025.09 release the following options have been added to the
iProcessingOptionSet:
PrintPickingList        - relevant for iAction = Generate.
Determines whether the report should
be printed or not after Picking List
was generated.
CombinePickingMission   - yes: outbound advices for the same
Run and Warehouse will be combined in
one picking mission;
no: a new picking mission is generated
for each Picking List.
CombineWithMission      - specifies which picking mission the
Picking List should be added to.
Mandatory if CombinePickingMission is
Yes.
Explanation about setting of defaults:
Run Value:      Value of the field stored in the Outbound Run is taken
as default value.
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
whinh403 Value: If SortOrderBy field is filled then value is retrieved
from table Sort Options for Picking List (whinh403),
otherwise the default value is tcyesno.no.
NAME                            TYPE                    DEFAULT
AllAdviceLines                  domain tcyesno          tcyesno.no
ExcludePickedAdviceLines        domain tcyesno          tcyesno.no
OrderOriginFrom                 domain whinh.oorg       Run Value
OrderOriginTo                   domain whinh.oorg       Run Value
OrderGroupFrom                  domain tcpdno           Run Value
OrderGroupTo                    domain tcpdno           Run Value
OrderNumberFrom                 domain tcorno           Run Value
OrderNumberTo                   domain tcorno           Run Value
OrderSetFrom                    domain tcwset           Run Value
OrderSetTo                      domain tcwset           Run Value
OrderLineFrom                   domain tcpono           Run Value
OrderLineTo                     domain tcpono           Run Value
OrderLineSequenceFrom           domain tcpono           Minimum Value
OrderLineSequenceTo             domain tcpono           Maximum Value
AdviceLineFrom                  domain tcpono           Minimum Value
AdviceLineTo                    domain tcpono           Maximum Value
SiteFrom                        domain tcsite           Run Value
SiteTo                          domain tcsite           Run Value
WarehouseFrom                   domain tccwar           Run Value
WarehouseTo                     domain tccwar           Run Value
ZoneFrom                        domain whwmd.zone       Minimum Value
ZoneTo                          domain whwmd.zone       Maximum Value
LocationFrom                    domain whloca           Minimum Value
LocationTo                      domain whloca           Maximum Value
RowFrom                         domain whwmd.strt       Minimum Value
RowTo                           domain whwmd.strt       Maximum Value
LevelFrom                       domain whwmd.coln       Minimum Value
LevelTo                         domain whwmd.coln       Maximum Value
BinFrom                         domain whwmd.rack       Minimum Value
BinTo                           domain whwmd.rack       Maximum Value
PlannedDeliveryDateFrom         domain tcdate           Run Value
PlannedDeliveryDateTo           domain tcdate           Run Value
ShipmentReferenceFrom           domain tcrefs           Minimum Value
ShipmentReferenceTo             domain tcrefs           Maximum Value
CustomerOrderFrom               domain tccorn           Minimum Value
CustomerOrderTo                 domain tccorn           Maximum Value
ItemFrom                        domain tcitem           Run Value
ItemTo                          domain tcitem           Run Value
LoadFrom                        domain whinh.load       Minimum Value
LoadTo                          domain whinh.load       Maximum Value
ShipmentFrom                    domain whinh.shpm       Minimum Value
ShipmentTo                      domain whinh.shpm       Maximum Value
HandlingUnitFrom                domain whhuid           Minimum Value
HandlingUnitTo                  domain whhuid           Maximum Value
SortOrderBy1                    domain tcfdnm.c         Minimum Value
SortDescend1                    domain tcyesno          whinh403 Value
SortNewMission1                 domain tcyesno          whinh403 Value
SortOrderBy2                    domain tcfdnm.c         Minimum Value
SortDescend2                    domain tcyesno          whinh403 Value
SortNewMission2                 domain tcyesno          whinh403 Value
SortOrderBy3                    domain tcfdnm.c         Minimum Value
SortDescend3                    domain tcyesno          whinh403 Value
SortNewMission3                 domain tcyesno          whinh403 Value
SortOrderBy4                    domain tcfdnm.c         Minimum Value
SortDescend4,                   domain tcyesno          whinh403 Value
SortNewMission4                 domain tcyesno          whinh403 Value
SortOrderBy5                    domain tcfdnm.c         Minimum Value
SortDescend5                    domain tcyesno          whinh403 Value
SortNewMission5                 domain tcyesno          whinh403 Value
SortOrderBy6                    domain tcfdnm.c         Minimum Value
SortDescend6                    domain tcyesno          whinh403 Value
SortNewMission6                 domain tcyesno          whinh403 Value
SortOrderBy7                    domain tcfdnm.c         Minimum Value
SortDescend7                    domain tcyesno          whinh403 Value
SortNewMission7                 domain tcyesno          whinh403 Value
SortOrderBy8                    domain tcfdnm.c         Minimum Value
SortDescend8                    domain tcyesno          whinh403 Value
SortNewMission8                 domain tcyesno          whinh403 Value
SortOrderBy9                    domain tcfdnm.c         Minimum Value
SortDescend9                    domain tcyesno          whinh403 Value
SortNewMission9                 domain tcyesno          whinh403 Value
SortOrderBy10                   domain tcfdnm.c         Minimum Value
SortDescend10                   domain tcyesno          whinh403 Value
SortNewMission10                domain tcyesno          whinh403 Value
PrintPickingList                domain tcyesno          tcyesno.yes
PrintNewPagePerOrder            domain tcyesno          tcyesno.no
PrintProject                    domain tcyesno          tcyesno.no
PrintLots                       domain tcyesno          tcyesno.no
PrintActualInventoryQuantity    domain tcyesno          tcyesno.no
PrintSerials                    domain tcyesno          tcyesno.no
PrintOwnership                  domain tcyesno          tcyesno.no
PrintItemStorageConditions      domain tcyesno          tcyesno.no
PrintLocationStorageConditions  domain tcyesno          tcyesno.no
SortOption                      domain whsb.loolsc      whsb.loolsc.location
CombinePickingMission           domain tcyesno          tcyesno.no
CombineWithMission              domain whinh.picm       Minimum Value
ReprintPickingMissionFrom       domain whinh.picm       Minimum Value
ReprintPickingMissionTo         domain whinh.picm       Maximum Value
ReprintPickingSequenceFrom      domain whinh.lino       Minimum Value
ReprintPickingSequenceTo        domain whinh.lino       Maximum Value
NumberOfCopies                  domain tcsrno           0
PrintRunAsBarcode               domain tcyesno          tcyesno.no
BarcodeType                     domain tcbctype         tcbctype.not.appl
BarcodeHeight                   domain tcmcs.byte1      Minimum Value
ReportName                      domain tcmcs.str16      Empty String
ReportName only needs to filled for customized reports, otherwise
the report related to the SortOption is automatically used.
ReportName must start with an "r", e.g. "rwhinh441511001"
Output: oDataProcessed          - true:  Picking List Generated/Printed.
false: Nothing Generated/Printed.
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
