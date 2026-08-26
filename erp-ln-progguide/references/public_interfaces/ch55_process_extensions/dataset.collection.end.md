# dataset.collection.end

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2000-2000

```baan
Syntax: long dataset.collection.end(
const           string           i.dataset.format(),
long             i.parent.id,
long             i.collection.id )
Usage:        This method is called just after records of a (child) table are added to the
dataset.
This method is optional in the dataset formatting.
Input:
-               i.dataset.format      - The dataset format name.
-               i.parent.id           - Parent ID of the collection.
-               i.collection.id       - ID of the collection.
Output:
Return:
-               0                     - OK.
-               DALHOOKERROR          - Not OK.
```
