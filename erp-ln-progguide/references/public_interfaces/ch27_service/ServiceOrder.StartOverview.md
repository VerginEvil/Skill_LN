# ServiceOrder.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1433-1435

```baan
DLL:   tsextsocapi
This function is available from     2024.10 (KB3532922  ).
Syntax: long ServiceOrder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iServiceOrder,
long             iViewFieldSet,
ref     domain  tcorno           oServiceOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Service Orders Overview
(tssoc2100m000).
Before calling ServiceOrder.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the table                              -index that is to be used. (Optional)
Supported values:
1: sort by Service Order
2: sort by Project
3: sort by Sold                               -to Business Partner
4: sort by Installation Group and (Serialized) Item
5: sort by Service Office and Preferred Engineer
6: sort by Order Status
7: sort by Service Office and Latest Finish Time
8: sort by Service Contract
10: sort by Customer Order
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on main
table tssoc200 are supported. (Optional)
iServiceOrder
The Service Order to display at the top of the grid if
present in the chosen view. (Optional)
iViewFieldSet
Processing Option Set to set the view fields
when the index used is not index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       Project                 domain  tccprj          empty
3       SoldToBusinessPartner   domain  tccom.bpid      empty
4       InstallationGroup       domain  tsbsc.clst      empty
4       Item                    domain  tcitem          empty
4       SerialNumber            domain  tcibd.sern      empty
5*      ServiceOffice           domain  tccwoc          empty
5       PreferredEngineer       domain  tcemno          empty
6       OrderStatus             domain  tssoc.osta      tssoc.osta.free
7*      ServiceOffice           domain  tccwoc          empty
7       LatestFinishTime        domain  tsmdm.pldt      0
8       ServiceContract         domain  tcorno          empty
10      CustomerOrder           domain  tccorn          empty
* The ServiceOffice property is used for indices 5 and 7.
Output:
oServiceOrder
The selected Service Order if iStartMode is MODAL and
the session is closed by a single selection.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
