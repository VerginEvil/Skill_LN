# brp.close()

## Syntax:
`function void brp.close( long brp_id )`

## Description
This stops the report writer for the specified report. *brp_id* is the report ID returned by [brp.open()](brp.open.md) or [brp.open.language()](brp.open.language.md) when the report was activated. The report is sorted (if necessary) and sent to the printer spooler.
If output from different reports is sent to one spool file, you can manage the opening and closing of the printer spooler in the script by calling [spool.open()](../functions_spooling/spool.open.md) before calling [brp.open()](brp.open.md) and by calling [spool.close()](../functions_spooling/spool.close.md) after closing the last report with [brp.close()](brp.close.md). By default, the spooler is opened and closed automatically.

## Arguments
| | | |
|---|---|---|
| `long` | `brp_id` |  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
See [brp.open()](brp.open.md).

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)
- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
