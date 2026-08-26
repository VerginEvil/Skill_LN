# Bshell resources
Resources are specified in the u<user> file in the '$BSE/lib/user' directory, but also in the files '$BSE/lib/defaults/<logical_name_of_bshell>' and '$BSE/lib/defaults/all'. The logical name of the bshell is the name you specify for the Bshell in BW.
A bshell resource often has a corresponding [environment variable](bshell_environment_variables.md) via which it is possible to set the value of the resource.
Resource values may be retrieved by means of the bshell function [get.resource$()](../functions_system_and_user_information/get.resource.md).
The following (incomplete) list shows some of the bshell resources.
-
-
-
| | | | |
|---|---|---|---|
| Resource name | Corresponding environment variable | Default value | Explanation |
| art_trace | BAAN_ART_TRACE | 0 | Set this resource to [debug the ARTM code](../functions_artm/artm_debugging.md) in the application scripts.  |
| debug_level | DEBUG_LEVEL | 0 |  Set the debug level. Choose a combination of the following (octal) flag values. Most of the flags have a corresponding [command line option](bshell_command_line_options.md) by which it can be set.  |
| debug_long64 | DEBUG_LONG64 | 0 |  Set the debug level for the tracing/logging of activities involving integer arithmetic outside the signed 32-bit value range. Choose a combination of the following (decimal) flag values. Messages triggered by this resource are saved in a separate log file in a separate directory. The name of the directory is IntegerArithmetic.%h, where the pattern %h is substituted with the current hostname. This directory is created in the same directory as where the normal log file of the bshell is created. See [command line option -logfile](bshell_command_line_options.md). The name of the separate file is %u.%p.log, where the pattern %u is substituted with the current (short) baan user name and the pattern %p is substituted with the OS process ID of the bshell. This file is created in the IntegerArithmetic.%h directory described above. If the directory or the file cannot be created, then the normal log file of the bshell is used.  |
| language | BSE_LANG | 2 | your current language |
| locale | BSE_LOCALE | ISO-8859-1 | your current locale |
| max_retry | MAX_RETRY | 10 | This resource indicates how often the system may return to a [retry point](../functions_database_handling/retry_points.md) as a result of an abort in an update action.  |
| mle_all_data_languages |  | 1 |  In a multi language environment, the default behavior for queries is to retrieve all data languages from the database. When this resource is set to non-default value 0 in a multi language environment, only the current language value of multi language fields is retrieved from the database. In some cases this may be undesirable, therefore several mechanisms are supplied to overrule this behavior. For overruling this behavior at query level, see [embedded SQL](../functions_database_handling/embedded_sql.md) and [dynamic SQL](../functions_database_handling/dynamic_sql.md) ( [sql.parse() function](../functions_dynamic_sql_queries/sql.parse.md)). For overruling this behavior at table level, see [rdi.table](../functions_runtime_dictionary_information/rdi.table.md). For overruling this behavior in (more or less deprecated) low level database operations, see [Database operations overview](../functions_db_operations/overview.md). It must be realized that the influence of this resource is not restricted to the bshell. All other tools of the porting set are also influenced by it. Where applicable, the overruling mechanisms referred to in the previous paragraph are also used implicitly in such tools in order to guarantee selection of all the data languages from the database. Notice that the mle_all_data_languages resource does not have a corresponding environment variable. The mle_all_data_languages resource is available as of [TIV level 2140](../tiv/tiv_2140.md).  |
| utc40 |  | 0 |  Activate the Utc40 mode in the porting set. In the bshell, also activate the 64-bit mode. It must be realized that the influence of this resource is not restricted to the bshell. For example, the amount of bytes used to exchange a UTC long format value between any client and a database server is also determined by this resource. See also the description of the SQL timestamp data type. Notice that the utc40 resource does not have a corresponding environment variable.  |

## Related topics
- [get.resource$()](../functions_system_and_user_information/get.resource.md)
- [Bshell command line option -set](bshell_command_line_options.md)
- [Bshell environment variables](bshell_environment_variables.md)
