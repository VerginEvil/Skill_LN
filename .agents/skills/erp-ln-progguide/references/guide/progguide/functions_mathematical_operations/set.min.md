# set.min()

## Syntax:
`function void set.min( ref void variable, [ string domain ] )`

## Description
This sets a specified standard variable to its minimum value.
For string variables, use [set.fmin()](set.fmin.md) instead.
For setting the maximum value, use [set.max()](set.max.md) and [set.fmax()](set.fmax.md).

## Arguments
| | | |
|---|---|---|
| `ref void` | `variable` |  Reference argument to be set. This can be a single variable or an array.  |
| `[ string` | `domain ]` |  Optional name of the domain of which the minimum value must be used. If it is not supplied, then the runtime domain of the first argument is used. The runtime domain of the first argument is determined by means of a lookup of its name in the runtime list of table fields. Notice that for a normal variable declared by means of a [domain declaration](../3gl_features/domains.md), its declared domain is not known at runtime. If for the first argument no runtime domain is found, then its name is looked up in the list of form fields of the current form of the process. If it is found, then the domain type as specified in the form is used. Otherwise, a default domain type is used which depends on the runtime type of the first argument. Notice that if the first argument is a subscripted variable, then at runtime its name is not available, so both the lookup in the runtime list of table fields and the lookup in the list of form fields is skipped. When the compiler has any reason to suspect that specifying the compile time domain of the first argument would lead to a different result than omitting it, then (as of [porting set TIV](../tiv/tiv_overview.md) [level 2100](../tiv/tiv_2100.md)) it issues [warning 23 or 24](../3gl_features/compiler.md). In the future, in some cases this will change to an error.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Notes
The following table shows the minimum and maximum values of domain types supported by Infor Enterprise Server.
| | | |
|---|---|---|
| Domain type | Minimum value | Maximum value |
| byte/enumerated (unsigned 7-bit integer range) | 0 | 127 (0x7f) |
| integer (signed 16-bit integer range) | -32,768 (-0x8000) | 32,767 (0x7fff) |
| long/text (signed 32-bit integer range) | -2,147,483,648 (-0x8000,0000) | 2,147,483,647 (0x7fff,ffff) |
| float (32-bit floating point range) | -999,999,999,999.9e20 | 999,999,999,999.9e20 |
| double (64-bit floating point range) | -999,999,999,999.9e64 | 999,999,999,999.9e64 |
| string[1] | chr(1) | "~" (or other value, depending on the locale, max length 1024) |
| enumerate | the minimal value of all the defined enumerate constants of the concerned enumerate domain | the maximal value of all the defined enumerate constants of the concerned enumerate domain |
| bitset | 0, which corresponds to the empty set | the value corresponding to the full set, i.e. a set containing all the defined set elements of the concerned bitset domain. |
| date | 0, which is an invalid date value. The minimum valid date value is 1, which corresponds to January 1, 0001. | 3,652,059, which corresponds to December 31, 9999 |
| time | 0, which corresponds to January 1, 1970, 00:00:00 UTC. | 2,147,483,647 (0x7fff,ffff), which corresponds to January 19, 2038, 03:14:07 UTC. In the [Utc40 mode](../functions_date_time_zones/overview.md#Utc40) and in the [Utc64 mode](../functions_date_time_zones/overview.md#Utc64) this maximum is set to 253,402,214,400 (0x3a,fff2,f000), which corresponds to the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC. Notice that even in local time this maximum value is well before the begin of the first five-digit year 10000, i.e. January 1, 10000, 00:00:00 local time When the bshell is not in [64-bit mode](../3gl_features/data_types.md#Long64), then this value cannot be stored in a long variable, so the maximum then remains 0x7fff,ffff. |
| multibyte string | configurable using the TSS dictionary programs (session: Maintain Locale Data) | configurable using the TSS dictionary programs (session: Maintain Locale Data) |

## Numeric domains with a range expression
When the concerned domain has a range expression, then it is tried to involve the range expression also in the calculation. However, it is practically impossible to do this for all allowed range expressions in general. At the moment it is implemented for numeric domains only. Above that, the range expression must be of a specific form:
`$$ in [number,number] [number, number]`
So, it is allowed to use multiple intervals. The interval bounds must be specified as literal numbers or the constant COMPNR.MAX, not as general expressions. When the range expression is not of this specific form, then it is ignored in the computations.
Examples of range expressions which will work for an integer domain (the minimum and maximum will be set to 0 and 159 respectively):
`$$ in [0,159]`
`$$ in [0,59] [100,159]`
Examples of range expressions which will work for a float domain (the minimum and maximum will be set to 0.0 and 159.9 respectively):
`$$ in [0.0,159.9]`
`$$ in [0.0,59.9] [100.0,159.9]`
Examples of range expressions which will be ignored because they are not of the correct form:
`$$ in [0,100+60-1]`
`(0 <= $$) and ($$ < 160)`

## Numeric domains with 'Digits before Decimal' or 'Digits after Decimal'
When the concerned domain is a numeric domain with a non-zero 'Digits before Decimal' or 'Digits after Decimal' value, then these values are also involved in the calculation.
For example, when 'Digits before Decimal' is set to 3, then the minimum and maximum of an integer domain will be set to -999 and 999 respectively.
When, above that, 'Digits after Decimal' is set to 4, then the minimum and maximum of a float domain will be set to -999.9999 and 999.9999 respectively.
When one of 'Digits before Decimal' and 'Digits after Decimal' is set to 0, then the minimum and maximum of the same float domain will be set either to -0.9999 and 0.9999 respectively or to -999.0 and 999.0 respectively.
When both 'Digits before Decimal' and 'Digits after Decimal' are set to 0, then these values are ignored and do not influence the calculation of the minimum and maximum of the float domain.

## Example
```

long value
set.min(value) | value contains -2147483648
```

## Related topics
- [Mathematical operations overview](overview.md)

- [Mathematical operations synopsis](synopsis.md)
