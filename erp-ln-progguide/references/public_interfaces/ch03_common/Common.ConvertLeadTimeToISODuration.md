# Common.ConvertLeadTimeToISODuration

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 102-102

```baan
DLL:   tcextcomapi
This function is available from     2023.08 (KB2275138  ).
Syntax: long Common.ConvertLeadTimeToISODuration(
long             iYears,
long             iMonths,
domain  tcmcs.double     iDays,
domain  tcmcs.double     iHours,
domain  tcmcs.double     iMinutes,
domain  tcmcs.double     iSeconds,
ref     domain  tcmcs.st24       oISODuration,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   The purpose of this function is to convert a specified number
of years, months, days, hours, minutes and/or seconds to an
ISO duration in the format PnYnMnDTnHnMnS or                       -PnYnMnDTnHnMnS in
case of a negative duration.
A duration is negative if the specified values have a negative
value. A combination of negative values and positive values is
not allowed. A duration is positive if the values are 0 or
greater than zero.
Years and months are without decimals.
Days, hours, minutes and seconds can be specified with decimals.
Pre     : NA
Post    : NA
Input   : iYears                              - Years
iMonths                                       - Months
iDays                                         - Days
iHours                                        - Hours
iMinutes                                      - Minutes
iSeconds                                      - Seconds
Output  : oISODuration                        - The ISO Duration
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
return  : 0                     Succesfully converted to ISO Duration
<> 0                    Otherwise
```
