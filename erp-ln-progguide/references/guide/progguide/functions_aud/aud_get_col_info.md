# aud_get_col_info()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function void aud_get_col_info( const string seqhdr(), long col_no, ref string col_name(), ref long col_type, ref long col_dep, ref long col_len )`

## Description
This retrieves information about a specified field from the sequence header of a particular sequence file. It retrieves the same information as [aud_get_audit_dd()](aud_get_audit_dd.md), but for a single field only.

## Arguments
| | | |
|---|---|---|
| `const string` | `seqhdr()` |  The buffer containing the sequence header. You fill this by calling [aud_read_seq_hdr()](aud_read_seq_hdr.md) or [aud_read_info_seq_hdr()](aud_read_info_seq_hdr.md).  |
| `long` | `col_no` |  The column number.  |
| `ref string` | `col_name()` |  The field name.  |
| `ref long` | `col_type` |  The field type – for example, DB.LONG, DB.STRING. See this list of database types.  |
| `ref long` | `col_dep` |  The field depth. This is always 1 for non-array fields.  |
| `ref long` | `col_len` |  The field length. See this list of database types and related byte counts. The length of fields of type DB.TIME depends on the TIV level of the porting set which generated the sequence file. If this TIV level is less than 2000, then DB.TIME fields have length 4 and the field contains a UTC long format value in Utc32 layout. If this TIV level is at least 2000, then DB.TIME fields have length 5 and the field contains a UTC long format value in Utc40 layout.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
