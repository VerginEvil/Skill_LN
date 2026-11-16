# InboundRun.StartAutomaticInboundProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundRun
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1097-1098

```baan
DLL:   whextinhapi
This function is available from 2020.05 (KB2117931).
Syntax: long InboundRun.StartAutomaticInboundProcessing(
domain  whinh.btno       iInboundRun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will start the processing of the next
automatic activity after the for the notified Run.
This public interface will handle the next automatic inbound
activity for the given inbound run. Please be aware that
multiple inbound advice lines and/or inbound order lines could
be processed when starting the automatic inbound process for the
run, especially when runs are reused.
This public interface will execute the following steps:
1) Clear any prior notifications done for the automatic inbound
process, within the current process.
2) Notify the run for automatic processing
3) Start the automatic inbound process for the notified run
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
ret.val = InboundRun.StartAutomaticInboundProcessing(..)
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
This public interface will be able to automatically perform the
next automatic steps for the given run. This public interface
will stop the automatic process when the next activity is not
set to automatic.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iInboundRun             - Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
