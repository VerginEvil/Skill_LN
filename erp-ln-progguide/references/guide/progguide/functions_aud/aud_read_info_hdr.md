# aud_read_info_hdr()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_read_info_hdr( const string host_name(), const string table_name(), long compno, ref string info_hdr() )`

## Description
This retrieves the header of the info file associated with a specified table and company number combination. You can access information in the info header using the [Macros - info header](macros_info_header.md).

## Arguments
| | | |
|---|---|---|
| `const string` | `host_name()` |  |
| `const string` | `table_name()` |  The name of the table with which the info file is associated. This takes the form *ppmmfff*, where *pp* is the package code, *mmm* is the module code, and *fff* is the file number.  |
| `long` | `compno` |  The company number.  |
| `ref string` | `info_hdr()` |  The buffer in which the info header is stored. The info header size is fixed. The predefined constant AUD_INFO_HDR_SIZE holds the size of the buffer.  |

## Return values
| | |
|---|---|
| > 0 | Success |
| -1 |  Error; Possible reasons are: host not found info file not found error opening info file info file locked unable to unlock file after read action unable to close info file  |
-
-
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
- [Macros - info header](macros_info_header.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
