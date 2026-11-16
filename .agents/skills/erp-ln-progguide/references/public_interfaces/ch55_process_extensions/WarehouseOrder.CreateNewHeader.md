# WarehouseOrder.CreateNewHeader

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2313-2314

```baan
Allows to invoke a new order header during warehouse order creation.
This process extension is available from 2024.12 (KB2331636).
Technical information for this process extension:
Usage:        With this Process Extension it becomes possible to influence the
release to warehousing process with respect to the reuse of an existing
warehouse order header. For each line that is released to warehousing
this process extension will be invoked, allowing for custom
determination of the reusing process.
To implement this process extension, you need to implement the following method(s):
```
