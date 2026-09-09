# ShipmentLine.SkipFreezeConfirm

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ShipmentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2271-2271

```baan
Skips Shipment Lines during Freeze/Confirm.
This process extension is available from 2026.09 (KB3690493).
Technical information for this process extension:
Usage:        Process Extension ShipmentLine.SkipFreezeConfirm can be used
to skip Shipment Lines during the freeze/confirm process.
Extender may specify a message, to present information about the skip
decision.
Note: This Process Extension will not be invoked when an Electronic
signature is required.
Fields that are available to be used in this Process Extension:
- All fields of tables:
- Shipment Lines (whinh431)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
Hook: Declarations
table twhinh431
Hook: ext.skip.with.reason
function extern boolean ext.skip.with.reason(ref string o.reason)
{
if <condition on whinh431 = true> then
o.reason = "Shipment Line skipped because ..."
return(true)
endif
return(false)
}
```
