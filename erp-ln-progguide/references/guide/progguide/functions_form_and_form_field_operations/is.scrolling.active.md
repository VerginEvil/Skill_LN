# is.scrolling.active()

## Syntax:
`function boolean is.scrolling.active( )`

## Description
This function tells whether the find.data section is called while scrolling is active.

## Return values
| | |
|---|---|
| true | Session is in a scrolling action. |
| false | Session is not in a scrolling action. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2490.

## Example
```

|Check whether find.data section is called while scrolling is active.

choice.find.data:
before.choice:
    if is.scrolling.active() then
        return
    endif

    .... before.choice find.data actions done when refreshing.
```

## Availability
This function is available in the following TIV level ranges:
- 2395 - 2399 (ES 10.7.4.1)
- 2481 - 2489 (ES 10.8.8)
- 2490 and above (ES 10.8.9)

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
