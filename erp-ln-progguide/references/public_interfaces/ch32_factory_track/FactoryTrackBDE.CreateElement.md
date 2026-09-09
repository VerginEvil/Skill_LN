# FactoryTrackBDE.CreateElement

> Chapter: Chapter 32 Public Interfaces for Factory Track
>
> Group: Public Interfaces for FactoryTrackBDE
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1682-1683

```baan
DLL:   brextbdeapi
This function is available from 2021.04 (KB2181351).
Syntax: long FactoryTrackBDE.CreateElement(
const           string           iElementID(),
const           string           iDomain(),
long             iParentNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID,
... )
Usage:        Expl:   Use this public interface to create a data element in the input
node.
Public Interface FactoryTrackBDE.CreateNode can be used to
create a parent node for this data element.
Example:
Create custom element "OrderNumber" in OutputNode.
long            ReturnValue
domain  tcorno          OrderNumber
ReturnValue = FactoryTrackBDE.CreateElement(
"OrderNumber",
"tcqiv1",
OutputNode,
ExceptionMessage,
ExceptionID,
OrderNumber)
This will add this element Node to the OutputNode (assuming
OrderNumber = "AAA000001"):
<OrderNumber
Type="String"
Domain="tcorno">AAA000001</OrderNumber>
Pre:    N.A.
Post:   N.A.
Input:
iElementID              - The name of the custom element:
Mandatory. Dots are truncated.
iDomain                 - The domain of the custom element:
Mandatory.
iParentNode             - The parent XML node of the element
that is being created: Mandatory.
... (1 argument)        - The value of the XML element:
Mandatory.
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                       - Success
<> 0                    - Failure
```
