# Pricing.RetrievePriceAndDiscounts

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Pricing
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2141-2141

```baan
Determine customer specific Price and Discounts.
This process extension is available from 2021.12 (KB2215124).
Technical information for this process extension:
Usage:        With this Process Extension, it is possible to set customer determined
price and discounts from an extension to a value other than the defaulted
values based on LN logic .
This price and discounts are then used in all flows where the price and
discounts are retrieved.
The extension provides the following hooks:
- tdext.pcg0001.get.customer.determined.price.and.discounts
This is the general-purpose hook used in most scenarios when prices
and discounts need to be determined.
- tdext.pcg0001.get.customer.determined.price.and.discounts.for.service
This hook is used in specific scenarios where price retrieval is
initiated by the Service package.
To implement this process extension, you need to implement the following method(s):
```
