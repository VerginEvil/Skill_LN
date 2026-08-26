# whext.dll0002.check.handling.unit

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventorySearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2046-2047

```baan
Syntax: long whext.dll0002.check.handling.unit(
ref             boolean          o.skip.handling.unit,
ref     domain  tcmcs.str132m    o.error.message.array() fixed mb )
Usage:        Expl:   Use this method to validate/check or skip a handling unit from
the inventory search engine. This interface will be called
during the inventory search engine after all standard
validations and checks are performed.
When a handling unit must be skipped from the selection the
output variable o.skip.handling.unit should be set to true. When
also an error must be given to either the advice log or the end
user the output variable o.error.message.array() can be set.
When the handling unit is not to be skipped, the error message
array will still be used for logging messages in the advice log,
allowing the extension to tell the user which checks have been
performed, prior to using the inventory. The messages that are
to be logged should be started with a @. Implementation note:
It is wise to start the message with a dedicated hard coded
string, so it is clear to the end user that the message logged
is set in the Extension.
Following tables are current when this extension is triggered:
tcibd001                       - Item
tcmcs003                       - Warehouses
whinh220                       - Outbound Order Line
whinh200                       - Warehouse Order Header
whinh480                       - Planned Loads/Shipments
(when load planning part of the search engine)
whinh430                       - Shipments
(when projected shipments selection is enabled
for the search engine)
whinh431                       - Shipment Lines
(when projected shipments selection is enabled
for the search engine)
whwmd530                       - Handling Units
Pre:    NA
Post:   NA
Input:  NA
Output: o.skip.handling.unit
o.error.message.array()
Return: 0/DALHOOKERROR
```
