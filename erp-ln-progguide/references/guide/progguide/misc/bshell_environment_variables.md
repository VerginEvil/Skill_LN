# Bshell environment variables
Environment variables may be set by any means supplied by the operating system.
Environment variables may also be set by means of [bshell command line option -set](bshell_command_line_options.md).
Environment variable values may be retrieved by means of the bshell function [getenv$()](../functions_system_and_user_information/getenv.md).
Environment variables may be set and modified by means of the bshell function [setenv()](../functions_system_and_user_information/setenv.md).
Notice that it is possible to set the value of a [resource](bshell_resources.md) via its corresponding environment variable.
Environment variables are not restricted to any list. The following (incomplete) list shows some environment variables which have some influence on some aspect of the bshell functionality.
-
-
| | | |
|---|---|---|
| Variable | Synopsis | Explanation |
| BAAN_SCM_GRP | `BAAN_SCM_GRP=<>` | Use components (if any) from the SCM folder of the developer.  |
| SUPPRESS_WINHELP | `SUPPRESS_WINHELP=[0|1]` | Suppress the Baan Windows Help and use the old-fashioned Baan Helpviewer. Remove this setting in order to see again the Baan Windows Help!  |
| AUDIT_FILE_PATH | `AUDIT_FILE_PATH= */your/audit/folder*` | Set the location of the audit files. See also [Audit Information Overview](../functions_aud/audit_information_overview.md).  |
| TEST_RETRY | `TEST_RETRY=X` | This variable indicates how often the system must go back to a retry point at the moment of committing. This cannot be used when testing different sessions with retry points parallel. See: [Retry points](../functions_database_handling/retry_points.md) |
| BSE_COMPNR | `BSE_COMPNR=` |  Set your current company to ``. *Note*: The package combination of the company must be: The same as your current user package combination OR The package combination of the company has no software differences with your current package combination. For example a test package combination.  |
| PACKAGE_COMB | `PACKAGE_COMB=` |  Sets your current package combination to ``.  |
| NO_WORKTOP | `NO_WORKTOP=1` |  Suppress the need of the usage of Worktop.  |

## Related topics
- [getenv$()](../functions_system_and_user_information/getenv.md)
- [setenv()](../functions_system_and_user_information/setenv.md)
- [Bshell command line option -set](bshell_command_line_options.md)
- [Bshell resources](bshell_resources.md)
