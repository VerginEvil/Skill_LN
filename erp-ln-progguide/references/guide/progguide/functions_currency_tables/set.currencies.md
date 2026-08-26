# set.currencies()

## Syntax:
`function void set.currencies( long seqno, string currency(3), [ string currency.desc mb ] )`

## Description
Use this function to create and fill the multicurrency table. The function inserts a single entry in the table. Currency rotation is based on the order of currencies in this table. Make sure that all the indices of the table (seqno) form a consecutive range, starting at 1

## Arguments
| | | |
|---|---|---|
| `long` | `seqno` |  sequence of currency when rotating  |
| `string` | `currency(3)` |  currency that is assigned to attr.currency$  |
| `[ string` | `currency.desc mb ]` |  Label referring to currency description or currency description itself. In the latter case, the currency description must start with the at sign [@]. Note that using a literal string makes the script language dependent.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

set.currencies( 1, "EUR" )
set.currencies( 2, "USD" )
set.currencies( 3, "GBP" )
```

## Example using labels for descriptions
```

set.currencies( 1, "EUR" , "tctcemms1000") |* Loc.Curr.
set.currencies( 2, "USD" , "tctcemms1001") |* Rep.1.Curr.
set.currencies( 3, "GBP" , "tctcmemm1002") |* Rep.2.Curr.
```

## Example using descriptions
```

set.currencies( 1, tcemm170.fcua , "@" & tt.field.desc("tcemm170.fcua"))
set.currencies( 2, tcemm170.fcub , "@" & tt.field.desc("tcemm170.fcub"))
set.currencies( 3, tcemm170.fcuc , "@" & tt.field.desc("tcemm170.fcuc"))
```

## Related topics
- [Currency tables overview and synopsis](overview_and_synopsis.md)
