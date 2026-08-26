# ServiceOrder.IssueInventory

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1418-1419

```baan
DLL:   tsextsocapi
This function is available from     2023.10 (KB2307524  ).
Syntax: long ServiceOrder.IssueInventory(
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
domain  tcpono           iMaterialLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to start the process of issuing materials for
a Service Order, Service Order Activity, or Service Order
Material Line.
If all material lines related to the Service Order have to be
done, then pass iActivityLine and iMaterialLine as 0.
If all material lines related to a Service Order Activity have
to be done, then pass iMaterialLine as 0.
If only for a specific material line this process has to
be executed, then pass iServiceOrder and iMaterialLine.
iActivityLine is ignored in this case.
Note that because of the possibility that for warehouse
orders some warehouse activities might have been set to
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
Input:  iServiceOrder
Service Order
Mandatory
iActivityLine
Service Order Activity
Not mandatory
iMaterialLine
Service Order Material Line
Not mandatory
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No Error
<> 0                          - Error
```
