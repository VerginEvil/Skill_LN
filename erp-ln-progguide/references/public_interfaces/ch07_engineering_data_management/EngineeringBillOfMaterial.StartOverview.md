# EngineeringBillOfMaterial.StartOverview

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringBillOfMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 261-262

```baan
DLL:   tiextedmapi
This function is available from     2025.10 (KB3554678  ).
Syntax: long EngineeringBillOfMaterial.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iEngineeringItem,
domain  tcedm.revi       iRevision,
domain  tcpono           iPositionNumber,
domain  tiedm.cmtp       iComponentType,
domain  tcitem           iComponent,
ref     domain  tcitem           oEngineeringItem,
ref     domain  tcedm.revi       oRevision,
ref     domain  tcpono           oPositionNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session ›¼ÀœEngineering Bill of Material›¼Àœ
(tiedm1110m000). An engineering bill of material is a bill of
material of the engineering item revision.
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
used.
Standard supported values:
1: Sort by Engineering Item, Revision,
Position Number (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iEngineeringItem        Engineering Item (Mandatory).
iRevision               Revision (Mandatory).
iPositionNumber         Posistion Number.
iComponentType          Component Type.
iComponent              Component.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oEngineeringItem        Engineering Item.
oRevision               Revision.
oPositionNumber         Position Number.
oExceptionMessage       The last message if any message is
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
