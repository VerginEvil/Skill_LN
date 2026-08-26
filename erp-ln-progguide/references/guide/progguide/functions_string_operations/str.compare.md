# str.compare()

## Syntax:
`function long str.compare( const string a$, const string b$, [ boolean ignorecase ] )`

## Description
Compares two strings on equality and returns whether string `a$` is greater than, equal to or less than string `b$`. By default the test is done in a case sensitive way, e.g. "A" is not equal to "a". Optionally the comparison can be done case insensitive.
Note that contrary to function [cmp.mem()](../functions_memory_operations/cmp.mem.md), this function compares the two strings using the length the of the *largest* string.
- According to [cmp.mem()](../functions_memory_operations/cmp.mem.md), "ab" and "abc" are equal, as [cmp.mem()](../functions_memory_operations/cmp.mem.md) tests the two strings using the shortest length.
- According to [str.compare()](str.compare.md), "ab" and "abc" are not equal.

## Arguments
| | | |
|---|---|---|
| `const string` | `a$` |  a string  |
| `const string` | `b$` |  another string  |
| `[ boolean` | `ignorecase ]` |  when `true` is specified the comparison is done case-insensitive; when this argument is not specified the comparison is case sensitive  |

## Return values
| | |
|---|---|
| > 0 | the value of `a$` is greater than the value of `b$` |
| < 0 | the value of `a$` is less than the value of `b$` |
| 0 | the value of `a$` is equal to the value of `b$` |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long ret

ret = str.compare("ab", "ab")
| ret equals 0

ret = str.compare("a", "A")
| ret is greater than 0 as the ASCII value of a (97) is greater the ASCII value of A (65)

ret = str.compare("a", "A", true)
| ret equals 0

ret = str.compare("ab", "abcd")
| ret is less than 0 as 'ab' is shorter than 'abcd'
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
