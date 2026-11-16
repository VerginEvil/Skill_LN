# OperationStepsByProductionOrder.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for OperationStepsByProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 824-825

```baan
DLL:   tiextsfcapi
This function is available from 2025.05 (KB3559434).
Syntax: long OperationStepsByProductionOrder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcsern           iOperationStep,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcopno           oOperation,
ref     domain  tcsern           oOperationStep,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Operation Steps by Production
Order (tisfc0121m000) in overview mode. Use this session to
display and modify the operation steps that are linked to an
operation of a specific production order.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used.
iSessionIndex           Specifies the table-index that is to be
used.
Standard supported values:
1: sort by Production Order, Operation,
Operation Step (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iSite                   Site (mandatory when the Sites concept
is active).
iProductionOrder        Production Order (Mandatory).
iOperation              Operation (Mandatory).
iOperationStep          Operation Step.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductionOrder        Production Order.
oOperation              Operation.
oOperationStep          Operation Step.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
