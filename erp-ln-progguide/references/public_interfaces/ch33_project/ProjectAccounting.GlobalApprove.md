# ProjectAccounting.GlobalApprove

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectAccounting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1710-1712

```baan
DLL:   tpextppcapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long ProjectAccounting.GlobalApprove(
domain  tccprj           iProject,
domain  tppdm.date       iFromRegistrationDate,
domain  tppdm.date       iToRegistrationDate,
domain  tclogn           iFromUser,
domain  tclogn           iToUser,
domain  tcmcs.str20      iApprovalProcess,
domain  tppdm.yeno       iPrimaryInterimResults,
domain  tppdm.yeno       iAlternateInterimResults,
domain  tppdm.yeno       iFinalResult,
domain  tppdm.yeno       iMaterialCommitments,
domain  tppdm.yeno       iMaterialProjectControl,
domain  tppdm.yeno       iMaterialPurchaseInvoice,
domain  tppdm.yeno       iMaterialCostForecast,
domain  tppdm.yeno       iLaborSubcontractingHours,
domain  tppdm.yeno       iLaborProjectControl,
domain  tppdm.yeno       iLaborPurchaseInvoice,
domain  tppdm.yeno       iLaborCostForecast,
domain  tppdm.yeno       iEquipmentCommitments,
domain  tppdm.yeno       iEquipmentProjectControl,
domain  tppdm.yeno       iEquipmentPurchaseInvoice,
domain  tppdm.yeno       iEquipmentCostForecast,
domain  tppdm.yeno       iSubcontractingCommitments,
domain  tppdm.yeno       iSubcontractingProjectControl,
domain  tppdm.yeno       iSubcontractingPurchaseInvoice,
domain  tppdm.yeno       iSubcontractingCostForecast,
domain  tppdm.yeno       iSundryCommitments,
domain  tppdm.yeno       iSundryProjectControl,
domain  tppdm.yeno       iSundryPurchaseInvoice,
domain  tppdm.yeno       iSundryCostForecast,
domain  tppdm.yeno       iOverheadCostForecast,
domain  tppdm.yeno       iRevenueProjectControl,
domain  tppdm.yeno       iRevenueProjectInvoice,
domain  tppdm.yeno       iRevenueSalesInvoice,
domain  tppdm.yeno       iPhysicalProgressElements,
domain  tppdm.yeno       iPhysicalProgressActivities,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    Use this function to globally confirm costs, revenue
transactions, and interim results.
Costs are transferred to Invoicing and the project history.
You can also use this session to undo confirm transactions.
This function offers similar functionality as session
Global Approving (tpppc4200m000).
Be aware that transaction management is handled within this
function.
Note: This interface will be executed for a single project.
Pre:    None.
Post:   None
Input:  iProject                              - Project. Mandatory
iFromRegistrationDate                         - From Registration Date. Optional
iToRegistrationDate                           - To Registration Date. Mandatory
iFromUser                                     - From User. Optional
iToUser                                       - To User. Mandatory
iApprovalProcess                              - Mandatory
Allowed Values: Approve/ Unapprove
This option indicates if the selected
transactions must be approved or unapproved
iPrimaryInterimResults                        -
PrimaryInterimResults (Yes/No).Mandatory.
iAlternateInterimResults                      -
AlternateInterimResults (Yes/No).Mandatory.
iFinalResult                                  - Final Result (Yes/No). Mandatory.
iMaterialCommitments                          -
Material Commitments (Yes/No). Mandatory.
iMaterialProjectControl                       -
Material Project Control (Yes/No). Mandatory.
iMaterialPurchaseInvoice                      -
Material Purchase Invoice (Finance) (Yes/No).
Mandatory.
iMaterialCostForecast                         -
Material Cost Forecast (Yes/No). Mandatory.
iLaborSubcontractingHours                      -
Labor Subcontracting Hours (Yes/No). Mandatory.
iLaborProjectControl                          -
Labor Project Control. (Yes/No). Mandatory.
iLaborPurchaseInvoice                         -
Labor Purchase Invoice (Finance) (Yes/No).
Mandatory.
iLaborCostForecast                            -
Labor Cost Forecast (Yes/No). Mandatory.
iEquipmentCommitments                         -
Equipment Commitments (Yes/No). Mandatory.
iEquipmentProjectControl                      -
Equipment Project Control (Yes/No). Mandatory.
iEquipmentPurchaseInvoice                      -
Equipment Purchase Invoice (Finance) (Yes/No).
Mandatory.
iEquipmentCostForecast                        -
Equipment Cost Forecast (Yes/No). Mandatory.
iSubcontractingCommitments                       -
Subcontracting Commitments (Yes/No). Mandatory.
iSubcontractingProjectControl                       -
Subcontracting Project Control (Yes/No).
Mandatory.
iSubcontractingPurchaseInvoice                      -
Subcontracting Purchase Invoice(Finance)(Yes/No).
Mandatory.
iSubcontractingCostForecast                       -
Subcontracting Cost Forecast (Yes/No).Mandatory.
iSundryCommitments                            -
Sundry Cost Commitments (Yes/No). Mandatory.
iSundryProjectControl                         -
Sundry Project Control (Yes/No). Mandatory.
iSundryPurchaseInvoice                        -
Sundry Purchase Invoice (Finance) (Yes/No).
Mandatory.
iSundryCostForecast                           -
Sundry Cost Forecast (Yes/No). Mandatory.
iOverheadCostForecast                         -
Overhead Cost Forecast (Yes/No). Mandatory.
iRevenueProjectControl                        -
Revenue Project Control (Yes/No). Mandatory.
iRevenueProjectInvoice                        -
Revenue Project Invoice (Yes/No). Mandatory.
iRevenueSalesInvoice                          -
Revenue Sales Invoice (Finance) (Yes/No).
Mandatory.
iPhysicalProgressElements                      -
Physical Progress Elements (Yes/No). Mandatory.
iPhysicalProgressActivities                      -
Physical Progress Activities (Yes/No). Mandatory.
Output: oExceptionMessage                     -
The last message if the return value is not
equal to 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID                                  -
An ID that refers to all error information.
Use the functions in Exception to get all
relevant information.
Return: 0                             - Global Approve done successfully.
<> 0                                  - Error.
```
