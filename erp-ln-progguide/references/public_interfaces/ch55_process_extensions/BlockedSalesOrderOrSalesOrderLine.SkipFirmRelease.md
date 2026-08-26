# BlockedSalesOrderOrSalesOrderLine.SkipFirmRelease

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BlockedSalesOrderOrSalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1957-1958

Skips Blocked Sales Order or Sales Order Line when executing Form Command 'Firm Release'. This process extension is available from 2025.02 ( KB3553809 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension BlockedSalesOrderOrSalesOrderLine.SkipFirmRelease can be
used to skip specific Blocked Sales Orders or Sales Order Lines when executing
Form Command "Firm Release".
Session where this Process Extension can be implemented:
-               Blocked Sales Order (Lines) (tdsls4520m000)
Fields that are available to be used in this Process Extension:
-               All fields of table Order (Line) Blocking (tdsls420)
Note: Table must also be declared in the Process Extension.
So skip conditions can be built on current tdsls420 data as
instructed below.
Pseudocode:
Here you can find an example how to handle the conditions for blocked
sales order (line)s.
Hook: Declarations
table   ttdsls420       |* Order (Line) Blocking
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tdsls420 = true> then
return(true)
endif
return (false)
}
```
