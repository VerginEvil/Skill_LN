# ProductionOrder.CompressAutomatedQueueTime

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 710-711

```baan
DLL:   tiextsfcapi
This function is available from 2025.10 (KB3548527).
Syntax: long ProductionOrder.CompressAutomatedQueueTime(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tisfc.stcm       iQueueCompressionMethod,
domain  tcutcs           iTargetStartDate,
domain  tcutcs           iTargetFinishDate,
domain  tisfc.dayp       iTargetedCompressionPercentage,
domain  tcyesno          iIncludeOperationsAtCriticalWorkCenter,
ref             boolean          oCompressTimeAdjusted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface evenly removes the queue time from all the
operations of a production order that are not yet completed. In
this way, you could meet a production order's modified delivery
date or start date. Queue time compression is supported for
forward planning methods as well as for backward planning
methods.
Compress time can be adjusted using the following options:
- Target Start Date and Target Finish Date
- Queue Compression Method
- Targeted Compression Percentage
- Include Operations at Critical Work Center
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory and must be
in iSite).
iQueueCompressionMethod
Queue Compression Method.
Possible values are:
Best Fit - tisfc.stcm.best.fit (default),
Targeted Percent -tisfc.stcm.target.perc.
iTargetStartDate        Target Start Date.
iTargetFinishDate       Target Finish Date.
iTargetedCompressionPercentage
Targeted Compression Percentage.
Default value is 100.
iIncludeOperationsAtCriticalWorkCenter
Include Operations At Critical Work
Center.
Default value is tcyesno.no.
Output: oCompressTimeAdjusted   Compress Time Adjusted.
oExceptionMessage       The last message, if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Automated Queue time is successfully
compressed.
<> 0                    Otherwise.
```
