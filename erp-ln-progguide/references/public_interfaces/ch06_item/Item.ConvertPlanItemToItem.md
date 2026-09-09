# Item.ConvertPlanItemToItem

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 166-167

```baan
DLL:   cpextrpdapi
This function is available from 2020.01 (KB2085127).
Syntax: long Item.ConvertPlanItemToItem(
domain  tcncmp           iLogisticCompany,
domain  cpitem           iPlanItem,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the tcitem code for the given
plan-item.
Pre:    None
Post:   None
Input:  iLogisticCompany        Logistic Company (Mandatory)
iPlanItem               Plan Item (Mandatory)
Output: oItem                   Item
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function is executed successfully
<> 0                    An error occurred
```
