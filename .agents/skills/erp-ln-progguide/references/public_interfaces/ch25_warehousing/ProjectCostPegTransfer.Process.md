# ProjectCostPegTransfer.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransfer
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1102-1102

```baan
DLL:   whextinhapi
This function is available from 2023.10 (KB2308375).
Syntax: long ProjectCostPegTransfer.Process(
domain  tcorno           iCostPegTransfer,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the cost peg transfer.
It is only allowed when the Project Pegging concept is enabled
in Implemented Software Components (tccom0500m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iCostPegTransfer - Project Cost Peg Transfer (Mandatory)
Output: NA
Return: 0: OK
<> 0: Error
```
