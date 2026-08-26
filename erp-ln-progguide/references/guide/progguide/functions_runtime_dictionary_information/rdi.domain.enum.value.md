# rdi.domain.enum.value()

## Syntax:
`function long rdi.domain.enum.value( string domain_name, long enum_item, string language, ref string keyword(.), ref string descr(.), ref long value )`

## Description
This returns information about a specified item in an enumerated domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_name` |  The name of the domain.  |
| `long` | `enum_item` |  The position of the enum item for which you want to retrieve information.  |
| `string` | `language` |  The language code for the enumerated domain.  |
| `ref string` | `keyword(.)` |  This returns the constant name of the specified enum item.  |
| `ref string` | `descr(.)` |  This returns the description of the specified enum item.  |
| `ref long` | `value` |  This returns the constant value of the specified enum item.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long    cnt
long    ret
long    i

string  keyword(15)
string  descr(40)   mb
long    val

ret = rdi.domain.enum("ttyeno", cnt)
for i = 1 to cnt
    rdi.domain.enum.value("ttyeno", i, "2", keyword, descr, val)
    |...
    |...
endfor
```

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
