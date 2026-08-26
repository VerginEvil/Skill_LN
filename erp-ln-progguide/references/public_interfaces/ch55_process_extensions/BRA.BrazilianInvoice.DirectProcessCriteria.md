# BRA.BrazilianInvoice.DirectProcessCriteria

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1969-1969

Define a customized direct process criteria for Brazilian invoices. This process extension is available from 2026.04 ( KB3665487 ). Technical information for this process extension:

```baan
Usage:                With this Process Extension it is possible to modify the
criteria for the invoicing direct process for generating the
Brazilian invoice, thus, modifying the behavior of submitting
it to the external system.
The function
lpext.dll0001.BRA.get.custom.direct.process.criteria
allows to modify the rules based on a personalized search
query using a set of data.
The index 1 of the 'Billable Lines' table (cisli810) and
the search result of the 'Direct Process Matrix' (lpbra014)
are provided.
```

To implement this process extension, you need to implement the following method(s):
