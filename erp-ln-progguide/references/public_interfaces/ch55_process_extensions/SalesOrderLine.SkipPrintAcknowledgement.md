# SalesOrderLine.SkipPrintAcknowledgement

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2260-2261

```baan
Skips Sales Order Line when Printing Sales Order Acknowledgement.
This process extension is available from 2021.05 (KB2181867).
To implement this process extension, you can use the information below:
Usage:        Process Extension SalesOrderLine.SkipPrintAcknowledgement can be used
to skip Sales Order Lines when printing the Sales Order Acknowledgement.
Sessions where this Process Extension can be implemented:
- Print Sales Order Acknowledgements/RMAs (tdsls4401m000)
- All sessions and processes that trigger the printing of the
sales order acknowledgement (like automatic processing logic).
Fields that are available to be used in this Process Extension:
- All fields of table Sales Order (tdsls400)
- All fields of table Sales Order Line (tdsls401)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
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
