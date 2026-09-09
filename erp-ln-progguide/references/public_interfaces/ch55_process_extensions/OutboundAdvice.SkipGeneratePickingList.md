# OutboundAdvice.SkipGeneratePickingList

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2113-2114

```baan
Skips Outbound Advice Line during Generate Picking List.
This process extension is available from 2021.04 (KB2177003).
To implement this process extension, you can use the information below:
Usage:        Process Extension OutboundAdvice.SkipGeneratePickingList can be used
to skip outbound advice lines during the generate picking list process.
For all instances where outbound advices are put on a picking list this
process extension will be invoked, this also includes automatic outbound
processing.
Fields that are available to be used in this Process Extension:
- All fields of tables:
- Outbound Advice (whinh225)
- Outbound Order Lines (whinh220)
```
