# tdext.cms0001.commission.rebates.determine.tax.country

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for CommissionsRebates
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1983-1985

```baan
Syntax: long tdext.cms0001.commission.rebates.determine.tax.country(
domain  tdcms.type       i.type,
domain  tcorno           i.sales.order,
domain  tcpono           i.sales.order.line,
domain  tcpono           i.sales.order.line.sequence,
domain  tcpono           i.actual.delivery.line.sequence,
domain  tcpono           i.invoice.line,
domain  tccom.bpid       i.relation,
domain  tcpono           i.serial.number,
domain  tcccty           i.relation.country,
domain  tcccty           i.tax.country.from.standard.logic,
ref     domain  tcccty           o.tax.country )
Usage:        Expl:   Use this method to get a customer determined tax country
from an extension. This tax country will be used in
Commissions and Rebates.
Note:
This method allows you to return different tax countries as
needed. Please be aware that during the invoice creation
process, each time a different tax country is returned (compared
to the previous one), a new invoice will be generated. If your
custom tax country determination logic produces alternating or
widely varying tax countries, this may result in the creation of
many invoices.
Invocation Contexts:
The method can be invoked from two distinct contexts:
* CMS Invoicing flow
The first 8 input arguments uniquely identify a record from
table tdcms050. These arguments can be used to read
additional data from tdcms050, or from any of the sales
order related tables.
* Master                        -data context
When the method is invoked in a master                          -data context, the
first eight input arguments are left empty except for the
input argument i.relation, which will be populated
if available. This means that, in this context, only
i.relation among the initial eight arguments may contain a
value; all others remain unset.
Fallback Logic:
If either of the following situations occurs:
* The extension returns a non                        -zero return-value, or
* The tax                        -country is left empty
Then, LN will automatically revert to the standard tax                      -country
determination logic.
Pre:    NA
Post:   NA
Input:  i.type                                        - Type
Possible value(s):
* tdcms.type.commission
(Commission)
* tdcms.type.rebate
(Rebate)
i.sales.order                                         - Sales Order
i.sales.order.line                                    - Sales Order Line
i.sales.order.line.sequence                           - Sales Sequence number
i.actual.delivery.line.sequence                       - Sales Actual Delivery
Sequence number
i.invoice.line                                        - Invoice Line
i.relation                                            - Relation
i.serial.number                                       - Serial Number
i.relation.country                                    - Relation Country
i.tax.country.from.standard.logic
-                                                       Tax Country, as determined by
the standard logic
Output: o.tax.country                                 - Tax Country, as determined by
the extension logic
Return: 0                                     -       Success
DALHOOKERROR                                  -       When an error occurs in the
determination of the tax country
```
