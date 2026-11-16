# BOD.ActionsBeforeProcessingIncomingRequest

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1652-1652

```baan
DLL:   tcextbodapi
This function is available from 2019.03 (KB2040021).
Syntax: long BOD.ActionsBeforeProcessingIncomingRequest(
long             iXMLRequest,
ref             boolean          oCancel,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function validates the incoming request and sets
parameters needed during the processing.
It validates if the Accounting Entity and the Location (Location
is not checked for master data BODs) of the incoming request
matches the Accounting Entity and Location of the current
company (in Tenant, Accounting Entity and Location setup or in
BOD Parameters) and sets output argument oCancel to true in
case of a mismatch.
It extracts the LastModificationPerson/IDs/ID from the incoming
request and determines the linked LN user. If the LN user can
be determined, it switches user to the LN user.
It sets a parameter that enables the staging of outgoing BODs
that are triggered from the processing of the incoming request.
Preferably, it should be called in the BeforeExecuteHook
of every OnEvent section, e.g. the OnProcess, OnLoad, OnSync,
OnShow, OnAcknowledge etc.
Pre:    NA
Post:   After the incoming request is processed,
BOD.ActionsAfterProcessingIncomingRequest() or
BOD.ActionsAfterProcessingIncomingRequestWithAutomaticProcessing()
must be called.
Input:  iXMLRequest             - XML structure with request. Mandatory
Output: oCancel                 - true, if BOD must be cancelled
- false, if BOD can be processed
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No error occurred while executing the
actions.
<> 0                    - An error occurred while executing the
actions, or a mismatch was detected
during accounting entity / location
validation and BOD parameter Inbound
Routing Error Handling is set to
Return Error.
```
