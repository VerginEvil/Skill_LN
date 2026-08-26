# ServiceOrderMaterialCosts.ProcessReturnDeliveries

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderMaterialCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1454-1455

```baan
DLL:   tsextsocapi
This function is available from     2022.11 (KB2262498  ).
Syntax: long ServiceOrderMaterialCosts.ProcessReturnDeliveries(
domain  tcorno           iServiceOrder,
domain  tcpono           iMaterialLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to start the process of creating
a Return Delivery for a Service Order Material line.
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
Input:  iServiceOrder                 - Service Order: Mandatory
iMaterialLine                         - Service Order Material Line: Mandatory
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
