# aud_read_next_tran()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_read_next_tran( long seqid, ref string tran_hdr() )`

## Description
This reads the next transaction header in the specified sequence file. You can use [aud_read_tran()](aud_read_tran.md) to read a specific transaction header and then use *aud_read_next_tran()* to read the next and subsequent transaction headers. You can access information in the transaction header using the [Macros - transaction header](macros_transaction_header.md).

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |  The sequence identifier returned by [aud_open_audit()](aud_open_audit.md) when the sequence file was opened.  |
| `ref string` | `tran_hdr()` |  A buffer containing the transaction header information. The predefined constant AUD_TRAN_HDR_SIZE holds the size of this buffer.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Error; Possible reasons are: *seqid* does not exist No more transactions in the sequence file. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Macros - transaction header](macros_transaction_header.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
