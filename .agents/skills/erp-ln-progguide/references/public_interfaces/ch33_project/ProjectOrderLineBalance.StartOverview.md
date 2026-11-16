# ProjectOrderLineBalance.StartOverview

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectOrderLineBalance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1762-1764

```baan
DLL:   tpextpssapi
This function is available from 2026.03 (KB3631151).
Syntax: long ProjectOrderLineBalance.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tppdm.cotp       iCostType,
domain  tccprj           iProject,
domain  tppdm.csub       iCostObject,
domain  tcitem           iItem,
domain  tppdm.reft       iReferenceType,
domain  tcdate           iTransactionDate,
domain  tppdm.cspa       iElement,
domain  tppdm.cact       iActivity,
domain  tpptc.cstl       iExtension,
domain  tccpcp           iCostComponent,
domain  tcorno           iOrderNumber,
domain  tcpono           iPositionNumber,
domain  tcpono           iSequenceNumber,
domain  tcemno           iBuyer,
domain  tcitem           iPhantomItem,
ref     domain  tccprj           oProject,
ref     domain  tppdm.csub       oCostObject,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the Order Line Balance session in overview mode.
Opens different sessions depending on cost type:
- tppdm.cotp.materials      - tppss6500m000
- tppdm.cotp.equipment      - tppss6501m000
- tppdm.cotp.subcontracting - tppss6502m000
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL   -       The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the session index that is to be used. Please be
aware that iStartFilter will overrule the index passed in
this argument. So when not using start filter the session
index will match the value of this variable.
Allowed values:
1)iCostType = tppdm.cotp.materials - Session: tppss6500m000
1: Sort by Project, Item, TransactionDate
View fields ›¼À“ Project
2: Sort by Project, Item, Extension
View fields ›¼À“ Project
3: Sort by Project, Order, Item
View fields ›¼À“ Project
4: Sort by Project, Element, Item
View fields ›¼À“ Project , Element
5: Sort by Project, Activity, Item
View fields ›¼À“ Project, Activity
6: Sort by Buyer, Project, Order
View fields ›¼À“ Buyer
7: Sort by Phantom Item, Item, Project, Transaction Date
View fields - PhantomItem, Item in Project
2)iCostType = tppdm.cotp.equipment - Session: tppss6501m000
1: Sort by Project, Equipment, Reference Type, Transaction Date
View fields ›¼À“ Project
2: Sort by Project, Equipment, Reference Type, Extension
View fields ›¼À“ Project
3: Sort by Project, Order, Equipment, Reference Type
View fields ›¼À“ Project
4: Sort by Project, Element, Equipment, Reference Type
View fields ›¼À“ Project, Element
5: Sort by Project, Activity, Equipment, Reference Type
View fields ›¼À“ Project , Activity
6: Sort by Buyer, Project, Order
View fields ›¼À“ Buyer
3)iCostType = tppdm.cotp.subcontracting - Session: tppss6502m000
1: Sort by Project, Subcontracting, Reference Type,
Transaction Date
View fields - Project
2: Sort by Project, Subcontracting, Reference Type, Extension.
View fields - Project
3: Sort by Project, Order, Subcontracting, Reference Type.
View fields - Project
4: Sort by Project, Element, Subcontracting, Reference Type.
View fields - Project, Element
5: Sort by Project, Activity, Subcontracting, Reference Type.
View fields - Project, Activity
6: Sort by Buyer, Project, Order
View fields - Buyer
iQueryExtend
A specific query to be used when zooming to this session.
iCostType
Mandatory
Determines which session need to be opened: Subcontracting,
Materials, or Equipment.
iProject
Optional
iCostObject
Optional
Depends on iCostType. If iCostType is Subcontracting, a
Subcontracting object is given,if Equipment, an Equipment object.
iItem
Optional
Only applicable when Cost Type is Materials
iReferenceType
Optional
iTransactionDate
Optional
iElement
Optional
iActivity
Optional
iExtension
Optional
iCostComponent
Optional
iOrderNumber
Optional
iPositionNumber
Optional
iSequenceNumber
Optional
iBuyer
Optional
iPhantomItem
Optional
Only applicable when Cost Type = Materials and index is 7.
Output: for iStartMode MODAL :
oProject                - project of the selected record.
oCostObject             - selected subcontracting / equipment.
oItem                   - selected item for material type.
oExceptionMessage       - The last message if any message is found.
If more than one message is given,
these are present in the oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use Exception functions
to get all relevant details.
Return: 0                       - Session started
<> 0                    - An error occurred
```
