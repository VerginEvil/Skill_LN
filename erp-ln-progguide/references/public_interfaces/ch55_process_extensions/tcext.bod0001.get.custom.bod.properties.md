# tcext.bod0001.get.custom.bod.properties

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1961-1962

```baan
Syntax: long tcext.bod0001.get.custom.bod.properties(
domain  tcbod.name       i.bodname,
ref     domain  tcmcs.str100     o.documentID,
ref     domain  tcmcs.str8       o.action.code,
ref     domain  tcmcs.long       o.bod.entity.type,
ref     domain  tcmcs.str9       o.bod.entity.code )
Usage:       Use this method to return meta data fields that are needed in the BOD.
Input:
-              i.bodname         - custom BOD name
Output:
-              o.documentID      - documentID
-              o.action.code     - BOD action code, possible values
"Add", "Change", "Delete", "Replace" or
"Canceled"
-              o.bod.entity.type - entity type used to set the accounting entity and
location attributes. Possible values
0 (no type), 1 (Warehouse), 2 (Department),
3 (Project). For Master Data BODs value 0 is
allowed. For other BOD types value must be 1, 2
or 3.
-              o.bod.entity.code - code related to the entity type.
if entity type = 0, code is not used
if entity type = 1, code must be a warehouse
if entity type = 2, code must be a department
if entity type = 3, code must be a project
return:
-              0                 - OK
-              DALHOOKERROR      - not OK
Example of implementation:
long   retval
retval = 0
o.documentID = ""
o.action.code = ""
o.bod.entity.type = 0
o.bod.entity.code = ""
on case trim$(i.bodname)
case "CustomEmployeeBOD":
o.documentID = tccom001.emno
o.action.code = "Add"
o.bod.entity.type = 0
o.bod.entity.code = ""
break
case "ColorBOD":
o.documentID = "CO_"& trim$(txcpr001.colr)
o.action.code = "Add"
o.bod.entity.type = 0
o.bod.entity.code = ""
break
default:
retval = DALHOOKERROR
break
endcase
return(retval)
```
