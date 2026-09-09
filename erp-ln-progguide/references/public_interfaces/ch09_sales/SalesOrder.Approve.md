# SalesOrder.Approve

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 311-312

```baan
DLL:   tdextslsapi
This function is available from 2021.11 (KB2200009).
Syntax: long SalesOrder.Approve(
domain  tcorno           iSalesOrder,
domain  tcgen.ynds       iRecalculatePricesAndDiscounts,
domain  tcgen.ynds       iRedetermineMaterialPriceInformation,
domain  tcgen.ynds       iRecalculateAdditionalCosts,
domain  tcyesno          iHandleCommissionsAndRebates,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl. : This Public Interface approves the given sales order.
After the approval, the automatic order processing is executed.
Note that promotions are not applied when Approving via this
Public Interface, because promotions require user-interaction.
This function contain its own transaction logic. As this Public
Interface starts Automatic Order Processing (which could take a
relatively long time) it is advised to not call this Public
Interface in a BOD or BDE context. Doing that would suppress
the internal transaction logic and would create one large database
transaction, with potential locking problems as a consequence.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iSalesOrder             - Sales order (Mandatory)
iRecalculatePricesAndDiscounts
- Recalculate prices and discounts:
No   - Do not recalculate
Yes  - Recalculate
Use Default Settings
- Consider the parameter and/or
sales office setting
'Recalculate Prices and Discounts'
iRedetermineMaterialPriceInformation
- Redetermine Material Price Information
No   - Do not redetermine
Yes  - Redetermine
Use Default Settings
- Consider the parameter and/or
sales office setting
'Redetermine Material Information
in Sales'
iRecalculateAdditionalCosts
- Recalculate additional costs.
No   - Do not recalculate
Yes  - See 'Use Default Settings'
Use Default Settings
- Consider the parameter and/or
sales office setting
'Recalculation of Additional
Costs'
iHandleCommissionsAndRebates
- Allow linking of relations and
Recalculation of commissions and
rebates (Yes/No)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Approval was successful
<> 0                    - An error occurred
```
