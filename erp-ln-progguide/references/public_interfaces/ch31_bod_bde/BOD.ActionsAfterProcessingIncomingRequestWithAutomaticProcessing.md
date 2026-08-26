# BOD.ActionsAfterProcessingIncomingRequestWithAutomaticProcessing

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1632-1633

```baan
DLL:   tcextbodapi
This function is available from     2019.03 (KB2040021  ).
Syntax: long BOD.ActionsAfterProcessingIncomingRequestWithAutomaticProcessing(
long             iXMLRequest,
domain  tcmcs.str132     iObjectType,
domain  tcmcs.str132     iObject,
ref             long             oResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function publishes the staged BODs that were triggered
from the processing of the incoming request and resets the
parameter that enabled the staging of outgoing BODs in the
BOD.ActionsBeforeProcessingIncomingRequest() function.
Furthermore, it starts the automatic processing (if any) for
the object that was created/updated in LN from the incoming
request.
Preferably, this function should be called in the AfterExecuteHook
of every OnEvent section, e.g. the OnProcess, OnLoad, OnSync,
OnShow, OnAcknowledge etc.
Pre:    Before the incoming BOD is processed, function
BOD.ActionsBeforeProcessingIncomingRequest() must be called.
Post:   NA
Input:  iXMLRequest                           - XML structure with request. Mandatory
iObjectType                                   - object type for which automatic
processing must be started,
e.g. "PurchaseOrder"
iObject                                       - The identifier of the given ObjectType
e.g. the purchase order if ObjectType
is "PurchaseOrder"
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
