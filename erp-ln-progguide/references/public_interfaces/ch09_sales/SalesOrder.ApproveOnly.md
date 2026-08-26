# SalesOrder.ApproveOnly

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 310-311

```baan
DLL:   tdextslsapi
This function is available from     2024.09 (KB3516530  ).
Syntax: long SalesOrder.ApproveOnly(
domain  tcorno           iSalesOrder,
domain  tcgen.ynds       iRecalculatePricesAndDiscounts,
domain  tcgen.ynds       iRedetermineMaterialPriceInformation,
domain  tcgen.ynds       iRecalculateAdditionalCosts,
domain  tcyesno          iHandleCommissionsAndRebates,
ref             boolean          oOrderApproved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl. : This Public Interface approves the given sales order. It does
not start the execution of automatic order steps.
Notes:
* A separate Public Interface can be used to
start automatic order steps if necessary:
'SalesOrderLine.StartAutomaticProcessing'
* Promotions are not applied when Approving via this Public
Interface, because promotions require user                          -interaction.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales order (Mandatory)
iRecalculatePricesAndDiscounts
-                                               Recalculate prices and discounts:
No                                                    - Do not recalculate
Yes                                                   - Recalculate
Use Default Settings
-                                                       Consider the parameter and/or
sales office setting
'Recalculate Prices and Discounts'
iRedetermineMaterialPriceInformation
-                                               Redetermine Material Price Information
No                                                    - Do not redetermine
Yes                                                   - Redetermine
Use Default Settings
-                                                       Consider the parameter and/or
sales office setting
'Redetermine Material Information
in Sales'
iRecalculateAdditionalCosts
-                                               Recalculate additional costs.
No                                                    - Do not recalculate
Yes                                                   - See 'Use Default Settings'
Use Default Settings
-                                                       Consider the parameter and/or
sales office setting
'Recalculation of Additional
Costs'
iHandleCommissionsAndRebates
-                                               Allow linking of relations and
Recalculation of commissions and
rebates (Yes/No)
Output: oOrderApproved                        - The order was approved (true/false)
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success.
Note: The order may not be approved in
this situation. However, the caller
must still commit the transaction,
even if the order is not approved
(i.e., oOrderApproved = false).
This is necessary, for example, to
commit the check results in ZWF
(e.g., export and sanction list screening).
<> 0                                          - An error occurred
```
