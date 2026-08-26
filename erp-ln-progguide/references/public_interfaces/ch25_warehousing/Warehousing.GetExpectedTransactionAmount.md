# Warehousing.GetExpectedTransactionAmount

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Warehousing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 979-980

```baan
DLL:   whextinhapi
This function is available from     2026.08 (KB3682905  ).
Syntax: long Warehousing.GetExpectedTransactionAmount(
domain  tcncmp           iWarehouseCompany,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcatse           iAttributeSet,
domain  tccprj           iPeggedProject,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tcttr.tagn       iTag,
domain  tcncmp           iOrderCompany,
domain  tckoor           iKindOfOrder,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcdate           iTransactionDate,
domain  tcqiv1           iQuantity,
domain  tcowns           iOwnership,
domain  tccom.bpid       iIssueFromBusinessPartner,
domain  tciown           iIssueOwnership,
domain  tcreje           iRejectionType,
domain  tcyesno          iUseFixedReceiptPrice,
domain  tcpric           iFixedReceiptPrice,
ref     domain  tcamnt           oTransactionAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface determines the expected transaction
amount of a warehouse transaction.
It is called for:
-                       Adjustment Orders
-                       Cycle Counting Orders
-                       Cost Peg Transfers
This function is called when creating an order line
to give the user insight in the estimated transaction amount.
At the moment order is processed the valuation price is
overwritten by the actual transaction amount.
Pre:    N.a.
Post:   N.a.
Input:  iWarehouseCompany                     - WH Logistic Company; Mandatory
iWarehouse                                    - Warehouse; Mandatory
iItem                                         - Item; Mandatory
iAttributeSet                                 - Attribute Set; Optional
iPeggedProject                                - Pegged Project; Optional
iLot                                          - Lot Code; Optional
iSerial                                       - Serial Code; Optional
iTag                                          - Tag; Optional
iOrderCompany                                 - Order Company; Mandatory
iKindOfOrder                                  - Kind of Order; Mandatory
iOrder                                        - Order Number; Mandatory
iOrderLine                                    - Order Line; Mandatory
iTransactionDate                              - Transaction Date; Mandatory
iQuantity                                     - Variance Quantity; Mandatory
iOwnership                                    - Ownership; Mandatory
iIssueFromBusinessPartner                       - Issue From Business Partner;
Optional (only applicable when
iQuantity < 0)
iIssueOwnership                               - Issue Ownership;
Optional (only applicable when
iQuantity < 0)
iRejectionType                                - Rejection Type; Optional
iUseFixedReceiptPrice                         - Use Fixed Receipt Price; Mandatory
iFixedReceiptPrice                            - Fixed Receipt Price; Mandatory when
iUseFixedReceiptPrice = tcyesno.yes
Output: oTransactionAmount                    - Expected Transaction Amount
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0               - Transaction amount determined successfully
<> 0                       - Error.
```
