# ProjectCostPegTransfer.CheckAllowedBetweenPegs

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransfer
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1088-1089

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2304789  ).
Syntax: long ProjectCostPegTransfer.CheckAllowedBetweenPegs(
domain  tccprj           iProjectFrom,
domain  tcpdm.cspa       iElementFrom,
domain  tcpdm.cact       iActivityFrom,
domain  tccprj           iProjectTo,
domain  tcpdm.cspa       iElementTo,
domain  tcpdm.cact       iActivityTo,
domain  tcorno           iCostPegTransfer,
domain  tcpono           iCostPegTransferLine,
domain  whinh.cpto       iOrigin,
domain  whinh.cptt       iTransferType,
ref             boolean          oTransferAllowed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface checks if cost peg transfers are allowed
between the given pegs.
At least one of the arguments iProjectFrom or iProjectTo has to
be filled when calling this Public Interface.
Pre:    N.a.
Post:   N.a.
Input:  iProjectFrom               - Project from
iElementFrom                       - Element from
iActivityFrom                       - Activity from
iProjectTo                       - Project to
iElementTo                       - Element to
iActivityTo                       - Activity to
iCostPegTransfer                       - Cost Peg Transfer
iCostPegTransferLine                       - Cost Peg Transfer Line
iOrigin                       - Origin
iTransferType                       - Transfer Type
Output: oTransferAllowed               - Transfer Allowed Indicator
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Cost Peg transfer is allowed between the pegs
<> 0                          - Error
```
