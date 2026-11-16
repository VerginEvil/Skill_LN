# tfext.gld0002.get.max.number.of.document.lines

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for IntegrationTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2054-2055

```baan
Syntax: long tfext.gld0002.get.max.number.of.document.lines(
ref             long             o.max.number.of.document.lines )
Usage:        Expl:
Use this Process Extension to influence the maximum number of
document lines during Posting Integration Transactions
(tfgld4282m000).
Standard, a maximum of 32000 lines are present within a document.
With this process extension, the maximum can be lowered. This is
needed if documents are sent to other packages/products where
those large documents cannot be handled.
Note that the maximum must be an even number >=2 and <=32000.
Pre:    N.A.
Post:   N.A.
Input:  N.A.
Output: o.max.number.of.document.lines
- The maximum number of document lines
to be used during posting integration
transactions.
Return: 0                       - Success
DALHOOKERROR            - Error situation
Example:
o.max.number.of.document.lines = 900
```
