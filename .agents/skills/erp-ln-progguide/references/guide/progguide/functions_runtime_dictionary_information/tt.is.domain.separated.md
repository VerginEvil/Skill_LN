# tt.is.domain.separated()

## Syntax:
`function boolean tt.is.domain.separated( const string a_domain(), [ ref long numberOfSeparators, ref string separatorCharacter() ] )`

## Description
Returns whether or not a segmented domain should be printed with separators

## Arguments
| | | |
|---|---|---|
| `const string` | `a_domain()` |  The domain name.  |
| `[ ref long` | `numberOfSeparators ]` |  An optional long, when passed it will return the number of separator characters that are used when printing this domain.  |
| `[ ref string` | `separatorCharacter() ]` |  An optional string (length 1 is sufficient), when passed it will return the separator character that is used, if any.  |

## Return values
True when the domain is separated, false otherwise.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
