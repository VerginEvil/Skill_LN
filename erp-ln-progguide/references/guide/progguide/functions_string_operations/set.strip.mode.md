# set.strip.mode()

## Syntax:
`function long set.strip.mode( long table.id, long mode )`

## Description
*set.strip.mode()* sets or resets the 'strip-on-assignment' flag for all string fields of the table specified by *table_id*. The *mode* argument indicates whether the flag is to be set on or off. Non-zero indicates set flag on, zero indicates set flag off. Setting this flag on a symbol *a$* means that assignments to other variables *from* this value will behave as an assignment from *strip$( a$ )*.

## Arguments
| | | |
|---|---|---|
| `long` | `table.id` |  |
| `long` | `mode` |  |

## Return values
0: success
< 0: error

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  This function does not affect the actual contents of the fields.
If *set.strip.mode()* is the first call on the table specified by *table_id*, then that table's structure will be loaded.

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
- [set.symbol.strip.mode()](set.symbol.strip.mode.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
