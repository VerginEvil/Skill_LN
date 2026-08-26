# Warehousing.ConvertKindOfOrderToOrderOrigin

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Warehousing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 978-978

```baan
DLL:   whextinhapi
This function is available from     2023.11 (KB2308457  ).
Syntax: long Warehousing.ConvertKindOfOrderToOrderOrigin(
domain  tckoor           iKindOfOrder,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts the domain whinh.oorg to tckoor.
Pre:    N.a.
Post:   N.a.
Input:  oKindOfOrder               - Kind of Order (Mandatory)
Output: iOrderOrigin               - Order Origin
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - No Error
<> 0                          - Error
```
