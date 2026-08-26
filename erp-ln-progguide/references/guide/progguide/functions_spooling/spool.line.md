# spool.line()

## Syntax:
`function long spool.line( )`

## Description
This sends the contents of the predefined variable *spool.pr.line* and a newline character to the spooler specified by the predefined variable *spool.id*. By default *spool.id* contains the ID of the current spooler. If more than one spooler is currently open, set *spool.id* to the ID of the required spooler before you call this function. After this function has been executed, *spool.pr.line* is cleared.
Note that this function uses the relevant spooler [Spooling overview and synopsis](overview_and_synopsis.md).

## Return values
0: success
<> 0: error

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Spooling overview and synopsis](overview_and_synopsis.md)
