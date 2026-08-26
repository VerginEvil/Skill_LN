# BOD.ActionsAfterProcessingIncomingRequest

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1631-1632

```baan
DLL:   tcextbodapi
This function is available from     2019.03 (KB2040021  ).
Syntax: long BOD.ActionsAfterProcessingIncomingRequest(
long             iXMLRequest,
ref             long             oResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function publishes the staged BODs that were triggered
from the processing of the incoming request and resets the
parameter that enabled the staging of outgoing BODs in the
BOD.ActionsBeforeProcessingIncomingRequest() function.
Preferably, it should be called in the AfterExecuteHook
of every OnEvent section, e.g. the OnProcess, OnLoad, OnSync,
OnShow, OnAcknowledge etc.
Pre:    Before the incoming BOD is processed, function
BOD.ActionsBeforeProcessingIncomingRequest() must be called.
Post:   NA
Input:  iXMLRequest                           - XML structure with request. Mandatory
Output: oResult                               - 0 if succes, otherwise <> 0
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Staged BODs are published.
<> 0                                          - Staged BODs could not be published.
```
