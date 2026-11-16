# BOD.HandleStagingBeforeProcessingIncomingRequest

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1674-1675

```baan
DLL:   tcextbodapi
This function is available from 2019.03 (KB2040021).
Syntax: long BOD.HandleStagingBeforeProcessingIncomingRequest(
domain  tcbod.name       iNoun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function sets a parameter that enables the staging of
outgoing BODs that are triggered from the processing of the
incoming request.
Preferably, it should be called in the BeforeExecuteHook
of every OnEvent section, e.g. the OnProcess, OnLoad, OnSync,
OnShow, OnAcknowledge etc.
Pre:    NA
Post:   After the incoming BOD is processed, function
BOD.HandleStagingAfterProcessingIncomingRequest()
must be called
Input:  iNoun                   - The noun of the incoming request
e.g. "PurchaseOrderBOD"
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Parameter that enables the staging
is set.
<> 0                    - Otherwise.
```
