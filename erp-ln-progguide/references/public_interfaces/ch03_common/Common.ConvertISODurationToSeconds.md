# Common.ConvertISODurationToSeconds

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 101-102

```baan
DLL:   tcextcomapi
This function is available from     2024.03 (KB2324302  ).
Syntax: long Common.ConvertISODurationToSeconds(
domain  tcmcs.st24       iISODuration,
ref             double           oNumberOfSeconds,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This Public Interface converts an ISO duration string to a
time in seconds.
Example 1:
ISO Duration          "P5Y2M9DT2H30M5S"
Number of seconds     163650605
Example 2:
ISO Duration          "P9D"
Number of seconds     777600
Example 3:
ISO Duration          "PT2.5H3.1M4.5S"
Number of seconds     9190.5
Pre     : NA
Post    : NA
Input   : iISODuration                        - The ISO duration (mandatory)
Output  : oNumberOfSeconds                    - The number of seconds
oExceptionMessage     The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID          An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
return  : 0                     Succesfully converted to ISO Duration
<> 0                    Otherwise
```
