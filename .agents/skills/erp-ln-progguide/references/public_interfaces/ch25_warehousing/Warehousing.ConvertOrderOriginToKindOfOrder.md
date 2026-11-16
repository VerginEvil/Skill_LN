# Warehousing.ConvertOrderOriginToKindOfOrder

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Warehousing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 988-989

```baan
DLL:   whextinhapi
This function is available from 2023.11 (KB2308457).
Syntax: long Warehousing.ConvertOrderOriginToKindOfOrder(
domain  whinh.oorg       iOrderOrigin,
ref     domain  tckoor           oKindOfOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts the domain whinh.oorg to tckoor.
Pre:    N.a.
Post:   N.a.
Input:  iOrderOrigin - Order Origin (Mandatory)
Output: oKindOfOrder - Kind of Order
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - No Error
<> 0    - Error
```
