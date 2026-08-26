# OutboundRun.UndoRelease

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundRun
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1200-1201

```baan
DLL:   whextinhapi
This function is available from     2025.12 (KB3613235  ).
Syntax: long OutboundRun.UndoRelease(
domain  whinh.btno       iOutboundRun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function undoes the release outbound advice step for the
advice lines related to the given outbound run which is not yet
picked. The advice is not removed.
This function has its own transaction management. It is not
allowed to call this inside a logical transaction.
When errors occur during the process the errors are visible
in the oExceptionID and the last message is present in
oExceptionMessage.
Pre:    NA
Post:   NA
Input:  iOutboundRun                          - Run Number (Mandatory)
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

## Public Interfaces for QuarantineInventory

The following functions are available: QuarantineInventory.Move QuarantineInventory.StartAutomaticInboundProcessing QuarantineInventory.StartDetail QuarantineInventory.StartDisposition QuarantineInventory.StartOverview
