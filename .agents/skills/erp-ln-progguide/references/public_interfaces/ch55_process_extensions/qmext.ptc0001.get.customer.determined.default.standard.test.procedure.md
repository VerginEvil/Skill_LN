# qmext.ptc0001.get.customer.determined.default.standard.test.procedure

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for QualityManagement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2216-2217

```baan
Syntax: long qmext.ptc0001.get.customer.determined.default.standard.test.procedure(
domain  qmptc.orgn       i.origin,
domain  tcitem           i.item,
domain  tcorno           i.order,
domain  tcpono           i.line,
domain  tccom.bpid       i.business.partner,
domain  tcitem           i.sub.item,
domain  tcedm.revi       i.revision,
domain  tcuef.effn       i.effectivity.unit,
domain  tcedm.revi       i.sub.item.revision,
domain  tcuef.effn       i.sub.item.effectivity.unit,
domain  tirou.opro       i.routing,
domain  tcopno           i.operation,
domain  tctano           i.task,
domain  tcsite           i.from.site,
domain  tcsite           i.to.site,
domain  tccwar           i.warehouse.from,
domain  tccwar           i.warehouse.to,
domain  qmrpt.wstt       i.work.station,
domain  qmptc.quid       i.stp.from.stnd.logic,
domain  qmptc.srno       i.version.from.stnd.logic,
ref     domain  qmptc.quid       o.standard.test.procedure,
ref     domain  qmptc.srno       o.version )
Usage:        Expl:   Use this method to get a customer determined default standard
test procedure from an extension. This standard test procedure
will be used in creation of Order Inspection in Quality Management.
The standard logic in LN determines the standard test procedure
for the given set of data.
Using this process extension, the defaulted value can be
changed to customer given value.
Note:
1. The input arguments can be used to determine the option.
2. LN will check if the provided default is valid.
3. The standard test procedure defaulted based on standard LN
logic will overrule the selected standard test procedure from
the extension when it is not valid or not given, otherwise
standard logic will fail for creation on QM Order Inspection.
Pre:    NA
Post:   NA
Input:  i.origin -> Origin
i.item -> Item
i.business.partner -> Business Partner (For Sales/Purchase)
i.order -> order
i.line -> Line (For Material (BOM))
i.sub.item -> Sub Item (For Material (BOM))
i.routing -> Routing (For Routing)
i.operation -> Operation (For Routing)
i.task -> Task (For origin Routing)
i.work.station  -> Work Station (for origin Routing (RPT))
i.warehouse.from -> Source warehouse (For Warehouse Transfer)
i.warehouse.to -> To Warehouse (For Warehouse Transfer)
i.work.station -> Work Station
i.stp.from.stnd.logic -> As defaulted under the standard logic
i.version.from.stnd.logic -> As defaulted under the standard logic
Output: o.standard.test.procedure - The standard test procedure
determined by the extension.
o.version       - The Version determined by the extension
Return: 0       -       Success
DALHOOKERROR    - Otherwise.
```
