# tcext.bod0001.get.initial.load.query

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1983-1984

```baan
Syntax: long tcext.bod0001.get.initial.load.query(
domain  tcbod.name       i.bodname,
ref             string           o.query() )
Usage:       Use this method to return the SQL query to read the index fields of the
root table for each custom BOD. In the query you can use the values of
the custom fields you defined in the process extension. The select
statement of the query must only select the index fields of the root
table. The values of the selected fields of the select statement are
forwarded as input arguments for the standard publish BOD function or are
forwarded as input arguments for the function that is defined in the
tcext.bod0001.get.custom.bod.publish.function() method.
Never implement a statement like "select <table>.*"
Input:
- i.bodname         - custom BOD name
Output:
- o.query           - dynamical query (max. length 2048)
return:
- 0                 - OK
- DALHOOKERROR      - not OK
Example of implementation:
long   retval
retval = 0
o.query = ""
on case trim$(i.bodname)
case "CustomEmployeeBOD":
o.query = "select tccom001.emno " &
"from tccom001 " &
"where tccom001.emno inrange " &
"{" & quoted.string(ext.empl.f) & "} and " &
"{" & quoted.string(ext.empl.t) & "} "
break
case "ColorBOD":
o.query = "select txcpr001.colr " &
"from txcpr001 " &
"where txcpr001.colr inrange " &
"{" & quoted.string(ext.colr.f) & "} and " &
"{" & quoted.string(ext.colr.t) & "} "
break
case "CustomTaxCountryBOD":
o.query = "select tcmcs036.ccty " &
"from tcmcs036 " &
"where tcmcs036._index1 inrange " &
"{" & quoted.string(ext.tax.country.f) & "} and " &
"{" & quoted.string(ext.tax.country.t) & "} " &
"group by tcmcs036.ccty "
default:
retval = DALHOOKERROR
break
endcase
return(retval)
```
