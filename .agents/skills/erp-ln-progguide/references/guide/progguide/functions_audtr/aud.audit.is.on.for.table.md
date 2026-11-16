# aud.audit.is.on.for.table()

## Syntax:
`function boolean aud.audit.is.on.for.table( const string table.code(), long company )`

## Description
This function checks whether audit is on for a specific database table.

## Arguments
| | | |
|---|---|---|
| `const string` | `table.code()` |  The table for which auditing must be checked.  |
| `long` | `company` |  The physical company of the table. The physical company number must be used, because the audit trail is created per physical company. For a logical table, the physical company can be retrieved using function db.get.physical.compnr()  |

## Return values
| | |
|---|---|
| True | Audit is on for the specified table. |
| False | Audit is not on for the specified table, or an error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Restrictions
None.

## Constraints
None.

## Example
To check whether audit is on for the Sales Order Headers table in the physical company 200:
```

boolean    retval
retval = aud.audit.is.on.for.table("tdsls400", 200)
```

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)
