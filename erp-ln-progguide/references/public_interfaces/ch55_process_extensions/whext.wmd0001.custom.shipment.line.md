# whext.wmd0001.custom.shipment.line

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for HandlingUnitBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2050-2051

```baan
Syntax: long whext.wmd0001.custom.shipment.line(
domain  whinh.shpm       i.shipment,
domain  tcpono           i.shipment.line,
domain  whhuid           i.handling.unit,
boolean          i.handling.unit.reused,
ref     domain  tcmcs.str132m    o.error.message.array() fixed mb )
Usage:        Expl:   This function can be implemented to influence the handling unit
building process during creation of handling units for the
given shipment line.
This function will be called from the standard process just
after a handling unit is linked to the given shipment line.
If a handling unit is re-used from inventory (during picking /
release outbound advice when picking is not in the outbound
process), the flag i.handling.unit.reused will be set to true.
Do not change the record buffers with the additional logic, or
if required, store and restore the record buffer prior to
changing records, or inserting new records.
Error messages can be logged in the error message array.
The messages that are to be logged should be started with a @.
Implementation note: it is wise to start the message with a
dedicated hard coded string, so it is clear to the end user that
the message logged is set in the Extension.
Pre:    NA
Post:   NA
Input:  i.shipment      - shipment
i.shipment.line - shipment line
i.handling.unit - handling unit
i.handling.unit.reused - picked handling unit is reused
Output: o.error.message.array()
Return: 0/DALHOOKERROR
```
