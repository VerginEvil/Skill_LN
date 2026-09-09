# tiext.cpr0001.standard.cost.skip.actualize

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for StandardCost
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2272-2272

```baan
Syntax: long tiext.cpr0001.standard.cost.skip.actualize(
ref             boolean          o.skip.actualize,
ref             string           o.message() )
Usage:        Expl:   This function is called in the process of Standard Cost
Actualization and Inventory Revaluation, in order to decide
if the process must be skipped for a specific
Item/Enterprise Unit combination.
A message may be returned, to present information about the
decision to the user.
When this function is called all fields of table:
- Item Costing Data (ticpr007) are read and current.
Pre:    NA
Post:   NA
Input:  NA
Output: o.skip.actualize        - decision result
o.message               - message, multibyte - max 300 characters
Return: 0                       - success
DALHOOKERROR            - error
```
