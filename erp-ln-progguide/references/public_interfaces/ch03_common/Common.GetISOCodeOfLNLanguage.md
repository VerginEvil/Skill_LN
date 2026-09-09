# Common.GetISOCodeOfLNLanguage

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 111-112

```baan
DLL:   tcextmcsapi
Syntax: long Common.GetISOCodeOfLNLanguage(
domain  tcclan           iLNLanguage,
boolean          iForceReading,
ref     domain  tcilng           oISOLanguage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    : This function gets the ISO code of the LN language code.
Pre     : -
Post    : -
Input   : iLNLanguage           - The LN language: Mandatory
iForceReading         - When false, the function uses cache
if possible.
Output  : oISOLanguage          - The ISO language code.
oExceptionMessage     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                       - ISO code read
<> 0                    - on Errors
```
