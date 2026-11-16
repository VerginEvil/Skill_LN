# dataset.end

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for Dataset
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2019-2020

```baan
Syntax: long dataset.end(
const           string           i.dataset.format(),
long             i.dataset.id )
Usage:        This method is called just after the data of the dataset is read and all
collections,
rows and fields are added.
This method is optional in the dataset formatting.
Input:
- i.dataset.format      - The dataset format name.
- i.dataset.id          - ID of the dataset.
Output:
Return:
- 0                     - OK.
- DALHOOKERROR          - Not OK.
```
