# BOD.GetPublishingAllowed

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1652-1653

```baan
DLL:   tcextbodapi
This function is available from     2023.05 (KB2292786  ).
Syntax: long BOD.GetPublishingAllowed(
ref             boolean          oAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if BOD publishing is allowed in the
current company.
Pre:    NA
Post:   NA
Input:  NA
Output: oAllowed                              - true: publishing is allowed
-                                               false: publishing is not allowed
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK.
<> 0                                          - Error occurred.
```
