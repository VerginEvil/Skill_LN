# Common.ValidateNumberGroupSeries

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 114-115

```baan
DLL:   tcextmcsapi
This function is available from     2022.03 (KB2201864  ).
Syntax: long Common.ValidateNumberGroupSeries(
domain  tcseri           iSeries,
domain  tcnrgr           iNumberGroup,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function checks if a series has been defined for the
specified number group.
Pre:                  -
Post:                 -
Input:  iSeries                               - The series.
iNumberGroup                                  - The number group (mandatory).
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0 If the order series is defined and not blocked.
1 If the order series is not defined
2 If the order series is blocked.
3 If the series length does not correspond to number group
4 If the series for a numbergroup is full.
```

## Public Interfaces for Contact

The following functions are available: Contact.StartOverview
