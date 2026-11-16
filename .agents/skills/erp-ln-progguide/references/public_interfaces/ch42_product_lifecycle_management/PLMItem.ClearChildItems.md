# PLMItem.ClearChildItems

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1858-1858

```baan
DLL:   pdextpdmapi
This function is available from 2023.04 (KB2286306).
Syntax: long PLMItem.ClearChildItems(
domain  tcguid.extend    iItemStructureId,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is to remove the child items from
cache table pderp201 and pderp202.
All the parameters are mandatory.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iItemStructureId        -Item Stucture Identification ID
Output: oExceptionMessage - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: long            - 0      if success
- <> 0  if fail
```
