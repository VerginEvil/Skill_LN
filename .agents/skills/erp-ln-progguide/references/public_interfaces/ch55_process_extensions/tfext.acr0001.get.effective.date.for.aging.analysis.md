# tfext.acr0001.get.effective.date.for.aging.analysis

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for AccountsReceivable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1966-1967

```baan
Syntax: long tfext.acr0001.get.effective.date.for.aging.analysis(
boolean          i.schedule,
ref     domain  tfgld.date       io.effective.date )
Usage:        Expl:
Use this Process Extension method to get a custom defined
effective date in session Calculate Receivables Aging Analysis
(tfacr2511m000). The session Calculate Receivables Aging Analysis
(tfacr2511m000) will then calculate the age of an invoice/schedule
based on this custom defined effective date.
Only if an implementation is done for this Process Extension,
and the Process Extension method is returning 0,
and the input/output parameter io.effective.date is filled
will the Document Date field (tfacr200.docd) and the Due date fields
(tfacr200.dued & tfacr201.recd) be filled with this
custom defined effective date.
Then in session Calculate Receivables Aging Analysis
(tfacr2511m000) this custom defined effective date is then used
to calculate the age of an invoice/schedule.
Pre:    N.A.
Post:   N.A.
Input:  i.schedule              - This field indicates whether the function
is called from an invoice or schedule line.
If false this function is called from
an invoice and the tfacr200 record
is current.
If true this funtion is called from
a schedule line and the tfacr201 record
is current.
IO:     io.effective.date       - This field is standard filled already.
If the aging calculation is based on
Document Date this field is filled with
tfacr200.docd (Document Date).
If the aging calculation is based on
Due Date this field is filled with
tfacr200.dued or tfacr201.recd (Due Date).
This field can be influenced by the
process extension based on own logic
e.g. a CDF on invoice or schedule line.
Return: 0                       - Success
DALHOOKERROR            - When an error occurs in setting
the effective date.
```
