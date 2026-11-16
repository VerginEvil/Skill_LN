# db.permission()

## Syntax:
`function long db.permission( long table_id, string field, [ ref string buffer ] )`

## Description
Use this to check the access permissions that a user has to a specified table or table field.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `string` | `field` |  To check the permissions for a particular field, enter the field name here. If you do not specify a field here, or if you specify an empty string, the function returns the permissions for the table.  |
| `[ ref string` | `buffer ]` |  A user's permissions for a table or table field can depend on the contents of a record. In this case, you must specify the record buffer of the table in the *buffer* argument. The function returns the user's permissions for the record in the record buffer. If a user's permissions depend on the contents of a record, and you do not specify the buffer argument, the function returns PERM.UNKNOWN.  |

## Return values
The function returns a long that indicates the permissions that the user has on the table or on a specified field of that table. The return value consists of one of, or a combination of, the following codes:
NO.PERMISSION 1
PERM.READ 2
PERM.MODIFY 4
PERM.WRITE 8
PERM.DELETE 16
NO.RESTRICTION (PERM.READ+PERM.MODIFY+PERM.WRITE+PERM.DELETE)
PERM.UNKNOWN 32
So, if the value 6 is returned, the user is permitted to both read and modify the specified table or table field.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long p
string buffer(18)

if attr.permission = PERM.UNKNOWN then
                p = db.permission(ttccom001, "", buffer)
else
                p = attr.permission
endif
if p > PERM.READ then
                ....
else
                | modifications not allowed in table tccom001 for this user
endif
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
