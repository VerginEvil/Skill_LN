# ProductionOrderAdvice.Transfer

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProductionOrderAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1308-1309

```baan
DLL:   whextinaapi
This function is available from 2025.08 (KB3613660).
Syntax: long ProductionOrderAdvice.Transfer(
domain  tcpdno           iProductionOrderAdvice,
domain  tcseri           iOrderSeries,
domain  whwmd.arso       iReleaseOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts confirmed production order advices
into actual production orders by transferring them to
"Manufacturing".
Pre:    db.retry.point() is set.
Production order advice is confirmed.
Post:   abort.transaction() or commit.transaction().
Transferred production order advices are deleted from table
Production Order Advice.
Input:  iProductionOrderAdvice  Production order advice number (mandatory)
iOrderSeries            The order series which has to be used
when the advice is transferred to a
production order. If empty the default
order series will be used. (optional)
iReleaseOrder           Allowed values:         (optional)
Yes - automatically release production
order which was created for the selected
production order advice;
No (default value) - do not release
production order automatically;
Default - the default setting is taken
from the Automatically Release
Production Orders check box in the
Item Data by Warehouse (whwmd2510m000)
session.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Returs: 0 -> successful
```
