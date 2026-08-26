# TransferOrderPlanning.CustomSorting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TransferOrderPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2282-2283

Define a custom sorting for transfer of Planned Orders. This process extension is available from 2024.06 ( KB2328644 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to set a customer defined
sorting for transfer of Planned Orders. This sorting will be used in
'Transfer Order Planning' (cppat1210m000).
Changing the sort sequence can have impact on the number of created orders.
E.g. Depending on settings in Procurement, multiple planned purchase orders
can be grouped by buy              -from business partner, planner and buyer into one
purchase order. Changing the sort sequence can result in much more created
purchase orders, all having one or a limited number of lines.
As the number of possible sort sequences is almost infinite,
there is no guarantee that all possible sort sequences will be handled
correctly by LN.
```

To implement this process extension, you need to implement the following method(s):
