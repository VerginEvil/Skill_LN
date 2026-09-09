# OrderPegging.StartOrderDetails

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for OrderPegging
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 596-597

```baan
DLL:   cpextrrpapi
This function is available from 2025.11 (KB3605560).
Syntax: long OrderPegging.StartOrderDetails(
long             iStartMode,
domain  cpcom.plnc       iScenario,
domain  tccom.long       iTransactionNumber,
domain  tcncmp           iCompanyNumber,
long             iParentSessionIdentifier,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface initiates the Order Details
(cprrp0141m000) session. You can start this session from a
Parent session.
The parent identifier provided by the user is used by the
session to register itself for notifications from the
specified parent.
Pre:    N.A.
Post:   N.A.
Input:  iStartMode
Specifies the start mode for the session. Mandatory.
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS_ALWAYS
Parent and child are parallel
sessions that can be manipulated
simultaneously, even if the session is
a Dialog.
iScenario               Planning Scenario.
iTransactionNumber      Transaction Number.
iCompanyNumber          Company Number.
iParentSessionIdentifier
Parent Session Identifier.
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started successfully.
<> 0                    Otherwise.
```
