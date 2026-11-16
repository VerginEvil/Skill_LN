# SerializedItem.GetSupplierWarrantyEndDate

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1358-1358

```baan
DLL:   tsextcfgapi
This function is available from 2023.06 (KB2290728).
Syntax: long SerializedItem.GetSupplierWarrantyEndDate(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tsmdm.date       oEndDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the Supplier Warranty End Date for the
given Serialized Item.
Pre:    -
Post:   -
Input:  iItem
Item
iSerialNumber
Serial Number; Mandatory
Output: oEndDate
The Supplier Warranty End Date in number of days from
01-01-0001.
0 if no Supplier Warranty is present.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - Determining end date successful
<> 0    - An error occurred
```
