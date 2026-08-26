# PickingList.PickMission

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PickingList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1258-1259

```baan
DLL:   whextinhapi
This function is available from     2026.08 (KB3682824  ).
Syntax: long PickingList.PickMission(
domain  whinh.btno       iRunNumber,
domain  tccwar           iWarehouse,
domain  whinh.picm       iPickMission,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface initiates picking for a specific
picking mission.
This function has its own db.retry.point and
commit.transaction.
Pre:    There should be no pending logical transaction before
calling this function.
Post:   No need to commit or abort the process, that is handled
within the function.
Input:  iRunNumber                            - Run Number(Mandatory)
iWarehouse                                    - Warehouse (Mandatory)
iPickMission                                  - Pick Mission (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Picking initiated successfully
<> 0                                          - Error
```
