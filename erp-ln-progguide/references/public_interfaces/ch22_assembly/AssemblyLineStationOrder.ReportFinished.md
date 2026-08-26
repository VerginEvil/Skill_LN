# AssemblyLineStationOrder.ReportFinished

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyLineStationOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 858-859

```baan
DLL:   tiextascapi
This function is available from     2020.12 (KB2163912  ).
Syntax: long AssemblyLineStationOrder.ReportFinished(
domain  tcsite           iSite,
domain  tcorno           iAssemblyOrder,
domain  tccwoc           iLineStation,
domain  tiutcs           iActualCompletionTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to report a Line Station Order
as Finished, as in session tiasl6510m000.
Transaction management (retry point, commit/rollback) is
handled within in this function, because also the created
inbound warehouse orders are processed in this function.
Inbound warehouse orders are only created when the last
line station of the order is finished.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:  iSite                   Not used
iAssemblyOrder          Assembly Order (mandatory).
iLineStation            Line Station (mandatory).
iActualCompletionTime   Actual Completion Time (mandatory).
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Report as Finished is successfully completed
<> 0                    Report as Finished is not completed
```
