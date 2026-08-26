# Logger.Open

> Chapter: Chapter 48 Public Interfaces for Software Utilities
>
> Group: Public Interfaces for Logger
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1926-1928

```baan
DLL:   tcextstlapi
This function is available from     2026.03 (KB3602838  ).
Syntax: long Logger.Open(
domain  tcmcs.str100     iLoggerFileName,
ref             long             oLoggerIdentifier,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is designed to programmatically open
logger utility.
Behavior:
-                       If the error LOGGER_ERR_LOGGING_OFF (-1) is encountered, then
logger is not enabled.
-                       Otherwise, logger is enabled.
Please refer to the session Application Logger (tcstl0502m000)
help for additional information.
Usage Example:
Code:
#pragma used dll "otcextstlapi"
long            logger.id, exception.id, ret
domain  tcmcs.s999m     exception.message
|* Logger Open
if      Logger.Open(
"",
logger.id,
exception.message,
exception.id) = 0
then
|* Logger Log
ret = Logger.Log(
tcstl.severity.debug,
__FILE__,
__LINE__,
logger.id,
"@Hello Everyone",
exception.message,
exception.id)
|* Logger Close
ret = Logger.Close(
logger.id,
exception.message,
exception.id)
endif
Pre:    N.A.
Post:   Logger must be closed.
Input:  iLoggerFileName         The file name for which the logger is
opened. In case empty, then
session code (prog.name$) from where
logger is opened is considered as
the logger file name.
Output: oLoggerIdentifier       Logger Identifier, reference to the
opened logging stream.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Logger opened successfully.
< 0                     Error(s) occurred.
-                                              1 -    logger is not enabled.
-                                              2 -    failed to open log file.
-                                              7 -    no open logs are found.
```

## Chapter 49 Public Interfaces for Exchange

## Public Interfaces for ExchangeScheme

The following functions are available: ExchangeScheme.NonRegularImport ExchangeScheme.RegularImport
