# aud_get_hdr_size()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_get_hdr_size( long seqid )`

## Description
Because the audit DD of a table can differ in different sequence files, the size of the sequence header can also differ from sequence file to sequence file.
This function returns the size (in bytes) of the header of a specified sequence file. You can use the return value to allocate space for the sequence header before retrieving it with [aud_read_info_seq_hdr()](aud_read_info_seq_hdr.md) or [aud_read_seq_hdr()](aud_read_seq_hdr.md). *seqid* is the sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the particular sequence file was opened.

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |    |

## Return values
| | |
|---|---|
| > 0 | Sequence header size (in bytes) |
| -1 | Error; probably invalid *seqid* |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  You can also use [aud_get_info_seq_hdr_size()](aud_get_info_seq_hdr_size.md) to retrieve the size of the sequence header. The value returned by both functions is normally the same.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
