# BOD.ExecutePublishForChameleon

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1665-1666

```baan
DLL:   tcextbodapi
Syntax: long BOD.ExecutePublishForChameleon(
domain  tcbod.name       iProtectedNoun,
long             iXMLRequest,
ref             long             oXMLResponse,
ref             long             oXMLResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes the publishing for a protected noun
of the chameleon BOD and can only be called from the
OnExecuteHook of the PublishEvent method of a protected noun.
It translates the protected noun to the public noun and
executes the PublishEvent method of the public noun
Pre:    NA
Post:   NA
Input:  iProtectedNoun  - The protected Noun, which is the BOD
that calls this function, e.g.
"ProductionOrderSFCBOD". Mandatory
iXMLRequest     - XML structure with request. Mandatory
Output: oXMLResponse    - XML structure with response (if PublishEvent
method is executed successfully)
oXMLResult      - XML structure with result (in case of error)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - BOD is published from LN.
<> 0                    - BOD could not be published from LN.
```
