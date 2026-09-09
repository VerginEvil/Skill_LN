# PurchaseSchedule.Regenerate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseSchedule
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 440-441

```baan
DLL:   tdextpurapi
This function is available from 2023.11 (KB2308628).
Syntax: long PurchaseSchedule.Regenerate(
domain  tcorno           iPurchaseSchedule,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function regenerates a purchase schedule, like session
›¼ÀœRegenerate Schedules›¼À• (tdpur3211m000). Regenerating a schedule
redetermines the requirement type of the schedule lines.
In addition, the price and discounts of schedule lines are
redetermined. The regeneration process is applicable only for
PUSH purchase schedules.
Pre:    Caller must set retry-point
Post:   Caller must set commit/abort transaction
Input:  iPurchaseSchedule       - Purchase Schedule (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> No error
<> 0    -> Error occurred
```
