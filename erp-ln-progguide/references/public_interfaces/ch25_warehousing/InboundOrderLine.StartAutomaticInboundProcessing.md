# InboundOrderLine.StartAutomaticInboundProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1082-1084

```baan
DLL:   whextinhapi
This function is available from     2020.05 (KB2117931  ).
Syntax: long InboundOrderLine.StartAutomaticInboundProcessing(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to start the automatic inbound
process for the given inbound order line.
This public interface will allow to start the automatic process
when one of following activities for the inbound order line has
been set to automatic:
Goods Received Note
Warehouse Receipt
This public interface will execute the following steps:
1) Clear any prior notifications done for the automatic inbound
process, within the current process.
2) Notify the inbound order line for automatic processing
3) Start the automatic inbound process for the notified
Inbound Order Line
The way to implement this public interface is to make sure that
the next activity is set to automatic. This can be already set
properly based on the order type setup, or can be achieved by
using public interface
InboundOrderLineActivity.ModifyAutomaticProcessing() for the
activity that should be automatically processed.
See below code example:
---
db.retry.point()
|* Set the activity to automatic
ret = InboundOrderLineActivity.ModifyAutomaticProcessing(..)
if ret <> 0 then
abort.transaction()
return(ret)
endif
commit.transaction()
|* Start the automatic order process
ret.val = InboundOrderLine.StartAutomaticInboundProcessing(..)
db.retry.point()
|* Set the activity to be not automatic
ret = InboundOrderLineActivity.ModifyAutomaticProcessing(..)
if ret <> 0 then
abort.transaction()
return(ret)
endif
commit.transaction()
return(ret.val)
---
This public interface will stop the automatic process when the
next activity is not set to automatic. This only applies when
either the Goods Received Note or the Warehouse Receipt activity
have been handled by this public interface.
When the order line is already received, and for the inbound
line there is no Goods Received Note or Warehouse Receipt to be
done, this public interface will not execute the next automatic
step. The next steps can be executed by one of the following
public interfaces:
ReceiptLine.StartAutomaticInboundProcess
InboundInspection.StartAutomaticInboundProcess
InboundAdvice.StartAutomaticInboundProcess
InboundRun.StartAutomaticInboundProcess
StorageList.StartAutomaticInboundProcess
HandlingUnit.StartAutomaticInboundProcess
QuarantineInventory.StartAutomaticInboundProcess
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iOrderOrigin                          - Mandatory
iOrderNumber                                  - Mandatory
iOrderLine                                    - Optional
iOrderSequence                                - Optional
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
