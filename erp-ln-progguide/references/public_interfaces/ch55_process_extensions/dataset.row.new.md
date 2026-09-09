# dataset.row.new

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2023-2023

```baan
Syntax: long dataset.row.new(
const           string           i.dataset.format(),
long             i.parent.id,
const           string           i.internal.name(),
const           string           i.external.name() )
Usage:        This method is called just before one record of a (child) table is added to the
dataset. It
can, for example when formatting in XML, be used to create a record XML node.
This method is mandatory in the dataset formatting.
Input:
- i.dataset.format      - The dataset format name.
- i.parent.id           - Parent ID of the new row. Can be the ID returned by the
dataset.new(), dataset.collection.new or a
dataset.row.new() call.
- i.internal.name       - Internal technical name of the row, this will be
the related table name of the collection.
- i.external.name       - External name of the row, specified in the dataset model
which is created by the Dataset Modeler.
Output:
Return:
- <> 0                  - Dataset Row ID, being a pointer to the row.
- 0                     - In case of error.
```
