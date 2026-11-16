# InboundAdvice.SkipPutawayAdvice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2052-2052

```baan
Skips Inbound Advice during Put Away Inbound Advice.
This process extension is available from 2024.04 (KB2327467).
Technical information for this process extension:
Usage:        Process Extension InboundAdvice.SkipPutawayAdvice can be used
to skip inbound advice during the put away inbound advice
process.
Extender may specify a message, to present information about the skip
decision.
For all instances where inbound advices are put away this process
extension will be invoked, this also includes automatic inbound
processing.
Fields that are available to be used in this Process Extension:
- All fields of tables:
- Inbound Advice (whinh215)
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhinh215
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on whinh215 = true> then
o.reason = "Putaway skipped because ..."
return(true)
endif
return(false)
}
```
