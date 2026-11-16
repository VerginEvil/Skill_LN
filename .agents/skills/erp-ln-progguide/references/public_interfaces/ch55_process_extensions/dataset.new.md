# dataset.new

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2021-2021

```baan
Syntax: long dataset.new(
const           string           i.dataset.format(),
const           string           i.dataset.name(),
const           string           i.top.level.name() )
Usage:        This method is called just before the data of the dataset is read. It can,
for example when formatting in XML, be used to create a top level node
for XML output.
This method is mandatory in the dataset formatting.
Input:
- i.dataset.format      - The dataset format name.
- i.dataset.name        - The dataset name.
- i.top.level.name      - A top level name of the output. Optional, when needed
for the
in the output format.
Output:
Return:
- <> 0                  - Dataset ID, being a pointer to the dataset.
- 0                     - In case of error.
```
