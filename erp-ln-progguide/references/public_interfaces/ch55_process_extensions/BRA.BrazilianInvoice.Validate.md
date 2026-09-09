# BRA.BrazilianInvoice.Validate

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BRA.BrazilianInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1990-1991

```baan
Modify the error checking of Brazilian invoices.
This process extension is available from 2026.04 (KB3665487).
Technical information for this process extension:
Usage:                With this Process Extension it is possible to modify the
validation of a invoice.
The function btext.sli0001.invoicing.extended.validation
allows query data and set custom error messages. If a custom
error exists, it will be displayed in the error report and it
won't be possible to send the invoice to the Brazilian tax
authority until the error is fixed.
To implement this process extension, you need to implement the following method(s):
```
