# dataset.row.field.new

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2003-2004

```baan
Syntax: long dataset.row.field.new(
const           string           i.dataset.format(),
long             i.row.id,
const           string           i.row.internal.name(),
const           string           i.field.internal.name(),
const           string           i.field.external.name(),
const           string           i.field.value() )
Usage:        This method is called when a selected field of a record is added to a dataset row.
It
can, for example when formatting in XML, be used to create a field XML element.
This method is mandatory in the dataset formatting.
Input:
-               i.dataset.format      - The dataset format name.
-               i.row.id              - Row ID for the new field. Is the ID returned by a
dataset.row.new() call.
-               i.row.internal.name   - Internal technical name of the row, this will be
the related table name of the collection.
-               i.field.internal.name - Internal technical name of the field, this will mostly
be
the tablefield name.
-               i.field.external.name - External name of the field, specified in the dataset
model
which is created by the Dataset Modeler.
-               i.field.value         - The value of the field in string representation.
Output:
Return:
-               <> 0                  - Dataset Row Field ID, being a pointer to the field.
-               0                     - In case of error.
```
