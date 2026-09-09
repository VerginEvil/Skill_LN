# mb.set.info()

## Syntax:
`function long mb.set.info( long setid, ref string name, string desc, ref long n_items )`

## Description
This function returns information about a specified character set.

## Arguments
| | | |
|---|---|---|
| `long` | `setid` |  The character set ID.  |
| `ref string` | `name` |  The name of the character set.  |
| `string` | `desc` |  The description of the character set.  |
| `ref long` | `n_items` |  The number of defined ranges in the character set. Currently, this value is always zero.  |

## Return values
0 success
-1 the set ID is not linked to a known character set

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long id, nr, n_items
string name(20), desc(80)
nr = mb.nsets()
for id = 0 to nr
        if mb.set.info( id, name, desc, n_items ) <> -1 then
                print name, cr$(), lf$()
        endif
endfor
```

## Related topics
- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
