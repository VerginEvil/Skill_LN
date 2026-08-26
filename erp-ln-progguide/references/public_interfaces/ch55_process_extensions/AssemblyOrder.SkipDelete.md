# AssemblyOrder.SkipDelete

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1949-1950

Skips Assembly Orders when deleting. This process extension is available from 2022.11 ( KB2230993 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension AssemblyOrder.SkipDelete can be used to skip certain
Assembly Orders when requesting the deletion of a range of Assembly
Orders.
Sessions where this Process Extension can be implemented:
-               Delete Assembly Orders (tiasc2200m000)
Fields that are available to be used in this Process Extension:
-               tiasc200.pvar  - tiasc200.ncmp - tiasc200.asso - tiasc200.asst
-               tiasc200.block - tiasc200.porn - tiasc200.posi - tiasc200.asln
-               tiasc200.smcs  - tiasc200.plod
```
