# ciext.sli0004.combine.advances.is.allowed

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Invoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2070-2071

```baan
Syntax: long ciext.sli0004.combine.advances.is.allowed(
ref             boolean          o.combine.advances.is.allowed )
Usage:        Expl:
Note:-  LN standard does not allow to compose advance billable
lines into one single invoice. Composing two or more
advance billable lines into one single invoice can have
consequences depending on Implementation and Parameter
settings for which LN standard will not be able to
provide a solution.
Use this method to check whether, at the time of composing,
the advance billable lines can be composed together in one
invoice.
At moment of composing Billable Line, LN will do own checks
first. According to the standard logic in LN, the Advance
invoices cannot be combined in one invoice and creates separate
invoice for each advance invoice.
But with this process extension, it will be possible to combine
two or more advance billable lines into one invoice.
In this method, own checks can be implemented and the variable
o.combine.advances.is.allowed can be set. If the variable
is set to true, then the advance billable lines will be composed
together in one single invoice subject to composing criteria.
Fields that are available to be used in this Process Extension:
- All fields of table: Billable lines (cisli810)
- All fields of table: Although the Invoice is not yet
committed, the Invoice Header (cisli305)
fields are already available. The Invoice
header key fields can be used to read
other tables like Invoice Lines
(cisli310) or Invoice Lines - Additional
Fields (cisli311).
The dal messages set in this function will be ignored by the
standard.
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.combine.advance.invoice.allowed
- Indicates whether the advance
billable lines can be combined.
Return: 0                       - Success
<> 0                    - Error
```
