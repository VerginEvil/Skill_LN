# BOD.ConvertFromERPDateToISODate

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1653-1654

```baan
DLL:   tcextbodapi
This function is available from 2023.10 (KB2308619).
Syntax: long BOD.ConvertFromERPDateToISODate(
domain  tcdate           iERPDate,
long             iDateConversion,
long             iDateFormat,
boolean          iERPDateIsUTC,
ref     domain  tcmcs.str30      oISODate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function converts a Date in LN (with Data Type "UTC
Date/Time" or "Date") to ISO 8601 format. Additionally this
function can set a date in ISO 8601 format if the Date in LN
is 0/empty.
Pre     : -
Post    : -
Input   : iERPDate              - The date in LN.
iDateConversion       - This determines the value of oISODate
if iERPDate is equal to 0. Allowed values:
1 - Set to minimum date
2 - Set to maximum date
3 - Set to current date
4 - Set no date (oISODate will be empty)
5 - Set to current date without time part
iDateFormat           - This determines the time part of oISODate.
Allowed values:
0 - Keep the standard time format: time
is kept if iERPDateIsUTC is true and
no time is set if iERPDateIsUTC is
false
1 - Set the time part
2 - Set no time part
iERPDateIsUTC         - Mandatory. Allowed values:
true: the Data Type for iERPDate is
"UTC Date/Time".
false: the Data Type for iERPDate is
"Date".
Output  : oISODate              - The date in ISO 8601 format.
oExceptionMessage     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Conversion failed.
```
