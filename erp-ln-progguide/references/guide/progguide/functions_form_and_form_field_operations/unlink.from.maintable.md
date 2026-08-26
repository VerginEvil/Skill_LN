# unlink.from.maintable()

## Syntax:
`function void unlink.from.maintable( string field, ... )`

## Description
By default, when a session has a maintable, all form fields are treated as if they have a link to the maintable. When such fields are modified by the user, the maintable's *update.status* is set and the current record is marked as changed.
In some cases this behavior is unwanted, e.g. if the fields are used as a kind of filter, or in case fields are used to select records (by means of checkboxes).
This function can be used to remove this link with the maintable. In that way when such fields are modified by the user, the *update.status* of the maintable is not set and the record is not marked as changed.
This will also prevent that when the session ends, the user is asked if data should be saved in case these fields have been modified.

## Arguments
| | | |
|---|---|---|
| `string` | `field, ...` |  One or more fields to unlink from the maintable. Use the format "field" or "field(element)".  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Preconditions
- field cannot be a maintable field

## Example
```

after.form.read:
    | Unlink 3 fields from the maintable
    unlink.from.maintable("writeoff", "post.diff", "amount(3)")
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
