# ServiceOrderActivity.ProcessReturnDeliveries

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1447-1448

```baan
DLL:   tsextsocapi
This function is available from     2022.05 (KB2235890  ).
Syntax: long ServiceOrderActivity.ProcessReturnDeliveries(
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to start the process of creating
Return Deliveries for service order material lines linked to
the service order activity.
If all material lines related to the service order have to be
done, then iActivityLine must be 0.
If only for a specific activity line number this process has to
be executed then specify the iActivityLine with an existing
activity line number.
Note that because of the possibility that for return warehouse
orders, some warehouse activities might have been set to
automatic, the system will commit the database transactions in
this function. This means that it is not necessary to set a
db.retry.point() before calling this function and abort/commit
after this function, because that is already handled within
this function.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   If warehouse procedures have been set to automatic, then these
are executed.
Input:  iServiceOrder                         - Service Order: Mandatory
iActivityLine                                 - Service Order Activity: Not mandatory
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No Error
<> 0                                          - Error
```
