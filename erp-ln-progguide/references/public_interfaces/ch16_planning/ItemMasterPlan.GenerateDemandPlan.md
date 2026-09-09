# ItemMasterPlan.GenerateDemandPlan

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 543-544

```baan
DLL:   cpextdspapi
This function is available from 2024.08 (KB2318565).
Syntax: long ItemMasterPlan.GenerateDemandPlan(
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
domain  tcmcs.chan       iChannel,
long             iPeriodFrom,
long             iPeriodTo,
boolean          iGenerateToExtraDemand,
boolean          iCalculateForecastSettings,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to generate the demand forecast for items
and item/channel combinations based on historical demand data.
Transaction management is handled by this public interface.
Pre:    N.A.
Post:   N.A.
Input:  iScenario
- Planning Scenario (Mandatory).
iPlanItem
- Plan Item (mandatory).
iChannel
- Channel, when left empty, the scope is Item Master
Plan level only.
iPeriodFrom
- Period as defined in Planning Scenario (mandatory).
iPeriodTo
- Period as defined in Planning Scenario (mandatory).
iGenerateToExtraDemand
- Control to move the calculated forecast to the extra
demand field in the Master Plan.
iCalculateForecastSettings
- Control to calculate the optimal set of parameters for
generation of the demand forecast.
Output: oExceptionMessage
- The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
- An ID that refers to the exception information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Demand Plan is generated successfully.
<> 0    - Demand Plan is not generated successfully.
```
