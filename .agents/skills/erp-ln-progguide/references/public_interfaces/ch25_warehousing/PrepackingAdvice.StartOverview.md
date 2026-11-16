# PrepackingAdvice.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PrepackingAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1323-1324

```baan
DLL:   whextwmdapi
This function is available from 2026.05 (KB3663692).
Syntax: long PrepackingAdvice.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iShipment,
ref     domain  whinh.shpm       oShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Prepacking Advice
(whwmd5140m000) in Overview Mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when starting the session.
Use this to specify a filter, e.g.
"whwmd540.hupr = tcyesno.yes"
Using the query extend may lead to a
"data not found, session not started" situation.
iShipment
Shipment/Prepacking Advice identifier. Optional
Output: oShipment               - Shipment of the selected record,
if iStartMode = MODAL.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
