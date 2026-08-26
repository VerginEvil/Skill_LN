# PurchaseOrderLine.Generate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 458-461

```baan
DLL:   tdextpurapi
This function is available from     2026.07 (KB3669194  ).
Syntax: long PurchaseOrderLine.Generate(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
long             iProcessingOptionSet,
ref     domain  tcorno           oPurchaseOrder,
ref     domain  tcpono           oPurchaseOrderLine,
ref     domain  tcpono           oPurchaseOrderLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function creates a purchase order line based on the data provided
in the processing option set; if the corresponding purchase order header
does not yet exist, it is created first.
When the input arguments iPurchaseOrder and/or iPurchaseOrderLine are
provided, the function attempts to create a new purchase order line
(sequence) for the specified purchase order (line). The newly created
purchase order and purchase order line, returned via the output arguments
oPurchaseOrder and oPurchaseOrderLine, can also be used as input arguments
to create subsequent purchase order lines, where possible.
This function does not start the execution of automatic order steps.
A separate Public Interface can be used to start automatic order steps
if necessary: 'PurchaseOrder.StartAutomaticProcessing'.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder                        - Purchase Order (Optional)
iPurchaseOrderLine                            - Purchase Order Line (Optional)
iProcessingOptionSet                          - Processing Option Set (Mandatory).
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
The processing option "OriginOfPurchaseOrder" can have one of the following
allowed
values: 'Manual', 'Project' or 'External'.
Discount              -related options can be defined in a dedicated sub processing option set
named "SubProcessingOptionSetDiscounts", which must be included in the main
processing option set.
Any options that are not provided as processing options are defaulted, where
possible,
in accordance with the standard purchase order session logic.
Processing options that are specified while a required Implemented Software
Component
is not available are ignored.
Supported Processing Options and their defaults:
NAME                                    TYPE                    DEFAULT
OriginOfPurchaseOrder                   domain  tdpur.corg      tdpur.corg.manual
PurchaseOrderSeries                     domain  tcseri          Determined by LN
Settings
PurchaseOffice                          domain  tccwoc          Determined by LN
Settings
PurchaseOrderType                       domain  tccotp          Determined by LN
Settings
OrderCurrency                           domain  tcccur          Determined by LN
Settings
Buyer                                   domain  tcemno          Determined by LN
Settings
Planner                                 domain  tcemno          Determined by LN
Settings
ReferenceA                              domain  tcrefa          ""
ReferenceB                              domain  tcrefb          ""
BuyFromBusinessPartner                  domain  tccom.bpid      Mandatory
ShipFromBusinessPartner                 domain  tccom.bpid      Determined by LN
Settings
ShipFromAddress                         domain  tccom.cadr      Determined by LN
Settings
Item                                    domain  tcitem          Mandatory
EffectivityUnit                         domain  tcuef.effn      0
ManufacturerPartNumber                  domain  tcmpnr          ""
Manufacturer                            domain  tcmcs.cmnf      ""
ItemRevision                            domain  tcedm.revi      ""
ProductVariant                          domain  tdobid          0
AcquisitionMethod                       domain  tcacqm          tcacqm.buying
Subcontracting                          domain  tcyesno         tcyesno.no
Site                                    domain  tcsite          Determined by LN
Settings
Warehouse                               domain  tccwar          Determined by LN
Settings
ReceiptAddress                          domain  tccom.cadr      Determined by LN
Settings
OrderedQuantity                         domain  tcqrd1          0.0
PurchaseUnit                            domain  tccuni          Determined by LN
Settings
PurchaseUnitConversionFactor            domain  tcconv          Determined by LN
Settings
OrderDate                               domain  tcdate          Current Date/Time
PlannedReceiptDate                      domain  tcdate          Current Date/Time
SetLotInformation                       boolean                 false
LotSelection                            domain  tclsel          tclsel.any
Lot                                     domain  tcclot          ""
Project                                 domain  tccprj          "", mandatory for
Origin 'Project'
ProjectElement                          domain  tccspa          "",
ProjectActivity                         domain  tccact          "",
ProjectExtension                        domain  tccstl          "",
ProjectCostComponent                    domain  tccpcp          "",
SetPrice                                boolean                 false
Price                                   domain  tcpric          Determined in
Pricing
PurchasePriceUnit                       domain  tccuni          Determined in
Pricing
PriceUnitConversionFactor               domain  tcconv          Determined in
Pricing
SetPriceOrigin                          boolean                 false
PriceOrigin                             domain  tdgen.porg      Determined in
Pricing
CopyMaterialPriceData                   boolean                 false
SubProcessingOptionSetDiscounts         long                    0
Supported Sub Processing Options and their defaults:
NAME                            TYPE                    DEFAULT
DiscountPercentage1..11         domain  tcdisc          Determined in
Pricing
Discount Percentages can be
set within the range of
DiscountPercentage1 through
DiscountPercentage11.
DiscountAmount1..11             domain  tddiam          Determined in
Pricing
Discount Amounts can be
set within the range of
DiscountAmount1 through
DiscountAmount11.
SetDiscountOrigin               boolean                 false
DiscountOrigin1..11             domain  tdgen.dorg      Determined in
Pricing
Discount Origins can be
set within the range of
DiscountOrigin1 through
DiscountOrigin11.
OrderAmount                             domain  tcamnt          Determined in
Pricing
Contract                                domain  tccono          Determined in
Pricing
ContractLine                            domain  tcpono          Determined in
Pricing
ContractLinePurchaseOffice              domain  tccwoc          Determined in
Pricing
ContractLineSequence                    domain  tcpono          Determined in
Pricing
CarrierLSP                              domain  tccfrw          Determined by LN
Settings
PurchaseType                            domain  tcpsty          Determined by LN
Settings
Output: oPurchaseOrder                                - The generated purchase order
oPurchaseOrderLine                                    - The generated purchase order line
oPurchaseOrderLineSequence                            - The generated purchase order line
sequence
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information
Return: 0                                             - No error
<> 0                                                  - Error occurred
```
