# BOD.ExecuteMethod

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1661-1662

```baan
DLL:   tcextbodapi
Syntax: long BOD.ExecuteMethod(
domain  tcbod.name       iNoun,
domain  tcmcs.str30      iMethod,
long             iXMLRequest,
ref             long             oXMLResponse,
ref             long             oXMLResult,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes a non-batch method for a specified
BOD and can only be called from the OnExecuteHook of the On<verb>
(e.g. OnProcess or OnSync) method of an incoming noun.
For example: if the actionCode of the incoming noun is "Add", call
this function with iMethod is "Create" or if the actionCode is
"Change", call this function with iMethod is "Change".
Pre:    NA
Post:   NA
Input:  iNoun           - The (protected) Noun for which the method
must be executed, e.g.
"ReceiveDeliveryWarehousingBOD". Mandatory
iMethod         - The method to be executed,
e.g. "Create" or "Change". Mandatory
iXMLRequest     - XML structure with request. Mandatory
Output: oXMLResponse    - XML structure with response (if method is
executed successfully)
oXMLResult      - XML structure with result (in case of error)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0               - Method is executed.
<> 0            - Method could not be executed.
```
