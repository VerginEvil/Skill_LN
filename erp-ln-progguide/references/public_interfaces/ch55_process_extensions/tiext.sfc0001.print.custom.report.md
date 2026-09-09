# tiext.sfc0001.print.custom.report

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2157-2159

```baan
Syntax: long tiext.sfc0001.print.custom.report(
domain  tcmcs.long       i.report.group,
domain  tcmcs.st14       i.spooler.device,
long             i.lfn.custom.spool,
ref             long             o.lfn.custom.brpfile,
ref             string           o.message() )
Usage:        Expl:   This function is called to print the custom reports, once for
every production order. The spooler device has already been
opened and the spool.id has been provided in i.lfn.custom.spool.
The function should open the report using the spooler device,
read all required data and send it to the custom report.
This function is called once for every custom report and every
Production Order to be printed.
The tisfc001 record for the Production Order to be printed has
been made current.
Implementation Example:
A custom report that prints the production order has been
created in report group 30 using spooler device "D".
extern  long            lfn.custom.spool
|* External logical Spool File
extern  long            lfn.custom.brpfile
|* External logical File
extern  boolean         open.custom.brp
|* Ext brp File Opening
table   ttisfc001
|* Production Order
tiext.sfc0001.print.custom.report(
domain  tcmcs.long      i.report.group,
domain  tcmcs.st14      i.spooler.device,
long            i.lfn.custom.spool,
ref             long            o.lfn.custom.brpfile,
ref             string          o.message)
{
reportgrp = i.report.group
choice.report(report$)
if not open.custom.brp then
open.custom.brpfile(    true,
i.spooler.device,
i.lfn.custom.spool,
o.lfn.custom.brpfile)
endif
brp.ready(o.lfn.custom.brpfile)
return(0)
}
function open.custom.brpfile(
boolean         i.do.brp.open,
domain  tcmcs.st14      i.spooler.device,
long            i.lfn.custom.spool,
ref             long            o.lfn.custom.brpfile)
{
if i.lfn.custom.spool = 0 then
return
endif
spool.id = i.lfn.custom.spool
if i.do.brp.open then
o.lfn.custom.brpfile = brp.open(
report$,
i.spooler.device,
0)
if o.lfn.custom.brpfile <= 0 then
job.process.error = true
return
endif
open.custom.brp = true
endif
}
Pre:    Determine if the custom report must be printed using
tiext.sfc0001.check.print.condition().
Post:   Update the print status using
tiext.sfc0001.update.print.status().
Input:  i.report.group          - The report group that will be printed.
i.spooler.device        - The spooler device that the report is
to be printed to.
i.lfn.custom.spool      - The logical Spool File for the spooler
device opened for the custom report.
Output: o.lfn.custom.brpfile    - The logical Baan report File opened
for the custom report.
o.message               - message, multibyte - max 300 characters
Return: 0                       - Success
DALHOOKERROR            - When an error occurs in the
added logic
```
