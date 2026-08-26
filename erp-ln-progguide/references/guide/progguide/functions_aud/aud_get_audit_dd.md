# aud_get_audit_dd()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function void aud_get_audit_dd( const string seqhdr(), ref string colnames(,), ref long colinfo(,) )`

## Description
This retrieves the audit data dictionary information from the sequence header of a particular sequence file.

## Arguments
| | | |
|---|---|---|
| `const string` | `seqhdr()` |  The buffer containing the sequence header. You fill this by calling [aud_read_seq_hdr()](aud_read_seq_hdr.md) or [aud_read_info_seq_hdr()](aud_read_info_seq_hdr.md).  |
| `ref string` | `colnames(,)` |  An array containing the names of the audited fields. This array must be allocated dynamically.  |
| `ref long` | `colinfo(,)` |  An array containing the data dictionary information for the audited fields. This array must be allocated dynamically. The information for the *n*-th audited field can be interpreted as follows: `colinfo(AUD_FLD_TYPE, n)` contains the field type; for example: `DB.LONG, DB.FLOAT`. See this list of database types. `colinfo(AUD_FLD_DEPT, n)` contains the field depth; for non-array fields this is always 1. `colinfo(AUD_FLD_LEN, n)` contains the field length; See this list of database types and related byte counts. The length of fields of type DB.TIME depends on the TIV level of the porting set which generated the sequence file. If this TIV level is less than 2000, then DB.TIME fields have length 4 and the field contains a UTC long format value in Utc32 layout. If this TIV level is at least 2000, then DB.TIME fields have length 5 and the field contains a UTC long format value in Utc40 layout.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long    audit_flds
string  colnames(1,1) based
long    colinfo(1,1) based

audit_flds = aud_get_no_audit_flds(seqhdr)   | get number of
audited fields
alloc.mem(colnames, AUD_COL_NAME_LEN, audit_flds)
alloc.mem(colinfo, 3, aud_flds)
aud_get_audit_dd( seqhdr, colnames, colinfo )
```

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
