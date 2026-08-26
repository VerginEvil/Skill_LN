# dataset.row.end

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2003-2003

```baan
Syntax: long dataset.row.end(
const           string           i.dataset.format(),
long             i.parent.id,
long             i.row.id )
Usage:        This method is called just after one record of a (child) table is added to the
dataset.
This method is optional in the dataset formatting.
Input:
-               i.dataset.format      - The dataset format name.
-               i.parent.id           - Parent ID of the row.
-               i.row.id              - ID of the row.
Output:
Return:
-               0                     - OK.
-               DALHOOKERROR          - Not OK.
```
