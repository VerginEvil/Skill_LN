# PlanItem.IsAggregateItem

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 222-222

```baan
DLL:   cpextrpdapi
This function is available from 2024.07 (KB2313149).
Syntax: long PlanItem.IsAggregateItem(
domain  tcncmp           iCompany,
domain  cpitem           iPlanItem,
ref             boolean          oIsAggregate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns whether a given Plan Item is
an Aggregate Item.
If an item is classified as an Aggregate Item, then, in planning,
also the items that are derived from this item must be handled.
Pre:    NA
Post:   NA
Input:  iCompany        Company (Optional) if not given,
the current company is used.
iPlanItem       Plan Item (Mandatory, must exist).
Output:
oIsAggregate    True if the Plan Item is an Aggregate Item,
false otherwise.
oExceptionMessage
The last message if any message is found.
If more than one message is
given, these are present in the
oExceptionID.
oExceptionID    An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 or <> 0
```
