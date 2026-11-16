# ProjectBudget.GetTotalBudgetAmountOfProject

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectBudget
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1720-1721

```baan
DLL:   tpextptcapi
This function is available from 2025.10 (KB3559609).
Syntax: long ProjectBudget.GetTotalBudgetAmountOfProject(
domain  tccprj           iProject,
domain  tpptc.ccal       iActualCostCalculationCode,
domain  tppdm.bdtp       iBudgetBy,
domain  tcyesno          iProjectTotalOnly,
ref     domain  tcamnt           oTotalBudgetAmount(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionId )
Usage:        Expl:   This Public Interface uses the Budgeted Project Costs
(tpptc3540m000) session to calculate the overall budget amount.
As a prerequisite, the Generate Budget Cost Analysis should
have been executed.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iProject                        - Project. Mandatory
iActualCostCalculationCode      - Actual Cost Calculation
Code. Optional
iBudgetBy                       - Budget By. Mandatory
Possible Values are:
tppdm.bdtp.struct.budget - Element
tppdm.bdtp.activity.budget - Activity
iProjectTotalOnly               - Project Total Only. Mandatory
Possible Values are:
tcyesno.yes - Yes
tcyesno.no  - No
if iProjectTotalOnly is Yes, then the budget amount
of only this project will be considered. It will not
consider budget amounts of subprojects even if the
project type is 'MainProject'
if iProjectTotalOnly is No, then the budget amount of
this project along with its subprojects will be
considered.
Output: oTotalBudgetAmount              - Array of Total Budget Amount
The following are the different currencies in which amounts are
retrieved:
1) Project Currency
2) Local Currency
3) Reporting Currency 1
4) Reporting Currency 2
oExceptionMessage               - The last message if any
message is found. If more than
one message is given, these
are present in the
oExceptionID.
oExceptionID                    - An ID that refers to the
exception information. Use the
functions in Exception to get
all relevant information.
Return: N.A
```
