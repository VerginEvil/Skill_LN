# SalesOrder.DetermineAdditionalCostLines

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 318-319

```baan
DLL:   tdextslsapi
This function is available from     2024.05 (KB2320802  ).
Syntax: long SalesOrder.DetermineAdditionalCostLines(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
ref             long             oNumberOfCostLines,
ref     domain  tcitem           oItemArray() fixed,
ref     domain  tcamnt           oAmountArray(),
ref     domain  tcdate           oPlannedDeliveryDateArray(),
ref     domain  tccprj           oProjectArray() fixed,
ref     domain  tccspa           oElementArray() fixed,
ref     domain  tccact           oActivityArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines and returns the Additional Cost lines
for the input Sales Order or Sales Order Line.
In case the input argument iSalesOrderLine is empty the
additional cost lines for the Sales Order header are returned,
otherwise for the input Order Line.
The Amount is expressed in the Currency of the input Order.
Pre:    N.A.
Post:   During the process the output arrays will be allocated,
so afterwards a free.mem() must be done by the caller in order
to free the memory which is occupied by the arrays.
Input:  iSalesOrder                              - Sales Order (Mandatory)
iSalesOrderLine                                  - Sales Order Line (Optional)
iSalesOrderLineSequence                          - Sales Order Line Sequence (Optional)
Output: oNumberOfCostLines                       - Number of Cost Lines that are
present in the arrays
oItemArray                                       - Array with Cost Items
oAmountArray                                     - Array with Amounts, expressed in
the Currency of the Sales Order
oPlannedDeliveryDateArray                        - Array with Planned Delivery Dates
oProjectArray                                    - Array with Projects
oElementArray                                    - Array with Elements
oActivityArray                                   - Array with Activities
oExceptionMessage                                - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                     - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                        - Determination of Additional Cost
was successful
<> 0                                             - An error occurred
```
