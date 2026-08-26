# BDE.ExecuteMethod

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BDE
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1662-1663

```baan
DLL:   tcextbdeapi
This function is available from     2019.06 (KB2061133  ).
Syntax: long BDE.ExecuteMethod(
domain  tcbod.name       iBusinessObject,
domain  tcmcs.str30      iMethod,
long             iXMLRequest,
ref             long             oXMLResponse,
ref             long             oXMLResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes a method for a specified public BDE.
Pre:    If the method to be executed updates the database, a db.retry.point()
must have been set in the calling program.
Post:   If the method to be executed updates the database, a commit.transaction()
must be done by the calling program. However, in case of a non                      -zero
return value, an abort.transaction() must be done, otherwise updates may
have been done partially, which, once committed, may cause significant
data corruption.
Input:  iBusinessObject                       - The Business Object for which the method
must be executed, e.g.
"Item_v3". Mandatory
iMethod                                       - The method to be executed,
e.g. "Create" or "Change". Mandatory
iXMLRequest                                   - XML structure with request. Mandatory
Output: oXMLResponse                          - XML structure with response (if method is
executed successfully)
oXMLResult                                    - XML structure with result (in case of error)
oExceptionMessage                             - A message if the return value is not equal
to 0. This message contains the root cause of
the of the method failure.
oExceptionID                                  - An ID that refers to all error information. Use
the functions in Exception to get the error
messages. Note that more detailed error
information is in oXMLResult.
Return values:
0                                             - method is executed successfully
<> 0                                          - on errors
```

## Chapter 32 Public Interfaces for Factory Track

## Public Interfaces for FactoryTrackBDE

The following functions are available: FactoryTrackBDE.CreateElement FactoryTrackBDE.CreateNode
