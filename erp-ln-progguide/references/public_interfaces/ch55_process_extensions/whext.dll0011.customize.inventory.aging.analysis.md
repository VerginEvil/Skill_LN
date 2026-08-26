# whext.dll0011.customize.inventory.aging.analysis

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventoryAgingAnalysis
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2043-2043

```baan
Syntax: long whext.dll0011.customize.inventory.aging.analysis(
domain  tcmcs.long       i.storage.time.in.seconds,
domain  tcdate           i.reference.date,
domain  tcqiv1           i.quantity,
domain  tcamnt           i.amount )
Usage:        Expl:   This process extension allows for customer specific inventory
analysis constraints. This process extension is called from the
Infor LN standard, after function
assign.quantity.and.amount.to.period is called.
Table "Inventory Receipt Transactions" (whina112) is current.
Input fields can for example be used extend the number of Aging
Periods on the report or overwrite the quantity/amount for a
certain Period by filling of a TX table.
Input fields are the same as those who are used for calling
function assign.quantity.and.amount.to.period.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.storage.time.in.seconds
i.reference.date
i.quantity
i.amount
Output: N.a.
Return: 0/DALHOOKERROR
```
