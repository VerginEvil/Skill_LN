# FreightLoadBuilding.CustomBuildingConstraints

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FreightLoadBuilding
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2041-2042

```baan
Allows to perform additional load building constraints during generate plan.
This process extension is available from 2020.11 (KB2155039).
Technical information for this process extension:
Usage:        With this Process Extension it is possible to perform additional checks
on the load building process. During the load building, the
process will search for an existing loads to ship the goods with.
There are however load building constraints which must force
Infor LN to not combine the freight order line with a found load.
This process extension allows a customer to define custom load
building criteria to match the business case which is required.
To implement this process extension, you need to implement the following method(s):
```
