# ProjectCostTransactions.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectCostTransactions
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1735-1737

```baan
DLL:   tpextppcapi
This function is available from 2024.06 (KB2295638).
Syntax: long ProjectCostTransactions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccprj           iProject,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tppss.cpla       iPlan,
domain  tcptc.cstl       iExtension,
domain  tcemno           iEmployee,
domain  tcccp.cpdt       iPeriodTable,
domain  tcccp.yrno       iYearHours,
domain  tcccp.peri       iPeriodHours,
domain  tppdm.cotp       iCostType,
domain  tpppc.coob       iCostObject,
domain  tpppc.koor       iOrderType,
domain  tcorno           iOrderNumber,
domain  tppono           iOrderLine,
domain  tcitem           iPhantomItem,
domain  tccono           iContract,
domain  tpctm.cnln       iContractLine,
ref     domain  tccprj           oProject,
ref     domain  tcpdm.cspa       oElement,
ref     domain  tcpdm.cact       oActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session
Cost Transactions(tpppc2100m000) in overview mode.
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byProject":
data is displayed by Project
session will be started on index 10
view fields: Project
"byProjectElement":
data is displayed by Project, Element
session will be started on index 1
view fields: Project, Element
"byProjectActivity"
data is displayed by Project, Activity
session will be started on index 5
view fields: Project, Plan, Activity
"byContract":
data is displayed by Contract, contract line
session will be started on index 11
view fields: Contract, Contract Line
"byEmployeeHoursPeriod":
data is displayed by Employee, Hours Control Period
session will be started on index 8
view fields: Employee, Hours Control Period, Project
"byCostObject":
data is displayed by Cost Type, Cost Object
session will be started on index 2
view fields: Cost Type, Cost Object, Project
"byProjectPhantom":
data is displayed by Project, Phantom Item
session will be started on index 9
view fields:Project, Phantom Item, Origin, Document
"byOriginDocumentLine":
data is displayed by Order Type, Order Number, Line
session will be started on index 4
view fields: Origin, Document
"byProjectExtension":
data is displayed by Project, Extension
session will be started on index 7
view fields: Project, Extension
iSessionIndex
Specifies the session index that is to be used. Please be
aware that iStartFilter will overrule the index passed in
this argument. So when not using start filter the session
index will match the value of this variable.
Allowed values:
1: sort by Project, Element
2: sort by Cost Object, Project
4: sort by Origin, Document Line
5: sort by Project, Activity
7: sort by Project, Extension
8: sort by Employee, Hours Period, Project
9: sort by Project, Phantom Item
10:sort by Project, Transaction time
11:sort by Contract Line
iQueryExtend
A specific query to be used when zooming to this session.
iProject        - Mandatory when start filter "byProject" or
"byProjectElement" or "byProjectActivity" or
"byCostObject" or "byProjectExtension" is used.
iElement        - Element code. Optional
iActivity       - Activity code. Optional
iPlan           - Plan linked to project. Optional
iExtension      - Extension. Optional
iEmployee       - Employee code. Optional
iPeriodTable    - Period Table Hours Accounting. Optional
iYearHours      - Year hours Accounting. Optional
iPeriodHours    - Period hours Accounting. Optional
iCostType       - Cost type linked to the project. Mandatory when
start filter "byCostObject" is used.
iCostObject     - Cost object linked to the project. Mandatory when
start filter "byCostObject" is used.
iOrderType      - Order origin type. Mandatory when start filter
"byOriginDocument" is used.
iOrderNumber    - Order number. Mandatory when start filter
"byOriginDocument"
is used and for all origin types except for
not applicable.
iOrderLine      - Order Line number.Mandatory when start filter
"byOriginDocument" is used and for all origin
types except for not applicable.
iPhantomItem    - code of the phantom item. Optional
iContract       - Mandatory when start filter "byContract" is used.
iContractLine   - Mandatory when start filter "byContract" is used.
Output: for iStartMode MODAL :
oProject        - Project of the selected transaction
oElement        - Element of the selected transaction
oActivity       - Activity of the selected transaction
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
