# InstallationGroup.ViewStructure

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for InstallationGroup
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1354-1355

```baan
DLL:   tsextbscapi
This function is available from 2025.11 (KB3612972).
Syntax: long InstallationGroup.ViewStructure(
domain  tsbsc.clst       iInstallationGroup fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the View Installation Group
Structure browser for the Installation Group.
Pre     : Not applicable.
Post    : Not applicable.
Input:  iInstallationGroup
Installation Group
Mandatory.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - GraphicalStructure was started
<> 0    - An error occured.
```
