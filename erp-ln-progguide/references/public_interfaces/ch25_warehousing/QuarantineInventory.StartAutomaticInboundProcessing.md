# QuarantineInventory.StartAutomaticInboundProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1202-1203

```baan
DLL:   whextinhapi
This function is available from     2020.05 (KB2117931  ).
Syntax: long QuarantineInventory.StartAutomaticInboundProcessing(
domain  tcorno           iQuarantineInventory,
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will start the processing of the next
automatic activity after the receipt line has been confirmed
which is related to Quarantine Inventory.
This public interface will generate inbound advices when this
is the next automatic activity of the related inbound
order line. When there is already an advice present which must
be putaway, please use one of the following public interfaces:
InboundAdvice.StartAutomaticInboundProcessing
InboundRun.StartAutomaticInboundProcessing
This public interface will execute the following steps:
1) Clear any prior notifications done for the automatic inbound
process, within the current process.
2) Notify the quarantine inventory, receipt line and the
potential handling unit for automatic processing
3) Start the automatic inbound process for the notified
Quarantine Inventory, Receipt Line and potential handling
unit
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
ret.val = QuarantineInventory.StartAutomaticInboundProcessing(.)
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
This public interface will be able to automatically generate
an inbound advice for the given quarantine inventory, receipt
line and potential handling unit. This public interface will
stop the automatic process when the next activity is not set to
automatic.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iQuarantineInventory                  - Mandatory
iReceipt                                      - Mandatory
iReceiptLine                                  - Mandatory
iHandlingUnit                                 - Optional
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
