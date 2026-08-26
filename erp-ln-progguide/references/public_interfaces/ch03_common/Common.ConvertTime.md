# Common.ConvertTime

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 104-105

```baan
DLL:   tcextcomapi
This function is available from     2022.01 (KB2221361  ).
Syntax: long Common.ConvertTime(
domain  tccuni           iFromUnit,
domain  tcqst1           iFromTime,
domain  tccuni           iToUnit,
ref     domain  tcqst1           oToTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts a time specified in a unit to
a time specified in another unit.
Rounding will not be done. Common.RoundQuantity can be used for
rounding.
Post:   None
Input:  iFromUnit                             - From Unit: Mandatory
iFromTime                                     - From Time
iToUnit                                       - To Unit: Mandatory
Output: oToTime                               - To Time
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                             - Time is converted.
<> 0                                  - Otherwise.
```
