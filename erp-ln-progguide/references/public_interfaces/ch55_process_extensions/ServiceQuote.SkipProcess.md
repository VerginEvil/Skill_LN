# ServiceQuote.SkipProcess

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2244-2245

Skips Service Quote when Processing. This process extension is available from 2025.04 ( KB3568308 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension ServiceQuote.SkipProcess can be used
to skip Service Quotes when processing.
Sessions where this Process Extension can be implemented:
-               Process Quotes (tsepp1203m000)
-               All sessions and processes that trigger a Service Quote to be
processed.
Fields that are available to be used in this Process Extension:
-               Key field of tsepp100         - tsepp100.orno (Quote)
This field can be used to read e.g. table tsepp100.
Note: table must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table   ttsepp100       |* Quotes
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tsepp100 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for ShiftsByWorkcell

The following process extension(s) is/are available: ShiftsByWorkcell.SkipCompleteShift
