# tt.align.according.domain()

## Syntax:
`function long tt.align.according.domain( string string_in(.), string string_out(), ref string domain_name )`

## Description
This aligns a string according to the alignment method of a specified domain.

## Arguments
| | | |
|---|---|---|
| `string` | `string_in(.)` |  The input string. This must have the same length as the specified domain. If it is longer than the domain, its final characters are ignored. The input string remains unchanged by the function.  |
| `string` | `string_out()` |  The returned string, aligned according to the alignment method of the domain. This must be the same length as the specified domain.  |
| `ref string` | `domain_name` |  The name of the domain whose alignment method must be used to align the output string. The alignment method can be left, right, or centered.  |

## Return values
0 success
-1 domain not found or domain is not of type string or multibyte string

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

table   ttiitm001
domain  tcitem  item
long    ret

item = "  XY"
ret = tt.align.according.domain(item, tiitm001.item, "tcitem")
    | Result tiitm001.item (if left adjusted): "XY              "
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
