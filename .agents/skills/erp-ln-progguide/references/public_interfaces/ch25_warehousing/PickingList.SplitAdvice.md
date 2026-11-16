# PickingList.SplitAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PickingList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1269-1270

```baan
DLL:   whextinhapi
This function is available from 2023.07 (KB2288175).
Syntax: long PickingList.SplitAdvice(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
ref     domain  tcpono           oNewAdvice,
ref     domain  whinh.lino       oNewPickingSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will split the given picking list.
Pre:    db.retry.point must be set
Post:   Commit the transaction in case of success.
Abort the transaction in case of failure.
Input:  iOrderOrigin            - Mandatory
iOrderNumber            - Mandatory
iOrderSet               - Optional
iOrderLine              - Optional
iOrderSequence          - Optional
iAdvice                 - Mandatory
Output: oNewAdvice              - Created Outbound Advice.
oNewPickingSequence     - Created Picking Sequence.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
