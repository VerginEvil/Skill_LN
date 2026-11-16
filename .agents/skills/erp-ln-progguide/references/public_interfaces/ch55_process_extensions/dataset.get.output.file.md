# dataset.get.output.file

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2020-2020

```baan
Syntax: long dataset.get.output.file(
const           string           i.dataset.format(),
const           string           i.output.file() )
Usage:        This method returns the dataset output of the latest dataset.read() function call
in
the given file.
This method is optional in the dataset formatting, although either
dataset.get.output(),
dataset.get.output.string() or dataset.get.output.file() must be used to retrieve
the
datast output.
Input:
- i.dataset.format      - The dataset format name.
- i.output.file         - The file the dataset output must be written to.
Output:
Return:
- 0                     - OK.
- DALHOOKERROR          - Not OK.
```
