# PlannedPRPOrders.StartGenerate

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for PlannedPRPOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1742-1743

```baan
DLL:   tpextpssapi
This function is available from 2024.07 (KB3503140).
Syntax: long PlannedPRPOrders.StartGenerate(
long             iStartMode,
domain  tccprj           iFromProject,
domain  tccprj           iToProject,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Generate Planned PRP Orders
(tppss6200m000).
Pre:    N.A
Post:   N.A
Input:  iStartMode              - Not Used.
iFromProject            - From Project selection field is filled with this
value. Optional
iToProject              - To Project selection field is filled with this
value. Optional
iProcessingOptionSet    - Optional
if 0, the default session options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Planned PRP Orders (tppss6200m000) are
not explained in further detail here. Please refer to the session help
for additional  information. Generate Planned PRP Orders session options
which are not available as Processing Options will get defaulted in
accordance with the session logic.
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
PrintWarnings                       domain  tppdm.yeno tppdm.yeno.yes
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
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
