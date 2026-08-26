# Warehousing.StartAutomaticOutboundProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Warehousing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 983-984

```baan
DLL:   whextinhapi
This function is available from     2025.03 (KB3541337  ).
Syntax: long Warehousing.StartAutomaticOutboundProcessing(
ref             boolean          oNotificationsFound,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will start the processing of the next
automatic outbound activity for the notified outbound object.
This public interface will be able to automatically perform
the next automatic steps. This public interface will stop the
automatic process when the next activity is not set to
automatic.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  N.a.
Output: oNotificationsFound                   - Outbound Notifications to be processed
are found.
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

## Public Interfaces for StockPoint

The following functions are available: StockPoint.CheckBlocking StockPoint.Move StockPoint.PackHandlingUnits
