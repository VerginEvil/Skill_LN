# ItemOrderPlan.Generate

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemOrderPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 543-545

```baan
DLL:   cpextrrpapi
This function is available from     2024.06 (KB2311388  ).
Syntax: long ItemOrderPlan.Generate(
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
boolean          iGenerateItemMasterPlan,
boolean          iUpdateOnly,
boolean          iRemoveFirmPlannedOrders,
boolean          iAllowMultipleSourcesPerDemand,
boolean          iFirmDemandPeggedOrder,
boolean          iGenerateWithinTimeFence,
boolean          iConfirmWithinTimeFence,
boolean          iScheduleRepetitiveWorkCells,
boolean          iUpdatePeggingRelations,
boolean          iAutomaticOrderGrouping,
boolean          iUpdateResourceMasterPlan,
boolean          iSaveExceptionMessages,
domain  tcemno           iPlannerId,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function is used to carry out an order-planning for one
plan item to generate orders of the following order types:
-                         Planned Production Order
-                         Planned Production Schedule
-                         Planned Purchase Order
-                         Planned Distribution Order
-                         Planned Subcontracting Order
If repetitive manufacturing is used, production schedules and
planned production schedules for repetitive items are
generated. The production schedule horizon is used to
differentiate between Production Schedules and Planned
Production Schedules.
Only generates orders that fall within the order horizon.
Pre     : There should be no pending logical transaction before calling
this function.
Post    : No need to commit or abort the process, that is handled within
the function.
Input   : iScenario             Planning Scenario (Mandatory).
iPlanItem             Plan Item (Mandatory).
iGenerateItemMasterPlan
Control for performing a Master Plan
Simulation Planning when a Plan Item has
performed an Order Planning.
iUpdateOnly           Control for performing a Master Plan
Simulation Planning and Update ATP.
iRemoveFirmPlannedOrders
Control for removing all previously
generated Planned Orders with the Firm
Planned Order status.
iAllowMultipleSourcesPerDemand
Control for allowing multiple sources
(Pur/ Manuf/Distr) for one Planned
Order.
iFirmDemandPeggedOrder
Control for setting Planned Orders with
an allocation to Firm Planned.
iGenerateWithinTimeFence
Control for Enterprise Planning to
generate Planned Orders within time
fence.
iConfirmWithinTimeFence
Control for setting Planned Orders
status with Planned finish dates within
time fence to Confirmed.
iScheduleRepetitiveWorkCells
Control for the Production Schedules
linked to the work cells, to be
scheduled against finite capacity.
iUpdatePeggingRelations
Control for updating Pegging Relations.
iAutomaticOrderGrouping
Control for rebuilding the
Automatic                                              -update Order Groups.
iUpdateResourceMasterPlan
Control for updating the resource master
plan for the resources involved in the
Planned Production Orders that
Enterprise Planning generates for the
specified Plan Item.
iSaveExceptionMessages
Control for updating the exception
messages in the Exception Messages
(cprao1125m000) session.
iPlannerId            Employee to whom all generated
exception messages are assigned.
Output  : oExceptionMessage     The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID          An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                     Item Order Planning is created.
<> 0                  Otherwise.
```
