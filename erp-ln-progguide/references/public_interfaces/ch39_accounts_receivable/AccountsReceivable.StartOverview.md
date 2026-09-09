# AccountsReceivable.StartOverview

> Chapter: Chapter 39 Public Interfaces for Accounts Receivable
>
> Group: Public Interfaces for AccountsReceivable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1822-1823

```baan
DLL:   tfextacrapi
This function is available from 2024.11 (KB3524683).
Syntax: long AccountsReceivable.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccwoc           iDepartment,
domain  tcseak           iSearchKey mb,
domain  tccom.cadr       iAddress,
domain  tcemno           iCreditAnalyst,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Overview session Accounts Receivable 360 -
(tfacr2560m000).
Pre:    na
Post:   na
Input:  iStartMode              - Start Mode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:""
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iInvoiceToBusinessPartner
- Invoice-To Business Partner
iDepartment             - Department
iSearchKey              - Search Key
iAddress                - Address
iCreditAnalyst          - Credit Analyst
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - succes
<> 0                      otherwise
```
