# tdext.sls0001.get.customer.defined.order.by

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesCheckInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2214-2215

```baan
Syntax: long tdext.sls0001.get.customer.defined.order.by(
ref             string           o.order.by.string.mb() )
Usage:        Expl:   Use this method to get a customer defined order by clause from
an extension. This order by clause will be used in 'Check
Inventory for Sales Orders' (tdsls4217m000) when the 'Sort Lines
By' option 'Customer Defined' is selected.
The standard order by clauses used by the 'Sort Lines By' are:
-                       Order Date:                   " order by tdsls417.odat asc "
-                       Customer Requested Date:      " order by tdsls417.ddtc asc "
-                       Planned Delivery Date:        " order by tdsls417.ddta asc "
Using 'Customer Defined' option, an order by constructed by
the extension could be, as an example:
" order by tdsls417.cdf_0001 desc, tdsls417.odat asc "
Note:
1. Only attributes from table tdsls417 can be used,
including customer defined fields.
2. Run time errors occur when specifying attributes from other
tables or when wrong syntax is constructed.
Pre:    NA
Post:   NA
Input:  NA
Output: o.order.by.string.mb                  - Maximum string length is 500. Multi
byte attributes are allowed.
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in determination of the
order by clause.
```
