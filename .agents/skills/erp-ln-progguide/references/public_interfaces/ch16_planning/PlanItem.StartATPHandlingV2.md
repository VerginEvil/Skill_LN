# PlanItem.StartATPHandlingV2

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 540-541

```baan
DLL:   cpextrrpapi
This function is available from 2026.11 (KB3685681).
Syntax: long PlanItem.StartATPHandlingV2(
long             iStartMode,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  tcncmp           iCompany,
domain  tcdate           iDeliveryDate,
domain  tcqsl1           iQuantity,
domain  tccuni           iUnit,
domain  tccwar           iWarehouse,
domain  tdqsl1           iMinimumAvailable,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface opens session ATP Handling (cprrp4800m000)
with extended control over fields that were not configurable
in PlanItem.StartATPHandling. In addition to the
PlanItem.StartATPHandling parameters, It adds Warehouse and
Minimum Available as specific parameters, and
Demand Pegging Type, Check Capacity, Check Component, and
Direct Delivery as Processing Options. The customer performs
When Available and Accept Check actions manually after the
session opens with populated fields.
Pre:    -
Post:   -
Input:  iStartMode
Mandatory - Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS -
Parent and child are parallel
sessions that can be manipulated
simultaneously.
iPlanningScenario       Mandatory - The Planning Scenario.
iPlanItem               Mandatory - Plan Item.
iCompany                Mandatory - Company to deliver from.
iDeliveryDate           Mandatory - Delivery Date.
iQuantity               Mandatory - Required Quantity.
iUnit                   Mandatory - Unit of Quantity.
iWarehouse              Optional  - Ordering Warehouse.
iMinimumAvailable       Optional  - Minimum Available.
iProcessingOptionSet    A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create().
If 0, then user default/session
default values are applied.
Processing Options have a direct relationship with the form fields
on session ATP Handling (cprrp4800m000) and are not explained in further
detail here. Please refer to the session help for additional information.
ATP Handling options which are not available as Processing Options will
get defaulted in accordance with the session logic.
NAME                    TYPE            DEFAULT NOTES
DemandPeggingType       domain  tcpgtp  empty   Controls pegging
behavior. Maps to
e.demand.peg.type
CheckCapacity           domain  tcyesno empty   Toggle for capacity
check.Maps to
e.check.capacity
CheckComponent          domain  tcyesno empty   Toggle for component
check. Maps to
e.check.component
DirectDelivery          domain  tcyesno empty   Toggle for direct
delivery mode. Maps to
e.direct.delivery
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
