# dte$()

## Syntax:
`function string dte$( )`

## Description
This returns the current date and time in the format MMDDYYHHMMSS

## Return values
A string containing the current date and time.

## Context
This function is implemented in the porting set and can be used in all script types.

- *dte$()* cannot be subscripted. To extract part of the return value, use a temporary string, as shown in the example below.

## Example
This example prints the current time in the format HH:MM:SS.
```

string  dat(12)
dat = dte$()
print dat(7;2), ":", dat(9;2), ":", dat(11;2)
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
