# Load.ConfirmDelivery

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for Load
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1335-1336

```baan
DLL:   fmextlbdapi
This function is available from 2019.05 (KB2050777).
Syntax: long Load.ConfirmDelivery(
domain  tcorno           iLoad,
domain  tcdate           iActualLoadDate,
domain  tcdate           iActualUnloadDate,
domain  fmlbd.conv       iShippedOrCompleted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to set the status of the load
and it's shipments and shipment lines to Shipped or Completed,
based on the iShippedOrCompleted indicator.
Pre:    This Public Interface will update records and as such must be
called within a transaction!
When implementing this Public Interface, please be aware of the
performance aspect. In standard, this functionality will have
it's own transaction management, while the Public Interface does
not!. Therefore it is strongly advisable to call this Public
Interface inside a seperate transaction and after returning
directly perform the abort is case of errors and the commit in
case this function returns 0. Long logical transaction must be
prevented as records will be locked and are not available for
other transactions!
Post:   Exception handling can be done, when needed.
Input:  iLoad                   - Load: Mandatory
iActualLoadDate         - Actual Load Date: Mandatory when
iShippedOrComplete is set to Shipped
iActualUnloadDate       - Actual Unload Date: Mandatory when
iShippedOrComplete is set to Complete
iShippedOrCompleted     - Confirm the delivery of the Load to
either Shipped (fmlbd.conv.shipped) or
Completed (fmlbd.conv.completed)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Confirm Delivery succeeded
<> 0                    - Error
```
