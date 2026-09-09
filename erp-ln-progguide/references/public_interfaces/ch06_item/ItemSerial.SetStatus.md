# ItemSerial.SetStatus

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSerial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 225-225

```baan
DLL:   tcextibdapi
This function is available from 2024.11 (KB2331329).
Syntax: long ItemSerial.SetStatus(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcibd.ssts       iStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface updates the status of Item Serial numbers.
Pre:    retry.point must be set
Post:   transaction must be committed or aborted
Input:
iItem                   - Item (Mandatory).
iSerialNumber           - Serial Number (Mandatory).
iStatus                 - Status (Mandatory).
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Successfully updated.
<> 0                    - Otherwise.
```
