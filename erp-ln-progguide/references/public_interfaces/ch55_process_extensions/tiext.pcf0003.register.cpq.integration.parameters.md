# tiext.pcf0003.register.cpq.integration.parameters

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2147-2148

```baan
Syntax: long tiext.pcf0003.register.cpq.integration.parameters(
ref             long             o.number.of.parameters,
ref     domain  tcmcs.str50      o.parameter.names() fixed )
Usage:        Expl:   This function is called when for a product variant a
configuration request towards CPQ is prepared.
A set of (custom) CPQ Integration parameters can be registered.
Implementation example:
|* allocate memory for integration parameters
o.number.of.parameters = 6
alloc.mem(      o.parameter.names,
50,
o.number.of.parameters)
o.parameter.names(1,1) = "ParameterString"
o.parameter.names(1,2) = "ParameterLong"
o.parameter.names(1,3) = "ParameterDouble"
o.parameter.names(1,4) = "ParameterDate"
o.parameter.names(1,5) = "ParameterBoolean"
o.parameter.names(1,6) = "ParameterNull"
return(0)
Pre:
Post:
Input:                -
Output: o.number.of.parameters                - The number of custom CPQ integration
parameters registered.
o.parameter.names                             - The array with custom CPQ integration
parameter names. Allocation of this
output array is required.
Return: 0                                     - Success
DALHOOKERROR                                  - When an error occurs in the
added logic
```
