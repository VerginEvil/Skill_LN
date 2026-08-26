# whext.dll0004.custom.load.building.constraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for LoadBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2079-2081

```baan
Syntax: long whext.dll0004.custom.load.building.constraints(
domain  whinh.load       i.found.load,
domain  whinh.shpm       i.found.shipment,
domain  whinh.oorg       i.order.origin,
domain  tcorno           i.order.number,
domain  tcpono           i.order.line,
domain  tcpono           i.order.sequence,
ref             boolean          o.use.selected.load )
Usage:        Expl:   This process extension allows for customer specific load
building constraints. This process extension is called from the
Infor LN standard, when one of the following events are
triggered:
-                       Create Projected Shipment
-                       Confirm Pick (when Outbound Inspections are not in use)
-                       Approve (when Outbound Inspections are in use)
-                       Cross Docking (when Confirmation of Receipt or Putaway of
Inbound Advice is done and the goods are to be
Cross                                       -Docked or when Approve is done for the
Inbound Inspection where Cross                                       -Docking should
be done in non location controlled warehouses.)
-                       Create Outbound Order Line for Cost/Service items which are
released to warehousing.
Note: This process extension is not called when composing a
load structure. The constraints that are applicable for the
load building should also be added as extension points for
composing loads, via dedicated table / field extensions on
the related field, in line with the load building criteria.
The load building process will try to search for loads
which are already present to perform the shipment of the newly
staged inventory to be shipped. Conditions apply on the
combinations which are allowed based on order type specific
load building criteria. This process extension allows to
define custom building criteria to be validated prior to
selecting the load for a newly created shipment and shipment
line.
When a shipment is found, which is suitable to perform the
shipping of the outbound order line, it can be that the load
will not allow to add a new shipment line, due to customer
defined constraint. The i.found.shipment is filled
only when there is also a shipment found in the shipment
building process, otherwise the i.found.shipment will be empty.
Table "Loads" (whinh440) is current, for the i.found.load.
Other data that is required to determine if the load can be
used can be retrieved by making use of the outbound order line
key, which is also part of the input of this process extension.
Setting the o.use.selected.load to false will take care that the
i.found.load will not be used because a custom criteria is not
matching with the load and the new inventory moved to the
staging location.
Within Freight Management there is also a process extension
called "FreightLoadBuilding.CustomBuildingConstraints" which
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
Input:  i.found.load                          - Load that is found during load
building
i.found.shipment                              - Shipment that is found during shipment
building
Outbound Order Line Key
i.order.origin
i.order.number
i.order.line
i.order.sequence
Output: o.use.selected.load                   - Indicator if the found load should
be used (true/false)
Please also set an error message
regarding this shipment building
constraint, so the users will get
feedback when required.
Return: 0/DALHOOKERROR
```

## Process Extensions for LocationSearchEngine

The following process extension(s) is/are available: LocationSearchEngine.CheckLocation
