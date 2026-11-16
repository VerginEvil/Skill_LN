# CitiesByCountry.StartDetail

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for CitiesByCountry
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 143-143

```baan
DLL:   tcextcomapi
This function is available from 2026.04 (KB3665487).
Syntax: long CitiesByCountry.StartDetail(
long             iStartMode,
domain  tcccty           iCountry,
domain  tcmcs.cste       iStateOrProvince,
domain  tccity           iCity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Detail session Cities By Country -
tccom4139s000.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL   -       The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS-       Parent and child are parallel sessions
that can be manipulated simultaneously.
iCountry        -       Country (Mandatory)
iStateOrProvince-       State or province (Not Mandatory)
iCity           -       City (Not Mandatory)
Output: Not Applicable
Return: 0               -       Session started
<> 0            -       Otherwise.
```
