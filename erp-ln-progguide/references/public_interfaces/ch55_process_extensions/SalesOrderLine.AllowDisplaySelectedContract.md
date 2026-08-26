# SalesOrderLine.AllowDisplaySelectedContract

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2234-2234

Determine whether the only one selected contract for the sales order line is allowed to be displayed. This process extension is available from 2025.12 ( KB3638151 ). Technical information for this process extension:

```baan
Usage:        This process extension determines if the only one selected contract for
the sales order line is allowed to start session "Selected Sales Contract
Lines" (tdsls3512s000), while the standard would not start it when only one
valid contract is found. Subsequently, the contract can be manually linked
or not.
```

To implement this process extension, you need to implement the following method(s):
