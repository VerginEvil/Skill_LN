# whext.dll0013.compose.shipping.structure.on.execute.custom.command

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ComposeShippingStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1994-1995

```baan
Syntax: long whext.dll0013.compose.shipping.structure.on.execute.custom.command(
domain  tcmcs.str50      i.custom.command,
domain  whinh.load       i.load,
domain  whinh.cntr       i.shipping.container,
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line )
Usage:        Expl:   This function provide extension to execute custom specific
command in the session Compose Handling Unit.
When this method is invoked, the transaction management is to be
handled by the extension.
Pre:    N.a.
Post:   N.a.
Input:  i.custom.command
Possible value is one of the elements of array
o.command.name.array() as returned from the function
whext.dll0013.compose.shipping.structure.get.custom.commands
i.load                        -       Load that is selected in the compose shipping
structure tree. Only filled when either the
Load or Shipping Container is selected
i.shipping.container
-                                     Shipping Container that is selected in the
compose shipping structure tree. Only filled
when a Shipping Container is selected.
i.shipment                       -    Shipment that is selected in the compose
shipping structure tree. Only filled when either
the Shipment or Shipment Line is selected.
i.shipment.line
-                                     Shipment Line that is selected in the compose
shipping structure tree. Only filled when a
Shipment Line is selected
Output:
Return: 0: Success / <> 0: Error
```

## Process Extensions for ConfigurableItem

The following process extension(s) is/are available: ConfigurableItem.SkipCompileConstraints
