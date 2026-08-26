# SalesOrderLine.GenerateProductionOrder

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 347-348

```baan
DLL:   tdextslsapi
This function is available from     2025.05 (KB3569018  ).
Syntax: long SalesOrderLine.GenerateProductionOrder(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
long             iProcessingOptionSet,
ref     domain  tcorno           oProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl. : This function generates a production order for the item of a
specific sales order line.
The execution of automatic order steps is not started. Function
SalesOrderLine.StartAutomaticProcessing can be used for this.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales order (Mandatory)
iSalesOrderLine                               - Sales order line (Mandatory)
iSalesOrderLineSequence                       - Sales order line sequence
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default options of session
"Generate Production Orders" are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields on session
"Generate Production Orders" (tdsls4243m000) and are not explained in further
detail here. Please refer to the session help for additional information.
The session's print options are not applicable, because printing is not
supported using this function to generate a production order for a single
sales order line.
Any options which are not available as Processing Option will get defaulted in
accordance with the session logic.
Processing Options which are set while a required Implemented Software Component
is not available are ignored.
Supported Processing Options and their defaults:
NAME                                    TYPE                    DEFAULT
ProductionOrderSeries                   domain tcseri           ""
ProcessDeliveryTypeProduction           domain tcyesno          tcyesno.yes
ProcessDeliveryTypeWarehouse            domain tcyesno          tcyesno.yes
ConsiderAllocatedToInventory            domain tcyesno          tcyesno.yes
ConsiderDemandPeggedToSupplyOrders      domain tcyesno          tcyesno.yes
Output: oProductionOrder                              - The generated production order
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
