# tiext.sfc0001.update.print.status

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2137-2139

```baan
Syntax: long tiext.sfc0001.update.print.status(
ref             boolean          i.custom.report.printed(),
ref             string           o.message() )
Usage:        Expl:   This function is called the reports have been printed for a
given Production Order. The function is called once for every
Production Order.
Use this function to update the print status for the custom
reports.
The tisfc001 record for the Production Order to be printed has
been made current.
The external variable proc_ext_print_cust_rep_num_of_cust_reports
is available and contains the length of the array.
The external array proc_ext_print_cust_rep_report_groups is
available and contains the array of report groups.
Implementation example:
Create a custom tx                      -table (example txext001) with an index of the
production order and the reportgroup. Add a field
(ex. txext001.stat) in the created tx                      -table for the print status
with domain tisfc.pdst.
Write the function as follows:
extern long proc_ext_print_cust_rep_num_of_cust_reports
extern domain tcmcs.long proc_ext_print_cust_rep_report_groups(1) based
function extern long tiext.sfc0001.update.print.status(
ref             boolean i.custom.report.printed(),
ref             string  o.message)
{
long    report
long    ret
for report = 1 to proc_ext_print_cust_rep_num_of_cust_reports
if i.custom.report.printed(report) = true
then
ret = set.print.status.printed(
tisfc001.pdno,
proc_ext_print_cust_rep_report_groups(report))
if ret <> 0 then
return(ret)
endif
endif
endfor
return(0)
}
function long set.print.status.printed(
domain  tcpdno          i.production.order,
domain  tcmcs.long      i.report.group)
{
domain  tisfc.pdst      status
long            ret
select  txext001.stat:status
from    txext001 for update
where   txext001._index1 = {    :i.production.order,
:i.report.group}
selectdo
ret = dal.change.object(txext001)
if ret <> 0 then
return(ret)
endif
dal.set.field(  "txext001.stat",
tisfc.pdst.doc.printed)
ret = dal.save.object(txext001)
if ret <> 0 then
return(ret)
endif
endselect
return(0)
}
Pre:    Print the custom reports using
tiext.sfc0001.print.custom.report().
Post:                 -
Input:  i.custom.report.printed               - The array indicating if the report has
been printed. The same sequence is
used as the array with the custom
report groups.
Output: o.message                             - message, multibyte - max 300 characters
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the
added logic
```
