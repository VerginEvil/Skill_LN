# FreightPlanning.GenerateForSpecificOrderSelection

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for FreightPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1319-1321

```baan
DLL:   fmextlbdapi
This function is available from     2019.08 (KB2070843  ).
Syntax: long FreightPlanning.GenerateForSpecificOrderSelection(
domain  tccwoc           iShippingOffice,
domain  fmfoc.cplg       iPlanningGroup,
domain  fmlbd.algo       iPlanningAlgorithm,
domain  fmlbd.dtdr       iShipmentDatesBasedOn,
domain  fmlbd.rsel       iCarrierSelectionCriterion,
domain  tcmcs.long       iNumberOfSpecificOrders,
ref     domain  tcorno           iSpecificOrders() fixed,
boolean          iSpecificOrderLineSelection,
ref     domain  tcpono           iSpecificOrderLines(),
domain  tcdsca           iPlanningDescription mb,
domain  tcyesno          iPlanningAlgorithmBinding,
domain  tcyesno          iFreightManagementLeadingPlan,
domain  tcyesno          iAllowMeansOfTransportInMultiplePlans,
domain  tcyesno          iCalculateAdditionalCosts,
domain  tcyesno          iReplan,
domain  tcorno           iPlanForReplan,
domain  tcyesno          iOnlyReplanLines,
domain  fmfoc.lnst       iReplanAdditionThroughStatus,
domain  fmlbd.replan     iReplanningMethod,
domain  tcyesno          iCommittedInventoryOnly,
domain  tcyesno          iDetailedPlanningLog,
boolean          iShowProgressIndicator,
ref     domain  tcorno           oPlan,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface allows to generate a freight plan for
a selection of freight orders and lines. It is assumed the
freight orders that are present in the order arrays are having
the status 'Expected' or 'Planned'.
When planning is not possible due to unreachable addresses or
low capacity of transport means, the plan will still be
generated till the stage it fails to plan, this will lead to an
unusable plan, but will allow for user analysis via the planning
log.
This public interface will not print the planning reports which
are printed normaly in the session "Generate Plan"
(fmlbd0280m000). Errors / information messages will be available
in the freight planning log, session "Planning Log"
(fmlbd0530m000).
Pre:    This Public Interface has it's own transaction management, as an
exception to the standard Public Interfaces. As generate plan
can be a long running transaction, the Public Interface should
not lock records too long.
Exception handling can be done when applicable
Post:   N.a.
Input:  iShippingOffice                       - Shipping Office: Mandatory
iPlanningGroup                                - Planning Group: Mandatory
iPlanningAlgorithm                            - Planning Algorithm: Mandatory
Possible values:
-                                                 Direct Shipping (fmlbd.algo.sing)
-                                                 Consolidation (fmlbd.algo.cons)
-                                                 Pooling (fmlbd.algo.pool)
iShipmentDatesBasedOn                         - Shipping Dates based On: Mandatory
Possible values:
-                                                 Earliest of Possible Dates
(fmlbd.dtdr.earliest)
-                                                 Latest of Possible Dates
(fmlbd.dtdr.latest)
-                                                 Minimum of Planned Unload Dates
(fmlbd.dtdr.minimum)
-                                                 Average of Planned Unload Dates
(fmlbd.dtdr.average)
iCarrierSelectionCriterion
-                                               Carrier Selection: Mandatory
Possible values:
-                                                 Cheapest (fmlbd.rsel.cheap)
-                                                 Fastest (fmlbd.rsel.fast)
-                                                 Shortest (fmlbd.rsel.short)
iNumberOfSpecificOrders                       - Number of specific orders in the
specific order array: Mandatory
iSpecificOrders                               - Array containing the freight order
headers for which planning must be
generated.
iSpecificOrderLineSelection                       - Apply specific line selection
This is to be used when specific
freight order lines must be planned,
when complete freight orders are to
be planned it is not required to pass
all the freight order lines.
iSpecificOrderLines                           - Array containing the freight order
lines for which planning must be
generated.
iPlanningDescription                          - Description of the freight plan
iPlanningAlgorithmBinding
-                                               Planning Algorithm Binding, if
planning is not possible for a certain
algorithm, the logic will plan for
other algorithms as well. This flag
can disable that behavior.
iFreightManagementLeadingPlan
-                                               Create a freight management
leading load plan.
iAllowMeansOfTransportInMultiplePlans
-                                               Allow the means of transport to be
planned in multiple plans.
iCalculateAdditionalCosts
-                                               Calculate Additional Costs for
the generated freight plan
iReplan                                       - Replanning
iPlanForReplan                                - Plan for Replanning: Mandatory when
iReplan is set to Yes
iOnlyReplanLines                              - Only Replan Freight Order Lines to
be Replanned.
iReplanAdditionThroughStatus
-                                               Replanning, allow updating of existing
Loads/Shipments till this status.
iReplanningMethod                             - Replanning Method
Possible Values
-                                                 Replan Freight Order Lines Separatly
(fmlbd.replan.separate)
-                                                 Combine with Planned Freight Orders
(fmlbd.replan.combine)
iCommittedInventoryOnly                       - Plan for Committed Inventory Only
iDetailedPlanningLog                          - Plan with the detailed planning log
iShowProgressIndicator                        - Show the progress indicator to the
user, this will give the user an
indication on the process flow and
the time required to complete the
generation of the freight plan.
Output: oPlan                                 - The generated plan
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
