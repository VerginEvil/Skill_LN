# aud_get_fld_values()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_get_fld_values( long colno, const long colinfo, const string rec_buff(), ref string values(,) )`

## Description
This retrieves the values of a specified field from an audit record. You can use this for records of type insert, delete, and update only. For records of type insert and delete, you can retrieve the values of any field. For records of type update, you can retrieve the values of changed fields and primary key fields only.

## Arguments
| | | |
|---|---|---|
| `long` | `colno` |  The column number.  |
| `const long` | `colinfo` |  An array containing the audit DD of the sequence file that contains the audit record. You fill this by calling [aud_get_audit_dd()](aud_get_audit_dd.md)  |
| `const string` | `rec_buff()` |  The buffer containing the audit record. You fill this by calling [aud_read_audit_rec()](aud_read_audit_rec.md) or [aud_read_next_audit_rec()](aud_read_next_audit_rec.md).  |
| `ref string` | `values(,)` |  An array containing the field values in string format. There are two string elements, the first containing the old value of the field, the second containing the new value. For example: values(1,1) old value values(2,1) new value The size of the both elements is determined by the predefined constant AUD_MAX_FLD_SIZE.  |

## Return values
| | |
|---|---|
| 0 | Record of type insert or delete. In these cases, there is no new value. Only *values* (1,1) is relevant.  |
| 1 | Record of type update. Both old and new values are relevant.  |
| -1 | Error. Possibly invalid column number or record not of type insert, delete, or update.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

| For a column of type DB.FLOAT

long    colno, coltype, coldept
string  rec_buff(AUD_MAX_REC_SIZE)
string  values(AUD_MAX_FLD_SIZE,2)
float   new_value, old_value

if ( aud_get_fld_values(colno, colinfo, rec_buff, values) = 1 ) then
                new_value = load.float( values(1,1) )
                old_value = load.float( values(2,1) )
endif
```

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
