# tfext.cmg0002.custom.audit.payment.advice.line

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2118-2118

```baan
Syntax: long tfext.cmg0002.custom.audit.payment.advice.line(
ref             boolean          o.custom.audit.errors.present )
Usage:        Expl:   Use this method to define Custom specific auditing and
return errors if present.
Fields that are available to be used in this Process Extension:
- All fields from tfcmg101 are current (we are processing a
particular tfcmg101 line related to the current composed
payment line).
Default value of 'o.custom.audit.errors.present' should be set
to False.
If audit errors are found, these must be set via
dal.set.error.message() and the 'o.custom.audit.errors.present'
must be set to true.
Pre:    preconditions
Post:   postconditions
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.custom.audit.errors.present
- Indicates whether errors are present
in the custom logic of auditing the
payment advice line.
Return: 0                       - Success
DALHOOKERROR            - When an error occurs during custom
auditing.
```
