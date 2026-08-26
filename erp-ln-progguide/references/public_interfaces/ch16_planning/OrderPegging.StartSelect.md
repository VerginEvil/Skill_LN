# OrderPegging.StartSelect

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for OrderPegging
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 593-595

```baan
DLL:   cpextrrpapi
This function is available from     2024.12 (KB3531509  ).
Syntax: long OrderPegging.StartSelect(
long             iStartMode,
domain  cpcom.plnc       iScenario,
domain  cpstream         iStreamingMethod,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the process session Browse Order
Pegging (cprrp0740m000). This function makes use of a
Processing Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete().
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session.(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
iScenario               Planning Scenario (Mandatory).
iStreamingMethod        Streaming Method.
iOrderType              Order Type.
iOrderNumber            Order Number.
iProcessingOptionSet    A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create().
If 0, then user default/session
default values are applied.
Processing Options have a direct relationship with the form fields
on session Browse Order Pegging (cprrp0740m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Browse Order Pegging options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                            TYPE                    DEFAULT
SetEffectivityUnit              domain  tcyesno         tcyesno.no
EffectivityUnit                 domain  tcuef.effn      0
SetPlanner                      domain  tcyesno         tcyesno.no
Planner                         domain  tcemno          ""
SetPlanItem                     domain  tcyesno         tcyesno.no
PlanItem                        domain  cpitem          ""
SetWorkCenter                   domain  tcyesno         tcyesno.no
WorkCenter                      domain  tccwoc          ""
SetProjectPCS                   domain  tcyesno         tcyesno.no
ProjectPCS                      domain  tccprj          ""
SetProductionOrderGroup         domain  tcyesno         tcyesno.no
ProductionOrderGroup            domain  tccprj          ""
SetPlannedOrderGroup            domain  tcyesno         tcyesno.no
PlannedOrderGroup               domain  tccprj          ""
SetOrderType                    domain  tcyesno         tcyesno.no
FromOrderNumber                 domain  cporno          iOrderNumber
ToOrderNumber                   domain  cporno          "ZZZZZZZZZ"
SetBuyFromBusinessPartner       domain  tcyesno         tcyesno.no
BuyFromBusinessPartner          domain  tccom.bpid      ""
ShipFromBusinessPartner         domain  tccom.bpid      ""
SetSoldToBP                     domain  tcyesno         tcyesno.no
SoldToBP                        domain  tccom.bpid      ""
ShipToBP                        domain  tccom.bpid      ""
SetProjectPeg                   domain  tcyesno         tcyesno.no
Project                         domain  tccprj          ""
Element                         domain  tccspa          ""
Activity                        domain  tccact          ""
FromDate                        domain  tcdate          0
ToDate                          domain  tcdate          max value of domain
CriticalBranches                domain  tcyesno         tcyesno.no
CriticalPriority                domain  cprao.prio      0
AnalyzeWhereUsedQuantity        domain  tcyesno         tcyesno.no
ExpandedLevels                  domain  tcsrnb          2
PrintProjectPeg                 domain  tcyesno         tcyesno.no
PrintOptionList                 domain  tcyesno         tcyesno.no
PrintEffectivityUnit            domain  tcyesno         tcyesno.no
PrnitExceptionMessages          domain  tcyesno         tcyesno.no
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started succesfully.
<> 0                    Otherwise.
```

## Public Interfaces for Specification

The following functions are available: Specification.StartDetail
