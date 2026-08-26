# EstimatedToolRequirement.StartOverview

> Chapter: Chapter 23 Public Interfaces for Manufacturing Tools
>
> Group: Public Interfaces for EstimatedToolRequirement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 871-873

```baan
DLL:   tiexttrpapi
This function is available from     2024.01 (KB2304919  ).
Syntax: long EstimatedToolRequirement.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  titrp.otyp       iOrderType,
domain  tcorno           iOrderNumber,
domain  tcponl           iLine,
domain  tcopno           iActivity,
domain  tcsern           iOperationStep,
domain  tcsern           iSequenceNumber,
domain  tcitem           iTool,
domain  tcibd.sern       iToolNumber,
ref     domain  titrp.otyp       oOrderType,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcponl           oLine,
ref     domain  tcopno           oActivity,
ref     domain  tcsern           oOperationStep,
ref     domain  tcsern           oSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Estimated Tool Requirement (titrp0111m000)
in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used
iSessionIndex
Value:  1:  Order Type, Order Number
2:  Tool, Tool Number
3:  Order Type, Order Number, Activity
iQueryExtend
A specific query to be used when starting the
session. Using the query extend may lead to a
"data not found, session not started" situation                               - Optional
iOrderType                                    - Order Type    (Optional)
iOrderNumber                                  - Order Number  (Optional)
iLine                                         - Line          (Optional)
iActivity                                     - Activity      (Optional)
iOperationStep                                - Operation Step (Optional)
iSequenceNumber                               - Sequence Number (Optional)
iTool                                         - Tool          (Optional)
iToolNumber                                   - Tool Number   (Optional)
Output:
Variables below contain the values of the selected record.
They are only filled if i.start.mode is MODAL and 1 record has
been selected.
oOrderType                                            - Order Type
oOrderNumber                                          - Order Number
oLine                                                 - Line
oActivity                                             - Activity
oOperationStep                                        - Operation Step
oSequenceNumber                                       - Sequence Number
oTool                                                 - Tool
oToolNumber                                           - Tool Number
oExceptionMessage                             - The last message if any message is
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

## Chapter 24 Public Interfaces for Manufacturing

## Project

## Public Interfaces for ProjectPCS

The following functions are available: ProjectPCS.CalculateCost ProjectPCS.CalculateCostV2 ProjectPCS.CalculateItemSalesPrice ProjectPCS.CalculateSurcharges ProjectPCS.CopyCustomizedProductStructureToCustomizedStructure ProjectPCS.CopyCustomizedProductStructureToStandardStructure ProjectPCS.CopyProject ProjectPCS.CopyStandardProductStructureToCustomizedStructure ProjectPCS.PrintActualStandardCost ProjectPCS.PrintEstimatedCost ProjectPCS.Start360 ProjectPCS.StartCopyCustomizedProductStructureToCustomizedStructure ProjectPCS.StartCopyCustomizedProductStructureToStandardStructure ProjectPCS.StartGenerateStructureForProductVariant
