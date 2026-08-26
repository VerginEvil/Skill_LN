# Sales.CalculatePlannedReceiptDate

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 273-274

```baan
DLL:   tdextslsapi
This function is available from     2023.07 (KB2297270  ).
Syntax: long Sales.CalculatePlannedReceiptDate(
domain  tcdate           iPlannedDeliveryDate,
domain  tcdate           iOrderDate,
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tccwar           iWarehouse,
domain  tccwoc           iWorkcenter,
domain  tccwoc           iSalesOffice,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
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
ref     domain  tcdate           oPlannedReceiptDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the Sales Planned Receipt Date.
The planned receipt date is calculated based on a source address
and ship to address.
This source address is determined within this function based on
the given input.
The source address is determined based on
warehouse (or site) address, work center (or site) address, or
sales office address.
If no source address found, in case of direct delivery,
the source address is based on the
ship                      -from business partner address of the linked purchase order
or the item supplier information if no purchase order has been
generated yet.
For the given Sales Order Number with Line and Sequence the
linked Purchase order is determined.
Pre:    None
Post:   None
Input:  iPlannedDeliveryDate                  - Planned Delivery Date. Mandatory.
iOrderDate                                    - Order Date
iItem                                         - Item
iSite                                         - Site
iWarehouse                                    - Warehouse
iWorkcenter                                   - Workcenter
iSalesOffice                                  - Sales Office
iSoldToBusiness.partner                       - Sold-to Business Partner
iShipToBusiness.partner                       - Ship-to Business Partner
iShipToAddress                                - Ship-to Address
iSalesOrder                                   - Sales Order - Needed for direct
delivery.
iSalesOrderLine                               - Sales Order Line. Mandatory if Sales
Order is filled. Needed for
direct delivery.
iSalesOrderLineSequence                       - Sales Order Line Sequence
iOrderQuantity                        - Order Quantity
iOrderQuantityConvFactorToInvUnit                       - Order Quantity
Conversion Factor to inventory Unit.
Mandatory.
This field must be filled with 1.0 if
no quantity is given.
iRoute                                        - Route
iServiceLevel                                 - Service Level
iTermsOfDelivery                              - Terms of Delivery
iPointOfTitlePassage                          - Point of Title Passage
iPreferredCarrier                             - Preferred Carrier
iCarrier                                      - Carrier
Output: oPlannedReceiptDate                   - The calculated Planned receipt date.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Calculate was successful
<> 0                                          - An error occurred
```
