# rprt_send()

## Syntax:
`function void rprt_send( )`

## Description
This is a short version of [brp.ready()](brp.ready.md). It has the same effect as:
brp.ready( spool.report )
That is, it signals the report writer that a record is ready to be imported into the current report. The predefined variable *spool.report* stores the name of the current report.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
See [rprt_open()](rprt_open.md).

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)

- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
