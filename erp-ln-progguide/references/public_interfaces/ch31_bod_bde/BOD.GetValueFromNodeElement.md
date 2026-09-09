# BOD.GetValueFromNodeElement

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1673-1673

```baan
DLL:   tcextbodapi
This function is available from 2023.05 (KB2292786).
Syntax: long BOD.GetValueFromNodeElement(
long             iXmlNode,
domain  tcmcs.str132     iPath,
domain  tcmcs.str14      iDomainCode,
ref     domain  tcmcs.s512m      oValue mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function gets the value from a specific element in a node.
It uses the path to locate the element in the node. If the
domain code is supplied, the element value is checked against the
domain definition and an error is returned if the value does
not match the domain definition.
Pre:    NA
Post:   NA
Input : iXmlNode                - The xml node to search in. Mandatory
iPath                   - The path in the xml node e.g.
"<Shipment><ShipmentHeader><DocumentID><ID>".
Mandatory
iDomainCode             - Domain code. If supplied, the element
value is checked against the domain
definition.
Output: oValue                  - The value that is extracted from the
node.
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
