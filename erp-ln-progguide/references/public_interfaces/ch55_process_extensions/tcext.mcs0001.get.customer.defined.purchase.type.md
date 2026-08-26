# tcext.mcs0001.get.customer.defined.purchase.type

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1987-1988

```baan
Syntax: long tcext.mcs0001.get.customer.defined.purchase.type(
domain  tccom.bpid       i.invoice.from.bp,
domain  tcorig           i.order.origin,
domain  tccwoc           i.department,
domain  tccitg           i.item.group,
domain  tccprj           i.project,
domain  tcitem           i.item,
domain  tcccat           i.project.category,
domain  tcynna           i.direct.delivery,
domain  tcncmp           i.financial.company,
domain  tcpsty           i.purchase.type.from.standard,
ref     domain  tcpsty           o.purchase.type )
Usage:        Expl:   This process extension gets the customer determined Purchase
Type.
The process extension is only called when the standard
defaulting logic is executed correctly.
The customer determined Purchase Type should exists in session
'Purchase Type (tcmcs2101m000)'.
If no purchase type has been determined by customer then the
standard defaulted purchase type is returned.
Pre:    NA
Post:   NA
Input:  i.invoice.from.bp                     - Invoice-from Business Partner
i.order.origin                                - Order Origin
Possible Values:
-                               tcorig.pur            - Purchase
-                               tcorig.int.inv        - Internal Invoice
-                               tcorig.freight        - Freight
-                               tcorig.project        - Project
-                               tcorig.all            - All Origins
-                               tcorig.services.procm - Service Procurement Order
i.department                                  - Department
i.item.group                                  - Item Group
i.project                                     - Project
i.item                                        - Item
i.project.category                            - Project Category
i.direct.delivery                             - Direct Delivery
Possible Values:
-                               tcynna.yes    - Yes
-                               tcynna.no     - No
-                               tcynna.not.app- Not Applicable
i.financial.company                           - Financial Company
i.purchase.type                               - Purchase Type
(Defaulted from Standard LN logic)
Output: o.purchase.type                       - Purchase Type
(Determined from Extension)
Return: 0                                     - Success
<> 0                                          - This value will be ignored and the
standard defaulting logic will be
executed.
```
