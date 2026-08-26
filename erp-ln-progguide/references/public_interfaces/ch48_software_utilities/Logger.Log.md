# Logger.Log

> Chapter: Chapter 48 Public Interfaces for Software Utilities
>
> Group: Public Interfaces for Logger
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1925-1926

```baan
DLL:   tcextstlapi
This function is available from     2026.03 (KB3602838  ).
Syntax: long Logger.Log(
domain  tcstl.severity   iLoggerSeverity,
const           string           iLoggerFileName(),
long             iLineNumber,
long             iLoggerIdentifier,
const           string           iMessage(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is designed to programmatically add
message to logger utility.
Behavior:
-                       If the error LOGGER_ERR_LOGGING_OFF (-1) is encountered, then
logger is not enabled.
-                       Otherwise, logger is enabled.
Please refer to the session Application Logger (tcstl0502m000)
help for additional information.
Usage Example:
Please refer Public Interface Logger.Open() Dll Usage.
Pre:    Logger must be open.
Post:   Logger must be closed.
Input:  iLoggerSeverity         The severity of the message that will
be logged. Possible Options:
1                                               - Debug
2                                               - Info
3                                               - Warning
4                                               - Error
5                                               - Fatal Error
6                                               - Unknown
iLoggerFileName         The file name where the message will be
logged. Use tools macro "__FILE__".
iLineNumber             Line Number. Use tools macro
"__LINE__".
iLoggerIdentifier       Logger Identifier, reference to the
opened logging stream.
iMessage                Message to be logged.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Logger message added successfully.
< 0                     Error(s) occurred.
-                                              2 -    failed to open log file.
-                                              3 -    failed to close log file.
-                                              4 -    failed to add messages to the
log file.
-                                              6 -    failed to create a backup file.
-                                              8 -    invalid logger identifier.
-                                              9 -    severity level does not match
with the logger severtiy level.
-                                              10 -   logger is not open for adding
messages.
```
