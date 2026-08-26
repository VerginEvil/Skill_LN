# dataset.get.output.string

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2002-2002

```baan
Syntax: long dataset.get.output.string(
const           string           i.dataset.format(),
ref             string           o.output.string() )
Usage:        This method returns the dataset output of the latest dataset.read() function call
in
an output string.
This method is optional in the dataset formatting, although either
dataset.get.output(),
dataset.get.output.string() or dataset.get.output.file() must be used to retrieve
the
datast output.
Input:
-               i.dataset.format      - The dataset format name.
Output:
-               o.output.string       - The based string variable which will get the dataset
output
in string format.
It's the responsibility of this function implementation to
allocate the based string.
Return:
-               0                     - OK.
-               DALHOOKERROR          - Not OK.
```
