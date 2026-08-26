# dataset.collection.new

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2000-2000

```baan
Syntax: long dataset.collection.new(
const           string           i.dataset.format(),
long             i.parent.id,
const           string           i.internal.name(),
const           string           i.external.name() )
Usage:        This method is called just before records of a (child) table are added to the
dataset. It
can, for example when formatting in XML, be used to create a grouping XML node.
This method is optional in the dataset formatting.
Input:
-               i.dataset.format      - The dataset format name.
-               i.parent.id           - Parent ID of the new collection. Can be the ID returned
by the
dataset.new() or a dataset.row.new() call.
-               i.internal.name       - Internal technical name of the collection, this will be
the related table name of the collection.
-               i.external.name       - External name of the collection, specified in the
dataset model
which is created by the Dataset Modeler.
Output:
Return:
-               <> 0                  - Dataset Collection ID, being a pointer to the
collection.
-               0                     - In case of error.
```
