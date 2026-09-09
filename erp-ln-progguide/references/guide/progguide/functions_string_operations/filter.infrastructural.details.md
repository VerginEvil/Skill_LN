# filter.infrastructural.details()

## Syntax:
`function string filter.infrastructural.details( const string unfiltered_text )`

## Description
Filter out any infrastructural data from the input string, if there is any. If there is any infrastructural data, it would be replaced by another string that explains what it is such as #${BSE}# or #${HOSTNAME}#.

## Arguments
| | | |
|---|---|---|
| `const string` | `unfiltered_text` |  A string containing infrastructural information.  |

## Return values
Masked version of the text for hiding infrastructural details.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.

## Example
```

string initial_text(120)
string filtered_text(120)

initial_text = "Pid 1234567 Uid 123456 Euid 123456 Gid 12 Egid 12 Pset username@<hostname>:1234567"
filtered_text = filter.infrastructural.details(initial_text)

| filtered text is now: "Pid 1234567 Uid 123456 Euid 123456 Gid 12 Egid 12 Pset username@#${HOSTNAME}#:1234567"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
