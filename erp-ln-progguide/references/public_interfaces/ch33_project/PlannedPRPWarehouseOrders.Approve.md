# PlannedPRPWarehouseOrders.Approve

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for PlannedPRPWarehouseOrders
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1725-1726

```baan
DLL:   tpextpssapi
This function is available from     2024.08 (KB3518771  ).
Syntax: long PlannedPRPWarehouseOrders.Approve(
domain  tccprj           iProject,
domain  tcorno           iFromPlannedOrder,
domain  tcorno           iToPlannedOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to approve planned
PRP (Project Requirements Planning)
warehouse orders for a single project, so that they can be
transferred.
This function offers similar functionality as
session (tppss6225m000                       - Approve Planned PRP Warehouse Orders).
Note: Be aware that transaction management is handled within
this function.
Pre:    N.A
Post:   N.A
Input:  iProject                                - Project. Mandatory
iFromPlannedOrder                               - From Planned Order. Optional
iToPlannedOrder                                 - To Planned Order. Optional
iProcessingOptionSet                       -
Optional, if 0, the default options are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Approved Planned PRP Warehouse Orders (tppss6225m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Approved Planned PRP Warehouse Orders options which are not
available as Processing Options
will get defaulted in accordance with the session logic.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
DeliveryTypeFrom                domain tppss.delt       tppss.delt.wp
DeliveryTypeTo                  domain tppss.delt       tppss.delt.pwb
PlannedOrderDateFrom            domain tppdm.date       Minimum Value
PlannedOrderDateTo              domain tppdm.date       Maximum Value
PlannedDeliveryDateFrom         domain tppdm.date       Minimum Value
PlannedDeliveryDateTo           domain tppdm.date       Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
ProjectWarehouseFrom            domain tccwar           Minimum Value
ProjectWarehouseTo              domain tccwar           Maximum Value
OrderStatusFrom                 domain tppss.osta       tppss.osta.planned
OrderStatusTo                   domain tppss.osta       tppss.osta.firm.planned
CostControlElementFrom          domain tppdm.cspa       Minimum Value
CostControlElementTo            domain tppdm.cspa       Maximum Value
CostControlActivityFrom         domain tppdm.cact       Minimum Value
CostControlActivityTo           domain tppdm.cact       Maximum Value
CostControlExtensionFrom        domain tpptc.cstl       Minimum Value
CostControlExtensionto          domain tpptc.cstl       Maximum Value
ItemInProjectFrom               domain tcitem           Minimum Value
ItemInProjectTo                 domain tcitem           Maximum Value
ItemInWarehousingFrom           domain tcitem           Minimum Value
ItemInWarehousingTo             domain tcitem           Maximum Value
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successful
<> 0                                          - An error occurred
```
