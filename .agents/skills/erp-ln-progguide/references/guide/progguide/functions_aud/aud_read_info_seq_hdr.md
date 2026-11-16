# aud_read_info_seq_hdr()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_read_info_seq_hdr( long seqid, long seqno, ref string seqhdr )`

## Description
This reads the header information for a particular sequence file from the associated info file. You can access information in the sequence header using the [Macros - sequence header](macros_sequence_header.md).
Use [aud_read_seq_hdr()](aud_read_seq_hdr.md) to read the sequence header from the sequence file itself. The information retrieved by both functions is normally the same.

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |  The sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the sequence file was opened.  |
| `long` | `seqno` |  The sequence number of the sequence file.  |
| `ref string` | `seqhdr` |  The buffer in which the sequence header information is stored. Use [aud_get_hdr_size()](aud_get_hdr_size.md) or [aud_get_info_seq_hdr_size()](aud_get_info_seq_hdr_size.md) to retrieve the size of this buffer.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Error; Probably invalid *seqid*. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Macros - sequence header](macros_sequence_header.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
