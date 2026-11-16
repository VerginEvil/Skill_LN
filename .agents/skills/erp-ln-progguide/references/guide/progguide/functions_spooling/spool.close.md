# spool.close()

## Syntax:
`function void spool.close( )`

## Description
This closes the spooler specified by the predefined variable *spool.id*. By default *spool.id* contains the ID of the current spooler. If more than one spooler is currently open, set *spool.id* to the ID of the required spooler before you call this function. After the spooler is closed, *spool.id* is set to zero.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Spooling overview and synopsis](overview_and_synopsis.md)
