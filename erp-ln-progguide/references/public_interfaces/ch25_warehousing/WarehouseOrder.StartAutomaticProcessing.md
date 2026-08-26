# WarehouseOrder.StartAutomaticProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1023-1024

```baan
DLL:   whextinhapi
This function is available from     2026.04 (KB3657658  ).
Syntax: long WarehouseOrder.StartAutomaticProcessing(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderSet,
ref             boolean          oInboundStarted,
ref             boolean          oOutboundStarted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to start both inbound and
outbound automatic process for the given warehouse order.
This public interface will execute the following steps:
1) Clear any prior notifications done for the automatic process,
within the current process.
2) Notify the warehouse order for automatic processing
3) Start the automatic process for the notified
Warehouse Order
This public interface will stop the automatic process when the
next activity is not set to automatic.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iOrderOrigin                          - Mandatory
iOrderNumber                                  - Mandatory
iOrderSet                                     - Optional
If iOrderSet is 0 (Zero), the automatic
process will be started for all sets
of the order.
Output: oInboundStarted:
True                                          - An automatic inbound process was
started successfully.
False                                         - No automatic inbound process was started.
oOutboundStarted:
True                                          - An automatic outbound process was
started successfully.
False                                         - No automatic outbound process was started.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <>0: Error
```
