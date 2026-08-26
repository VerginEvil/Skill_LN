# SalesOrder.SkipPrintAcknowledgement

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2226-2227

Skips Sales Order when Printing Sales Order Acknowledgement. This process extension is available from 2019.09 ( KB2076283 ). To implement this process extension, you can use the information below:

```baan
Usage:        Process Extension SalesOrder.SkipPrintAcknowledgement can be used
to skip Sales Orders when printing the Sales Order Acknowledgement.
Sessions where this Process Extension can be implemented:
-               Print Sales Order Acknowledgements/RMAs (tdsls4401m000)
-               All sessions and processes that trigger the printing of the
sales order acknowledgement (like automatic processing logic).
Fields that are available to be used in this Process Extension:
-               All fields of table Sales Order (tdsls400)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
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
