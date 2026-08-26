# Dataset.CustomOutputFormat

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1998-1999

Format Dataset output. This process extension is available from 2026.04 ( KB3662274 ). Technical information for this process extension:

```baan
Usage: With this process extension the output of an Infor LN Dataset can be constructed.
An Infor LN Dataset can be created via session Datasets (ttrpi5100m000).
After a dataset has been created, it can be executed with the function dataset.read
(included via <bic_dset>). One of the arguments of the dataset.read function is
the output format. The output format argument describes how the dataset output will
be formatted. This process extension can be used for the data formatting in
different formats.
The following methods are present:
-             dataset.new()
This method is called just before the data of the dataset is read. It can,
for example when formatting in XML, be used to create a top level node
for XML output.
-             dataset.end()
This method is called just after the data of the dataset is read.
-             dataset.collection.new()
This method is called just before records of a (child) table are added to the
dataset. It
can, for example when formatting in XML, be used to create a grouping XML node.
-             dataset.collection.end()
This method is called just after records of a (child) table are added to the
dataset.
-             dataset.row.new()
This method is called just before one record of a (child) table is added to the
dataset. It
can, for example when formatting in XML, be used to create a record XML node.
-             dataset.row.end()
This method is called just after one record of a (child) table is added to the
dataset.
-             dataset.row.field.new()
This method is called when a selected field of a record is added to a dataset row.
It
can, for example when formatting in XML, be used to create a field XML element.
-             dataset.get.output()
This method returns a pointer to the dataset output of the latest dataset.read()
function call. Useful when the output is for example XML or JSON.
-             dataset.get.output.string()
This method returns the dataset output of the latest dataset.read() function call
in
a string.
-             dataset.get.output.file()
This method returns the dataset output of the latest dataset.read() function call
in
the given file.
```

To implement this process extension, you need to implement the following method(s):
