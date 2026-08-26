# OutboundAdvice.SkipReleaseAdvice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2091-2092

Skips Outbound Advice Line during Release Outbound Advice. This process extension is available from 2021.04 ( KB2177003 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension OutboundAdvice.SkipReleaseAdvice can be used
to skip outbound advice lines during the release outbound advice
process.
For all instances where outbound advices are released this process
extension will be invoked, this also includes automatic outbound
processing.
Fields that are available to be used in this Process Extension:
-               All fields of tables:
-                       Outbound Advice (whinh225)
-                       Outbound Order Lines (whinh220)
```

## Process Extensions for OutboundOrderLine

The following process extension(s) is/are available: OutboundOrderLine.SkipGenerateAdvice
