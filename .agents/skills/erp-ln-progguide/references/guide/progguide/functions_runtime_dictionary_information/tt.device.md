# tt.device()

## Syntax:
`function boolean tt.device( string device(9), ref string desc() mb, ref long device_type )`

## Description
This returns information about a specified device.

## Arguments
| | | |
|---|---|---|
| `string` | `device(9)` |  The device name.  |
| `ref string` | `desc() mb` |  This returns the device description.  |
| `ref long` | `device_type` |  This indicates the device type. Possible values are: 1 physical printer 2 logical printer 3 append to file 4 rewrite file 6 direct 7 display 8 Windows printer 9 Mail API 10 Windows Server Printer 11 External Reporting Services 12 Document Output Management  |

## Return values
false error; device not found
true success

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
