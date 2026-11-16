# spool.open()

## Syntax:
`function long spool.open( string reportname, string device, string mode )`

## Description
This opens a specified spooler device.

## Arguments
| | | |
|---|---|---|
| `string` | `reportname` |  If you specify a report name in the *reportname* argument, it is stored in the predefined variable *spool.report*, and the current date and time are stored in the predefined variables *spool.date* and *spool.time*. The settings for the predefined variables *spool.fontnumber*, *spool.paper.type*, and *spool.left.mrg* are taken from the default settings for the specified report. If both *reportname* and *device* are specified, the defaults for the predefined variables are taken from the default settings for the specified report. The device name is stored in *spool.device*. If both reportname and device are empty (""), the predefined variables retain their values from the previous spool action.  |
| `string` | `device` |  If you specify a device name in the *device* argument, it is stored in the predefined variable *spool.device*. The settings for the predefined variables *spool.paper.type*, *spool.left.mrg*, *spool.fileout*, and *spool.pg.length* are taken from the default settings for the specified device.  |
| `string` | `mode` |  This determines whether or not a window is displayed where the user can change the device settings: 0 no window displayed 1 window displayed with a Cancel button 2 window displayed without a Cancel button  |

## Return values
0 spooler cannot be opened
> 0 ID of opened spooler – this is also available in *spool.id*

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  To use several spoolers simultaneously, first open all the spoolers. Then set the predefined variable *spool.id* to the relevant spooler ID before each [spool.line()](spool.line.md) function call.
After opening a second spooler, the predefined spool variables are set to the settings used for the newly opened spooler. In order to retrieve the original settings for the first spooler, use the function [spool.restore.variables()](spool.restore.variables.md).

## Example 1
```

long spooler
spooler = spool.open("","",1)
spooler = spool.open("rtccom040101000","D",0)
```

## Example 2
```

long spooler1, spooler2

spooler1 = spool.open("", "", 1)
spooler2 = spool.open("", "1", 0)

spool.pr.line = "Hello spooler1"
spool.id = spooler1
spool.line()
spool.pr.line = "Hello spooler2"
spool.id = spooler2
spool.line()

spool.id = spooler1
spool.close()          | close spooler 1
spool.id = spooler2
spool.close()          | close spooler 2
```

## Related topics
- [Spooling overview and synopsis](overview_and_synopsis.md)
