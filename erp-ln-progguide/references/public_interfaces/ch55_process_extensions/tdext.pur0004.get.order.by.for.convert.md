# tdext.pur0004.get.order.by.for.convert

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for RequestForQuoteConvert
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2203-2203

```baan
Syntax: long tdext.pur0004.get.order.by.for.convert(
ref             string           o.order.by.string.mb() )
Usage:        Expl:   Use this method to define a customized ordering of RFQ responses.
This order                      -by clause will be used in session 'Convert RFQs'
(tdpur1202m000). But note that this Process Extension will not
be considered in scenarios where the quantity is to be split
among the bidders (Setting on the ConvertRFQs session).
The standard order by clause that is used is:
" order by tdpur106._index2 with retry "
When implementing this method, an alternative ordering could be,
as an example:
" order by tdpur106.cdf_0001 desc, tdpur106.otbp asc "
Notes:
1. Only attributes from tables tdpur100, tdpur105 and tdpur106
can be used, including customer defined fields.
2. Run time errors occur when specifying attributes from other
tables or when wrong syntax is constructed.
3. It is advised to include 'with retry' at the end of the
order                         -by string. This will make sure that only part of the
query is repeated after a database update resulted in a
retry.
Pre:    NA
Post:   NA
Input:  NA
Output: o.order.by.string.mb                  - Maximum string length is 500. Multi
byte attributes are allowed.
Return: 0                                     - Success
<> 0                                          - When an error occurs in determination
of the order by clause.
```

## Process Extensions for

## ReservedApprovedCommissionsRebates

The following process extension(s) is/are available: ReservedApprovedCommissionsRebates.SkipPrint
