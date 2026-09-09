# ciext.sli0005.split.revenue.by.component

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2086-2087

```baan
Syntax: long ciext.sli0005.split.revenue.by.component(
domain  tcncmp           i.financial.company,
domain  tctran           i.transaction.type,
domain  tcgld.docn       i.invoice.number,
domain  tcamnt           i.invoice.revenue.amount,
domain  tcccur           i.invoice.currency,
ref             long             o.no.cost.components,
ref     domain  tccpcp           o.cost.components() fixed,
ref     domain  tcamnt           o.split.invoice.revenue.amounts(),
ref     domain  tccpcp           o.cost.component.for.rounding.diff )
Usage:        Expl:   Use this method to split the revenue amount (in invoice
currency) into multiple cost components. Each cost component
and its corresponding split amount will be inserted as a
separate line in the integration transactions.
This process extension is called during the revenue analysis
posting of invoice and is only applicable for Source Type:
1) Sales Orders
2) Intercompany Trade Orders
The standard creates a single integration transaction line
with the total revenue amount. By implementing this process
extension, the revenue amount can be split per cost component
resulting in multiple integration transaction lines.
Note:
1) The sum of all split amounts
(o.split.invoice.revenue.amounts) MUST equal the input revenue
amount (i.invoice.revenue.amount).
If the sum does not equal, then standard will stop the process
and return error.
2) It is expected that the number of cost components
(o.no.cost.components) will be equal to the array size of
o.cost.components and o.split.invoice.revenue.amounts.
3) It is expected that the split amounts
o.split.invoice.revenue.amounts are already rounded.
If there is a rounding difference between the standard LN
revenue amount in home currency and the total of the split
amounts in home currency, the cost component specified in
o.cost.component.for.rounding.diff will be used to post the
rounding difference.
If the cost component for rounding difference is empty then
customer is expected to run session tfgld4295m500 after posting
of the invoice is completed.
Fields that are available to be used in this Process Extension:
- All fields of table: Invoice Lines (cisli310)
- The input invoice key fields can be used to select fields
from cisli305.
The dal messages set in this function will be ignored by the
standard.
Known Limitations and Considerations: -
1) Revenue Recognition does not support cost-component-level
splitting. Revenue invoiced may be split, but revenue
recognized will not be, which can lead to differences that
are not handled automatically.
2) Interim Revenue (SBI): - Sales Schedule SBI-related interim
revenue transactions are not split by cost component.
This is a functional limitation.
3) Segment reporting is not supported with this process
extension.
Pre:    N.A.
Post:   N.A.
Input:  i.financial.company     - Financial company of the invoice
i.transaction.type      - Transaction type of the invoice
i.invoice.number        - Invoice number of the invoice
i.invoice.revenue.amount- Total revenue amount in invoice
currency to be split
i.invoice.currency      - Currency of the Invoice
Output: o.no.cost.components    - Number of cost components returned
o.cost.components       - Array of cost components
o.split.invoice.revenue.amounts
- Array of split amounts in invoice
currency per cost component
o.cost.component.for.rounding.diff
- Cost component to be used if there is
a rounding difference between the
standard LN revenue amount in home
currency and the total of split
amounts in home currency
Return: 0                       - Success
<> 0                    - Error
```
