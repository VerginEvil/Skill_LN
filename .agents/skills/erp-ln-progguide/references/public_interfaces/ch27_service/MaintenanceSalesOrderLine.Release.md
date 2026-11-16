# MaintenanceSalesOrderLine.Release

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1496-1498

```baan
DLL:   tsextmscapi
This function is available from 2025.05 (KB3567472).
Syntax: long MaintenanceSalesOrderLine.Release(
domain  tcorno           iMaintenanceSalesOrder,
domain  tcpono           iMaintenanceSalesOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to release one specific maintenance sales order
line (tsmsc110 record). See functionality when a
maintenance sales order line is released with the form command
'Release' in sessions:
Maintenance Sales Order - Part Maintenance Lines (tsmsc1110m100);
Maintenance Sales Order - Part Loan Lines (tsmsc1110m200);
Maintenance Sales Order - Part Delivery Lines (tsmsc1110m300);
Maintenance Sales Order - Part Receipt Lines (tsmsc1110m400).
If the complete action does not succeed, this function will
return a value unequal zero.
If completing succeeds then the value zero is returned.
This function does its own database handling, so before
calling this function the existing database transactions should
either have been aborted or committed.
This is necessary because the system will execute the blocking
checks and if the order gets blocked, the blocking flag on
header level is set and committed and the release action will
fail.
If return warehouse orders are created, then the system will
at the end also process the warehouse activities which are set
to automatic.
Note:
- When a maintenance sales order line is released for a
maintenance sales order with the status free, the maintenance
sales order is also released. If that fails, the release of
the maintenance sales order line is aborted.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   If the order gets blocked, the blocking flag is set on header
level.
If return warehouse orders are created and warehouse activities
have been set to Automatic, these are executed.
If the maintenance sales order of the line that is released
has the status free when trying to release the maintenance sales
order line, the maintenance sales order is also released.
Input:  iMaintenanceSalesOrder
The maintenance sales order number for the maintenance
sales order line that needs to be released.
Mandatory input.
iMaintenanceSalesOrderLine
The maintenance sales order line that needs to be
released.
Mandatory input.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       -       No Error and the status of the given
maintenance sales order line changed to released.
<> 0    -       The status of the maintenance sales order line
could not be changed to released.
```
