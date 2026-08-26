# OutboundOrderLine.SkipGenerateAdvice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2092-2093

Skips Outbound Order Lines during Generate Outbound Advice. This process extension is available from 2021.04 ( KB2177003 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension OutboundOrderLine.SkipGenerateAdvice can be used
to skip outbound order lines during the generate outbound advice
process.
For all instances where outbound advices are generated this process
extension will be invoked, this also includes automatic outbound
processing.
Fields that are available to be used in this Process Extension:
-               All fields of tables:
-                       Outbound Order Lines (whinh220)
```

## Process Extensions for PackingList

The following process extension(s) is/are available: PackingList.SkipPrint
