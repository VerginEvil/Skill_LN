# PLMObject.SendToIDMForProject

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMObject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1851-1851

```baan
DLL:   pdextpdmapi
This function is available from 2024.10 (KB3532922).
Syntax: long PLMObject.SendToIDMForProject(
domain  pdobjt           iObjectType,
domain  pdokey           iKey,
domain  pdrevi           iRevision,
domain  pdcmpy           iERPCompany,
domain  pdpdm.eprj       iTPProject,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is for "Send to IDM for Project"
Action.
All other parameters(except TPProject)  are mandatory.
This function will work only when "Tansfer to IDM based on Conditions"
is enabled in IDM Preferences.
Any conditions to restrict certain Item Characters can be
handled in IDM Integration Configurations(pdadm0530m000).
Refer to Infor PLM for Discrete_Integration_Guide_for_Infor IDM Guide
for more information on configurations.
Pre:    The transaction must have been already committed prior to
calling this function. This function internally performs
transaction handling.
Post:   None
Input:  iObjectType     - Object Type
Possible values are:
- pdobjt.item (Item)
- pdobjt.document (Document)
- pdobjt.file (File)
iKey                    - Object Key
iRevision               - Object Revision
iERPCompany             - ERP Company
iProject                - TP project
Output: oExceptionMessage       - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID    -       An ID that refers to all error information. Use
the XML functions in Exception to get all relevant
information.
Return: long            - 0      if success
- <> 0  if fail
```
