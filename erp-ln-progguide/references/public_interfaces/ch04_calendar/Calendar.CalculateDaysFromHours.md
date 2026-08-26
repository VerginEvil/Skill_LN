# Calendar.CalculateDaysFromHours

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 148-149

```baan
DLL:   tcextccpapi
This function is available from     2025.10 (KB3568051  ).
Syntax: long Calendar.CalculateDaysFromHours(
domain  tcccp.ract       iAvailabilityType,
double           iHours,
domain  tcutcs           iEffectiveDate,
ref             double           oDays,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface converts a given number of hours into the
corresponding number of days, using the average number of hours
per day as the conversion factor.
Input:
iAvailabilityType                             - Availability Type (Mandatory).
iHours                                        - Hours (Mandatory).
iEffectiveDate                                - Effective Date. Default value is the
current date if the value is zero.
Output: oDays                                 - Days
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Calculated the number of days
Successfully.
<> 0                                          - Error occurred.
```
