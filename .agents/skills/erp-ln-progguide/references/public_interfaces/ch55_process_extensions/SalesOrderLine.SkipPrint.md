# SalesOrderLine.SkipPrint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2260-2260

```baan
Skips Sales Order Line when Printing.
This process extension is available from 2023.09 (KB2300881).
To implement this process extension, you can use the information below:
Usage:        Process Extension SalesOrderLine.SkipPrint can be used to skip specific
Sales Order Lines when Printing the Sales Order.
Session where this Process Extension can be implemented:
- Print Sales Order Lines (tdsls4409m000)
Fields that are available to be used in this Process Extension:
- All fields of table Sales Order (tdsls400)
- All fields of table Sales Order Lines (tdsls401)
Note: Tables must also be declared in the Process Extension.
So skip conditions can be built on current tdsls400 and
tdsls401 data as instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for sales
order lines.
Hook: Declarations
table   ttdsls400       |* Sales Orders
table   ttdsls401       |* Sales Order Lines
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls401 = true> then
return(true)
endif
return (false)
}
```
