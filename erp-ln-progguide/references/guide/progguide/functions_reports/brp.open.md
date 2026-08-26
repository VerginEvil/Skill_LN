# brp.open()

## Syntax:
`function long brp.open( string rep_name(16), string device(14), long mode )`

## Description
This activates a specified report and opens a specified spooler device (if it is not already open). Several reports can be active simultaneously. In a 4GL script, the name of the current report is stored in the predefined variable *spool.report*. This variable is available in the *on.choice* subsection of a *choice.print.data* section.

## Arguments
| | | |
|---|---|---|
| `string` | `rep_name(16)` |  The name of the report. Do not include a language code. The language of the user is automatically used.  |
| `string` | `device(14)` |  The code of the device on which the report must be printed. This code must be defined in the data dictionary. If you specify an empty string here, you can use the mode argument to display a window in which the user can select the required device.  |
| `long` | `mode` |  0 User is not prompted to select a spooler device. 1 A window is displayed in which the user can select a spooler device. A Cancel button enables the user to cancel the operation. 2 A window is displayed in which the user can select a spooler device. There is no option for canceling the operation.  |

## Return values
> 0 an ID for the activated report
0 report could not be activated
-1 spooler could not be opened

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and The report should be a tx report

## Example 1
```

brp_id1 = brp.open( "rtccom040101000", "F", 0 )
       | Spooler is opened automatically
brp.ready( brp_id1 )
brp.close( brp_id1 )
```

## Example 2
```

spool.open( "", spool.device, 1 )
        | Open spooler in script
brp_id1 = brp.open( "rtccom040101000", "D", 1 )
        | Spooler is not opened by report writer
brp_id2 = brp.open.language( "rtccom0401010003", spool.device, 1 )
        | Open next report in language code 3
...
<store values>
brp.ready( brp_id1 )
brp.ready( brp_id2 )
...
brp.close( brp_id1 )         | Close reports
brp.close( brp_id2 )
spool.close()                | Close spooler in script
```

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)
- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
