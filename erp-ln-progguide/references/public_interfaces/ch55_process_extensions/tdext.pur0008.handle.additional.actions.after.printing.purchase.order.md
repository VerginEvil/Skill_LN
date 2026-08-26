# tdext.pur0008.handle.additional.actions.after.printing.purchase.order

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2169-2170

```baan
Syntax: long tdext.pur0008.handle.additional.actions.after.printing.purchase.order(
domain  tcorno           i.purchase.order,
boolean          i.draft )
Usage:        Expl:   Use this method to handle additional actions after printing the
Purchase Order.
If the after action fails, the extension must put an
error                      -message on the stack and return a non-zero value.
Notes:
-                       A retry point is already set before the printing and
abort.transaction / commit.transaction is done already after the
printing.
-                       When printing a draft (i.draft = true) the
the system will always do a abort.transaction after the print.
All database changes in the extension and within the
same transaction will be reverted in that case!
Input:  i.purchase.order                      - Purchase Order
i.draft                                       - The Purchase Order was printed as a
draft.
Output: NA
Return: 0                                     - Additional actions after printing was
a Success.
<> 0                                          - A error occurred in the additional
actions after printing. LN will skip
further actions for this Purchase Order
during the print.
```
