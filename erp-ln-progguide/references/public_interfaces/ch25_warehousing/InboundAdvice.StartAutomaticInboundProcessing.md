# InboundAdvice.StartAutomaticInboundProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1071-1073

```baan
DLL:   whextinhapi
This function is available from     2020.05 (KB2117931  ).
Syntax: long InboundAdvice.StartAutomaticInboundProcessing(
domain  tcorno           iInboundAdvice,
domain  tcpono           iInboundAdviceLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will start the processing of the next
automatic activity after the inbound advice has been created.
This public interface will be able to Putaway the Inbound
Advice, Generate a Storage List or Putaway a Storage List when
this is the next automatic activity of the related inbound order
line. When the inbound advice is already putaway or the storage
list is already putaway, this public interface will not perform
any automatic step, as Inbound Inspections cannot be automated
or the order line is already finished.
This public interface will execute the following steps:
1) Clear any prior notifications done for the automatic inbound
process, within the current process.
2) Notify the inbound advice for automatic processing
3) Start the automatic inbound process for the notified
inbound advice
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
ret.val = InboundAdvice.StartAutomaticInboundProcessing(..)
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
This public interface will be able to putaway the inbound
advice, generate a storage list or putaway the storage list.
This public interface will stop the automatic process when the
next activity is not set to automatic.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iInboundAdvice                        - Mandatory
iInboundAdviceLine                            - Mandatory
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
