# brp.ready()

## Syntax:
`function long brp.ready( long brp_id )`

## Description
This signals the report writer that a record is ready to be imported into a particular report. The report writer then prints the record. You call this function after filling the fields of a record that the report writer can process. The fields are specified in the report and must be declared as EXTERN in the program script.

## Arguments
| | | |
|---|---|---|
| `long` | `brp_id` |  This identifies the particular report into which the record must be imported. It is the ID returned by [brp.open()](brp.open.md) or [brp.open.language()](brp.open.language.md) when the report was activated.  |

## Return values
0 success
-1 error: unknown ID specified

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
See [brp.open()](brp.open.md).

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)
- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
