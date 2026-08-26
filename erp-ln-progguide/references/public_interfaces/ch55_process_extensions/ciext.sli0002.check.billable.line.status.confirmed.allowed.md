# ciext.sli0002.check.billable.line.status.confirmed.allowed

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BillableLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1955-1955

```baan
Syntax: long ciext.sli0002.check.billable.line.status.confirmed.allowed(
ref             boolean          o.line.status.confirmed.allowed )
Usage:        Expl:
Use this method to check whether, at adding Billable Line, the
line status may be set to Confirmed.
At moment of adding a Billable Line, LN will do own checks
first. Only if the Billable Line status may be set to Confirmed
according to the standard logic in LN, this method in the
Process Extension is called.
In this method, own checks can be implemented and the variable
o.line.status.confirmed.allowed can be set. If the variable is
set to false, the Billable Line status will be set to On Hold;
otherwise, the status will be set to Confirmed.
Fields that are available to be used in this Process Extension:
although the Billable Line is to be added and not yet committed,
the Billable Line fields from cisli810 are already available.
Note that dal messages set in this function will be ignored by
the standard.
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.line.status.confirmed.allowed               - Indicates whether the billable
line status may be set to
'Confirmed'.
Return: 0                                     - Success
<> 0                                          - When an error occurs during checking;
status will not be set to 'Confirmed'.
```
