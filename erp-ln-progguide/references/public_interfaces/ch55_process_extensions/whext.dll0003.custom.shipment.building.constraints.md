# whext.dll0003.custom.shipment.building.constraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ShipmentBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2269-2270

```baan
Syntax: long whext.dll0003.custom.shipment.building.constraints(
domain  whinh.shpm       i.found.shipment,
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order.number,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
ref             boolean          o.use.found.shipment )
Usage:        Expl:   This process extension allows for customer specific shipment
building constraints. This process extension is called from the
Infor LN standard, when one of the following events are
triggered:
- Create Projected Shipment
- Confirm Pick (when Outbound Inspections are not in use)
- Approve (when Outbound Inspections are in use)
- Cross Docking (when Confirmation of Receipt or Putaway of
Inbound Advice is done and the goods are to be
Cross-Docked or when Approve is done for the
Inbound Inspection where Cross-Docking should
be done in non location controlled warehouses.)
- Create Outbound Order Line for Cost/Service items which are
released to warehousing.
Note: This process extension is not called when composing a
shipment structure. The constraints that are applicable for the
shipment building should also be added as extension points for
composing shipments, via dedicated table / field extensions on
the related field, in line with the shipment building criteria.
The shipment building process will try to search for shipments
which are already present to perform the shipment of the newly
staged inventory to be shipped. Conditions apply on the
combinations which are allowed based on order type specific
shipment building criteria. This process extension allows to
define custom building criteria to be validated prior to
selecting the shipment for a newly created shipment line.
Table "Shipments" (whinh430) is current, for the
i.found.shipment.
Other data that is required to determine if the shipment can be
used can be retrieved by making use of the outbound order line
key, which is also part of the input of this process extension.
Setting the o.use.found.shipment to false will take care that
the i.found.shipment will not be used because a custom criteria
is not matching with the shipment and the new inventory moved to
the staging location.
Within Freight Management there is also a process extension
called "FreightShipmentBuilding.CustomBuildingConstraints" which
will be triggered during the generation of a plan. If freight
is implemented and used for planning purposes, it is advisable
to apply the same customer specific building criteria in freight
management, as otherwise the planning will be overruled by
warehousing.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.found.shipment        - Shipment that is found during shipment
building
Outbound Order Line Key
i.order.origin
i.order.number
i.order.line
i.order.sequence
Output: o.use.found.shipment    - Indicator if the found shipment should
be used (true/false)
Please also set an error message
regarding this shipment building
constraint, so the users will get
feedback when required.
Return: 0/DALHOOKERROR
```
