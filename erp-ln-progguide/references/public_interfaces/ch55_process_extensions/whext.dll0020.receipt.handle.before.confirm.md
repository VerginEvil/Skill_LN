# whext.dll0020.receipt.handle.before.confirm

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Receipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2196-2196

```baan
Syntax: long whext.dll0020.receipt.handle.before.confirm(
domain  whinh.shpm       i.receipt )
Usage:        Expl:   This function allows to manipulate Receipt and Receipt Lines
between their creation and confirmation. This process extension
is called from the Infor LN standard, before goods are received.
No table fields are current, based on the input arguments the
records must be fetched.
This process extension is called within a logical transaction.
Transaction handling is prohibited.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.receipt                             - Receipt
Output: N.a.
Return: 0/DALHOOKERROR
```

## Process Extensions for ReceiptLine

The following process extension(s) is/are available: ReceiptLine.HandleConfirm
