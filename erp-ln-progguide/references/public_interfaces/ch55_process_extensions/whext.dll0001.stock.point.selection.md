# whext.dll0001.stock.point.selection

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for InventorySearchEngine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2049-2049

```baan
Syntax: long whext.dll0001.stock.point.selection(
long             i.query.id )
Usage:        Expl:   Use this method to fetch the stock points which are going to be
selected by the Inventory Search Engine. The i.query.id is the
parsed query by the standard which can be fetched using this
process extension.
The flow is as follows:
-                       Inventory Search Engine is started
-                         Functional loop is executed to determine the best
stock points, based on the setup applicable for the
order line that is to be advised. In this loop a query
is created.
-                         When the process extension is implemented:
-                               The query id (i.query.id) is the query that can be
fetched in this extension point
-                         Standard fetches the stock points and will generate an
outbound advice / backflush if this is allowed.
Technically the Infor LN standard will perform the sql.exec and
sql.break, within the process extension only the sql.fetch is
needed to be executed on the i.query.id. Fetching a record can
of course result in a fetched record or not.
Upon fetching the query.id, the following tables will be
current, and can be used in this process extension:
whinr150                               - Inventory Structure
whinr140                               - Inventory
whwmd300                               - Locations (for location controlled warehouses)
Pre:    This process extension will run within a logical transaction, so
it is not allowed to use abort.transaction() or
commit.transaction(), db.retry.point() should also not be set.
Post:   NA
Input:  i.query.id
Output: NA
Return: 0/DALHOOKERROR
```
