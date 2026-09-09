# PaymentAdvice.SkipPrintPaymentAdvice

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2119-2120

```baan
Skips printing of a Payment Advice.
This process extension is available from 2023.09 (KB2297959).
To implement this process extension, you can use the information below:
Usage:        PaymentAdvice.SkipPrintPaymentAdvice can be used to skip
printing of a Payment Advice.
Session where this Process Extension can be implemented:
- Print Payment Advice (tfcmg1401m000)
Fields that are available to be used in this Process Extension:
- All fields of "Payment Advice"  (tfcmg101)
Note: tables must also be declared in the Process Extension.
Pseudocode:
Below you can find an example:
Hook: Declarations
table   ttfcmg101               |* Payment Advice
Hook: ext.skip
function extern boolean ext.skip()
{
if <condition on tfcmg101 = true> then
return(true)
endif
return (false)
}
```
