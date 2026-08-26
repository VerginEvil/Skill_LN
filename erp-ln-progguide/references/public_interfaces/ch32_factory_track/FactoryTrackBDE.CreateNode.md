# FactoryTrackBDE.CreateNode

> Chapter: Chapter 32 Public Interfaces for Factory Track
>
> Group: Public Interfaces for FactoryTrackBDE
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1664-1666

```baan
DLL:   brextbdeapi
This function is available from     2021.04 (KB2181351  ).
Syntax: long FactoryTrackBDE.CreateNode(
const           string           iNodeID(),
long             iBDEResponseArgument,
ref             long             oNode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to create a child in the response node
of a custom Factory Track BDE.
Public interface FactoryTrackBDE.CreateElement can be used
to create elements in this node.
Example:
Custom BDE "FactoryTrackTransaction" has method "DoTransaction".
The XML tree of the response node is by default
<DoTransactionResponse>
<DataArea>
<FactoryTrackTransaction/>
</DataArea>
</DoTransactionResponse>
To create child node "ReqOutput", the public interface
FactoryTrackBDE.CreateNode can be executed as follows.
long            ReturnValue
long            Node
ReturnValue = FactoryTrackBDE.CreateNode(
"ReqOutput",
bl.ResponseArgument,
Node,
ExceptionMessage,
ExceptionID)
Then the XML tree of the response node (bl.ResponseArgument) is
<DoTransactionResponse>
<DataArea>
<FactoryTrackTransaction>
<ReqOutput/>
</FactoryTrackTransaction>
</DataArea>
<DoTransactionResponse>
Pre:    N.A.
Post:   N.A.
Input:
iNodeID                                       - The name of the node to be created.
iBDEResponseArgument                          - The response argument of the BDE. This
is the XML node bl.ResponseArgument in
the business object layer of the BDE.
Output:
oNode                                         - A reference to the newly created node.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:
0                                             - Success
<> 0                                          - Failure
```

## Public Interfaces for FactoryTrackQuery

The following functions are available: FactoryTrackQuery.CreateElement FactoryTrackQuery.CreateRow FactoryTrackQuery.GetElement
