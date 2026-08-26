# StorageList.SplitAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for StorageList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1255-1255

```baan
DLL:   whextinhapi
This function is available from     2023.07 (KB2288171  ).
Syntax: long StorageList.SplitAdvice(
domain  tcorno           iInboundAdvice,
domain  tcpono           iInboundAdviceLine,
ref     domain  tcpono           oNewInboundAdviceLine,
ref     domain  whinh.lino       oNewStorageSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will split the given storage list.
Pre:    db.retry.point must be set.
Post:   Commit the transaction in case of success.
Abort the transaction in case of failure.
Input:  iInboundAdvice                        - Mandatory
iInboundAdviceLine                            - Mandatory
Output: oNewInboundAdviceLine                 - Created Inbound Advice Line.
oNewStorageSequence                           - Created Storage Sequence
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
