# SalesOrder.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2225-2226

Skips Sales Order when Printing. This process extension is available from 2023.09 ( KB2300881 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesOrder.SkipPrint can be used to skip Sales Orders
when Printing the Sales Order.
Session where this Process Extension can be implemented:
-               Print Sales Orders (tdsls4405m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Orders (tdsls400)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdsls400 data as
instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for sales
orders.
Hook: Declarations
table   ttdsls400       |* Sales Orders
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls400 = true> then
return(true)
endif
return (false)
}
```
