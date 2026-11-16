# ProductionOrder.Release

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 752-753

```baan
DLL:   tiextsfcapi
This function is available from 2021.03 (KB2165373).
Syntax: long ProductionOrder.Release(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface releases the given Production Order.
In case Electronic Signature is required this function cannot
be used.
In case a check on shortages must be done before releasing the
production order, public interface function
ProductionOrder.CheckShortages can be called first.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Production Order released successfully
<> 0                    Otherwise
```
