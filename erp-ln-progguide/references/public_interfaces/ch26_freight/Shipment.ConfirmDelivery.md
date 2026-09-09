# Shipment.ConfirmDelivery

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for Shipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1336-1337

```baan
DLL:   fmextlbdapi
This function is available from 2019.05 (KB2050777).
Syntax: long Shipment.ConfirmDelivery(
domain  tcorno           iShipment,
domain  tcdate           iActualLoadDate,
domain  tcdate           iActualUnloadDate,
domain  fmlbd.conv       iShippedOrCompleted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to set the status of the
shipment and it's shipment lines to Shipped or Completed, based
on the iShippedOrCompleted indicator.
Pre:    This Public Interface will update records and as such must be
called within a transaction.
When implementing this Public Interface, please be aware of the
performance aspect. In standard, this functionality will have
it's own transaction management, while the Public Interface does
not!. Therefore it is strongly advisable to call this Public
Interface inside a seperate transaction and after returning
directly perform the abort in case of errors and the commit in
case this function returns 0. Long logical transaction must be
prevented as records will be locked and are not available for
other transactions!
Post:   Exception handling can be done, when needed.
Input:  iShipment               - Shipment: Mandatory
iActualLoadDate         - Actual Load Date: Mandatory when
iShippedOrComplete is set to Shipped
iActualUnloadDate       - Actual Unload Date: Mandatory when
iShippedOrComplete is set to Complete
iShippedOrCompleted     - Confirm the delivery of the Shipment
to either Shipped (fmlbd.conv.shipped)
or Completed (fmlbd.conv.completed)
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
