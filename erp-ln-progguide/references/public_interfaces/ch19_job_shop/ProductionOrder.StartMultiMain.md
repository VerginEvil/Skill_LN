# ProductionOrder.StartMultiMain

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 774-775

```baan
DLL:   tiextsfcapi
This function is available from 2023.05 (KB2280731).
Syntax: long ProductionOrder.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts Multi Main session Production Order
(tisfc0101m100).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL - ›¼•  ›¼•  The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS - ›¼•  ›¼• Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used
iSessionIndex
Not used
iQueryExtend
Not used
iSite
Optional - Mandatory when the Sites concept is active
iProductionOrder
Production Order - Mandatory
Output: ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    Error Occurred
```
