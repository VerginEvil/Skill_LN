# EstimatedToolRequirement.StartDetail

> Chapter: Chapter 23 Public Interfaces for Manufacturing Tools
>
> Group: Public Interfaces for EstimatedToolRequirement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 870-871

```baan
DLL:   tiexttrpapi
This function is available from     2024.01 (KB2304919  ).
Syntax: long EstimatedToolRequirement.StartDetail(
long             iStartMode,
domain  titrp.otyp       iOrderType,
domain  tcorno           iOrderNumber,
domain  tcponl           iLine,
domain  tcopno           iActivity,
domain  tcsern           iOperationStep,
domain  tcsern           iSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Estimated Tool Requirement (titrp0111m000)
in Detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iOrderType                                    - Order Type      (Mandatory)
iOrderNumber                                  - Order Number    (Mandatory)
iLine                                         - Line            (Mandatory)
iActivity                                     - Activity        (Mandatory)
iOperationStep                                - Operation Step  (Mandatory)
iSequenceNumber                               - Sequence Number (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```
