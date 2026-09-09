# aud_read_next_audit_rec()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_read_next_audit_rec( long seqid, ref string rec_buff )`

## Description
This reads the next audited record from the current transaction. You can use [aud_read_audit_rec()](aud_read_audit_rec.md) to read a specific audit record and then use *aud_read_next_audit_rec()* to read the next and subsequent records. You can access information in the audited record using the [Macros - transaction record](macros_transaction_record.md)

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |  The sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the sequence file was opened.  |
| `ref string` | `rec_buff` |  A buffer containing the actual audited record. The predefined constant AUD_MAX_REC_SIZE holds the size of the buffer.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Error; Possible reasons are: *seqid* does not exist no more records in the current transaction of the specified sequence file |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Macros - transaction record](macros_transaction_record.md)

- [Macros - transaction dates and times](macros_transaction_dates_and_times.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
