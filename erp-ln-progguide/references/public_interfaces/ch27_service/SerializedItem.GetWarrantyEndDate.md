# SerializedItem.GetWarrantyEndDate

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1346-1347

```baan
DLL:   tsextcfgapi
This function is available from     2025.10 (KB3613621  ).
Syntax: long SerializedItem.GetWarrantyEndDate(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tsmdm.date       oEndDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the Warranty End Date based on the
Warranty Template or the Generic Warranty. The latest of these
two days is used as Expiry Term.
The End Date that is determined by this function is the same as
the date of the field Terms Expire On on the Warranty tab in
session tscfg2100m000.
Pre:                  -
Post:                 -
Input:  iItem
Item
iSerialNumber
Serial Number; Mandatory.
Output: oEndDate
The Warranty End Date in number of days from 01                              -01-0001.
0 if no Supplier Warranty is present.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Determining end date successful.
<> 0                          - An error occurred.
```
