# db.retry.hit()

## Syntax:
`function long db.retry.hit( )`

## Description
Use this to check whether the client database layer has returned to a retry point. You must set the retry point by using db.retry.point() before you call db.retry.hit(). See also [Database handling overview](../functions_database_handling/overview.md).

## Return values
| | |
|---|---|
| 0 | Retry point defined but not returned to. |
| > 0 | System returned to retry point. |
| -1 | No Retry point defined |
| -2 | Stack Error (Programming error in script. A db.retry.point() was done at a deeper stack level) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
The following code construct can be used for checking purposes:
```

if db.retry.hit() > 0    then
      | retry point hit
endif
```
The following frequently used code construct is wrong:
```

if db.retry.hit()       then        | db.retry.hit() can also -1 or
-2 as error condition!
       | retry point hit
endif
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
