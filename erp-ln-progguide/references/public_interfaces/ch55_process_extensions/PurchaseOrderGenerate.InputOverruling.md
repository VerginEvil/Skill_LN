# PurchaseOrderGenerate.InputOverruling

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrderGenerate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2180-2180

Determine which input must be overruled and set it to a customer determined value. This process extension is available from 2026.06 ( KB3668896 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to overrule certain input
when generating purchase order lines.
The extension provides the following hook:
-               Determine the input that must be overruled and set them to a customer
determined value.
This hook is called for generate processes that can create a new
purchase order.
```

To implement this process extension, you need to implement the following method(s):
