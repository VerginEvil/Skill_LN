# fmext.dll0002.custom.load.building.constraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FreightLoadBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2023-2024

```baan
Syntax: long fmext.dll0002.custom.load.building.constraints(
domain  tcorno           i.found.load,
domain  tcorno           i.freight.order,
domain  tcpono           i.freight.order.line,
ref             boolean          o.use.found.load )
Usage:        Expl:   This process extension allows for customer specific load
building constraints. This process extension is called from the
Infor LN standard, when generating a freight plan.
Note: This process extension is not called when composing a
load structure. The constraints that are applicable for the
load building should also be added as extension points for
composing load, via dedicated table / field extensions on
the related field, in line with the load building criteria.
The load building process will try to search for load which are
already present to perform the load.
Conditions apply on the combinations which are allowed based on
order type specific load building criteria. This process
extension allows to define custom building criteria to be
validated prior to selecting the load for a newly created
shipment and shipment line.
Table "Loads" (fmlbd400) is current, for the
i.found.load.
Other data that is required to determine if the load can be
used can be retrieved by making use of the freight order line
key, which is also part of the input of this process extension.
Setting the o.use.found.load to false will take care that the
i.found.load will not be used as a custom critiria is not
matching with the load and the related freight order line.
Within Warehousing there is also a process extension
called "LoadBuilding.CustomBuildingConstraints" which
will be triggered during the load building in Warehousing.
It is advisable to apply the same customer specific building
criteria in Warehousing, as otherwise the planning will be
overruled by warehousing.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.found.load                          - Load that is found during load
building
i.freight.order                               - Freight Order
i.freight.order.line                          - Freight Order Line
Output: o.use.found.load                              - Indicator if the found load should
be used (true/false)
Return: 0/DALHOOKERROR
```

## Process Extensions for FreightShipmentBuilding

The following process extension(s) is/are available: FreightShipmentBuilding.CustomBuildingConstraints
