# PhysicalBreakdown.ItemExistsInBreakdownOfParent

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PhysicalBreakdown
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1372-1372

```baan
DLL:   tsextcfgapi
This function is available from 2024.06 (KB2331323).
Syntax: long PhysicalBreakdown.ItemExistsInBreakdownOfParent(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcitem           iParentItem,
domain  tcibd.sern       iParentSerialNumber,
ref             boolean          oExists,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to determine if the given child
(serialized) item is present in the physical breakdown of the
given parent serialized item directly or indirectly.
If a child serial number is provided, the physical breakdown
under the parent serialized item will only be searched for that
specific child serialized item.
If no child serial number is provided, the physical breakdown
under the parent serialized item will be searched for any child
item with the given item code.
Note that only installed statuses are taken into account.
Pre:    Any provided serialized item must exist.
Input:  iItem
Child Item; Mandatory if iSerialNumber is empty
iSerialNumber
Child Serial Number; Mandatory if iItem is empty
iParentItem
Parent Item; Not mandatory
iParentSerialNumber
Parent Serial Number; Mandatory
Output: oExists
True: The given child (serialized) item exists in the
physical breakdown tree under the given parent
serialized item.
False: The given child (serialized) item does not exist
in the physical breakdown tree under the given
parent serialized item.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0:      No error
<> 0:   An error occurred
```
