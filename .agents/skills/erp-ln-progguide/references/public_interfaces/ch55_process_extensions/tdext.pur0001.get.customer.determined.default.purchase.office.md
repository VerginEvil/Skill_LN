# tdext.pur0001.get.customer.determined.default.purchase.office

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Procurement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2152-2153

```baan
Syntax: long tdext.pur0001.get.customer.determined.default.purchase.office(
domain  tcmcs.str8       i.defaulting.origin,
domain  tccwoc           i.purchase.office.from.standard.logic,
domain  tcemm.grid       i.enterprise.unit,
domain  tccom.bpid       i.buy.from.business.partner,
domain  tccom.bpid       i.ship.from.business.partner,
domain  tcitem           i.item,
domain  tcncmp           i.logistic.company,
domain  tcsite           i.site,
domain  tccwar           i.warehouse,
ref     domain  tccwoc           o.purchase.office )
Usage:        Expl:   Use this method to get a customer determined default purchase
office from an extension. This office will be used in
Procurement.
The standard logic in LN determines the purchase office from
master data like enterprise unit, item data or user profile.
Using this process extension, the defaulted value can be
changed to another value.
Note:
1. The input arguments can be used to determine the option.
2. LN will check if the provided default is valid.
3. The purchase office defaulted based on standard LN logic will
overrule the selected office from the extension, otherwise
standard logic may fail.
Pre:    NA
Post:   NA
Input:  i.defaulting.origin                     - Defaulting Origin,
Possible Values:
tdpur100 - RFQ
tdpur200 - Purchase Requisition
tdpur300 - Purchase Contract
tdpur310 - Purchase Schedule
tdpur400 - Purchase Order
tdpur600 - Services Procurement Order
Empty    - Generation of a purchase order /
schedule via 'generate purchase
order/schedule flows' when e.g.,
calling from other packages (Project,
Service, Warehousing, etc.).
i.purchase.office.from.standard.logic   - As defaulted under the
standard logic
i.enterprise.unit                       - Enterprise Unit
i.buy.from.business.partner             - Buy-from Business
Partner
i.ship.from.business.partner            - Ship-from Business
Partner
i.item                                  - Item
i.logistic.company                      - Logistic Company
i.site                                  - Site
i.warehouse                             - Warehouse
Output: o.purchase.office                       - The purchase office
determined by the
extension.
Return: 0                       -       Success
DALHOOKERROR            -       When an error occurs in the
determination of the purchase
office.
```
