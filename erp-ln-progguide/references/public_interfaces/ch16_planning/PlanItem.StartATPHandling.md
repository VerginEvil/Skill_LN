# PlanItem.StartATPHandling

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 539-540

```baan
DLL:   cpextrrpapi
This function is available from 2023.11 (KB2303683).
Syntax: long PlanItem.StartATPHandling(
long             iStartMode,
domain  cpcom.plnc       iPlanningScenario,
domain  cpitem           iPlanItem,
domain  tcncmp           iCompany,
domain  tcdate           iDeliveryDate,
domain  tcqsl1           iQuantity,
domain  tccuni           iUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   *** Warning ***
This public interface is deprecated.
use:    PlanItem.StartATPHandlingV2
This Public Interface starts the session ATP Handling
(cprrp4800m000).
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
