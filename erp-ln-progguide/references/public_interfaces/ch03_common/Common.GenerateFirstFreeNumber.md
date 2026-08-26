# Common.GenerateFirstFreeNumber

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 105-106

```baan
DLL:   tcextmcsapi
Syntax: long Common.GenerateFirstFreeNumber(
domain  tcseri           iSeries,
domain  tcnrgr           iNumberGroup,
domain  tcmcs.byte       iMaximumLength,
ref     domain  tcorno           oFirstFreeNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function generates a new first free number based upon the
series, number group and the first free number length.
The function checks the entered series. Blocked series
and series being full are rejected.
Example:
If the iSeries is "SLS" and the iMaximumLength = 7
the oFirstFreeNumber will be "SLS9999".
Pre:    Transaction handling must be done when no cashing is used.
Post:   Transaction handling must be done when no cashing is used.
Input:
iSeries                                       - The series for which the first free
number must be generated.
iNumberGroup                                  - The number group (parameters)
for which the first free number must
be generated.(mandatory)
iMaximumLength                                - This is the total length of the output,
Inclusive used series.
iMaximumLength > 0 and
iMaximumLength =< domain length of
domain tcorno (standard = 9).
(mandatory)
Output: oFirstFreeNumber                      - The first free number based on the
series, numbergroup and Maximum length
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                                             - First Free Number is generated
<> 0                                          - on errors
```
