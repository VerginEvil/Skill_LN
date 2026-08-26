# ProjectInstallments.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectInstallments
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1737-1738

```baan
DLL:   tpextpinapi
This function is available from     2024.08 (KB3501648  ).
Syntax: long ProjectInstallments.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
domain  tccprj           iProject,
domain  tppdm.yeno       iApprovedForInvoicing,
ref     domain  tppdm.nins       oInstallment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Installments (tppin4151m000) in overview
mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter                       -
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
iQueryExtend                       -
A specific query to be used when zooming to this session.
iContract                       - Contract. Optional
iContractLine                       -
Contract Line. Optional
iProject                       -
Project code linked to the Contract Line and Installment. Optional
iApprovedForInvoicing                       -
Approved for Invoicing. (Yes/No) Optional
Output: For i.start.mode MODAL and i.single.multi.occurence = MULTI_OCC:
oInstallment                                  - Installment number of selected
record.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```

## Public Interfaces for

## ProjectAdvanceInstallmentSettlementMapping

The following functions are available: ProjectAdvanceInstallmentSettlementMapping.StartOverview
