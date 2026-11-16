# BuyFromBusinessPartner.StartOverview

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BuyFromBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 134-135

```baan
DLL:   tcextcomapi
This function is available from 2023.02 (KB2277106).
Syntax: long BuyFromBusinessPartner.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcseak           iSearchKey mb,
domain  tccom.cadr       iAddress,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Buy-from Business Partners -
(tccom4520m000).
Input:  iStartMode
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
Possible values are:
"" (Session has no start filter)
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
Optional
A specific query to be used when zooming to this session.
iBuyFromBusinessPartner - Business Partner      Not Mandatory
iSearchKey              - Search Key            Not Mandatory
iAddress                - Address               Not Mandatory
Output: for iStartMode MODAL:
oBuyFromBusinessPartner -
Selected Buy-from Business Partner
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
