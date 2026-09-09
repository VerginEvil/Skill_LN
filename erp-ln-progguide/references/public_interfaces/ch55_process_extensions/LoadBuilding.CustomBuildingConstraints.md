# LoadBuilding.CustomBuildingConstraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for LoadBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2100-2100

```baan
Allows to perform additional load building constraints during load building.
This process extension is available from 2020.11 (KB2155039).
Technical information for this process extension:
Usage:        With this Process Extension it is possible to perform additional checks
on the load building process. During the load building, the
process will search for existing loads to add newly picked inventory to
be shipped with. There are however load building constraints which must
force Infor LN to not combine the picked inventory with a found load.
This process extension allows a customer to define custom load building
criteria to match the business case which is required.
To implement this process extension, you need to implement the following method(s):
```
