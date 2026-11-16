# tdext.pur0008.handle.additional.actions.after.printing.purchase.order.line

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2193-2193

```baan
Syntax: long tdext.pur0008.handle.additional.actions.after.printing.purchase.order.line(
domain  tcorno           i.purchase.order,
domain  tcpono           i.purchase.order.line,
domain  tcpono           i.purchase.order.line.sequence,
boolean          i.draft )
Usage:        Expl:   Use this method to handle additional actions after printing the
Purchase Order.
If the after action fails, the extension must put an
error-message on the stack and return a non-zero value.
Notes:
- A retry point is already set before the printing and
abort.transaction / commit.transaction is done already after the
printing.
- When printing a draft (i.draft = true) the
the system will always do a abort.transaction after the print.
All database changes in the extension and within the
same transaction will be reverted in that case!
Input:  i.purchase.order                - Purchase Order
i.purchase.order.line           - Purchase Order Line
i.purchase.order.line.sequence  - Purchase Order Line Sequence
i.draft                         - The Purchase Order was printed as a
draft.
Output: NA
Return: 0                       - Additional actions after printing was
a Success.
<> 0                    - A error occurred in the additional
actions after printing. LN will skip
further actions for this Purchase Order
during the print.
```
