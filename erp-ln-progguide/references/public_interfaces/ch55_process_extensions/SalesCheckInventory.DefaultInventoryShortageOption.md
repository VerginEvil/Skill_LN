# SalesCheckInventory.DefaultInventoryShortageOption

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesCheckInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2215-2215

Determine customer specific default 'Automatic Inventory Shortage Option' for Sales Check Inventory. This process extension is available from 2021.04 ( KB2181351 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to set a customer determined
automatic inventory option (enumerated value of domain
tdsls.ssop) to a value other than the defaulted value based on LN
Master Data (sales order type) from an extension.
This option will be used in 'Check Inventory for Sales Orders'
(tdsls4217m000) and any other process triggering the automatic inventory
handling in Sales.
```

To implement this process extension, you need to implement the following method(s):
