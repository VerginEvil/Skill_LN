# tiext.sfc0001.check.print.condition

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2133-2134

```baan
Syntax: long tiext.sfc0001.check.print.condition(
domain  tcmcs.long       i.report.group,
domain  tcyesno          i.print.originals,
domain  tcyesno          i.print.duplicates,
domain  tcyesno          i.print.modified,
ref             boolean          o.print.report,
ref             string           o.message() )
Usage:        Expl:   This function is called in session tisfc0408m000 when
determining which custom reports to print. The function is
called once for every Production Order and every report to be
printed.
The tisfc001 record for the Production Order to be printed has
been made current.
Implementation example:
Create a custom tx                      -table (example txext001) with an index of the
production order and the report group. Add a field
(ex. txext001.stat) in the created tx                      -table for the print status
with domain tisfc.pdst.
Write the function as follows:
function extern long tiext.sfc0001.check.print.condition(
domain  tcmcs.long      i.report.group,
domain  tcyesno         i.print.originals,
domain  tcyesno         i.print.duplicates,
domain  tcyesno         i.print.modified,
ref             boolean         o.print.report,
ref             string          o.message)
{
domain  tisfc.pdst      print.status
print.status = get.print.status.(
tisfc001.pdno,
i.report.group)
if print.status = tisfc.pdst.original.doc
and i.print.originals = tcyesno.yes
then
return(true)
endif
if print.status = tisfc.pdst.modified.doc
and i.print.modified = tcyesno.yes
then
return(true)
endif
if print.status = tisfc.pdst.doc.printed
and i.print.duplicates = tcyesno.yes
then
return(true)
endif
return(false)
}
function domain tisfc.pdst get.print.status(
domain  tcpdno          i.production.order,
domain  tcmcs.long      i.report.group)
{
domain  tisfc.pdst      print.status
select  txext001.stat:print.status
from    txext001
where   txext001._index1 = {    :i.production.order,
:i.report.group}
selectempty
print.status = tisfc.pdst.original.doc
endselect
return(print.status)
}
Pre:    The custom reports must be registered using
tiext.sfc0001.registrate.custom.reports().
Post:   Print the custom reports using
tiext.sfc0001.print.custom.report()
Input:  i.report.group                        - The report group of the custom report
i.print.originals                             - Print Option: original reports must be
printed.
i.print.duplicates                            - Print Option: duplicate reports must
be printed.
i.print.modified                              - Print Option: modified reports must be
printed.
Output: o.print.report                        - If true, the custom report should be
printed.
If false, the custom report should
not be printed.
o.message                                     - message, multibyte - max 300 characters
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the
added logic
```
