# GeneratePlan.SkipOrderLine

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for GeneratePlan
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2047-2047

```baan
Allows to skip Freight Order line from generating a freight plan.
This process extension is available from 2025.06 (KB3565345).
To implement this process extension, you can use the information below:
Usage:        Process Extension GeneratePlan.SkipOrderLine can be used to skip
Freight Order line from a load planning.
For all instances where freight plans are generated this process
extension will be invoked.
Fields that are available to be used in this Process Extension:
- All fields of tables:
- Freight Order (fmfoc200)
- Freight Order Lines (fmfoc201)
In case of replaning the existing plans:
- All fields of tables:
- Freight Order Lines to Be Replanned (fmlbd020)
```
