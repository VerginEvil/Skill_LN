# plcm.add.command

## Syntax:
`function long plcm.add.command( string command.id, string command.text, [ enum ecatg, boolean command.checked ] )`

## Description
Adds a custom command. This command will appear in the specific menu of the plan chart.

## Arguments
| | | |
|---|---|---|
| `string` | `command.id` |  Unique ID of the command. If ID equals "SEPARATOR", a separator will be added to the specific menu. If a command with this ID has been added before, the command text will be changed.  |
| `string` | `command.text` |  Command text.  |
| `[ enum` | `ecatg ]` |  An optional parameter for specifying the category of the command. This parameter is applicable when running in one of the following UI-modes: WEBUI_COMMONUI, HTML_UI or SOHO_XI. If this parameter is not specified while running in one of these three UI-modes, the category Actions will be used by default.  |
| `[ boolean` | `command.checked ]` |  An optional parameter for specifying the check mark in front of the command. Specify TRUE if you want the command to appear checked. Specify FALSE to show the command unchecked.  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)

- [Example](example.md)
