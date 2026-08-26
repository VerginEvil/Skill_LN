# rebuild.query()

## Syntax:
`function void rebuild.query( )`

## Description
Use this function to rebuild a query. If the query.extend functions are used the default query should be rebuild. This is done automatically after the before.program and the before.open.object.set sections. If these functions are used in other sections (to adjust them dynamically), the 4GLE has to be informed when the query has to be rebuild.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
