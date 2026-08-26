# ProductionOrder.StartReportOrdersCompleted

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 779-780

```baan
DLL:   tiextsfcapi
This function is available from     2023.05 (KB2288027  ).
Syntax: long ProductionOrder.StartReportOrdersCompleted(
long             iStartMode,
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Report Orders Completed
(tisfc0120s000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSite
Optional                               - Mandatory when the Sites concept is active
iProductionOrder
Production Order                               - Mandatory
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
