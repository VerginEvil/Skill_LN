# WarehouseInspection.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1266-1267

```baan
DLL:   whextinhapi
This function is available from     2021.09 (KB2202105  ).
Syntax: long WarehouseInspection.Process(
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
ref     domain  tcpono           oNewInspectionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the warehouse inspection having status
In Process. This implies either approved or rejected quantities
have been specified which still need to be processed.
If no handling units are present, all inspection lines linked to
the inspection will be processed.
If handling units are present, the inspection lines related to
the handling unit structure are processed.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iInspection                           - Inspection Number (mandatory)
iInspectionSequence                           - Inspection Sequence (mandatory)
Output: oNewInspectionSequence                - New sequence for remainder after
processing a partial inspection
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
