# StandardCosts.CalculateForSimulation

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for StandardCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 612-613

```baan
DLL:   tiextcprapi
This function is available from 2021.11 (KB2199520).
Syntax: long StandardCosts.CalculateForSimulation(
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
domain  tccpcc           iCalculationCode,
domain  tcdate           iCalculationDate,
domain  tcccmt           iMethod,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the standard costs for the specified
item.
When standard items are calculated, the calculation code should
not be the Standard Cost Calculation Code as defined in Standard
Cost Calculation Parameters (ticpr0100m000).
Retry points and commit / abort transactions are set and
executed within this public interface.
Pre:    None.
Post:   None.
Input:  iItem                   Item (Mandatory)
iEnterpriseUnit         Enterprise Unit (Mandatory when the
concept Standard Cost per EU
is active, otherwise empty).
iCalculationCode        Calculation Code (Mandatory).
iCalculationDate        Reference Date for calculation.
iMethod                  - Top Down
- Single Level
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Standard Cost calculated for simulation.
<> 0                    Failure.
```
