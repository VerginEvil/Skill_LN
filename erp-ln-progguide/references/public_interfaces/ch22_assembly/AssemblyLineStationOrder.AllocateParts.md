# AssemblyLineStationOrder.AllocateParts

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyLineStationOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 867-868

```baan
DLL:   tiextascapi
This function is available from 2020.12 (KB2163912).
Syntax: long AssemblyLineStationOrder.AllocateParts(
domain  tcsite           iSite,
domain  tcorno           iAssemblyOrder,
domain  tccwoc           iLineStation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to allocate parts (= build or rebuild
the Assembly Part Requirements) for the specified Assembly
Order and Line Station.
Errors that occur during the actual allocation of the
parts are logged in the Assembly Messages table (session
tiasc0501m000), but also included in oExceptionID.
oExceptionMessage and oExceptionID will also indicate if
messages are logged.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Not used
iAssemblyOrder          Assembly Order (mandatory).
iLineStation            Line Station (mandatory).
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Allocate Parts was completed without any
messages in the Assembly Messages table.
<> 0                    Allocate Parts could not be completed, or
was completed with messages logged in
the Assembly Messages table.
Use session Assembly Messages
(tiasc0501m000) to view the messages.
```
