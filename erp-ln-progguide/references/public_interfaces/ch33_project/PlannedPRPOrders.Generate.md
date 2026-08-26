# PlannedPRPOrders.Generate

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for PlannedPRPOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1721-1723

```baan
DLL:   tpextpssapi
This function is available from     2026.03 (KB3631483  ).
Syntax: long PlannedPRPOrders.Generate(
domain  tccprj           iFromProject,
domain  tccprj           iToProject,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface enables the generation of Planned PRP
(Project Requirements Planning) orders across multiple projects.
The number groups for PRP Warehouse Orders, PRP Purchase Orders,
and Planned Equipment Requests are retrieved from the
Project Planning Parameters session (tppss0100s000).
This function provides capabilities equivalent to those available
in the session (Generate Planned PRP Orders                       - tppss6200m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iFromProject                          - From Project. Optional
iToProject                                    - To Project. Optional
iProcessingOptionSet                          - Optional
if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Planned PRP Orders (tppss6200m000) are
not explained in further detail here. Please refer to the session help
for additional  information. Generate Planned PRP Orders session options
which are not available as Processing Options will get defaulted in
accordance with the session logic.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                               TYPE          DEFAULT
PrpWarehouseOrderSeries             domain  tcseri   <From Project User Profile
if exists, else from the
Project Planning Parameters>
PrpPurchaseOrderSeries              domain  tcseri   <From Project User Profile
if exists, else from the
Project Planning Parameters>
PlannedEquipmentRequestSeries       domain  tcseri   <From Project User Profile
if exists, else from the
Project Planning Parameters>
ProcessOnlyNetChangesinPRPRun       domain  tppdm.yeno tppdm.yeno.no
DeleteFirmPlannedOrders             domain  tppdm.yeno tppdm.yeno.no
ApprovePlannedOrders                domain  tppdm.yeno tppdm.yeno.no
PlannedOrdersTimeFence              domain  tppss.tmfc 0
IgnoreReschedulingMessages          domain  tppdm.yeno tppdm.yeno.no
ReschedulingMessagesTimeFence       domain  tppss.tmfc 1
ApplyOrderQuantityIncrement         domain  tppdm.yeno tppdm.yeno.no
ApplyMinimumOrderQuantity           domain  tppdm.yeno tppdm.yeno.no
ApplyMaximumOrderQuantity           domain  tppdm.yeno tppdm.yeno.no
ApplyFixedOrderQuantity             domain  tppdm.yeno tppdm.yeno.no
UseBudgetCostRateasPurchasePrice    domain  tppdm.yeno tppdm.yeno.no
CopyTextfromBudget                  domain  tppdm.yeno tppdm.yeno.no
CopyTextfromDeliverables            domain  tppdm.yeno tppdm.yeno.no
UseATPPriorities                    domain  tppdm.yeno tppdm.yeno.no
AtpPriority                         domain  tcsern     0
Item                                domain  tppdm.yeno tppdm.yeno.yes
FromItem                            domain  tcitem     <Minimum value>
ToItem                              domain  tcitem     <Maximum value>
Equipment                           domain  tppdm.yeno tppdm.yeno.yes
FromEquipment                       domain  tppdm.cequ <Minimum value>
ToEquipment                         domain  tppdm.cequ <Maximum value>
Subcontracting                      domain  tppdm.yeno tppdm.yeno.yes
FromSubcontracting                  domain  tppdm.csub <Minimum value>
ToSubcontracting                    domain  tppdm.csub <Maximum value>
FromElement                         domain  tppdm.cspa <Minimum value>
ToElement                           domain  tppdm.cspa <Maximum value>
FromActivity                        domain  tppdm.cact <Minimum value>
ToActivity                          domain  tppdm.cact <Maximum value>
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Process successful
<> 0                          - An error occurred
```
