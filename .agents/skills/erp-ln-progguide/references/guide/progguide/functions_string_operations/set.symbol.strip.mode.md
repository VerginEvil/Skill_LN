# set.symbol.strip.mode()

## Syntax:
`function long set.symbol.strip.mode( ref string str$, long mode )`

## Description
*set.symbol.strip.mode()* sets or resets the 'strip-on-assignment' flag for the actual variable passed as function argument *str$*. The *mode* argument indicates whether the flag is to be set on or off. Non-zero indicates set flag on, zero indicates set flag off. Setting this flag on a symbol *a$* means that assignments to other variables *from* this value will behave as an assignment from *strip$( a$ )*.

## Arguments
| | | |
|---|---|---|
| `ref string` | `str$` |    |
| `long` | `mode` |    |

## Return values
0: success
< 0: error

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function does not affect the actual contents of the variable.

## Example
```

table   tttaad200
string  s(100)
string  s2(100) fixed
string  s3(100)

if( set.strip.mode(tttaad200, 1) < 0 ) or
        ( set.symbol.strip.mode(s2, 1) < 0 ) then
                        | handle error
endif

db.first(tttaad200)

s = tttaad200.user  | s contains username without trailing spaces
s2 = s              | s2 is fixed so username is filled out with spaces
s3 = s2             | s3 contains username without trailing spaces
s3 = strip$(s2)     | strip$ is useless here, the set.symbol.strip.mode did this
```

## Related topics
- [set.strip.mode()](set.strip.mode.md)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
