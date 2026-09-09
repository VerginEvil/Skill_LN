# ItemMasterPlan.Generate

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for ItemMasterPlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 542-543

```baan
DLL:   cpextrmpapi
This function is available from 2024.05 (KB2309900).
Syntax: long ItemMasterPlan.Generate(
domain  cpcom.plnc       iScenario,
domain  cpitem           iPlanItem,
long             iPeriodFrom,
long             iPeriodTo,
boolean          iGenerateWithinTimeFence,
boolean          iUpdateGoodsFlow,
boolean          iUpdateExceptionMessages,
boolean          iUpdateResourceMasterPlan,
boolean          iConsiderCapacityConstraints,
boolean          iConsiderMaterialConstraints,
long             iWorkLoadControlIterations,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates a Master Planning for the given Scenario
and Plan Item in the requested period.
Retry point and commit / abort transaction are
executed within this Public Interface.
Pre:    N.A.
Post:   N.A.
Input:  iScenario                       Scenario (Mandatory).
iPlanItem                       Plan Item (Mandatory).
iPeriodFrom                     Period as defined in Scenario
(Mandatory).
iPeriodTo                       Period as defined in Scenario
(Mandatory).
iGenerateWithinTimeFence        Control to allow generation also
within the defined Time Fence.
iUpdateGoodsFlow                Control to update the goods flow
data in the master plan before
generating.
iUpdateExceptionMessages        Control to update the exception
messages for the Plan Item
involved.
iUpdateResourceMasterPlan       Control to update the
Resource Master Plan.
iConsiderCapacityConstraints    When using Workload Control,
whether or not to consider
capacity constraints must be
considered. Can only be set
when workload control is
implemented (cprpd000.iwlc).
iConsiderMaterialConstraints    When using Workload Control,
whether or not to consider
material constraints must be
considered. Can only be set when
workload control is
implemented (cprpd000.iwlc).
iWorkLoadControlIterations      When using Workload Control,
the maximum number of iterations
used to optimize the schedule.
only used when workload control
is implemented (cprpd000.iwlc).
Output: oExceptionMessage               The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID                    An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                               Function completed succesfully.
<> 0                            Error occurred.
```
