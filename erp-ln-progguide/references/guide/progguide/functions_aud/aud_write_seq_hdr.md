# aud_write_seq_hdr()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_write_seq_hdr( long seqid, const string seqhdr() )`

## Description
This writes header information to a specified sequence file. You can set the information for the sequence header with the [Macros - sequence header](macros_sequence_header.md).
The function writes the header information to the sequence file *and* to the associated info file.

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |  The sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the sequence file was opened.  |
| `const string` | `seqhdr()` |  The buffer that contains the header information to be written to the sequence file.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Error; Probably incorrect *seqid*.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
- [Macros - sequence header](macros_sequence_header.md)
