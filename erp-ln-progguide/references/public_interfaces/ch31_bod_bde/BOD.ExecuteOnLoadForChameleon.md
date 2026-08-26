# BOD.ExecuteOnLoadForChameleon

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1643-1644

```baan
DLL:   tcextbodapi
Syntax: long BOD.ExecuteOnLoadForChameleon(
domain  tcbod.name       iProtectedNoun,
long             iXMLRequest,
ref             long             oXMLResponse,
ref             long             oXMLResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes the OnLoad method of a protected noun
of the chameleon BOD and can only be called from the
OnExecuteHook of the OnLoad method of an incoming public noun.
The function is used to route an incoming BOD with Load verb to
a protected noun.
Pre:    NA
Post:   NA
Input:  iProtectedNoun                - The (protected) Noun for which the OnLoad
method must be executed, e.g.
"SalesOrderInBOD". Mandatory
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
Return: 0                                     - BOD is processed in LN.
<> 0                                          - BOD could not be processed in LN
```
