# GenerateFieldChangeOrderLine.SkipSerializedItem

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for GenerateFieldChangeOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2026-2027

Skips generating Field Change Order Line for Serialized Items. This process extension is available from 2025.11 ( KB3597898 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension GenerateFieldChangeOrderLine.SkipSerializedItem can be
used to skip generating field change order lines for specific serialized
items.
Sessions where this Process Extension can be implemented:
-               Generate Field Change Order Lines (tssoc5210m000).
Fields that are available to be used in this Process Extension:
-               Key fields of tscfg200        - tscfg200.item (Item)
-                                               tscfg200.sern (Serial Number)
These fields can be used to read e.g. table tscfg200.
Note: table must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table   ttscfg200       |* Serialized Items
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tscfg200 = true> then
return(true)
endif
return (false)
}
```

## Process Extensions for GenerateHandlingUnits

The following process extension(s) is/are available: GenerateHandlingUnits.SkipOrderLine
