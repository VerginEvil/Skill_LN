# Item.GetRevision

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 179-179

```baan
DLL:   tcextibdapi
This function is available from 2023.10 (KB2295055).
Syntax: long Item.GetRevision(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tcdate           iDate,
ref     domain  tcibd.irev       oRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the Item Revision on the given date.
Pre:    None
Post:   None
Input:
iLogisticCompany        - Logistic Company: Mandatory
iItem                   - Item: Mandatory
iDate                   - Date: Mandatory
Output: oRevision               - Item Revison
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Data read.
<> 0                    - Otherwise.
```
