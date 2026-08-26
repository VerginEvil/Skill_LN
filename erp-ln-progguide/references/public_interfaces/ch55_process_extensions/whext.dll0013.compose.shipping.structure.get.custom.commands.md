# whext.dll0013.compose.shipping.structure.get.custom.commands

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ComposeShippingStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1993-1994

```baan
Syntax: long whext.dll0013.compose.shipping.structure.get.custom.commands(
ref             long             o.nr.custom.commands,
ref     domain  tcmcs.str50      o.command.name.array() fixed,
ref     domain  tcmcs.str30m     o.command.description.array() fixed mb,
ref             long             o.category.array() )
Usage:        Expl:   This function returns arrays with Custom Specific commands in
the GBF session Compose Shipping Structure.
Pre:    NA
Post:   NA
Input:  NA
Output: o.nr.custom.commands
o.command.name.array
o.command.description.array
o.category.array
0:      print menu
1:      specific menu
Return: 0/DALHOOKERROR
```
