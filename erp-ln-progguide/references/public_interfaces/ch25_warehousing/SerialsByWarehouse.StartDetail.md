# SerialsByWarehouse.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for SerialsByWarehouse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1124-1124

```baan
DLL:   whextltcapi
This function is available from 2021.04 (KB2179943).
Syntax: long SerialsByWarehouse.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tccwar           iWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Item - Serials and
Warehouses (whltc5100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Following input variables form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iItem
iSerialNumber
iWarehouse
Output: oExceptionMessage       - The last message if any message is
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
