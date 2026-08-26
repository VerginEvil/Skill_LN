# Invoice.CustomComposingCriteriaMet

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2052-2052

Determines whether billable line should be composed in the current invoice number or not. This process extension is available from 2023.10 ( KB2305642 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to have custom composing
criteria defined by customer/extender to check whether the current
billable line should be composed in the current invoice or not. If
this Process Extenstion returns false then program will look for the
next available invoice number and if available then this process
extension is called again. If no invoice number is available then a
new invoice number will be created and this process extenstion will not
be called again.
```

To implement this process extension, you need to implement the following method(s):
