# dataset.clear

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1999-2000

```baan
Syntax: long dataset.clear(
const           string           i.dataset.format() )
Usage:        This method offers the possibility to clear the response of the latest
dataset.read()
function call.
Input:
-               i.dataset.format      - The dataset format name.
Output:
Return:
-               0                     - OK.
-               <> 0                  - Failure.
```
