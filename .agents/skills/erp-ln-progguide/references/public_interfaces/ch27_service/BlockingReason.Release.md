# BlockingReason.Release

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for BlockingReason
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1353-1354

```baan
DLL:   tsextmdmapi
This function is available from 2026.09 (KB3689761).
Syntax: long BlockingReason.Release(
domain  tsmdm.orig       iOrigin,
domain  tcorno           iOrder,
domain  tsmdm.serb       iSequence,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function releases a blocking reason attached to an
order header, unblocking its related order.
Pre:    db.retry.point set
Post:   commit/abort transaction
Input:
iOrigin
Origin / Order Type
Supported Origins are:
tsmdm.orig.call - Call
tsmdm.orig.msc  - Maintenance Sales Order
tsmdm.orig.orno - Service Order or Rental Order
Mandatory.
iOrder
Order
Mandatory.
iSequence
Sequence
If not specified, then all blocking reasons
for the specified order are released.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set.
Currently, no processing options are offered, but this
may change in the future.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       No errors occurred.
<> 0    Error(s) occurred.
```
