# ItemOrderPlan.GetV2

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 550-552

```baan
DLL:   cpextrrpapi
This function is available from 2026.02 (KB3599795).
Syntax: long ItemOrderPlan.GetV2(
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  cprrp.perl       iPeriodLength,
boolean          iShowOrderDistribution,
ref             long             oNumberOfRows,
ref     domain  cporno           oOrderNumber() fixed,
ref     domain  tckoor           oOrderType(),
ref     domain  tcpono           oLinePositionNumber(),
ref     domain  tcpono           oSequenceNumber(),
ref     domain  tcpono           oDistributionLine(),
ref     domain  tckotr           oTransactionType(),
ref     domain  cpitem           oPlannedItem() fixed,
ref     domain  tcdate           oFinishDate(),
ref     domain  tcqiv1           oScheduledReceipt(),
ref     domain  tcqiv1           oPlannedDemand(),
ref     domain  tcqiv1           oActualDemand(),
ref     domain  tcqiv1           oUnconsumedForecast(),
ref     domain  tcqiv1           oOnHand(),
ref     domain  tcqiv1           oNetRequirement(),
ref     domain  tcqiv1           oPlannedAvailable(),
ref     domain  tcqiv1           oSafetyStockLevel(),
ref     domain  tcqiv1           oProductionPlan(),
ref     domain  tcqiv1           oPurchasePlan(),
ref     domain  tcqiv1           oConfirmedDemand(),
ref     domain  tcqiv1           oConfirmedDemandItemOnly(),
ref     domain  tcqiv1           oConfirmedOnHand(),
ref     domain  tcqiv1           oConfirmedPlanningAvailable(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the Item Order Plan for the specific
Scenario and Plan Item and returns the results in arrays.
The results are detailed or grouped per day/week/2weeks/4weeks.
Limitations:
This function does not support Project Pegging. For a single
order, retrieved plan does not include the derived from items.
Pre:    Technical: Output arrays must be defined as based arrays.
Post:   Technical: Execute free.mem() for the output arrays (after
usage of the data).
Input:
iPlanningScenario       Planning Scenario (Mandatory).
iPlanItem               Plan Item (Mandatory).
iPeriodLength           Possible values:            (Mandatory).
1day (= grouped in 1 day periods),
7days (= grouped in 1 week periods),
14days (= grouped in 2 week periods),
28days (= grouped in 4 week periods),
detail (= not grouped),
plan (= grouped in Plan Periods),
iShowOrderDistribution  If true and period length is set to
'Detail', then the output will be on the
most detailed level (order distribution).
Else output is aggregated on Order
Position level.
Values: true, false
Output:
oNumberOfRows           Number of item orders.
oOrderNumber            Numbers array.
oOrderType              Type array.
oPositionNumber         Position Number array.
oSequenceNumber         Sequence number array.
oDistributionLine       Distribution line position array.
oTransactionType        Transaction type array.
oPlannedItem            Planned Item or Plan Item materials.
oFinishDate             Finish date.
oScheduledReceipt       Scheduled receipt array.
oPlannedDemand          Planned demand array.
oActualDemand           Actual demand array.
oUnconsumedForecast     Forecast array.
oOnHand                 On hand array.
oNetRequirement         Net requirement array.
oPlannedAvailable       Planned availability array.
oSafetyStockLevel       Safety stock level array.
oProductionPlan         Production plan array.
oPurchasePlan           Purchase plan array.
oConfirmedDemand        Confirmed Demand array.
oConfirmedDemandItemOnly
Confirmed Demand Item Only array.
oConfirmedOnHand        Confirmed On Hand array.
oConfirmedPlanningAvailable
Confirmed Planning Available array.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function is executed successfully
<> 0                    An error occurred
```
