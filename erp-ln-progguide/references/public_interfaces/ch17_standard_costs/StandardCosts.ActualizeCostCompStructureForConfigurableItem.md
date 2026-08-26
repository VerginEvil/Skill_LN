# StandardCosts.ActualizeCostCompStructureForConfigurableItem

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 602-603

```baan
DLL:   tiextcprapi
This function is available from     2025.07 (KB3592930  ).
Syntax: long StandardCosts.ActualizeCostCompStructureForConfigurableItem(
domain  tcitem           iItem,
ref             boolean          oCostComponentStructureUpdated,
ref             boolean          oSurchargesActualized,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function Actualizes the Cost Component Structure and
Surcharges for a Configurable Item, like the form command
Actualize Cost Comp Structure for Configurable Item available on
session Item                       - Costing (ticpr0107m000).
Pre:    N.A.
Post:   N.A.
Input:  iItem                   Item (Mandatory)
Output: oCostComponentStructureUpdated
Indicates whether or not the Cost
Component Structure was updated.
oSurchargesActualized   Indicates whether or not Surcharges were
actualized.
oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Actualizes cost component structure and
surcharges of a given configurable item
successfully.
<> 0                    An error occurred while actualizing cost
component structure and surcharges.
```
