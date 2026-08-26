# tcext.bod0001.get.custom.bodnames

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1963-1964

```baan
Syntax: long tcext.bod0001.get.custom.bodnames(
ref     domain  tcbod.name       o.bodnames() fixed,
ref     domain  tcmcs.str70m     o.labels() fixed mb,
ref     domain  tcmcs.str8       o.root.tables() fixed,
ref             long             o.indx )
Usage:       Use this method to define the custom BOD names for publishing. You can
define upto 50 BODs. Each BOD must exist in the session BOD
Implementation Registration (bobod1100m000) and the check box for the
field "Standard" must not be selected. The BOD root table is mandatory
for Master Data BODs and is optional for other BOD types.
Input: N.A.
Output:
-              o.bodnames        - array with custom BOD names (max.50, length 70)
-              o.labels          - array with custom BOD labels (max.50,
length 70 multi                                    -byte)
-              o.root.tables     - array with custom BOD root tables (max.50, length 8)
-              o.indx            - number of custom BODs in stack
Return:
-              0                 - OK
-              DALHOOKERROR      - not OK
Example of implementation:
o.indx = 3
alloc.mem(o.bodnames, 70, o.indx)
alloc.mem(o.labels, 70, o.indx)
alloc.mem(o.root.tables, 8, o.indx)
|* CustomEmployeeBOD
o.bodnames(1, 1) = "CustomEmployeeBOD"  |* bodname
o.labels(1, 1) = "Employee"             |* label on session
o.root.tables(1, 1) = "tccom001"        |* root table
|* ColorBOD
o.bodnames(1, 2) = "ColorBOD"           |* bodname
o.labels(1, 2) = "Color"                |* label on session
o.root.tables(1, 2) = "txcpr001"        |* root table
|* CustomTaxCountryBOD
o.bodnames(1, 3) = "CustomTaxCountryBOD"|* bodname
o.labels(1, 3) = "Tax Country"          |* label on session
o.root.tables(1, 3) = "tcmcs036"        |* root table
return(0)
```
