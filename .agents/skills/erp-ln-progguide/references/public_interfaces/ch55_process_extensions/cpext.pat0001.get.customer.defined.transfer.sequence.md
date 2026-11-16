# cpext.pat0001.get.customer.defined.transfer.sequence

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for TransferOrderPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2311-2312

```baan
Syntax: long cpext.pat0001.get.customer.defined.transfer.sequence(
domain  tckoor           i.order.type,
ref             string           o.order.by.string() )
Usage:        Expl:   This method is called during the transfer order process
(cppat1210m000) to get a custom defined order by clause from
an extension.
Note:
1. Attributes from tables cppat010 and cprrp100 can be used
in the order by clause, including customer defined
fields.
2. Errors will occur if attributes from other tables
are specified in the custom order by clause
3. Errors will occur if otherwise incorrect sql syntax is
constructed.
Example.
o.order.by.string = ""
if i.order.type = tckoor.cp.pur then
o.order.by.string =
" order by " &
"cppat010.cdf_0001 desc, " &
"cppat010.suno asc "
endif
return(0)
If this function returns an empty string in o.order.by.string,
then LN will use the standard order by clause.
The standard order by clauses vary per order type:
- Planned Production Order
" order by
cppat010.idnr,
cppat010.plnc,
cppat010.tort,
cppat010.orno,
cppat010.pono "
- Planned Purchase Order,
" order by
cppat010.suno,
cprrp100.cplb,
cprrp100.buyr,
cppat010.item,
cppat010.stdt,
cppat010.orno "
- Planned Subcontracting Order:
" order by
cppat010.suno,
cprrp100.cplb,
cppat010.item,
cppat010.stdt,
cppat010.orno "
- Planned Distribution Order
" order by
cprrp100.susi,
cppat010.item,
cppat010.stdt,
cppat010.orno "
Pre:    NA
Post:   NA
Input:  i.order.type            - The following order types are handled:
tckoor.cp.sfc
tckoor.cp.pur,
tckoor.cp.ipl,
tckoor.cp.sub
In case of other order types, LN will
use the standard order by clause.
Output: o.order.by.string       - Maximum string length is 500.
Return: 0
```
