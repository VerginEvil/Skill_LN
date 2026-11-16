# ItemLotSerialTransactions.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemLotSerialTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1130-1132

```baan
DLL:   whextltcapi
This function is available from 2024.07 (KB3501687).
Syntax: long ItemLotSerialTransactions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcibd.sern       iSerial,
domain  tctrns.date      iTransactionDate,
domain  tcpono           iSequence,
domain  tcltc.boty       iBusinessObjectType,
domain  tcprbo           iBusinessObject,
domain  tcborf           iBusinessObjectReference,
ref     domain  tcitem           oItem,
ref     domain  tcclot           oLot,
ref     domain  tcibd.sern       oSerial,
ref     domain  tctrns.date      oTransactionDate,
ref     domain  tcpono           oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Item - Lot - Serial
Transactions(whltc3510m000).
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
"byItem":
data is displayed by Item
session will be started on index 1
view field: Item
"byBusinessObject":
data is displayed by Business Object
session will be started on index 2
view field: Business Object Reference,
Business Object, Business Object Type
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iItem
Mandatory when iStartFilter "byItem" is used and
the session is started in overview mode with start mode
MODELESS
iLot
Not mandatory
iSerial
Not mandatory
iTransactionDate
Not mandatory
iSequence
Not mandatory
iBusinessObjectType
Mandatory when iStartFilter is "byBusinessObject" is and
the session is started in overview mode with start mode
MODELESS
iBusinessObject
Not mandatory. Relevant when iStartFilter is
"byBusinessObject" or iSessionIndex is 2
iBusinessObjectReference
Not mandatory. Relevant when iStartFilter is
"byBusinessObject" or iSessionIndex is 2.
If this argument is empty, it will be overwritten by
the first value for the given iBusinessObjectType and
iBusinessObject
Output: for iStartMode MODAL:
oItem                   - Selected Item.
oLot                    - Selected Lot.
oSerial                 - Selected Serial.
oTransactionDate        - Selected Transaction Date.
oSequence               - Selected Sequence
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
