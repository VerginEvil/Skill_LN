# ProductionOrder.SkipClose

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2139-2140

Skips Production Orders when executing Close Orders. This process extension is available from 2023.06 ( KB2284251 ). Technical information for this process extension:

```baan
Usage:        Process Extension ProductionOrder.SkipClose can be used
to skip closure of specific Production Orders.
A message may be filled, to present information about the skip
decision on the report. This message can have max 300 characters.
Sessions where this Process Extension can be implemented:
-               Close Production Orders (ticst0201m000)
Fields that are available to be used in this Process Extension:
-               All fields of table: Production Orders (tisfc001)
```
