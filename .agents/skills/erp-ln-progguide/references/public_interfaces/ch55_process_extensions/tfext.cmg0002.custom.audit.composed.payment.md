# tfext.cmg0002.custom.audit.composed.payment

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PaymentAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2117-2118

```baan
Syntax: long tfext.cmg0002.custom.audit.composed.payment(
ref             boolean          o.custom.audit.errors.present )
Usage:        Expl:   Use this method to define Custom specific auditing and
return errors if present.
Fields that are available to be used in this Process Extension:
- Below fields present in the select of tfcmg103, are current.
tfcmg103._index1 - Fields of Index 1
tfcmg103.amth    - Amount in Home Currency
tfcmg103.amnt    - Transaction Amount
tfcmg103.bank    - Bank
tfcmg103.ifbp    - Invoice-from Business Partner
tfcmg103.icmp    - Invoice Company
Default value of 'o.custom.audit.errors.present' should be set
to False.
If audit errors are found, these must be set via
dal.set.error.message() and the 'o.custom.audit.errors.present'
must be set to true.
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.custom.audit.errors.present
- Indicates whether errors are present
in the custom logic of auditing the
composed payment.
Return: 0                       - Success
DALHOOKERROR            - When an error occurs during custom
auditing.
```
