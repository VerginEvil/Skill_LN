# FreightShipmentBuilding.CustomBuildingConstraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FreightShipmentBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2043-2043

```baan
Allows to perform additional shipment building constraints during generate plan.
This process extension is available from 2020.11 (KB2155039).
Technical information for this process extension:
Usage:        With this Process Extension it is possible to perform additional checks
on the shipment building process. During the shipment building, the
process will search for an existing shipment to ship the goods with.
There are however shipment building constraints which must force
Infor LN to not combine the freight order line with a found shipment.
This process extension allows a customer to define custom shipment
building criteria to match the business case which is required.
To implement this process extension, you need to implement the following method(s):
```
