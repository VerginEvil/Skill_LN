# AssemblyOrder.SkipGenerate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1950-1951

Skips Generation of Assembly Orders. This process extension is available from 2022.09 ( KB2228471 ). Technical information for this process extension:

```baan
Usage:        Process Extension AssemblyOrder.SkipGenerate can be used to skip
generation of Assembly Orders for product variants.
Extender may specify a message, to present information about the skip
decision on the report.
Sessions where this Process Extension can be implemented:
-               Generate Assembly Orders (tiapl3201m000)
Fields that are available to be used in this Process Extension:
-               Key Fields from table: Product Variant (tiapl300)
1) tiapl300.cpva
2) tiapl300.item
3) tiapl300.smsc
4) tiapl300.reft
5) tiapl300.refo
6) tiapl300.apsv
Note: (1)Tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table ttiapl300
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on tiapl300 = true> then
o.reason = "Product Variant skipped because ..."
return(true)
endif
return(false)
}
```

## Process Extensions for AssemblyPart

The following process extension(s) is/are available: AssemblyPart.SkipBackflush
