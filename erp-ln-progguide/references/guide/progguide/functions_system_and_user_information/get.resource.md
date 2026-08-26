# get.resource$()

## Syntax:
`function string get.resource$( string resource_name )`

## Description
This function returns the value associated with the given [bshell resource](../misc/bshell_resources.md) of the current user. Resources are specified in the u<user> file in the '$BSE/lib/user' directory, but also in the files '$BSE/lib/defaults/<logical_name_of_bshell>' and '$BSE/lib/defaults/all'. The logical name of the bshell is the name you specify for the Bshell in BW.
A string containing the resource value will be returned. If the resource can't be found, an empty string will be returned (please note that an existing resource may also be empty!).

## Arguments
| | | |
|---|---|---|
| `string` | `resource_name` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  The resources have a specific type internally in the Bshell. The value of a resource is always returned as a *string* by get.resource$(). The way the value is returned depends on the underlying type:
| | | |
|---|---|---|
| Type | Value in resource file | Return from get.resource$() |
| long/string | <none> | default value specified in Bshell |
| long | 0 | "0" |
| long | 1 | "1" |
| long | 001 | "1" |
| long | some_string | "0" (but in fact a wrong configuration) |
| string | hello_world | "hello_world" |
| string | 001 | "001" |

## Example
```

| user file contains e.g. following information:
| compnr:100
| pacc:70b

string company(3), pack_comb(8)
company   = get.resource$("compnr")
pack_comb = get.resource$("pacc")

| Now, company contains the string "100" and pack_comb = "70b"
```

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
- [Bshell resources](../misc/bshell_resources.md)
