# Sales.DetermineAdditionalCostSet

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Sales
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2209-2209

Determine customer specific Additional Cost Set that must be used in Sales. This process extension is available from 2026.09 ( KB3688067 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to determine the additional
cost set that must be used in the sales process.
The extension provides the following hook:
-               Determine the additional cost set, based on the context passed via
the Processing Option Set and the result from standard logic.
This hook is called whenever LN determines the additional cost set
for a sales order, shipment, or price calculation.
```

To implement this process extension, you need to implement the following method(s):
