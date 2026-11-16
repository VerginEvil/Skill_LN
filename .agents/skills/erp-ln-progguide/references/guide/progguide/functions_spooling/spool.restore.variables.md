# spool.restore.variables()

## Syntax:
`function boolean spool.restore.variables( [ long brp.id ] )`

## Description
This function sets the predefined spool variables to the values they had when the spooler was opened. If the optional argument is not specified, this function uses the predefined variable spool.id to look up the spooler to use.

## Arguments
| | | |
|---|---|---|
| `[ long` | `brp.id ]` |  Optional, use this to restore the variables using a report id instead of spooler id.  |

## Return values
true if the spooler was found and the variables are restored, false otherwise.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

	| These 2 reports may go to different devices with different settings
	progress.report = brp.open("tfacr522101000", "", 1)
	error.report = brp.open("tfacr522102000", "", 1)

	| To check whether the first report is being printed to an SSRS device, first
	| the spool variables should be restored for that report:
	spool.restore.variables(progress.report)
	if spool.ssrs then
		|...
	endif
```

## Related topics
- [Spooling overview and synopsis](overview_and_synopsis.md)
