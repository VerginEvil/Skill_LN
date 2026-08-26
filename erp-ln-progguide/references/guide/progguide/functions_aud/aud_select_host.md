# aud_select_host()

## Warning
*The functions and macros listed below must not be used anymore.* Using them in BaanERP 5.0c or higher releases may result in less reliable data. Know that there is a new set of functions that you can use for retrieval of audit information. Refer to [Audit management overview](../functions_audtr/audit_management_overview.md)

## Syntax:
`function long aud_select_host( const string table_name(), long compno, long user_interaction, ref string host_name() )`

## Description
Audit files can be located on more than one host (for example, on the local host and a remote host, or on two or more remote hosts). The system maintains a list of hosts where audit files for particular table and company number combinations are located. When accessing audit files, this host list is used to select the particular host on which the files are to be accessed.
*aud_select_host()* selects and returns the name of the host on which the audit files for a specified table and company are to be accessed. You can use this host name as input to [aud_open_audit()](aud_open_audit.md), [aud_read_info_hdr()](aud_read_info_hdr.md), and [aud_write_info_hdr()](aud_write_info_hdr.md).

## Arguments
| | | |
|---|---|---|
| `const string` | `table_name()` |  The name of the table for which audit files are to be accessed. This takes the form *ppmmfff*, where *pp* is the package code, *mmm* is the module code, and *fff* is the file number.  |
| `long` | `compno` |  The company number.  |
| `long` | `user_interaction` |  Specifies whether or not user interaction is required. Possible values are:  |
| `ref string` | `host_name()` |  This returns the name of the selected host.  |

## Return values
| | |
|---|---|
| >= 0 | Success |
| -1 | Error; Possibly unable to find host list or auditing not enabled for the specified table and company.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  If the AUD_HOST_NAME environment variable is set, *aud_select_host()* always returns the host name stored in this variable, regardless of the setting specified by the function. For example, the application will use the audit file on the remote host 'ed5c21', if the environment variable has been set as follows:
```

AUD_HOST_NAME=ed5c21
```
Note that this environment variable applies to all tables. If it is set, it is used for accessing the audit files of all tables.

## Related topics
- [Audit Information Overview](audit_information_overview.md)
- [Audit Information Synopsis](audit_information_synopsis.md)
- [Audit Information Sample Program](audit_information_sample_program.md)
