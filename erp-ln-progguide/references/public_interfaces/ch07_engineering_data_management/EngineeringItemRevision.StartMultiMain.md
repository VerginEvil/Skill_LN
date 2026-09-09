# EngineeringItemRevision.StartMultiMain

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 256-257

```baan
DLL:   tiextedmapi
This function is available from 2026.03 (KB3609108).
Syntax: long EngineeringItemRevision.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iEngineeringItem,
domain  tcedm.revi       iEngineeringItemRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the Multi Main Session "Engineering
Item Revision"(tiedm1100m100). Use "Engineering Item
Revision" session to modify and define revisions of E-items.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a Zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Start Filter (Not used)
iSessionIndex           Specifies the table-index that is to be
used.
Standard supported values:
1: Sort by Engineering Item, Engineering
Item Revision.
iQueryExtend            A specific query to be used when zooming
to this session.
iEngineeringItem        Engineering Item (Mandatory).
iEngineeringItemRevision
Revision (Mandatory).
Output: oExceptionMessage       The last message if any message is
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
