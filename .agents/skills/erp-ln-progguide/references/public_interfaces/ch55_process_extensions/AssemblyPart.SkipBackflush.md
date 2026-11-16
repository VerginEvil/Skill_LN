# AssemblyPart.SkipBackflush

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for AssemblyPart
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1970-1970

```baan
Skips backflushing of Assembly Parts.
This process extension is available from 2022.12 (KB2267502).
Technical information for this process extension:
Usage:        Process Extension AssemblyPart.SkipBackflush can be used to
skip backflushing of Assembly Parts.
Extender may specify a message, to present information about the skip
decision on the report.
Sessions where this Process Extension can be implemented:
- Backflush Requirements (tiasc7241m000)
Fields that are available to be used in this Process Extension:
- All fields of table: Assembly Part Requirements (tiasc740)
- All fields of table: Items (tcibd001)
- The Warehouse Order in table: Clustered Line Station Orders (tiasc730)
- tiasc730.worn
Note: Tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table tiasc740
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on tiasc740 = true> then
o.reason = "Assembly Part skipped because ..."
return(true)
endif
return(false)
}
```
