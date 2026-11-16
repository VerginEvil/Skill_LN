# ProjectAccounting.GenerateInterimResults

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectAccounting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1726-1729

```baan
DLL:   tpextppcapi
This function is available from 2025.04 (KB3568308).
Syntax: long ProjectAccounting.GenerateInterimResults(
domain  tpctm.rrby       iCalculateResultsFor,
domain  tccono           iFromContract,
domain  tccono           iToContract,
domain  tpctm.cnln       iFromContractLine,
domain  tpctm.cnln       iToContractLine,
domain  tccprj           iFromProject,
domain  tccprj           iToProject,
domain  tppdm.yeno       iGenerateResultTypeRevenues,
domain  tppdm.cprv       iFinancialResultRevenue,
domain  tppdm.yeno       iGenerateResultTypeCosts,
domain  tppdm.cprv       iFinancialResultCost,
domain  tppdm.yeno       iGenerateResultTypeBalances,
domain  tppdm.yeno       iPrimaryInterimResults,
domain  tppdm.yeno       iAlternateInterimResults,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This public interface can be used to generate interim results
for the project, contract or contract line specified in the
cost, commitments and cost forecasts and the anticipated
revenues and revenue forecast sessions. You can generate
interim results by either contract or project but not
simultaneously. This function offers similar functionality as
session Generate Interim Results(tpppc3250m000).
Be aware that transaction management is handled within this
function.
Pre:    N.A
Post:   N.A
Input:  iCalculateResultsFor        - Contract/Project. Optional
Default Value: Contract
iFromContract               - From Contract. Optional
iToContract                 - To Contract. Optional
iFromContractLine           - From Contract Line. Optional
iToContractLine             - To Contract Line. Optional
iFromProject                - From Project. Optional
iToProject                  - To Project. Optional
iGenerateResultTypeRevenues -
Generate Result Type Revenues (Yes/No). Mandatory
iFinancialResultRevenue     -
Financial Result Revenue.
Mandatory if iGenerateResultTypeRevenues is Yes.
Otherwise Optional.
iGenerateResultTypeCosts    -
Generate Result Type Costs (Yes/No). Mandatory
iFinancialResultCost        -
Financial Result Cost.
Mandatory if iFinancialResultCost is Yes.
Otherwise Optional.
iGenerateResultTypeBalances -
Generate Result Type Balances (Yes/No). Mandatory
iPrimaryInterimResults      -
Primary Interim Results (Yes/No). Mandatory
iAlternateInterimResult     -
Alternate Interim Results (Yes/No). Mandatory
Note :  1) When iCalculateResultsFor is 'By Contract' then
iFromContract,iToContract,iFromContractLine and
iToContractLine arguments will be considered.
2) When iCalculateResultsFor is 'By Project' then
iFromProject and iToProject will be considered.
1) iFinancialResultRevenue is mandatory when
iGenerateResultTypeRevenues is Yes.
2) iFinancialResultCost is mandatory when
iGenerateResultTypeCosts is Yes.
iProcessingOptionSet -
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Interim Results (tpppc3250m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Generate Interim Results options which are not available as
Processing Options will get defaulted in accordance with the session
logic.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
FromExtension                   domain tpptc.cstl       Minimum Value
ToExtension                     domain tpptc.cstl       Maximum Value
FromCostControlYear             domain tcccp.yrno       Minimum Value
FromCostControlPeriod           domain tcccp.peri       Minimum Value
ToCostControlYear               domain tcccp.yrno       Maximum Value
ToCostControlPeriod             domain tcccp.peri       Maximum Value
FromFiscalYear                  domain tcccp.yrno       Minimum Value
FromFiscalPeriod                domain tcccp.peri       Minimum Value
ToFiscalYear                    domain tcccp.yrno       Maximum Value
ToFiscalPeriod                  domain tcccp.peri       Maximum Value
RevenueResultDescription        domain tppdm.desc       Revenue Result Description
CostResultDescription           domain tppdm.desc       Cost Result Description
RevenuePercentageOfCompletion   domain tppdm.yeno       tppdm.yeno.yes
RevenueMilestones               domain tppdm.yeno       tppdm.yeno.yes
RevenueReimbursement            domain tppdm.yeno       tppdm.yeno.yes
RevenueEarnedRevenueFactor      domain tppdm.yeno       tppdm.yeno.yes
RevenueActualRevenues           domain tppdm.yeno       tppdm.yeno.yes
CostPercentageOfCompletion      domain tppdm.yeno       tppdm.yeno.yes
CostProfitPercentage            domain tppdm.yeno       tppdm.yeno.yes
CostReimbursement               domain tppdm.yeno       tppdm.yeno.yes
FiscalPeriodSelection           domain tcyesno          tcyesno.no
FiscalPeriodType                domain tppdm.ofps       tppdm.ofps.previous
FiscalPeriodForDate             domain tcdate           Current Date
ManualFiscalYear                domain tcccp.yrno       Year of Previous Period
ManualFiscalPeriod              domain tcccp.peri       Previous Period
RegistrationDate                domain tpdate           Current Date and Time
PostToCostControlYear           domain tcccp.yrno       Registration Date Year
PostToCostControlPeriod         domain tcccp.peri       Registration Date Period
MaterialCosts                   domain tppdm.yeno       tppdm.yeno.yes
MaterialCommitments             domain tppdm.yeno       tppdm.yeno.yes
MaterialForecast                domain tppdm.yeno       tppdm.yeno.no
LaborCosts                      domain tppdm.yeno       tppdm.yeno.yes
LaborForecast                   domain tppdm.yeno       tppdm.yeno.no
EquipmentCosts                  domain tppdm.yeno       tppdm.yeno.yes
EquipmentCommitments            domain tppdm.yeno       tppdm.yeno.yes
EquipmentForecast               domain tppdm.yeno       tppdm.yeno.no
SubcontractingCosts             domain tppdm.yeno       tppdm.yeno.yes
SubcontractingCommitments       domain tppdm.yeno       tppdm.yeno.yes
SubcontractingForecast          domain tppdm.yeno       tppdm.yeno.no
SundryCosts                     domain tppdm.yeno       tppdm.yeno.yes
SundryCommitments               domain tppdm.yeno       tppdm.yeno.yes
SundryForecast                  domain tppdm.yeno       tppdm.yeno.no
OverheadCosts                   domain tppdm.yeno       tppdm.yeno.yes
OverheadForecast                domain tppdm.yeno       tppdm.yeno.no
Revenues                        domain tppdm.yeno       tppdm.yeno.yes
ExpectedRevenues                domain tppdm.yeno       tppdm.yeno.yes
ForecastRevenues                domain tppdm.yeno       tppdm.yeno.yes
SettlePreviousFinancialResult   domain tppdm.yeno       tppdm.yeno.yes
AggregateByProjectExtension     domain tppdm.yeno       tppdm.yeno.yes
SkipLinesWithEmptyAmounts       domain tppdm.yeno       tppdm.yeno.yes
IncludeAdvancePaymentsInRevenue domain tppdm.yeno       tppdm.yeno.no
Output: oExceptionMessage       -
The last message if the return value is not
equal to 0.
If more than one  message is given,
these are present in the oExceptionID.
oExceptionID            -
An ID that refers to all error information.
Use the functions in Exception to get all
relevant information.
Return: 0               - Process Transaction completed successfully.
<> 0            - Error.
```
