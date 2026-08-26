# Item.ProjectPegAllowed

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 184-185

```baan
DLL:   tcextibdapi
This function is available from     2022.02 (KB2201342  ).
Syntax: long Item.ProjectPegAllowed(
domain  tcitem           iItem,
ref             boolean          oProjectPegAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Check whether it is allowed to use a project peg for an item.
Pre:                  -
Post:                 -
Input:  iItem
Item (Mandatory).
Output: oProjectPegAllowed
-                                True         if Project peg is allowed.
-                                False        if Project peg is not allowed.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Project peg allowed was succesfully determined.
<> 0                          - Error. Project peg allowed could not be determined.
```
