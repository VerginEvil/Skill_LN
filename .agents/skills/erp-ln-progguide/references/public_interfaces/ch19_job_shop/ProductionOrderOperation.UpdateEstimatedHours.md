# ProductionOrderOperation.UpdateEstimatedHours

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 805-806

```baan
DLL:   tiextsfcapi
This function is available from 2024.08 (KB2330119).
Syntax: long ProductionOrderOperation.UpdateEstimatedHours(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to update the Estimated Hours record
for the Production Order's operation. When the production
order's estimated costs are not frozen, a programmed update to a
Production Order's Operation may require an update to the
associated Estimated Hours record as well. When the Production
Order setting Update Method for Estimated Hours in section Hours
Settings is Interactive, an update to Estimated Hours will not
be done automatically. In such a case, this function may be be
called to get a required update in Estimated Hours.
Note that in case the Update Method for Estimated Hours setting
is Automatic, this function need not be called.
Transaction management is under control of extender
Pre:    A record of tisfc010 was updated. db.retry.point must be set
Post:   Need to commit or abort the process
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory. Must be in
iSite).
iOperation              Production Order Operation (Mandatory).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Estimated Hours are updated.
<> 0                    Errors occurred.
```
