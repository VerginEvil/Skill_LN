# ProjectAdvancePayments.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectAdvancePayments
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1754-1755

```baan
DLL:   tpextpinapi
This function is available from 2024.08 (KB3501208).
Syntax: long ProjectAdvancePayments.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tccprj           iProject,
domain  tppdm.yeno       iApprovedForInvoicing,
ref     domain  tppdm.serc       oAdvancePayment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session
Advance Payments(tppin4110m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the session index that is to be used. Please be
aware that iStartFilter will overrule the index passed in
this argument. So when not using start filter the session
index will match the value of this variable.
Allowed values:
1: sort by Contract, Contract Line
2: sort by Approved for Invoicing
3: sort by Project
iQueryExtend
A specific query to be used when zooming to this session.
iContract
Contract. Optional
iContractLine
Contract Line. Optional
iProject
Project code linked to the Advance Payment request. Optional
iApprovedForInvoicing
Approved for Invoicing. (Yes/No) Optional
Output: for iStartMode MODAL :
oAdvancePayment - The selected Advance Payment.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
