# tfext.gld0003.set.document.series

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IntegrationTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2055-2056

```baan
Syntax: long tfext.gld0003.set.document.series(
domain  tcguid           i.integration.transaction.guid,
domain  tfgld.date       i.integration.transaction.date,
domain  tfgld.year       i.integration.transaction.financial.year,
domain  tfgld.prod       i.integration.transaction.financial.period,
ref     domain  tfgld.seri       io.document.series )
Usage:        Expl:
Use this Process Extension to influence the Series to be used
for creating a Document during Posting Integration Transactions
(tfgld4282m000).
Standard, the Document Series comes from the Mapping Scheme.
With this Process Extension, the Document Series can be overwritten.
This is needed if e.g. the Series depends on the Financial Period.
Pre:    N.A.
Post:   N.A.
Input:  i.integration.transaction.guid
- Unique ID of the Integration Transaction.
i.integration.transaction.date
- Transaction Date (non-UTC) of the
Integration Transaction.
i.integration.transaction.financial.year
- Financial (Fiscal) Year of the
Integration Transaction (Credit).
i.integration.transaction.financial.period
- Financial (Fiscal) Period of the
Integration Transaction (Credit).
IO:     io.document.series      - The Document Series used by the
Standard (derived from the Mapping
Scheme) is passed to the function.
In the implementation, it can be
overwritten by another Series (e.g.
because it depends on the Fiscal Year).
Output: N.A.
Return: 0                       - Success
DALHOOKERROR            - Error situation
Example:
if i.integration.transaction.financial.year = 2026 then
io.document.series = 26
endif
```
