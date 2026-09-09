# aud_open_audit()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_open_audit( const string host_name(), const string table_name(), long compno, long seqno )`

## Description
This opens a specified sequence file. You identify the file to open by the table/company combination with which it is associated, the host on which it is located, and the sequence file number. The function returns a unique identifier for the file. Other audit functions use this identifier (referred to as the sequence identifier) to refer to this particular sequence file.
When you open a sequence file, the associated info file is automatically opened also (unless it is already open).

## Arguments
| | | |
|---|---|---|
| `const string` | `host_name()` |  The name of the host on which the sequence file is to be accessed. You can use [aud_select_host()](aud_select_host.md) to select the host to be used. If this argument is an empty string, *aud_select_host()* is called automatically to select a host name.  |
| `const string` | `table_name()` |  The name of the table with which the sequence file is associated. This takes the form *ppmmfff*, where *pp* is the package code, *mmm* is the module code, and *fff* is the file number.  |
| `long` | `compno` |  The company number.  |
| `long` | `seqno` |  The number of the particular sequence file to open.  |

## Return values
| | |
|---|---|
| > 0 | Sequence id for file |
| -1 | Error; Possible reasons are: Table or sequence file does not exist Error occurred while opening sequence file Open file limit reached |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Audit Information Overview](audit_information_overview.md)

- [Audit Information Synopsis](audit_information_synopsis.md)

- [Audit Information Sample Program](audit_information_sample_program.md)
