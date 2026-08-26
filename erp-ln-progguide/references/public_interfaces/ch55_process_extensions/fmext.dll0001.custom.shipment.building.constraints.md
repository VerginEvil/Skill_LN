# fmext.dll0001.custom.shipment.building.constraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FreightShipmentBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2024-2026

```baan
Syntax: long fmext.dll0001.custom.shipment.building.constraints(
domain  tcorno           i.found.shipment,
domain  tcorno           i.freight.order,
domain  tcpono           i.freight.order.line,
ref             boolean          o.use.found.shipment )
Usage:        Expl:   This process extension allows for customer specific shipment
building constraints. This process extension is called from the
Infor LN standard, when generating a freight plan.
Note: This process extension is not called when composing a
shipment structure. The constraints that are applicable for the
shipment building should also be added as extension points for
composing shipments, via dedicated table / field extensions on
the related field, in line with the shipment building criteria.
The shipment building process will try to search for shipments
which are already present to perform the shipment.
Conditions apply on the combinations which are allowed based on
order type specific shipment building criteria. This process
extension allows to define custom building criteria to be
validated prior to selecting the shipment for a newly created
shipment line.
Table "Shipments" (fmlbd300) is current, for the
i.found.shipment.
Other data that is required to determine if the shipment can be
used can be retrieved by making use of the freight order line
key, which is also part of the input of this process extension.
Setting the o.use.found.shipment to false will take care that
the i.found.shipment will not be used as a custom criteria is
not matching with the shipment and the related freight order
line.
Within Warehousing there is also a process extension
called "ShipmentBuilding.CustomBuildingConstraints" which
will be triggered during the shipment building in Warehousing.
It is advisable to apply the same customer specific building
criteria in Warehousing, as otherwise the planning will be
overruled by warehousing.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.found.shipment                      - Shipment that is found during shipment
building
i.freight.order                               - Freight Order
i.freight.order.line                          - Freight Order Line
Output: o.use.found.shipment                  - Indicator if the found shipment should
be used (true/false)
Return: 0/DALHOOKERROR
```

## Process Extensions for

## GenerateFieldChangeOrderLine

The following process extension(s) is/are available: GenerateFieldChangeOrderLine.SkipSerializedItem
