# aud_write_info_hdr()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_write_info_hdr( long host_name(), string table_name(), long compno, const string info_hdr )`

## Description
This writes info header information to a specified info file. You can set the information for the info header with the [Macros - info header](macros_info_header.md)

## Arguments
| | | |
|---|---|---|
| `long` | `host_name()` |  |
| `string` | `table_name()` |  The name of the table with which the info file is associated. This takes the form *ppmmfff*, where *pp* is the package code, *mmm* is the module code, and *fff* is the file number.  |
| `long` | `compno` |  The company number.  |
| `const string` | `info_hdr` |  The buffer that contains the header information to be written to the info file.  |

## Return values
| | |
|---|---|
| > 0 | Success |
| -1 |  Error; Possible reasons are: Host not found Table or information file does not exist Error occurred while opening information file Open file limit reached  |
-
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
- [Macros - info header](macros_info_header.md)
