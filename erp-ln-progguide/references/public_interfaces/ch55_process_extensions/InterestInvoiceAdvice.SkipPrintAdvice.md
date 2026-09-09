# InterestInvoiceAdvice.SkipPrintAdvice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InterestInvoiceAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2057-2058

```baan
Skips printing of an Interest Advice.
This process extension is available from 2023.09 (KB2306340).
To implement this process extension, you can use the information below:
Usage:        InterestInvoiceAdvice.SkipPrintAdvice can be used to skip
Printing of an Interest Invoice Advice
Session where this Process Extension can be implemented:
- Print Interest-Invoice Advice (tfacr5410m000)
Fields that are available to be used in this Process Extension:
- All fields of "Selection of Cust. Invoices for Interest Invoice
Generation"  (tfacr510)
All fields of "Invoice to Business Partners" (tccom112)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfacr510       |* Selection of Cust. Invoices for Interest
|* Invoice Generation
table   ttccom112       |* Invoice to Business Partners
Hook: ext.skip
function extern boolean ext.skip()
{
if      <condition on tccom112 = true> and
<condition on tfacr510 = true> then
return(true)
endif
return (false)
}
```
