# Kanban.StartGenerate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Kanban
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1299-1299

```baan
DLL:   whextinhapi
This function is available from 2025.10 (KB3629008).
Syntax: long Kanban.StartGenerate(
domain  tckbid           iKanbanSignal,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the session Generate Orders (Kanban)
(whinh2200m00).
Input:  i.kanban.signal
Kanban Signal for which an order or advice needs to be
generated.
Output: N.a.
Return: 0 / DALHOOKERROR
```
