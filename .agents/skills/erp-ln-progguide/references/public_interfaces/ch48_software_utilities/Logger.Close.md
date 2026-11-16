# Logger.Close

> Chapter: Chapter 48 Public Interfaces for Software Utilities
>
> Group: Public Interfaces for Logger
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1943-1944

```baan
DLL:   tcextstlapi
This function is available from 2026.03 (KB3602838).
Syntax: long Logger.Close(
long             iLoggerIdentifier,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is designed to programmatically close
logger utility.
Behavior:
- If the error LOGGER_ERR_LOGGING_OFF (-1) is encountered, then
logger is not enabled.
- Otherwise, logger is enabled.
Please refer to the session Application Logger (tcstl0502m000)
help for additional information.
Usage Example:
Please refer Public Interface Logger.Open() Dll Usage.
Pre:    Logger must be open.
Post:   N.A.
Input:  iLoggerIdentifier       Logger Identifier, reference to the
opened logging stream. (Mandatory)
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Logger closed successfully.
< 0                     Error(s) occurred.
-3 -    failed to close log file.
-8 -    invalid logger identifier.
-10 -   log file is not open.
```
