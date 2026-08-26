# ProjectPCS.CalculateCostV2

> Chapter: Chapter 24 Public Interfaces for Manufacturing Project
>
> Group: Public Interfaces for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 875-876

```baan
DLL:   tiextpcsapi
This function is available from     2026.07 (KB3677707  ).
Syntax: long ProjectPCS.CalculateCostV2(
domain  tccprj           iProject,
boolean          iCalculateEstimatedCost,
boolean          iCalculateActualCost,
domain  tcdate           iEffectiveDate,
boolean          iNetChangeOnly,
boolean          iSimulatedCalculation,
domain  tccpcc           iSimulationCalculationCode,
boolean          iUpdateCOSDistribution,
boolean          iRecalculateStandardParts,
domain  tccpcc           iCalculationCodeStandardItems,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will Calculate the PCS Project Cost for one
project, according to the logic of session Calculate Standard Costs
by Project (tipcs3250m000).
Note that even when the function returns 0 (indicating success),
in various parts of the calculation process warning messages may
have been set.
These messages can be found in the returned ExceptionID structure.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within.
Input:  iProject                The PCS project (Mandatory).
iCalculateEstimatedCost When true: Calculate Estimated Cost.
iCalculateActualCost    When true: Calculate Actual Cost.
iEffectiveDate          Use this date as the Effective Date of
Standard Cost and Valuation Prices.
When set to 0, the current date is used.
iNetChangeOnly          When true: Only calculate actual cost
when transactions were logged after
the previous actual cost calculation.
iSimulatedCalculation   When true: perform simulated calculation
of Standard Cost of all project items.
Simulation cannot be combined with
Estimated or Actual Cost calculation.
iSimulationCalculationCode
(Optional), if provided, the calculation
is done using the given code. Otherwise
the Calculation Code of the Project is
used. This affects the Simulated
Cost calculation.
iUpdateCOSDistribution  When true: the COS (Cost of Sales)
distribution is updated. This option
is independent of other calculation
options.
iRecalculateStandardParts
When true: Standard Parts in the
customized bill of material are
recalculated. This option affects the
Estimated Cost calculation.
i.calculation.code.standard.items
Calculation Code for Standard Items
(Mandatory if iSimulated.calculation is True)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successful completion
<> 0                    Failure
```
