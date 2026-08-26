# whext.dll0009.check.generate.handling.unit.for.order.line

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for GenerateHandlingUnits
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2027-2028

```baan
Syntax: long whext.dll0009.check.generate.handling.unit.for.order.line(
boolean          i.inbound,
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
ref             boolean          o.generate.hu )
Usage:        Expl:   This function checks whether generating of handling unit
must be skipped for specific order line.
Pre:    N.a.
Post:   N.a.
Input:  i.inbound               -     Inbound or Outbound process
Inbound includes:       Inbound order line
ASN Line
Receipt Line
Inbound Advice
Inbound Inspection
Outbound                Outbound Advice
Outbound Inspection
Shipping Container
Shipment
Shipment Line
Output: o.generate.hu
Return: 0/DALHOOKERROR
```

## Process Extensions for GeneratePlan

The following process extension(s) is/are available: GeneratePlan.SkipOrderLine
