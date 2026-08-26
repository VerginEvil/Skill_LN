# InventorySearchEngine.CheckStockPoint

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventorySearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2047-2048

Allows to perform preview of the stock point selection and skips of stock points. This process extension is available from 2019.09 ( KB2073261 ). Technical information for this process extension:

```baan
Usage:        With this Process Extension, it is possible to perform additional
checks on the inventory search engine related to the found stock points,
which is used during the generation of outbound advices (whinh4201m000)
and the Backflushing process.
There are 2 extension points within the process extension, which can be
implemented individually, the first one
(whext.dll0001.stock.point.selection) will be called from the standard
prior to actually selecting the stock points. This allows the extender
to get a preview of the stock points which will be selected within the
inventory search engine. This can be used to evaluate which stock points
will be part of the selection, during the execution of the inventory
search engine.
The other extension point (whext.dll0001.check.stock.point) will be
called when the inventory search engine has selected the actual stock
point, in which it will be possible to skip the stock point and
additionally provide a message which will be forwarded to the advice
log, if necessary.
These extension functions share the same declaration and will allow for
usage of the same variables (arrays) to determine what should be done.
Another option is to use a tx table to store what is the optimal
selection, based on the stock points which are considered for
allocations during the inventory search engine.
An example:
Suppose there are a couple of locations in the system which require
higher priority when advising / picking inventory as opposed to the
location type (bulk / pick). So the following locations:
BULK1               - Bulk - Prio 10  - Available inventory: ITEM X 20 pcs
BULK2               - Bulk - Prio 20  - Available inventory: ITEM X 40 pcs
BULK3               - Bulk - Prio 30  - Available inventory: ITEM X 60 pcs
PICK1               - Pick - Prio 10  - Available inventory: ITEM X 80 pcs
The standard will first always consider the locations of type Pick, but
suppose the customer wants to use the bulk locations first, which has
the highest priority. An order is created for 80 pcs of the item ITEM X.
When selecting the inventory in the standard flow, the location PICK1
will be selected, as that has the exact quantity 80 pcs and it is a
pick location, suppose the BULK3 location and BULK2 location are to be
used first, because the inventory located there needs to be consumed
prior to the inventory on the picking location, the extension can be
implemented as such:
Implement whext.dll0001.stock.point.selection to see which stock points
are about to be selected by the standard. Based on extension logic, the
customer can write logic to determine which locations should be used and
which should be skipped. When the inventory search engine will select
the inventory, the function whext.dll0001.check.stock.point will be
executed, in which the extension can skip the selected stock point.
So suppose PICK1 should be skipped, BULK1 should be skipped, and the
inventory on BULK2 and BULK 3 can be used. The standard will first come
with PICK1 which will be skipped by the extension, then BULK1 which will
also be skipped. Then BULK2 will be selected, only 40 pcs are available
on that location, so an outbound advice of 40 pcs will be created, next
the BULK3 will be selected from which also 40 pcs will be available, as
a result also an outbound advice will be created, for the remaining 40
pcs.
```

To implement this process extension, you need to implement the following method(s):
