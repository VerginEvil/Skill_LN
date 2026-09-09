# update.occ()

## Syntax:
`function void update.occ( )`

## Description
The [4GL engine](../glossary/glossary.md#fourgl_engine) automatically detects changes a user makes to a field. However, it cannot detect changes to field values made in the program script. When you modify a field of the main table in the program script, you must call *update.occ()* to lock the record (delayed lock) and to switch on the *update.status* flag of the [4GL engine](../glossary/glossary.md#fourgl_engine). This ensures when that the database is next updated, the modifications are saved to the database. The database update action can be initiated either by the user or within the script (use execute(update.db)).
Before the *update.db* command is executed, the user can undo the changes with the *recover.set* command. If you do not want users to be able to undo changes, you can force an immediate update by calling execute(update.db) in the script.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## See also
[do.occ()](do.occ.md)

## Example
```

functions:
function extern void form.command.X()
{
    tiitm001.abcd = 9999
    update.occ()              | Sets flag to indicate change
    execute(update.db)
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
