# IntercompanyTradeOrder.SkipReleaseToInvoicing

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IntercompanyTradeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2038-2038

Skips Release to Invoicing for Intercompany Trade. This process extension is available from 2026.05 ( KB3668064 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension IntercompanyTradeOrder.SkipReleaseToInvoicing
can be used to skip the release to invoicing of intercompany trade
order transaction lines.
Sessions where this Process Extension can be implemented:
-               Release to Invoicing (tcitr3210m000)
Fields that are available to be used in this Process Extension:
-               All fields of tables:
-                       Intercompany Trade Orders (tcitr300)
-                       Intercompany Trade Order Transaction Lines (tcitr310)
```

## Process Extensions for InterestInvoiceAdvice

The following process extension(s) is/are available: InterestInvoiceAdvice.SkipPrintAdvice
