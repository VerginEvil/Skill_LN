# SalesOrder.UnpackObjectReference

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 332-333

```baan
DLL:   tdextslsapi
This function is available from     2025.04 (KB3568308  ).
Syntax: long SalesOrder.UnpackObjectReference(
domain  tcborf           iObjectReference,
ref     domain  tcpono           oSalesOrderLine,
ref     domain  tcpono           oSalesOrderLineSequence,
ref     domain  tcpono           oActualDeliveryLineSequence,
ref     domain  tcpono           oInvoiceLine,
ref     domain  tcnins           oInstallment,
ref     domain  tdcms.type       oCommissionRebateType,
ref     domain  tccom.bpid       oRelation,
ref     domain  tcpono           oCommissionRebateSequence,
ref     domain  tcpono           oSalesOrderBomLine,
ref     domain  tctax.indi       oTaxIndicator,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function unpacks the given object reference of a sales order.
It retrieves relevant information based on the packed object reference
in the input field.
Pre:    Not applicable
Post:   Not applicable
Input:  iObjectReference                              - Object Reference (mandatory)
Output: oSalesOrderLine                               - Sales Order Line
oSalesOrderLineSequence                               - Sales Order Line Sequence Number
oActualDeliveryLineSequence                           - Actual Delivery Line Sequence Number
oInvoiceLine                                          - Invoice Line
oInstallment                                          - Installment
oCommissionRebateType                                 - Type Commission or Rebate
oRelation                                             - Relation by sales order line
oCommissionRebateSequence                             - Sequence Commission or Rebate
oSalesOrderBomLine                                    - BOM Line of Sales Order
oTaxIndicator                                         - Tax Indicator
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - No error
<> 0                                                  - Error occurred
```
