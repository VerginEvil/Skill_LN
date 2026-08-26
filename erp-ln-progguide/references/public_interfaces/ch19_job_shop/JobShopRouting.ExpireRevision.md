# JobShopRouting.ExpireRevision

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 662-663

```baan
DLL:   tiextrouapi
This function is available from     2021.12 (KB2219788  ).
Syntax: long JobShopRouting.ExpireRevision(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tirou.rouc       iRouting,
domain  tirou.revi       iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to expire the specified Job Shop
Routing Revision if the specified revision is not already expired.
Both Standard and non                      -Standard Routings can be expired.
Pre:    Job Shop by Site must be In Preparation or Active.
Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory).
iProduct                Product.
iRouting                Routing (mandatory).
iRevision               Revision (mandatory).
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - JS Routing Revision is Expired.
<> 0                                          - JS Routing Revision could not be Expired.
```
