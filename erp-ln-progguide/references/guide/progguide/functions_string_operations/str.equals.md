# str.equals()

## Syntax:
`function boolean str.equals( const string a$, const string b$, [ boolean ignorecase ] )`

## Description
Tests two strings on equality. By default the test is done in a case sensitive way, e.g. "A" is not equal to "a". Optionally the test can be done case insensitive.
This function is a shorthand for `(str.compare(a$, b$) = 0)`.
Note that contrary to function [cmp.mem()](../functions_memory_operations/cmp.mem.md), this function compares the two strings using the length the of the *largest* string.

- According to [cmp.mem()](../functions_memory_operations/cmp.mem.md), "ab" and "abc" are equal, as [cmp.mem()](../functions_memory_operations/cmp.mem.md) tests the two strings using the shortest length.

- According to [str.equals()](str.equals.md), "ab" and "abc" are not equal.

## Arguments
| | | |
|---|---|---|
| `const string` | `a$` |  a string  |
| `const string` | `b$` |  another string  |
| `[ boolean` | `ignorecase ]` |  when `true` is specified the test on equality is done case-insensitive; when this argument is not specified the test is case sensitive  |

## Return values
| | |
|---|---|
| true | the value of `a$` is equal to the value of `b$` |
| false | the value of `a$` is different from the value of `b$` |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

boolean ret

ret = str.equals("ab", "ab")
| ret = true

ret = str.equals("a", "A")
| ret = false

ret = str.equals("a", "A", true)
| ret = true

ret = str.equals("ab", "abcd")
| ret = false
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
