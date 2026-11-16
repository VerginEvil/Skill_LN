# Invoice.SplitRevenueByComponent

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2085-2086

```baan
Split revenue amount in invoice currency by cost component for integration transactions.
This process extension is available from 2026.10 (KB3661191).
Technical information for this process extension:
Usage:        LN standard creates a single revenue line in the integration
transaction with the total revenue amount in invoice currency.
With this Process Extension, it is possible to split this revenue
amount per cost component. Each cost component and its splitted
amount in invoice currency will be inserted as separate lines
in the integration transactions (Sales Order/Revenue Analysis,
Warehouse Issue/Revenue Analysis).
To implement this process extension, you need to implement the following method(s):
```
