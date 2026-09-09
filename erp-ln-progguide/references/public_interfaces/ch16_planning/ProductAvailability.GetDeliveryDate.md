# ProductAvailability.GetDeliveryDate

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ProductAvailability
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 578-581

```baan
DLL:   cpextrmpapi
This function is available from 2024.02 (KB2300215).
Syntax: long ProductAvailability.GetDeliveryDate(
domain  cpcom.plnc       iPlanningScenario,
domain  tcitem           iProduct,
domain  tccpva           iProductVariant,
domain  tcuef.effn       iEffectivityUnit,
domain  cpcom.quan       iRequiredQuantity,
domain  tccuni           iRequiredQuantityUnit,
domain  cpcom.date       iRequiredDate,
domain  tcncmp           iCompany,
domain  tccwar           iWarehouse,
domain  tcmcs.chan       iChannel,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
domain  tckotr           iOrderTransactionType,
domain  tcpono           iOrderLinePosition,
domain  tcpono           iOrderLineSequence,
boolean          iIncludeComponentAvailability,
boolean          iIncludeCapacityAvailability,
boolean          iAllowFamilyItems,
domain  tcguid           iSpecification,
domain  tccom.bpid       iOwner,
domain  tccom.bpid       iDemandPegSoldToBusinessPartner,
domain  tccom.bpid       iDemandPegShipToBusinessPartner,
domain  tcalbt           iDemandPegAllocationToBusinessObjectType,
domain  tcboid           iDemandPegBusinessObjectId,
domain  tcborf           iDemandPegBusinessObjectReference,
domain  tcrefa           iDemandPegReference mb,
domain  tcyesno          iDemandPegUseUnallocatedInventory,
domain  tccprj           iProjectPegProject,
domain  tccspa           iProjectPegElement,
domain  tccact           iProjectPegActivity,
ref     domain  cpcom.quan       oQuantity,
ref     domain  cpcom.date       oDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to get a delivery date
for the Required Quantity of the specified Product, in the
specified Warehouse.
Setting the Required Date to a date in the future will
cause the logic to check if the Required Quantity is available
at that date. If the quantity becomes available later, the
Date (output) will indicate that available date.
Order details input parameters (iOrder...) are required when
the changes to an order line quantity need to be considered.
In that case Planned Inventory Transactions related to the
specified source order need to be rebuilt in order to get to
a correct available date.
The Delivery Date calculation requires specification information
in order to be able to segregate availability for different
demand origins.
Two ways of providing a specification are possible, which cannot
be mixed.
- One option is to provide the Demand Peg parameters
(iDemandPeg...). The demand peg parameter set is not used when
iDemandPegSoldToBusinessPartner and
iDemandPegShipToBusinessPartner and
iDemandPegReferenceleft are given empty and
iDemandPegAllocationToBusinessObjectType is Not Applicable.
- The other option, when Demand Peg parameters are not used,
is to provide a value for the iSpecification parameter
which should refer to an existing specification in
Demand Pegging Relationships (tcibd4520m000).
To use this specification for a customer owned Product,
the iOwner can be specified as well.
Project pegging parameters can be used to focus on
availability of the product for a specific project peg.
Pre:    N.A.
Post:   N.A.
Input:  iPlanningScenario       - Planning Scenario used for the
the calculation (Mandatory).
iProduct                - Product to be delivered (Mandatory).
iProductVariant         - Product Variant to be delivered.
iEffectivityUnit        - Effectivity Unit.
iRequiredQuantity       - Required Quantity of Product
(Mandatory).
iRequiredQuantityUnit   - Required Quantity Unit (Mandatory).
iRequiredDate           - Date on which Product is required
(Mandatory).
iCompany                - Company where Product needs to
be available (Mandatory).
iWarehouse              - The Warehouse the Product needs
to be available in (Mandatory).
iChannel                - Channel to sell or distribute the
specified Product. When provided,
the constraints imposed by
the given channel are included in
the calculation.
iOrderType              - Order Type.
iOrderNumber            - Order Number.
iOrderTransactionType   - Order Transaction Type.
iOrderLinePosition      - Order Line Position.
iOrderLineSequence      - Order Line Sequence.
iIncludeComponentAvailability
- Include the constraints imposed by
availability of critical components
in the calculation.
iIncludeCapacityAvailability
- Include the constraints imposed by
availability of critical resources /
work centers in the calculation.
iAllowFamilyItems       - It is allowed to use family items
in the calculation of the available
date.
iSpecification          - Specification as present in session
Demand Pegging Relationships
(tcibd4520m000).
iOwner                  - Business Partner owning the Product.
Used when Product is customer owned.
iDemandPegSoldToBusinessPartner
- Sold To Business Partner.
iDemandPegShipToBusinessPartner
- Ship To Business Partner.
iDemandPegAllocationToBusinessObjectType
- Allocation To Business Object Type.
iDemandPegBusinessObjectId
- Business Object ID.
iDemandPegBusinessObjectReference
- Business Object Reference.
iDemandPegReference     - Demand Peg Reference.
iDemandPegUseUnallocatedInventory
- Include available Unallocated
Inventory in the calculation.
iProjectPegProject      - Project Peg Project.
iProjectPegElement      - Project Peg Element.
iProjectPegActivity     - Project Peg Activity.
Output: oQuantity               - Quantity of available Product
(expressed in iRequiredQuantityUnit).
This value may differ from the
input iRequiredQuantity because of
rounding and/or conversions.
oDate                   - Date on which the Quantity will
be available.
oExceptionMessage       - The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function completed succesfully.
<> 0                    - A fatal problem occurred.
```
