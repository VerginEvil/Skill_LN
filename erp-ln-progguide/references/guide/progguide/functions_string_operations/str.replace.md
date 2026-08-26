# str.replace()

## Syntax:
`function void str.replace( const string string$, const string oldstr$, const string newstr$, ref string result$ )`

## Description
Returns as an output argument a (null terminated) copy of `string$` that will have all instances of `oldstr$` replaced with `newstr$`.
The `result$` string will be resized as required, which ensures that in `result$` all occurrences of `oldstr$` have been replaced. In order to be able to resize `result$`, the variable passed must be declared as a based string. Use ` [len()](len.md)` to know the new number of characters in `result$`.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `const string` | `oldstr$` |  the part to replace  |
| `const string` | `newstr$` |  the part to replace `oldstr$` with  |
| `ref string` | `result$` |  a copy of `string$`, with all instances of `oldstr$` replaced with `newstr$`  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Preconditions
Note: The following preconditions no longer apply when `get.tools.tiv()` returns 2210 or higher.
- In case one of the variables passed to `string$`, `oldstr$`, or `newstr$` is declared as a multibyte string, then the variable passed to `result$` must be declared as a multibyte string as well.
- The variable passed to the `result$` parameter must be declared as a based string.
- The variable passed in `string$` respectively in `result$` can not be the same. (Conflict in declaration memory as constant and as output.)

## Example
```

string source(50)
string target(1) based
long target.len

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

| target is not yet allocated...

str.replace(source, "dog", "cat", target)
| target now is allocated and contains "the quick brown fox jumps over the lazy cat"
target.len = len(target)
| target.len = 43

str.replace(source, "the", "a", target)
| target is shrinked and now contains "a quick brown fox jumps over a lazy dog"
target.len = len(target)
| target.len = 39

str.replace(source, "o", "O", target)
| target is not resized and now contains "the quick brOwn fOx jumps Over the lazy dOg"
target.len = len(target)
| target.len = 43

str.replace(source, " ", "  ", target)
| target is enlarged and now contains "the  quick  brown  fox  jumps  over  the  lazy  dog"
target.len = len(target)
| target.len = 51

str.replace(source, "the", "", target)
| this removes all instances of "the"
| target is shrinked and now contains "quick brown fox jumps over lazy dog"
target.len = len(target)
| target.len = 35

str.replace(source, "", "the", target)
| nothing is replaced
| target is resized to the size of source and now
| contains "the quick brown fox jumps over the lazy dog"
target.len = len(target)
| target.len = 43

string nonbased(100)

str.replace(source, " ", "  ", nonbased)
| this results in an assert message, as string 'nonbased' should have been declared as based
```

## Related topics
- [str.replace$()](str.replace$.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
