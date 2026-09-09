# BOD.CreateCodeDefinitionReferenceNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1658-1658

```baan
DLL:   tcextbodapi
This function is available from 2023.05 (KB2292786).
Syntax: long BOD.CreateCodeDefinitionReferenceNode(
domain  tcncmp           iCompany,
domain  tcmcs.str50      iListId,
domain  tcmcs.str100     iCode,
domain  tcmcs.str50      iTagName,
ref     domain  tcmcs.long       oXmlNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a node with a reference to the
CodeDefinitionBOD.
Example for iListId is "Process Codes", iCode is "xxx" and
iTagName is "ProcessCode":
<ProcessCode
listID="Process Codes"
accountingEntity="aaa">xxx</ProcessCode>
Pre:    NA
Post:   NA
Input:  iCompany                - Company. Mandatory.
iListId                 - List ID name to be used for the listID
attribute. Mandatory
iCode                   - Code. Mandatory
iTagName                - Tag name. Mandatory
Output: oXmlNode                - Generated Node
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - OK.
<> 0                    - Error occurred.
```
