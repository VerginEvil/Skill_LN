# SalesOrder.SkipApprove

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2225-2225

Skips Sales Order when Approving. This process extension is available from 2019.09 ( KB2076283 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesOrder.SkipApprove can be used
to skip Sales Orders when Approving the Sales Order.
Sessions where this Process Extension can be implemented:
-               Approve Sales Orders (tdsls4211m000).
-               All sessions and processes that trigger the Approve.
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Order (tdsls400).
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example.
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
