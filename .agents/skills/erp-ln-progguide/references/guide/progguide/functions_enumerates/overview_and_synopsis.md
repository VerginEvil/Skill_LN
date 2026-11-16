# Enumerates overview and synopsis

## Overview
Use these functions for handling enumerated domains and table fields.

## Synopsis
| | | |
|---|---|---|
| `domain` | [ask.enum()](ask.enum.md) | `( string quescode(14), domain default_enumvalue [, arg ]... )` |
| `string` | [enum.descr$()](enum.descr.md) | `( string domain code(12), enum_expr [, string language_code] )` |
| `long` | [etol()](etol.md) | `( domain domain_value )` |
| `domain` | [ltoe()](ltoe.md) | `( long long_value )` |
| `void` | [set.ask.enum.values()](set.ask.enum.values.md) | `( enum_constant,... )` |
| `void` | [set.enum.values.for.field()](set.enum.values.for.field.md) | `( const string field.name.string, [ALL_ENUMS_EXCEPT], enum_value,... )` |
| `void` | [set.enum.array.for.field()](set.enum.array.for.field.md) | `( const string field.name.string, long size, long values())` |
| `void` | [set.initial.enum.values.for.field()](set.initial.enum.values.for.field.md) | `( const string field.name.string, [ALL_ENUMS_EXCEPT], enum_value,... )` |
| `void` | [set.initial.enum.values.for.workflow.status.field()](set.initial.enum.values.for.workflow.status.field.md) | `([ALL_ENUMS_EXCEPT], enum_value,... )` |
| `void` | [set.initial.enum.array.for.field()](set.initial.enum.array.for.field.md) | `( const string field.name, long size, const long values() )` |
| `void` | [set.enum.values()](set.enum.values.md) | `( enum_constant,... )` |

## Related topics
- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
