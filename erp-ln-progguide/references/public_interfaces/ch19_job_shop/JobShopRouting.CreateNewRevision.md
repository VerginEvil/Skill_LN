# JobShopRouting.CreateNewRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 661-662

```baan
DLL:   tiextrouapi
This function is available from     2020.11 (KB2158375  ).
Syntax: long JobShopRouting.CreateNewRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tirou.rouc       iJobShopRouting,
domain  tirou.revi       iJobShopRoutingRevision,
ref     domain  tirou.revi       oNewJobShopRoutingRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a new Job Shop Routing revision based on
the given revision.
The operations in the new revision are copied from the set
of operations of the original revision.
Prerequisite: 'Job Shop by Site' is 'In Preparation' or 'Active'
Example usage:
JobShopRouting.CreateNewRevision(
|* Fixed arguments:
site,                                                   --> input
product,                                                --> input
routing                                                 --> input
revision                                                --> input
new.revision                                            --> output
exception.message,                                      --> output
exception.id)                                           --> output
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSite                   Site: Mandatory
iProduct                Product: Mandatory
iJobShopRouting         Job Shop Routing: Mandatory
iJobShopRoutingRevision Job Shop Routing Revision: Mandatory
Output:
oNewJobShopRoutingRevision
Newly created Job Shop Routing Revision
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Success
<> 0                    Failure, exception message is present
```
