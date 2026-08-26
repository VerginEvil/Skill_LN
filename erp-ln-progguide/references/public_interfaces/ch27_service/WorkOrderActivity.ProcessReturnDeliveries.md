# WorkOrderActivity.ProcessReturnDeliveries

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1501-1501

```baan
DLL:   tsextwcsapi
This function is available from     2023.04 (KB2281710  ).
Syntax: long WorkOrderActivity.ProcessReturnDeliveries(
domain  tcorno           iWorkOrder,
domain  tsmdm.acln       iActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to start the process of creating
Return Deliveries for Work Order Material lines linked to
a Work Order Activity.
If all material lines related to the Work Order have to be
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
Input:  iWorkOrder                            - Work Order: Mandatory
iActivityLine                                 - Work Order Activity: Not mandatory
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No Error
<> 0                                          - Error
```
