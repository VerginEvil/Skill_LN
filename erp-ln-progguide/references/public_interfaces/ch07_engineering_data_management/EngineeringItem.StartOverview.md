# EngineeringItem.StartOverview

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 266-268

```baan
DLL:   tiextedmapi
This function is available from     2026.03 (KB3609151  ).
Syntax: long EngineeringItem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iEngineeringItem,
domain  tcseak           iSearchKey1 mb,
domain  tcseak           iSearchKey2 mb,
domain  tccprj           iProject,
ref     domain  tcitem           oEngineeringItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Engineering Item
(tiedm0110m000). This session can be used to define and modify
engineering items.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a Zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iSessionIndex           Specifies the table                      -index that is to be
used. Default index is 1.
Standard supported values:
1: Sort by Engineering Item.
2: Sort by Search Key 1, Engineering Item.
3: Sort by Search Key 2, Engineering Item.
4: Sort by Project, Engineering Item.
iQueryExtend            A specific query to be used when zooming
to this session.
iEngineeringItem        Engineering Item.
iSearchKey1             Search Key 1.
iSearchKey2             Search Key 2.
iProject                Project.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oEngineeringItem        Engineering Item.
oExceptionMessage       The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```

## Chapter 8 Public Interfaces for CRM

## Public Interfaces for Opportunity

The following functions are available: Opportunities.StartOverview Opportunity.StartMultiMain
