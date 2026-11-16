# 505 ENOSERVER - Server not available
| |
|---|
| *Description:* |
| This error can indicate that: The virtual machine cannot find information about a table's database. The server cannot be started. For more information, see the log file. |
| *Solution:* |
| Start the *Tables by Database (ttaad4111m000)* session to check whether the database is specified for the table that caused the problem. If the table is not specified for the database, add the table to the database and convert the table to the runtime datadictionary. |
