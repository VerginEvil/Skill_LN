# ItemMasterPlan.GenerateInventoryPlan

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 540-541

```baan
DLL:   cpextdspapi
This function is available from     2024.08 (KB2318565  ).
Syntax: long ItemMasterPlan.GenerateInventoryPlan(
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
long             iPeriodFrom,
long             iPeriodTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to  generate the Inventory Plan in the
Item Master Plan.
Transaction management is handled by this public interface.
Pre:    N.A.
Post:   N.A.
Input:  iScenario                             - Planning Scenario (Mandatory).
iPlanItem                                     - Plan Item (mandatory).
iPeriodFrom                                   - Period as defined in Planning Scenario
(mandatory).
iPeriodTo                                     - Period as defined in Planning Scenario
(mandatory).
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Inventory Plan is generated
successfully.
<> 0                                          - Inventory Plan is not generated
successfully.
```
