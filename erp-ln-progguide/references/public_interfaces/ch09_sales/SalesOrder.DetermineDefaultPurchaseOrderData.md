# SalesOrder.DetermineDefaultPurchaseOrderData

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 319-320

```baan
DLL:   tdextslsapi
This function is available from     2024.12 (KB3541875  ).
Syntax: long SalesOrder.DetermineDefaultPurchaseOrderData(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tccwoc           iSalesOffice,
domain  tccwoc           iSalesDepartment,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tcdate           iSalesOrderDate,
domain  tcitem           iItem,
domain  tdsls.dltp       iDeliveryType,
domain  tcsite           iSite,
domain  tcyesno          iIsReturnOrder,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tccom.bpid       oShipFromBusinessPartner,
ref     domain  tccom.cadr       oShipFromAddress,
ref     domain  tccwoc           oPurchaseOffice,
ref     domain  tccwoc           oFinancialDepartment,
ref     domain  tcccur           oCurrency,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the default purchase order data for a
given sales order. It retrieves relevant information such as
supplier details based on the sales order requirements in the
input fields. The more specific the input fields are filled, the
better the correct defaults can be found.
Pre:    Not applicable
Post:   Not applicable
Input:  iSalesOrder                                   - Sales Order
iSalesOrderLine                                       - Sales Order Line
iSalesOrderLineSequence                               - Sales Order Line Sequence
(should be >= 0)
iSalesOffice                                          - Sales Office (mandatory)
iSalesDepartment                                      - Sales Department
iSoldToBusinessPartner                                - Sold-to Business Partner
iShipToBusinessPartner                                - Ship-to Business Partner
iSalesOrderDate                                       - Sales Order Date
iItem                                                 - Item (mandatory)
iDeliveryType                                         - Delivery Type
iSite                                                 - Site
iIsReturnOrder                                        - Flag if the Sales Order is a
Return Order (yes/no)
Output: oBuyFromBusinessPartner                       - Buy-from Business Partner
oShipFromBusinessPartner                              - Ship-from Business Partner
oShipFromAddress                                      - Ship-from Address
oPurchaseOffice                                       - Purchase Office
oFinancialDepartment                                  - Financial Department
oCurrency                                             - Currency
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -> No error
<> 0                          -> Error occurred
```
