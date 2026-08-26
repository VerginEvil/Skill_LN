# PackingSlip.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PackingSlip
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2093-2094

Skips printing of Packing Slips. This process extension is available from 2025.04 ( KB3569968 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PackingSlip.SkipPrintShipmentLine can be used
to skip the printing of Shipment Lines on a Packing Slip.
This process extension will be invoked when printing a Packing Slip,
either via session Print Packing Slips (whinh4475m000) or via the
automatic printing of the shipping documents.
Fields that are available to be used in this Process Extension:
-               All fields of tables:
-                       Shipments (whinh430)
-                       Shipment Lines (whinh431)
```

## Process Extensions for PaymentAdvice

The following process extension(s) is/are available: PaymentAdvice.CustomAuditPayments PaymentAdvice.SkipPaymentBatch PaymentAdvice.SkipPrintPaymentAdvice
