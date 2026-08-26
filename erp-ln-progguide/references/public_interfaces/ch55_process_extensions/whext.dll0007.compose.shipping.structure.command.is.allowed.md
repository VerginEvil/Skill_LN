# whext.dll0007.compose.shipping.structure.command.is.allowed

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ComposeShippingStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1991-1992

```baan
Syntax: boolean whext.dll0007.compose.shipping.structure.command.is.allowed(
const           string           i.action(),
domain  whinh.load       i.load,
domain  whinh.cntr       i.shipping.container,
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line )
Usage:        Expl:   This function allows for disabling of commands that are present
within the compose shipping structure tree. The enabling of the
standard will first be evaluated, if the standard allows the
execution of the command this function is called to evaluate if
the command should also be allowed based on extension logic.
It is not possible to  enable a command which is disabled by the
standard.
Pre:    N.a.
Post:   N.a.
Input:  i.action               -      This argument determines the action which is
performed.
Possible values are:
-                                               FreezeLoad
-                                               FreezeShippingContainer
-                                               FreezeShipment
-                                               FreezeShipmentLine
-                                               ReopenLoad
-                                               ReopenShippingContainer
-                                               ReopenShipment
-                                               ReopenShipmentLine
-                                               ConfirmLoad
-                                               ConfirmShippingContainer
-                                               ConfirmShipment
-                                               ConfirmShipmentLine
-                                               SelectCarrierLoad
-                                               NewLoad
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
Return: true                  --> command is allowed
false                         --> command is not allowed
```
