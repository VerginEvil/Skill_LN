# SalesOrderGenerate.DetermineOrderForCombining

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2229-2229

Determine customer specific sales order for combining sales order lines when generating orders. This process extension is available from 2024.01 ( KB2317750 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to let the extension decide
which sales order must be used to combine a sales order line on an
existing sales order.
It is implemented for generate processes that can create a new sales
order header.
```

To implement this process extension, you need to implement the following method(s):
