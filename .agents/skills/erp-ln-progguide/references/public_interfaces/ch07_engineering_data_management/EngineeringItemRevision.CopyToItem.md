# EngineeringItemRevision.CopyToItem

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 253-253

```baan
DLL:   tiextedmapi
This function is available from 2023.12 (KB2300366).
Syntax: long EngineeringItemRevision.CopyToItem(
domain  tcitem           iEngineeringItem,
domain  tiedm.revi       iRevision,
domain  tcitem           iTargetItem,
domain  tccitg           iTargetItemGroup,
boolean          iOverwriteItem,
boolean          iOverwriteDescription,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to copy E-Item to Item (tcibd001 Items
- General Data).
The Item data is created if the Item is not already present.
If the Item is present, then it is overwritten by the E-Item
Revision data.
Note: Below checks are executed before copying engineering
item to items:
- Engineering Data Management should be active and Engineering
Revision must be implemented in Implemented Software
Components and Engineering Data Management Parameters
must be present.
- Engineering Item Revision status must be Approved by
Production.
- Engineering Item to copied can only have relations with items
for the same project.
- If Target Item is present in Items then the target Item must
be a Product or an Engineering Module.
- If Target Item is not present in Items then valid Item
Defaults must be present for Target Item to be created.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iEngineeringItem        - Engineering Item (Mandatory).
iRevision               - Revision (Mandatory).
iTargetItem             - Target Item (Mandatory).
iTargetItemGroup        - Target Item Group (Mandatory).
iOverwriteItem          - Control for overwriting existing item
data.
iOverwriteDescription   - Control for overwriting descriptions
and/or search keys.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Copy E-Item to Item is successful.
<> 0                    - Copy E-Item to Item is not successful.
```
