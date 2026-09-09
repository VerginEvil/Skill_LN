# Run.DetermineNumber

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Run
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1318-1318

```baan
DLL:   whextinhapi
This function is available from 2025.03 (KB3541252).
Syntax: long Run.DetermineNumber(
domain  whinh.kofr       iRunType,
domain  tclogn           iUser,
ref     domain  whinh.btno       oRunNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will determine the first available run
number.
Pre:    N.A.
Post:   N.A.
Input:  iRunType        - Run Type (Mandatory)
1 - Inbound
2 - Outbound
iUser           - User Login (Optional)
Output: oRunNumber      - Determined Run Number
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```
