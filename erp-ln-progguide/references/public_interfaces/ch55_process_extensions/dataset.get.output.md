# dataset.get.output

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2001-2001

```baan
Syntax: long dataset.get.output(
const           string           i.dataset.format() )
Usage:        This method returns a pointer to the dataset output of the latest dataset.read()
function call. Useful when the output is for example XML or JSON.
This method is optional in the dataset formatting, although either
dataset.get.output(),
dataset.get.output.string() or dataset.get.output.file() must be used to retrieve
the
datast output.
Input:
-               i.dataset.format      - The dataset format name.
Output:
Return:
-               0                     - Not OK.
-               <> 0                  - Dataset Output pointer.
```
