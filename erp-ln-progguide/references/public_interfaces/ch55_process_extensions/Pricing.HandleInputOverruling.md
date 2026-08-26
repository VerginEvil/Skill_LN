# Pricing.HandleInputOverruling

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2116-2117

Handle customer determined input for pricing. This process extension is available from 2026.06 ( KB3670627 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to set a customer determined
quantity from an extension to a value other than the defaulted
value based on LN logic.
This quantity (if valid) is then used in all pricing flows where
prices and discounts are retrieved using the order quantity.
```

To implement this process extension, you need to implement the following method(s):
