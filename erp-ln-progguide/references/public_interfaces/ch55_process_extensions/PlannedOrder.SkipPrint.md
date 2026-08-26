# PlannedOrder.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2106-2107

Skips printing Planned Orders. This process extension is available from 2025.09 ( KB3553172 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PlannedOrder.SkipPrint can be used
to skip certain Planned Orders when printing a range of
Planned Orders.
Sessions where this Process Extension can be implemented:
-               Print Planned Orders (cprrp1410m000)
Fields that are available to be used in this Process Extension:
-               All fields of table: Planned Orders (cprrp100)
-               All fields of table: Items - Planning (cprpd100)
-               All fields of table: Scenarios (cprpd400)
-               All fields of table: Carriers/LSP (tcmcs080)
-               All fields of table: Projects (tcmcs052)
```
