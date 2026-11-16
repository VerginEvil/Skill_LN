# ItemWarehouse.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemWarehouse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 913-914

```baan
DLL:   whextwmdapi
This function is available from 2025.11 (KB3631517).
Syntax: long ItemWarehouse.StartDetail(
long             iStartMode,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Item Data by Warehouse in Detail
mode (whwmd21100s000).
Pre:    NA
Post:   NA
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iWarehouse      - Mandatory
iItem           - Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0     Session started
<> 0: Error
```
