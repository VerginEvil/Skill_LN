# tcext.bod0001.get.custom.bod.publish.function

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1981-1982

```baan
Syntax: long tcext.bod0001.get.custom.bod.publish.function(
domain  tcbod.name       i.bodname,
ref     domain  tcmcs.str100     o.functionname,
ref     domain  tcmcs.long       o.instruction )
Usage:       Use this method to return the function and instruction that is needed
to publish the BOD.
When this method is not present or not implemented, default values will
be used. The default values are:
functionname = "tcbod.dll0005.publish.custom.bod"
instruction = 1
Input:
- i.bodname         - custom BOD name
Output:
- o.functionname    - the function name which has been created by the
extension team to publish the BOD. The name of the
DLL wherein this function exists, is derived from
the function name. The function name must start
with the package (tx), module, hardcoded ".dll",
and the DLL number (4 characters). E.g. function
name "txbod.dll0005.publish.custom.bod.tax.cty"
must exist in DLL txboddll0005.
- o.instruction     - The instruction code. Possible values:
1 (PD_NO_SPECIFIC_COMMAND): the logic of the
standard publish BOD function is used for
counting and for publishing data.
2 (PD_CALL_FUNCTION_IN_SELECTDO_COUNT): the logic
for counting and publishing data is programmed
in the function of output argument o.functionname.
In the current implementation, the value of
o.instruction must be set to 2.
return:
- 0                 - OK
- DALHOOKERROR      - not OK
Example of implementation:
o.functionname = ""
o.instruction = 0
on case trim$(i.bodname)
case "CustomTaxCountryBOD":
o.functionname = "txbod.dll0005.publish.custom.bod.tax.cty"
o.instruction = 2
break
default:
break
endcase
return(0)
Example of a custom BOD publish function:
Following function could be programmed in txboddll0005 for an example
where o.functionname = "txbod.dll0005.publish.custom.bod.tax.cty" and
o.instruction = 2. The first argument and the last two arguments are
fixed; in between each value returned by the initial load SQL query
must exist as input argument
function extern long txbod.dll0005.publish.custom.bod.tax.cty(
const   domain  tcbod.mode      i.mode,                 |* mandatory argument
domain  tcccty          i.ccty, |*<<< Use one or more identifiers here
ref             long            io.nr.bods.to.publish,  |* mandatory argument
ref             long            io.nr.bods.published)   |* mandatory argument
{
long    return.value
domain  tcmcs.s999m     error.message
long    error.id
if db.retry.hit() = 0 then
io.nr.bods.to.publish = io.nr.bods.to.publish + 1
endif
if i.mode <> tcbod.mode.count then
return.value =
BOD.Publish(
"CustomTaxCountryBOD",
"tcmcs036",
"Add",
0,                      |* bod.entity.type
"",                     |* bod.entity.code
i.ccty,                 |* documentID
"OnlyPublish",
error.message,
error.id,
i.ccty)
if return.value = 0 then
io.nr.bods.published =
io.nr.bods.published + 1
else
dal.set.error.message("@"&error.message)
return(return.value)
endif
endif
return(0)
}
```
