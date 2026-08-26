# PLMObject.GenerateKeyNumber

> Chapter: Chapter 42 Public Interfaces for Product Lifecycle Management
>
> Group: Public Interfaces for PLMObject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1829-1830

```baan
DLL:   pdextpdmapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long PLMObject.GenerateKeyNumber(
domain  pdadm.clas       iTable,
domain  pdadm.keyn       iField,
domain  pdproj           iProject,
ref     domain  pds060           oKeyID,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is to generate next sequence number
using PLM Mask.
All the parameters are mandatory.
Input:  iTable                                - Table Name
iField                                        - Field Name
iProject                                      - Project Code
Output: oKeyID                                - output Key
oExceptionMessage                       - The error message if the return value is not
equal to 0. A warning message if filled and the
return value is 0.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return:  long                         - 0      if success
-                                       <> 0  if fail
```
