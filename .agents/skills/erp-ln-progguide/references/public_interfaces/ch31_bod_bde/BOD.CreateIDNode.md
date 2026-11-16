# BOD.CreateIDNode

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1658-1659

```baan
DLL:   tcextbodapi
This function is available from 2023.05 (KB2292786).
Syntax: long BOD.CreateIDNode(
domain  tcncmp           iCompany,
domain  tcbod.name       iNoun,
domain  tcmcs.str256     iNounId,
domain  tcmcs.str100     iTagName,
ref     domain  tcmcs.long       oXmlNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates an ID node with a reference to a BOD.
The function determines the accounting entity, location and
lid attributes for the NounId in the specified Noun and returns
a Node with the NounId and related attributes.
<ID
accountingEntity="aaa"
location="bbb"
lid="ccc">iNounId</ID>
If iTagName is filled, the node is created with the value of
iTagName. Otherwise, the tag name is <ID>.
Pre:    NA
Post:   NA
Input:  iCompany                - Company. Mandatory.
iNoun                   - Noun name e.g. "SalesOrderBOD" or
"ItemMasterCommonBOD". Mandatory
iNounId                 - Noun ID value. Mandatory
iTagName                - Tag Name
Output: oXmlNode                - Generated Node for the NounId
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
