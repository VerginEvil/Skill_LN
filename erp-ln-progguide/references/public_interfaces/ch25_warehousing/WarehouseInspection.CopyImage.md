# WarehouseInspection.CopyImage

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1262-1263

```baan
DLL:   whextinhapi
This function is available from     2025.03 (KB3540411  ).
Syntax: long WarehouseInspection.CopyImage(
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequenceSource,
domain  tcpono           iInspectionSequenceTarget,
domain  tcguid           iInspectionImageSource,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function copies the image from the source inspection
sequence to the target inspection sequence.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iInspection                           - Mandatory
iInspectionSequenceSource                       - Mandatory
iInspectionSequenceTarget                       - Mandatory
iInspectionImageSource                        - Mandatory
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
