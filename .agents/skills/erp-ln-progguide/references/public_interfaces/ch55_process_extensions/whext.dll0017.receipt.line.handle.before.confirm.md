# whext.dll0017.receipt.line.handle.before.confirm

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2220-2220

```baan
Syntax: long whext.dll0017.receipt.line.handle.before.confirm(
domain  whinh.shpm       i.receipt,
domain  tcpono           i.receipt.line )
Usage:        Expl:   This function allows to manipulate the receipt line before
confirmation. This process extension is called from the
Infor LN standard, before the confirmation of a receipt line
is executed.
No table fields are current, based on the input arguments the
records must be fetched.
The function is executed within a transaction management, so no
db.retry.point() must be set before calling and there is no need
to commit/abort transaction after the function calls.
Note: If you execute queries on the standard Infor LN tables,
bind the table fields to local variables to prevent disturbing
the standard flow.
Pre:    N.a.
Post:   N.a.
Input:  i.receipt               - Receipt
i.receipt.line          - Receipt Line
Output: N.a.
Return: 0/DALHOOKERROR
```
