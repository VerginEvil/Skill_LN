# tdext.sls0008.sales.order.line.allow.display.selected.contract

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2234-2235

```baan
Syntax: long tdext.sls0008.sales.order.line.allow.display.selected.contract(
domain  tccono           i.contract,
domain  tcpono           i.contract.line,
domain  tccwoc           i.contract.office,
domain  tcitem           i.item,
domain  tccom.bpid       i.sold.to.bp,
domain  tccom.bpid       i.ship.to.bp,
boolean          i.display.selected.contract.from.standard.logic,
ref             boolean          o.display.selected.contract.from.extension )
Usage:        Expl:   Use this method to determine if the only one selected contract for the
sales order line is allowed to start session "Selected Sales Contract
Lines" (tdsls3512s000), while the standard would not start it when only
one valid contract is found. Subsequently, the contract can be manually
linked or not.
Using this process extension, the 'display selected contract' variable
from standard logic can be changed.
The 'display selected contract' from extension is only retrieved
and used if:
-                       Process Extension SalesOrderLine.AllowDisplaySelectedContract
(tdsls.sol.allow.disp.sel.contr) is implemented;
-                       No errors are found during executing the extension.
Pre:    Not applicable
Post:   Not applicable
Input:  i.contract                            - Sales Contract
i.contract.line                               - Sales Contract Line
i.contract.office                             - Sales Contract Office
i.item                                        - Item
i.sold.to.bp                                  - Sold-to Business Partner
i.ship.to.bp                                  - Ship-to Business Partner
i.display.selected.contract.from.standard.logic                       -
As defaulted under the standard logic
Output: o.display.selected.contract.from.extension                    -
The 'display selected contract' (true/false) determined
by the extension
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the determination
of the 'display selected contract' from
extension
```
