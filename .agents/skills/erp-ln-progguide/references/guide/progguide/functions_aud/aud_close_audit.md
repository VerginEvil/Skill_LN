# aud_close_audit()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_close_audit( long seqid )`

## Description
Discards the specified sequence identifier. *seqid* is the identifier returned by [aud_open_audit()](aud_open_audit.md) aud_open_audit when the particular sequence file was opened. When the last sequence file associated with an info file is closed, the info file is also closed.

## Arguments
| | | |
|---|---|---|
| `long` | `seqid` |    |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | error (for example, could not close the sequence file or info file). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
