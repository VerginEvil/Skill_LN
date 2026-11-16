# get.user.default()

## Syntax:
`function boolean get.user.default( const string session.code, const string field, ref string field.value )`

## Description
Returns the default value for the passed sessioncode, field combination. The default is retrieved using the current user and current company.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  The sessioncode (i.e. ttaad2500m000) for which the default is wanted.  |
| `const string` | `field` |  The field (i.e. ttaad200.user) for which the default is wanted.  |
| `ref string` | `field.value` |  The current default value for the passed field.  |

## Return values
FALSE default not found
TRUE default found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
