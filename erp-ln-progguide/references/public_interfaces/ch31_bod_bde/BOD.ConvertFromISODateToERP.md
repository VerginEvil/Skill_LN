# BOD.ConvertFromISODateToERP

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1636-1637

```baan
DLL:   tcextbodapi
This function is available from     2023.10 (KB2308619  ).
Syntax: long BOD.ConvertFromISODateToERP(
domain  tcmcs.str30      iISODate,
ref     domain  tcdate           oERPDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function converts a string, representing a date[time] in
ISO 8601 format to a Date in LN (with Data Type "UTC Date/Time"
or "Date").
Pre     :               -
Post    :               -
Input   : iISODate                            -  The date in ISO 8601 format. Mandatory.
The following formats are supported:
"yyyy                                                   -mm-ddThh:mm:ssZ" (GMT)
"yyyy                                                   -mm-ddThh:mm:ss+hh:mm"
"yyyy                                                   -mm-ddThh:mm:ss-hh:mm"
"yyyy                                                   -mm-ddThh:mm:ss"  (interpreted
as local date/time)
"yyyy                                                   -mm-dd"
Output  : oERPDate                            - The date in LN.
If iISODate contains the character T,
the date is converted to a UTC value,
which contains the date and time based
on the LN Data Type "UTC Date/Time".
The earliest date is 1970                                                -01-01.
If iISODate does not contain the
character T, the date is converted to
a local date value based on the LN Data
Type "Date". This does not take the
time zone into account.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                                   - OK.
<> 0                                          - Conversion failed.
```
