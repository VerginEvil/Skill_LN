# brext.qry0001.custom.query

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for FactoryTrackQuery
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2030-2033

```baan
Syntax: long brext.qry0001.custom.query(
domain  tcmcs.str40      i.query.bde,
long             i.query.number,
domain  tcmcs.s999       i.query.input,
ref     domain  tcmcs.str999m    o.error.message mb )
Usage:        Expl:   Use this method to define custom Factory Track queries.
Only query numbers greater than or equal to 100000 can be used
for custom queries.
Public interface FactoryTrackQuery.CreateRow can be used to
create output rows in the query output.
Public interface FactoryTrackQuery.CreateElement can be
used to create custom elements in the current query output row.
Example implementation:
IWMStdQuery 100001 lists the warehouses which have inventory on
hand for some item, ordered by descending quantity.
IWMStdQuery 100002 returns the buy-from business partner for
some lot code.
#pragma used dll obrextqryapi
#include <bic_dam>
function extern long brext.qry0001.custom.query(
domain  tcmcs.str40     i.query.bde,
long            i.query.number,
domain  tcmcs.s999      i.query.input,
ref     domain  tcmcs.str999m   o.error.message)
{
long            ret.val
long            exception.id
long            dummy.long
domain  tcitem          item
domain  tccwar          warehouse
domain  tcqiv1          quantity.on.hand
domain  tcclot          lot
domain  tccom.bpid      business.partner
domain  tcbpid.nama     business.partner.name
on case i.query.bde
case "IFTStdHUPackingQuery":
case "IFTStdTimeTrack":
case "IWMStdConsignmentWrhQuery":
case "IWMStdExtQuery":
case "IWMStdHoursQuery":
case "IWMStdKanQuery":
case "IWMStdPackingQuery":
o.error.message = "Invalid query number"
return(DALHOOKERROR)
case "IWMStdQuery":
on case i.query.number
case 100001:
item = strip$(i.query.input)
select  whwmd215.cwar :warehouse,
whwmd215.qhnd :quantity.on.hand
from    whwmd215
where   whwmd215._index2 = { :item }
order by whwmd215.qhnd desc
selectdo
ret.val = FactoryTrackQuery.CreateRow(
o.error.message,
exception.id)
if ret.val <> 0 then
return(ret.val)
endif
ret.val = FactoryTrackQuery.CreateElement(
"Warehouse",
domainof(warehouse),
o.error.message,
exception.id,
warehouse)
if ret.val <> 0 then
return(ret.val)
endif
ret.val = FactoryTrackQuery.CreateElement(
"QuantityOnHand",
domainof(quantity.on.hand),
o.error.message,
exception.id,
quantity.on.hand)
if ret.val <> 0 then
return(ret.val)
endif
selectempty
o.error.message = "Inventory not found"
return(DALHOOKERROR)
endselect
break
case 100002:
item = ""
lot = ""
dummy.long = string.scan(
i.query.input,
"%s~%s",
item,
lot)
business.partner = ""
business.partner.name = ""
select  whltc100.bfbp :business.partner,
tccom100.nama :business.partner.name
from    whltc100, tccom100
where   whltc100._index1 = {    :item,
:lot }
and     whltc100.bfbp refers to tccom100
unref clear
as set with 1 rows
selectdo
endselect
ret.val = FactoryTrackQuery.CreateRow(
o.error.message,
exception.id)
if ret.val <> 0 then
return(ret.val)
endif
ret.val = FactoryTrackQuery.CreateElement(
"BusinessPartner",
domainof(business.partner),
o.error.message,
exception.id,
business.partner)
if ret.val <> 0 then
return(ret.val)
endif
ret.val = FactoryTrackQuery.CreateElement(
"BusinessPartnerName",
domainof(business.partner.name),
o.error.message,
exception.id,
business.partner.name)
if ret.val <> 0 then
return(ret.val)
endif
break
default:
o.error.message = "Invalid query number"
return(DALHOOKERROR)
endcase
break
endcase
return(0)
}
Pre:    NA
Post:   NA
Input:
i.query.bde             - The called query bde
i.query.number          - The called query number
i.query.input           - The query input
Output:
o.error.message         - The error message in case of an error
Return:
0                       - Success
<> 0                    - Error
```
