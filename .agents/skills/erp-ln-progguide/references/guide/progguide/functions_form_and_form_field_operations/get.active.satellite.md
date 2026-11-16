# get.active.satellite()

## Syntax:
`function string get.active.satellite( [ ref long satellite.nr ] )`

## Description
This function returns the active satellite and can be used in UI scripts for multi main table controller sessions to determine which satellite is currently active. It can be used after the first satellite has been started; it cannot be used in the before.program section.

## Arguments
| | | |
|---|---|---|
| `[ ref long` | `satellite.nr ]` |  The number of the active satellite, as defined in MMT Satellite Sessions of the controller session. 0 when the active satellite cannot be determined.  |

## Return values
session code when successful, otherwise empty string.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [1804](../tiv/tiv_1804.md).

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
