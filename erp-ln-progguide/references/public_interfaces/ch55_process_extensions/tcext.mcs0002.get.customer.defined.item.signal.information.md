# tcext.mcs0002.get.customer.defined.item.signal.information

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1988-1990

```baan
Syntax: long tcext.mcs0002.get.customer.defined.item.signal.information(
domain  tcncmp           i.company,
domain  tccsig           i.item.signal,
ref     domain  tcdsca           io.description mb,
ref     domain  tcblst           io.blcp,
ref     domain  tcbls2           io.blcs,
ref     domain  tcbls2           io.blsv,
ref     domain  tcblst           io.blpo,
ref     domain  tcblst           io.blpi,
ref     domain  tcblst           io.blps,
ref     domain  tcblst           io.blad,
ref     domain  tcblst           io.blcc,
ref     domain  tcblst           io.blrc,
ref     domain  tcblst           io.bloc,
ref     domain  tcblst           io.blac,
ref     domain  tcblst           io.blpl,
ref     domain  tcblst           io.blmi )
Usage:        Expl:   This process extension gets customer defined item signal
information.
The process extension is only called when the standard
signal information retrieval logic is executed correctly.
External variables available for use by this process extension
function:
-                       proc_ext_get_item_signal_info_item
[type: domain tcitem]
Related Item code.
-                       proc_ext_get_item_signal_info_site
[type: domain tcsite]
Related Site. Only used when the sites concept is
available.
Implementation Example:
Intention:
For a specific Site (For Example: Site                               - "ABC") and
Item (For Example: Item                               - XYZ), when Item Signal is
blocked it is still allowed to process further without
blocking for specific users profiles (For Example: Sales
User Profile Table                               - tdsls039).
Hook Declarations:
table ttdsls039
extern domain tcsite proc_ext_get_item_signal_info_site
extern domain tcitem proc_ext_get_item_signal_info_item
Hook tcext.mcs0002.get.customer.defined.item.signal.information:
function extern long tcext.mcs0002......
{
domain  tdtdgen.login   current.user
boolean         processing.allowed
processing.allowed = false
current.user = logname$
select  tdsls039.*
from    tdsls039
where   tdsls039._index1 = {:current.user}
and     tdsls039.site =
:proc_ext_get_item_signal_info_site
selectdo
processing.allowed = true
endselect
if      processing.allowed
and   proc_ext_get_item_signal_info_item =
"XYZ"
and   (io.blcs <> tcbls2.free
or    io.blcs <> tcbls2.no.warning)
then
io.blcs = tcblst.free
endif
return(0)
}
Pre:    NA
Post:   NA
Input:  i.company                             - Company to which the signal applies
i.item.signal                                 - Item Signal
Input/Output:
io.description                                - Item Signal Description
io.blcp                                       - Purchase Status
io.blcs                                       - Sales Status
io.blsv                                       - Service Status
io.blpo                                       - Requisition through Production Status
io.blpi                                       - Production Issue Status
io.blps                                       - Process Issue Status
io.blad                                       - Adjustments Status
io.blcc                                       - Cycle Counting Status
io.blrc                                       - Receipt Correction Status
io.bloc                                       - Ownership Change Status
io.blac                                       - Allocation Change Status
io.blpl                                       - Planning Status
io.blmi                                       - Miscellaneous Status
Return: 0                                     - Success
<> 0                                          - Error
```

## Process Extensions for ComposeShippingStructure

The following process extension(s) is/are available: ComposeShippingStructure.CommandHandling ComposeShippingStructure.CustomCommand
