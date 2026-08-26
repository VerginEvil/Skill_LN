# HandlingUnitBuilding.CustomShipmentLine

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for HandlingUnitBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2031-2031

Allows to perform additional structure updates after a handling unit is reused or filled up. This process extension is available from 2019.11 ( KB2086985 ). Technical information for this process extension:

```baan
Usage:
With this Process Extension, it is possible to implement modifications
in the handling unit structure when a handling unit is linked to the
shipment line as a result of picking inventory or (re)generation of
handling units on a shipment line.
Note: This process extension will be called after the handling unit
has been linked to the shipment line. A handling unit can either be
generated, filled              -up (anonymous stock is put in an already existing
handling unit) or reused (picked handling unit is reused, or part of a
picked handling unit is reused).
```

To implement this process extension, you need to implement the following method(s):
