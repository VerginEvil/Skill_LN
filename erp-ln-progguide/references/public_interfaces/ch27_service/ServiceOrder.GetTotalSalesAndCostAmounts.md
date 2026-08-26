# ServiceOrder.GetTotalSalesAndCostAmounts

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1416-1418

```baan
DLL:   tsextsocapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long ServiceOrder.GetTotalSalesAndCostAmounts(
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
boolean          iOnlyCostLinesDirectlyLinkedToHeader,
domain  tsmdm.cotp       iCostType,
boolean          iSkipSalesAmountsCoveredByQuote,
boolean          iCalculateEstimatedAmounts,
ref             long             oNumberOfHomeCurrencies,
ref     domain  tcccur           oArrayWithHomeCurrencies() fixed,
ref     domain  tcamnt           oTotalEstimatedSalesAmount,
ref     domain  tcamnt           oTotalEstimatedCostAmountArray(),
ref     domain  tcamnt           oTotalEstimatedInvoiceableSalesAmount,
ref     domain  tcamnt           oTotalEstimatedInvoiceableCostAmountArray(),
ref     domain  tcamnt           oTotalEstimatedNettSalesAmount,
ref     domain  tcamnt           oTotalSalesAmount,
ref     domain  tcamnt           oTotalCostAmountArray(),
ref     domain  tcamnt           oTotalInvoiceableSalesAmount,
ref     domain  tcamnt           oTotalInvoiceableCostAmountArray(),
ref     domain  tcamnt           oTotalNettSalesAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function will retrieve the total of all the sales and
cost amounts of all material, labor or other lines belonging to
the Service Order or Activity Line.
If iActivityLine is zero, all lines are aggregated.
If iActivityLine is not zero then the totals are
calculated for the given activity line.
If iActivityLine is zero, but
iOnlyCostLinesDirectlyLinkedToHeader is True, the amount of
the cost lines directly linked to the header is calculated.
If iSkipSalesAmountsCoveredByQuote is True, sales
amounts of cost lines that are covered by a quote are not added
to the sales totals.
If iCalculateEstimatedAmounts is True, the estimated
total amounts of estimated lines are calculated as well.
Otherwise these will remain zero.
Pre:    iServiceOrder should be filled and the output arrays should
have been allocated three elements deep.
Post:   N.A.
Input:  iServiceOrder                                 - The Service Order
Mandatory
iActivityLine                                         - The Activity Line
Not Mandatory
If not zero, cost lines
linked to the specific
activity are aggregated.
iOnlyCostLinesDirectlyLinkedToHeader
-                                                       Used if Activity Line is zero
only. If True, cost lines
directly linked to the header
are aggregated.
If False, all cost lines
belonging to the order are
aggregated.
iCostType                                             - The Cost Type to indicate
the type of costs to be
calculated. Possible values:
-                                                            Material
Material Cost lines are
aggregated.
-                                                            Labor
Labor Cost lines are
aggregated.
-                                                            Other
Other Cost lines are
aggregated (all cost
types except material
and labor).
-                                                            Order
All Cost lines of the
entire Order are
aggregated.
-                                                            Activity
All Cost lines of the
given Activity are
aggregated. The
Activity is mandatory
in this case.
Mandatory
iSkipSalesAmountsCoveredByQuote
-                                                       If True, sales amounts of
cost lines covered by a quote
are not added to the total.
iCalculateEstimatedAmounts
-                                                       If True estimated cost line
amounts are calculated as
well.
Output: oNumberOfHomeCurrencies                       - The Number of Home Currencies
which relate to the financial
company of the work order
department.
oArrayWithHomeCurrencies                              - The Array with Home Currencies
which relate to the financial
company of the work order
department.
oTotalEstimatedSalesAmount                            - The Total Estimated Sales
Amount.
oTotalEstimatedCostAmountArray                        - The array with the Total
Estimated Cost Amount.
oTotalEstimatedInvoiceableSalesAmount
-                                                       The Total Estimated Invoiceable
Sales Amount.
oTotalEstimatedInvoiceableCostAmountArray
-                                                       The array with the Total
Estimated Invoiceable Cost
Amount.
oTotalEstimatedNettSalesAmount
-                                                       The Total Nett Sales Amount.
oTotalSalesAmount                                     - The Total Sales Amount.
oTotalCostAmountArray                                 - The array with the Total
Cost Amount.
oTotalInvoiceableSalesAmount
-                                                       The Total Invoiceable
Sales Amount.
oTotalInvoiceableCostAmountArray
-                                                       The array with the Total
Invoiceable Cost
Amount.
oTotalNettSalesAmount                                 - The Total Nett Sales Amount.
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - No Error
<> 0                                                  - Error
```
