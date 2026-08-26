# clear.query.extend.in.zoom()

## Syntax:
`function void clear.query.extend.in.zoom( )`

## Description
This clears a query extension that was previously defined in the *selection.filter* section. The 4GL engine automatically clears the extension in the *after.zoom* section of the session. Use this function to force an earlier removal of the query extension. For example, to clear the query extension before defining an extension for another zoom session.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Column filtering](column_filtering.md)
- [Query extensions sample program](example.md)
