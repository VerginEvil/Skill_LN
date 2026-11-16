# whext.dll0019.put.away.inbound.advice.handle.before.check

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StockPointBlocking
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2283-2284

```baan
Syntax: long whext.dll0019.put.away.inbound.advice.handle.before.check(
domain  tcorno           i.advice,
domain  tcpono           i.advice.line )
Usage:        Expl:   This process extension allows to include customer specific
functionality before the check on stock point blocking.
This process extension will be called from Infor LN
standard when the inbound advice is put away via session
"Put Away Inbound Advice" (whinh3203m000), or when put away
inbound advice is an automatic order step. For each inbound
advice the process extension is executed before the check on
stock point blocking.
Following table is current when this extension is triggered:
whinh215 - Inbound Advice
When the process extension is executed, this done within the
current database transaction. So no new db.retry.point should be
set or abort/commit should be performed.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.advice        - Inbound Advice Number
i.advice.line   - Inbound Advice Line
Output: N.a.
Return: 0: Success / <> 0: Error
```
