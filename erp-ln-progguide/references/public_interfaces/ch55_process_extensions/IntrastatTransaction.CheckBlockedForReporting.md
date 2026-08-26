# IntrastatTransaction.CheckBlockedForReporting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IntrastatTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2040-2041

Check whether, at adding Intrastat Transaction, the status must be set to Blocked for Reporting. This process extension is available from 2024.10 ( KB3532922 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to have additional checks
before an Intrastat Transaction record is written, to set the status
'Blocked for Reporting' at creating an Intrastat Transaction.
```

To implement this process extension, you need to implement the following method(s):
