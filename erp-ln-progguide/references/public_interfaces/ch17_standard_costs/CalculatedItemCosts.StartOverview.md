# CalculatedItemCosts.StartOverview

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for CalculatedItemCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 599-601

```baan
DLL:   tiextcprapi
This function is available from     2023.12 (KB2303582  ).
Syntax: long CalculatedItemCosts.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccpcc           iCostCalculationCode,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
ref     domain  tccpcc           oCostCalculationCode,
ref     domain  tcitem           oItem,
ref     domain  tcemm.grid       oEnterpriseUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Calculated Item Costs
in overview mode (ticpr2501m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported values:
1: sort by Item/Enterprise Unit
2: sort by Enterprise Unit/Item
iQueryExtend            A specific query to be used when zooming
to this session.
iCostCalculationCode    Cost Calculation Code
iItem                   Item
iEnterpriseUnit         Enterprise Unit
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oCostCalculationCode
Cost Calculation Code
oItem           Item
oEnterpriseUnit Enterprise Unit
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```

## Public Interfaces for StandardCosts

The following functions are available: StandardCosts.Actualize StandardCosts.ActualizeCostCompStructureForConfigurableItem StandardCosts.Calculate StandardCosts.CalculateAndGetStandardCost StandardCosts.CalculateAndGetStandardCostV2 StandardCosts.CalculateAndGetStandardCostV3 StandardCosts.CalculateForNewItem StandardCosts.CalculateForSimulation StandardCosts.CalculateSingleItem StandardCosts.PrintMultilevelCostCalculation StandardCosts.StartCalculate
