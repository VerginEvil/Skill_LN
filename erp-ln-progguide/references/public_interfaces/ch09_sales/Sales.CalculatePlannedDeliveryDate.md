# Sales.CalculatePlannedDeliveryDate

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 273-275

```baan
DLL:   tdextslsapi
This function is available from 2023.11 (KB2310725).
Syntax: long Sales.CalculatePlannedDeliveryDate(
domain  tcdate           iPlannedReceiptDate,
domain  tcdate           iOrderDate,
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tccwoc           iSalesOffice,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tccwar           iWarehouse,
domain  tccwoc           iWorkcenter,
domain  tccwar           iShipToWarehouse,
domain  tccom.cadr       iShipToAddress,
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcqsl1           iOrderQuantity,
domain  tcconv           iOrderQuantityConvFactorToInvUnit,
domain  tccrte           iRoute,
domain  tcmcs.serv       iServiceLevel,
domain  tccdec           iTermsOfDelivery,
domain  tcptpa           iPointOfTitlePassage,
domain  tccfrw           iPreferredCarrier,
domain  tccfrw           iCarrier,
ref     domain  tcdate           oPlannedDeliveryDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the sales planned delivery date based
on the planned receipt date (date at customer's site).
For the calculation, the planned receipt date is reduced with the
transportation time between the address of the sales office or
supplier warehouse and the ship-to address.
If the item is filled, applicable if a calculation for a sales
order line is done, a check is done if a pattern can be found in
Terms and conditions. If so the planned delivery date is updated
by the first preceeding delivery moment of the pattern.
Finally, the planned delivery date is shifted backward to the
availability of the warehouse address calendar (calculated planned
delivery date must be a workable date in the warehouse calendar).
Pre:    Not applicable
Post:   Not applicable
Input:  iPlannedReceiptDate             - Planned Receipt Date (mandatory)
iOrderDate                      - Order Date
iItem                           - Item
iSite                           - Site
iSalesOffice                    - Sales Office
iSoldToBusinessPartner          - Sold-to Business Partner
iShipToBusinessPartner          - Ship-to Business Partner
iWarehouse                      - Warehouse
iWorkcenter                     - Workcenter
iShipToWarehouse                - Ship-to Warehouse
iShipToAddress                  - Ship-to Address
iSalesOrder                     - Sales Order
Needed for direct delivery
iSalesOrderLine                 - Sales Order Line
Mandatory if Sales Order is filled.
Needed for direct delivery.
iSalesOrderLineSequence         - Sales Order Line Sequence
iOrderQuantity                  - Order Quantity
iOrderQuantityConvFactorToInvUnit
- Order Quantity Conversion Factor
to Inventory Unit (mandatory).
This field must be filled with
1.0 if no quantity is given.
iRoute                          - Route
iServiceLevel                   - Service Level
iTermsOfDelivery                - Terms of Delivery
iPointOfTitlePassage            - Point of Title Passage
iPreferredCarrier               - Preferred Carrier
iCarrier                        - Carrier
Output: oPlannedDeliveryDate            - The calculated Planned Delivery Date.
oExceptionMessage               - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                    - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> No error
<> 0    -> Error occurred
```
