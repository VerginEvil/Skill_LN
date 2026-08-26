# FactoryTrackQuery.CreateRow

> Chapter: Chapter 32 Public Interfaces for Factory Track
>
> Group: Public Interfaces for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1667-1668

```baan
DLL:   brextqryapi
This function is available from     2020.09 (KB2143379  ).
Syntax: long FactoryTrackQuery.CreateRow(
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to create a new output row.
This public interface can only be used in the context of process
extension 'FactoryTrackQuery.QueryExtend' for custom queries.
Example:
long            ReturnValue
ReturnValue = FactoryTrackQuery.CreateRow(
ExceptionMessage,
ExceptionID)
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                                             - Success
<> 0                                          - Failure
```
