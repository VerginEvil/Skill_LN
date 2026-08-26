# tiext.pcs0003.get.customer.defined.project.series

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProjectPCS
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2160-2161

```baan
Syntax: long tiext.pcs0003.get.customer.defined.project.series(
domain  tcseri           i.project.series,
ref     domain  tcseri           o.project.series )
Usage:        Expl:   This method is called prior to the creating of a Project,
to get a custom Project Series.
This custom project series will override the Project Series
given on session 'Project Control Parameters'
(tipcs0100m000/tipcs0100s000).
Implementation Example:
Intention:
The user want to use a special project code when
processing quotations to generate sales orders and the
associated PCS projects.
Hook Declarations:
|* Control flag defined/set as external in session
|* tdsls1200m000
`               extern boolean use.specific.series.for.quotation.copy
Hook Implementation:
function extern long tiext.pcs0003.....
...
{
|* replacing empty for custom ABC when request
|* flag set in calling process.
if      use.specific.series.for.quotation.copy
and isspace(i.project.series)
then
o.project.series = "ABC"
endif
return(0)
}
Pre:    N.A.
Post:   N.A.
Input:  i.project.series                      - The project series from the standard
session.
Output: o.project.series                      - The project series to use. May be left
empty, in that case the input Project
series will be used for the processing.
Return: 0                                     - Success.
```
