# ProjectPeggedInventory.StartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectPeggedInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1230-1230

```baan
DLL:   whextwmdapi
This function is available from 2023.04 (KB2286306).
Syntax: long ProjectPeggedInventory.StartDetail(
long             iStartMode,
domain  tccwar           iWarehouse,
domain  tccprj           iProject,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tcptc.cstl       iExtension,
domain  tccpcp           iCostComponent,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Project Pegged Inventory
(whwmd2560m000) in Detail Mode.
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
Following input variables form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iWarehouse
iProject
iItem
iEffectivityUnit
iElement
iActivity
iExtension
iCostComponent
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
