# ProjectBudget.GenerateBudgetCostAnalysis

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectBudget
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1716-1719

```baan
DLL:   tpextptcapi
This function is available from 2023.12 (KB2300365).
Syntax: long ProjectBudget.GenerateBudgetCostAnalysis(
domain  tccprj           iProject,
domain  tpptc.cuca       iProcessOptions,
domain  tcyesno          iUseActualBudgetCostAnalysisVersion,
domain  tpptc.ccal       iBudgetCostAnalysisVersion,
domain  tppdm.desc       iBudgetCostAnalysisVersionDesc mb,
domain  tppdm.yeno       iUpdateActualBudgetCostAnalysisVersion,
domain  tppdm.bdtp       iBudgetType,
domain  tcrtyp           iExchangeRateType,
domain  tppdm.yeno       iUseBudgetLineDate,
domain  tppdm.date       iRateDate,
domain  tppdm.yeno       iIncludeBudgetCostStatusFree,
domain  tppdm.yeno       iIncludeBudgetCostStatusActual,
domain  tppdm.yeno       iIncludeBudgetCostStatusFinal,
domain  tppdm.yeno       iIncludeBudgetCostExtension,
domain  tcyesno          iIncludeBudgetCostContingency,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to generate cost calculations for the cost
analyses for a selected project.
This function offers similar functionality as session
(tpptc3200m000 - Generate Budget Cost Analysis).
Note: In case of main and sub project; the sequence of all
calling this function should be main project first and
then the related subprojects.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iProject                                -
Project: Mandatory
iProcessOptions                         -
Process Options, Mandatory
Allowed Values:
tpptc.cuca.create - Create Cost Analysis Version
tpptc.cuca.update - Update Cost Analysis
The option Create Cost Analysis Version creates a new cost
analysis version, overwriting an existing one.
The option Updates Cost Analysis updates an existing cost
analysis version.
iUseActualBudgetCostAnalysisVersion     -
Use Actual Budget Cost Analysis Version, Mandatory
Allowed Values:
tcyesno.yes     - Yes
tcyesno.no      - No
The field is applicable if the Process Options is set to
Update Cost Analysis Version.
This field is set to Yes then the actual budget cost
analysis version defined on the project is updated.
iBudgetCostAnalysisVersion              -
Budget Cost Analysis Version, Optional
The field is applicable when Use Actual Budget Cost
Analysis Version is set to No.
This field is used to add a cost analysis version/code.
In combination with the project and cost analysis code the
budget is stored. This is used to compare the different
budget cost analysis versions.
iBudgetCostAnalysisVersionDesc          -
Budget Cost Analysis Version Description, Optional
The fields is applicable when Use Actual Budget Cost
Analysis Version is set to No.
This field is used add Cost Analysis Version description.
iUpdateActualBudgetCostAnalysisVersion  -
Update Actual Budget Cost Analysis Version, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
The field is applicable only if the Use Actual Budget
Cost Analysis Version is set to No.
This field is set to Yes then the specified cost
analysis version is updated as the actual cost analysis
version and replaces any previous cost analysis version
defined for the selected project.
iBudgetType                     -
Project Budget Type, Mandatory
Allowed Values:
tppdm.bdtp.struct.budget - Element
tppdm.bdtp.activity.budget - Activity
The option Element is applicable only if an element
budget is available for the selected project.
The option Activity is applicable only if a bottom-up
activity budget is linked to the selected project.
iExchangeRateType                       -
Exchange Rate Type, Optional
The exchange rate type used for the project.
iUseBudgetLineDate                      -
Use Budget Line Date, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
This option field indicates whether to consider the budget
line date for the exchange rate date for the budget
cost analysis.
iRateDate                       -
Rate Date, Optional
The fields is applicable when Use Budget Line Date
is set to No
The date and time considered to calculate the exchange
rate for the budget cost analysis.
iIncludeBudgetCostStatusFree            -
Include Budget Cost Budget With Free Status, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
This option field indicates whether to include the
budget lines with the status Free in the budget cost
analysis.
iIncludeBudgetCostStatusActual          -
Include Budget Cost Budget With Actual Status, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
This option field indicates whether to include the
budget lines with the status Actual in the budget
cost analysis.
iIncludeBudgetCostStatusFinal           -
Include Budget Cost Budget With Final Status, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
This option field indicates whether to include the
budget lines with the status Final in the budget cost
analysis.
iIncludeBudgetCostExtension             -
Include Extension to Budget Cost, Mandatory
Allowed Values:
tppdm.yeno.yes  - Yes
tppdm.yeno.no   - No
This option field indicates whether to include extension
budget cost in the budget cost analysis.
iIncludeBudgetCostContingency           -
Include Cost Contingency Amount to Budget Cost, Mandatory
Allowed Values:
tcyesno.yes     - Yes
tcyesno.no      - No
This option field indicates whether to include contingency
amount of the bottom-up budget in the budget cost analysis.
Output:
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successful
<> 0                    - An error occurred
```
