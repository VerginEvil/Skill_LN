# SalesScheduleLine.Reprice

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesScheduleLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 309-310

```baan
DLL:   tdextslsapi
This function is available from 2021.11 (KB2212442).
Syntax: long SalesScheduleLine.Reprice(
domain  tcorno           iSalesSchedule,
domain  tdsls.reltype    iSalesScheduleType,
domain  tcpono           iSalesScheduleRevision,
domain  tcpono           iSalesScheduleLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   The purpose of this function is to reprice the given schedule
line. An error is returned if repricing is not allowed anymore
for the given schedule line.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesSchedule          - Sales Schedule (Mandatory)
iSalesScheduleType      - Sales Schedule Type (Mandatory)
iSalesScheduleRevision  - Sales Schedule Revision
iSalesScheduleLine      - Sales Schedule Line (Mandatory)
Output: NA
Return: 0                       - Schedule repriced
<> 0                    - An error occurred or repricing not allowed.
```
