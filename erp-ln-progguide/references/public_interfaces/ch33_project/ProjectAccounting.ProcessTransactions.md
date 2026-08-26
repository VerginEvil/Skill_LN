# ProjectAccounting.ProcessTransactions

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectAccounting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1712-1715

```baan
DLL:   tpextppcapi
This function is available from     2024.03 (KB2280409  ).
Syntax: long ProjectAccounting.ProcessTransactions(
domain  tccprj           iProject,
domain  tclogn           iFromUser,
domain  tclogn           iToUser,
domain  tpdate           iFromRegistrationDate,
domain  tpdate           iToRegistrationDate,
domain  tppdm.yeno       iPrimaryInterimResults,
domain  tppdm.yeno       iAlternateInterimResults,
domain  tppdm.yeno       iBalance,
domain  tppdm.yeno       iFinalResult,
domain  tppdm.yeno       iUpdateCostControl,
domain  tpdate           iRegistrationDate,
domain  tppdm.yeno       iMaterialCommitments,
domain  tppdm.yeno       iMaterialProjectControl,
domain  tppdm.yeno       iMaterialPurchaseInvoice,
domain  tppdm.yeno       iLaborSubcontractingHours,
domain  tppdm.yeno       iLaborProjectControl,
domain  tppdm.yeno       iLaborPurchaseInvoice,
domain  tppdm.yeno       iEquipmentCommitments,
domain  tppdm.yeno       iEquipmentProjectControl,
domain  tppdm.yeno       iEquipmentPurchaseInvoice,
domain  tppdm.yeno       iSubcontractingCommitments,
domain  tppdm.yeno       iSubcontractingProjectControl,
domain  tppdm.yeno       iSubcontractingPurchaseInvoice,
domain  tppdm.yeno       iSundryCommitments,
domain  tppdm.yeno       iSundryProjectControl,
domain  tppdm.yeno       iSundryPurchaseInvoice,
domain  tppdm.yeno       iRevenueProjectControl,
domain  tppdm.yeno       iRevenueProjectInvoice,
domain  tppdm.yeno       iRevenueSalesInvoice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function can be used to post confirmed transactions to
the project cost ledger and to Financials (on the basis of the
accounts that are selected in the Financials Integration).
Costs are transferred to Invoicing and project history.
This function offers similar functionality as session
Process Transactions(tpppc4802m000).
Be aware that transaction management is handled within this function.
Note: This function should be called for one project at a time.
Pre:    None.
Post:   None
Input:  iProject                              - Project. Mandatory
iFromUser                                     - From User. Optional
iToUser                                       - To User. Mandatory
iFromRegistrationDate                         - From Registration Date. Optional
iToRegistrationDate                           - To Registration Date. Mandatory
iPrimaryInterimResults                        -
PrimaryInterimResults (Yes/No).Mandatory.
If it is Yes, then interim result for
the primary scenario is posted to
Financials
iAlternateInterimResults                      -
AlternateInterimResults (Yes/No). Mandatory.
If it is yes, then interim result for
the alternate scenario is finalized.
The result is not posted to Financials.
iBalance                                      - Balance (Yes/No). Mandatory.
If it is Yes, then the WIP balance of
the project is processed
iFinalResult                                  - Final Result (Yes/No). Mandatory.
If yes, the financial results are
processed to Financials for the project
with status Finished and with the
financial result status set to
Determine Result. The project status is
set to Closed.
iUpdateCostControl                            - Update Cost Control (Yes/No). Mandatory.
If yes, build actual cost control is
performed for the project
iRegistrationDate                             - Registration Date. Optional
The Registration Date for the
transactions is only used when
Final Result is yes.
iMaterialCommitments                          -
Material Commitments (Yes/No). Mandatory.
iMaterialProjectControl                       -
Material Project Control (Yes/No). Mandatory.
iMaterialPurchaseInvoice                      -
Material Purchase Invoice (Finance) (Yes/No).
Mandatory.
iLaborSubcontractingHours                      -
Labor Subcontracting Hours (Yes/No). Mandatory.
iLaborProjectControl                          -
Labor Project Control. (Yes/No). Mandatory.
iLaborPurchaseInvoice                         -
Labor Purchase Invoice (Finance) (Yes/No).
Mandatory.
iEquipmentCommitments                         -
Equipment Commitments (Yes/No). Mandatory.
iEquipmentProjectControl                      -
Equipment Project Control (Yes/No). Mandatory.
iEquipmentPurchaseInvoice                      -
Equipment Purchase Invoice (Finance) (Yes/No).
Mandatory.
iSubcontractingCommitments                       -
Subcontracting Commitments (Yes/No). Mandatory.
iSubcontractingProjectControl                       -
Subcontracting Project Control (Yes/No).
Mandatory.
iSubcontractingPurchaseInvoice                      -
Subcontracting Purchase Invoice(Finance)(Yes/No).
Mandatory.
iSundryCommitments                            -
Sundry Cost Commitments (Yes/No). Mandatory.
iSundryProjectControl                         -
Sundry Project Control (Yes/No). Mandatory.
iSundryPurchaseInvoice                        -
Sundry Purchase Invoice (Finance) (Yes/No).
Mandatory.
iRevenueProjectControl                        -
Revenue Project Control (Yes/No). Mandatory.
iRevenueProjectInvoice                        -
Revenue Project Invoice (Yes/No). Mandatory.
iRevenueSalesInvoice                          -
Revenue Sales Invoice (Finance) (Yes/No).
Mandatory.
Output: oExceptionMessage                     -
The last message if the return value is not
equal to 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID                                  -
An ID that refers to all error information.
Use the functions in Exception to get all
relevant information.
Return: 0                             - Process Transaction completed successfully.
<> 0                                  - Error.
```

## Public Interfaces for

## ProjectCostingBreaksServiceActivities

The following functions are available: ProjectCostingBreaksServiceActivities.StartOverview
