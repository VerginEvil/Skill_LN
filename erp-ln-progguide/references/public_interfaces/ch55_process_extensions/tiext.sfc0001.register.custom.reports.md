# tiext.sfc0001.register.custom.reports

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2136-2137

```baan
Syntax: long tiext.sfc0001.register.custom.reports(
ref             long             o.number.of.custom.reports,
ref             long             o.custom.report.groups(),
ref     domain  tcmcs.st14       o.custom.print.devices() fixed,
ref             string           o.message() )
Usage:        Expl:   This function is called when session
Print Production Order Documents (tisfc0408m000),
is started.
With this method, one or more custom reports can be registered
and spooler devices can be defined.
All custom report groups must 30 or higher.
Implementation example:
Implementing a custom report linked to tisfc0408m000 in
reportgroup 30 using spooler device "D".
function extern long tiext.sfc0001.register.custom.reports(
ref long o.number.of.custom.reports,
ref long o.custom.report.groups(),
ref domain tcmcs.st14 o.custom.print.devices(),
ref string o.message())
{
string  dummy.string(1)
long    dummy.long
long    domain.length
rdi.domain(     "tcmcs.st14",
dummy.string,
dummy.string,
dummy.string,
dummy.long,
dummy.string,
dummy.long,
domain.length)
alloc.mem(      o.custom.report.groups,
1)
alloc.mem(      o.custom.report.spools,
domain.length,
1)
o.custom.report.groups(1) = 30
o.custom.report.spools(1, 1) = "D"
o.number.of.custom.reports = 1
return (0)
}
Pre:    Use the extension modeler to link the custom report to session
tisfc0408m000.
Post:   Determine if the custom report must be printed using
tiext.sfc0001.check.print.condition().
Input:                -
Output: o.number.of.custom.reports
-                                               The number of custom reports
registered in this method.
o.custom.report.groups                        - The array with the group numbers of
all custom reports.
o.custom.report.spools                        - The array with the spooler devices for
the custom reports.
o.message                                     - message, multibyte - max 300 characters.
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the
added logic
```
