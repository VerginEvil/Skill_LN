# Procurement.HandleGeneralLedgerCodeDefaulting

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Procurement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2153-2153

```baan
Customize the logic for defaulting the general ledger code in LN Procurement processes.
This process extension is available from 2025.09 (KB3613480).
Technical information for this process extension:
Usage:        This Process Extension allows customization of the logic used for
defaulting the general ledger code in Procurement processes.
Specifically, it enables you to override or skip the defaulting behavior
of the general ledger code.
The extension is invoked whenever the standard LN logic attempts to
determine a default ledger code for Procurement-related objects.
To implement this process extension, you need to implement the following method(s):
```
