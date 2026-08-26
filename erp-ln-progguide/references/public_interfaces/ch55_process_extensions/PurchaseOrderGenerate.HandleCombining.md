# PurchaseOrderGenerate.HandleCombining

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2175-2176

Customize the logic with regards to combining new purchase order lines to existing purchase orders. This process extension is available from 2024.04 ( KB2326972 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to customize the logic with
regards to combining new purchase order lines to existing purchase
orders.
The extension provides hooks for:
-               Get a customer determined purchase order that will be used when
generating purchase order lines.
-               Suppress combining purchase order lines on an existing purchase order
during generation.
These hooks are called for generate processes that can create a new purchase
order header.
```

To implement this process extension, you need to implement the following method(s):
