# HoldReasons.StartOverview

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for HoldReason
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 138-139

```baan
DLL:   tcextmcsapi
This function is available from     2022.11 (KB2257724  ).
Syntax: long HoldReasons.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcmcs.hrea       iHoldReason,
ref     domain  tcmcs.hrea       oHoldReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Hold Reasons
in overview mode (tcmcs2110m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The index that will be used.
Supported value:
1: sort by Hold Reason
iQueryExtend            A specific query to be used when zooming
to this session.
iHoldReason             Hold Reason
Output: for iStartMode MODAL:
oHoldReason     Selected Hold Reason
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```

## Public Interfaces for BillingCycle

The following functions are available: BillingCycle.GetInvoicedate
