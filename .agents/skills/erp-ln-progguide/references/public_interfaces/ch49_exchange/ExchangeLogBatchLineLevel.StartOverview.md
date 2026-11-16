# ExchangeLogBatchLineLevel.StartOverview

> Chapter: Chapter 49 Public Interfaces for Exchange
>
> Group: Public Interfaces for ExchangeLogBatchLineLevel
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1951-1951

```baan
DLL:   daextxchapi
This function is available from 2024.03 (KB2321682).
Syntax: long ExchangeLogBatchLineLevel.StartOverview(
long             iStartMode,
const           string           iStartFilter(),
long             iSessionIndex,
const           string           iQueryExtend(),
domain  daxch.txch       iTypeOfExchange,
const           string           iExchangeScheme(),
long             iRunNumber,
long             iTryNumber,
domain  daxch.cbat       iBatch,
ref             string           oExceptionMessage(),
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Log Table (Batch Line Level)
(daxch0509m000).
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
Not Used
iSessionIndex
Not Used
iQueryExtend
Not Used
iTypeOfExchange
Mandatory
iExchangeScheme
Mandatory
iRunNumber      The Run Number
If value = 0 then the last runnumber is used
iTryNumber      The Try Number
If value = 0 then the last try number is used
iBatch          The Batch
Output: oExceptionMessage       - The last message if the return
value is not equal to 0.
If more than one  message is
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
