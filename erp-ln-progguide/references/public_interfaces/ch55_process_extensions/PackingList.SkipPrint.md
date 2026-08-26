# PackingList.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PackingList
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2093-2093

Skips Printing of Packing List. This process extension is available from 2023.11 ( KB2307865 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension PackingList.SkipPrint can be used
to skip the printing of a Packing List.
This process extension will be invoked when printing a Packing List,
either via session Print Packing Lists (whinh4476m000) or via the.   .   .   .   .
automatic printing of the shipping documents.
Fields that are available to be used in this Process Extension:
-               All fields of tables:
-                       Shipments (whinh430)
-                       Shipment Lines (whinh431)
```

## Process Extensions for PackingSlip

The following process extension(s) is/are available: PackingSlip.SkipPrint
