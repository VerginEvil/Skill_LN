# ShipmentBuilding.CustomBuildingConstraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ShipmentBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2246-2246

Allows to perform additional shipment building constraints during shipment building. This process extension is available from 2020.11 ( KB2155039 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension it is possible to perform additional checks
on the shipment building process. During the shipment building, the
process will search for an existing shipment to ship the goods with.
There are however shipment building constraints which must force
Infor LN to not combine the picked inventory with a found shipment.
This process extension allows a customer to define custom shipment
building criteria to match the business case which is required.
```

To implement this process extension, you need to implement the following method(s):
