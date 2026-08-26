# BOD.ExecuteShowForChameleon

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1648-1649

```baan
DLL:   tcextbodapi
Syntax: long BOD.ExecuteShowForChameleon(
domain  tcbod.name       iProtectedNoun,
long             iXMLRequest,
ref             long             oXMLResponse,
ref             long             oXMLResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes the Show method of the public noun
of the chameleon BOD and can only be called from the
OnExecuteHook of the Show method of a protected noun.
It translates the protected noun to the public noun and
executes the Show method of the public noun. Then it renames
the response XML to the response XML of the protected noun
Pre:    NA
Post:   NA
Input:  iProtectedNoun                - The protected Noun, which is the BOD
that calls this function, e.g.
"ProductionOrderSFCBOD". Mandatory
iXMLRequest                           - XML structure with request. Mandatory
Output: oXMLResponse                  - XML structure with response (if method is
executed successfully)
oXMLResult                            - XML structure with result (in case of error)
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Method is executed succesfully.
<> 0                                          - Otherwise.
```
