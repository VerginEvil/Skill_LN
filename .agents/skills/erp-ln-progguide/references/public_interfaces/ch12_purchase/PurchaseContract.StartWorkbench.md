# PurchaseContract.StartWorkbench

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 429-429

```baan
DLL:   tdextpurapi
This function is available from 2020.03 (KB2111387).
Syntax: long PurchaseContract.StartWorkbench(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwoc           iPurchaseOffice,
domain  tcemno           iBuyer,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcsite           iSite,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the workbench session Purchase Contracts
(tdpur8330m000).
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
Not Used.
iQueryExtend
Not Used.
Following input variables form the filtering fields, these
fields are not mandatory.
iPurchaseOffice         Purchase Office
iBuyer                  Buyer
iBuyFromBusinessPartner Buy-from Business Partner
iSite                   Site
iItem                   Item
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
