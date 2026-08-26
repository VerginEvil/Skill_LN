# tiext.pcf0003.get.cpq.integration.parameter.value

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2146-2147

```baan
Syntax: long tiext.pcf0003.get.cpq.integration.parameter.value(
domain  tcmcs.str50      i.parameter.name,
ref             long             o.type,
ref             boolean          o.is.null,
ref             string           o.string.value(),
ref             long             o.long.value,
ref             double           o.double.value )
Usage:        Expl:   Return the proper value for the additional CPQ integration
parameter.
Variables made current in support of decision logic:
-                        CPQ configurator settings (tipcf011) table fields:
tipcf011.ccfg: Configuration Group
tipcf011.item: Configurable Item
tipcf011.name: Namespace
tipcf011.prid: Profile
-                       Product Variant IDs (tipcf500): all table fields.
Supported types in o.type and mapping to CPQ base type:
10                       - string       --> o.string.value -> CPQ type String
20                       - long         --> o.long.value   -> CPQ type Number
30                       - double       --> o.double.value -> CPQ type Number
40                       - date-time    --> o.string.value -> CPQ type DateTime
date                           -time format "YYYYMMDD HHMMSS"
50                       - boolean      --> o.long.value   -> CPQ type Boolean
Implementation example:
o.type = 0
o.string.value = ""
o.long.value = 0
o.double.value = 0.0
o.is.null = false
on case strip$(i.parameter.name)
case "ParameterString":
o.type = 10
o.string.value = "CustomIntegrationParameterValue"
break
case "ParameterLong":
o.type = 20
|* This example assumes a long value is kept in a
|* customer defined field, retrieval requires generic
|* item and business partner.
o.long.value = read.cdf.field.for.item.business.partner(
tipcf500.item,
tipcf500.cuno)
break
case "ParameterDouble":
o.type = 30
o.double.value = 3.1415927
break
case "ParameterDate":
o.type = 40
o.string.value = "20240124 141632"
break
case "ParameterBoolean":
o.type = 50
o.long.value = true
break
case "ParameterNull":
o.is.null = true
o.type = 10
break
default:
|* Unknown parameter name, will be encoded, but with
|* NULL value, and type String
o.is.null = true
o.type = 10
break
endcase
return(0)
Pre:    Parameter was registered via method:
tiext.pcf0003.register.cpq.integration.parameters.
Post:
Input:  i.parameter.name                      - name of a registered custom CPQ
integration parameter.
Output: o.type                                - type, see supported types in
description above
o.is.null                                     - encode parameter using NULL value
o.string.value                                - string value if needed for type,
max 512 characters.
o.long.value                                  - long value if needed for type
o.double.value                                - long value if needed for type
Return: 0                       successfully set output variables
<> 0                    to indicate failure
```
