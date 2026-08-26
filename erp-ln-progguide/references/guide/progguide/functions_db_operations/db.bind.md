# db.bind()

## Syntax:
`function long db.bind( string table_name(9), [ ref string buffer(.), long comp_nr ] )`

## Description
This creates a pointer to a specified table. It returns a table ID that you use in other database calls to identify the table. The pointer is to a table with a particular company number and record buffer. You can create additional pointers to the same table by calling the function with a different company number and/or record buffer.Every call to db.bind()returns a unique pointer.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The table name.  |
| `[ ref string` | `buffer(.) ]` |  This optional argument specifies the record buffer to be used for the table. If you omit this argument, or if you specify an empty string, the default record buffer is used (that is, `rcd.tppmmmxxx`). When the default record buffer is used, the contents of the buffer are automatically copied to the table fields in your program script. This does not happen when you specify a record buffer other than the default buffer. Therefore, when a record buffer is used which is not the default record buffer, you must call [db.record.to.columns()](db.record.to.columns.md) to copy the field values from the record buffer to the table fields after using calls which change the record buffer, such as [db.set.to.default()](db.set.to.default.md) or [db.eq()](db.eq.md). Also use the function [db.columns.to.record()](db.columns.to.record.md) to copy the field values from the table fields to the record buffer before using calls which use the record buffer, such as [db.update()](db.update.md) or (again) [db.eq()](db.eq.md).  |
| `[ long` | `comp_nr ]` |  This optional argument specifies a company number for the table. The default company is the company of the user. If you include this argument, you must also include the *buffer* argument. So, if you want to specify a company other than the default company but want to use the default record buffer, specify the default buffer or an empty string in the *buffer* argument.  |

## Return values
| | |
|---|---|
| 0 | Error. |
| > 0 | Success; pointer is returned. |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  When you create more than one pointer to a table, you must use a different record buffer for each one.

## Example
```

long tcmcs001_id

if (switch.to.company(200) > 0) then
                tcmcs001_id = db.bind("ttcmcs001")
                db.first(ttcmcs001_id)
endif
                ...
db.first(ttcmcs001)
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
