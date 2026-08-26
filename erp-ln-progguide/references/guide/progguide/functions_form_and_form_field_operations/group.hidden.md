# group.hidden()

## Syntax:
`function void group.hidden( long i.group.nr )`

## Description
This function hides the group from the form, including all associated fields, labels, and subgroups. The group can be made visible again by a user by Personalizing the Form.

## Arguments
| | | |
|---|---|---|
| `long` | `i.group.nr` |  The number of the group  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Example
```

after.form.read:
    group.hidden(28)
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
