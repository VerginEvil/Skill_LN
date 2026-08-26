# ProjectCostPegTransferLine.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransferLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1095-1096

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2304375  ).
Syntax: long ProjectCostPegTransferLine.Process(
domain  tcorno           iCostPegTransfer,
domain  tcpono           iCostPegTransferLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the cost peg transfer line.
It is only allowed when the Project Pegging concept is enabled
in Implemented Software Components (tccom0500m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iCostPegTransfer               - Project Cost Peg Transfer (Mandatory)
iCostPegTransferLine                       - Project Cost Peg Transfer Line(Mandatory)
Output: NA
Return: 0: OK
<> 0: Error
```
