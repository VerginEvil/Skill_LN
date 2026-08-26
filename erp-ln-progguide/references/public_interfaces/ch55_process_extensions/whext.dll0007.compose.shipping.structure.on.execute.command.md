# whext.dll0007.compose.shipping.structure.on.execute.command

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ComposeShippingStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1992-1993

```baan
Syntax: long whext.dll0007.compose.shipping.structure.on.execute.command(
const           string           i.action(),
boolean          i.before,
domain  whinh.load       i.load,
domain  whinh.cntr       i.shipping.container,
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line )
Usage:        Expl:   This function allows to implement extension logic within the
execution of commands in the compose shipping structure
tree. This function is called when one of the following commands
is executed by the user:
-                       Freeze
-                       Reopen
-                       Confirm
-                       Select Carrier/LSP
-                       New Load
When the command is executed, this function is called twice to
allow extension logic to be performed before and after execution
of the command in the standard. The i.before argument indicates
if the function is called before execution of the standard logic
When this method is invoked, the transaction management is to be
handled by the extension. The standard command execution will
have it's own transaction management.
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
i.before                       -      Boolean, determines at which moment the function
is called, meaning:
true:   the function is called before the
standard functionality of the command is
executed.
false:  the function is called after the
standard functionality of the command is
executed.
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
