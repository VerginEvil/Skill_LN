# aud_update_infofile()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_update_infofile( long seqid, const string seqhdr )`

## Description
This writes sequence header information to the info file associated with the specified sequence file. You can set the information for the sequence header with the [Macros - sequence header](macros_sequence_header.md)
Note that the sequence header information is not automatically copied to the sequence header in the sequence file itself. To ensure that there is no mismatch between the sequence headers in the info file and in the sequence file, use [aud_write_seq_hdr()](aud_write_seq_hdr.md) instead to update a sequence header.

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |  The sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the sequence file was opened.  |
| `const string` | `seqhdr` |  The buffer that contains the sequence header information.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 |  Error; Possible reasons are: Error occurred while opening the information file Open file limit reached Incorrect sequence identifier  |
-
-
-

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
