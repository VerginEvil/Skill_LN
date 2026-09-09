# Warehouse.StartOverview

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Warehouse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 91-92

```baan
DLL:   tcextemmapi
This function is available from 2024.08 (KB3501694).
Syntax: long Warehouse.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcncmp           iOperationalCompany,
domain  tccwar           iWarehouse,
domain  tcemm.grid       iEnterpriseUnit,
domain  tcemm.clus       iPlanningCluster,
domain  tcsite           iSite,
boolean          iInEnterprisePlanningOnly,
ref     domain  tccwar           oWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Warehouses (tcemm1112m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Optional: Specifies the start filter
Possible values are:
"byCompanyCluster":
Filter on specified variables
iOperationalCompany and iPlanningCluster
"byCompanyWarehouse":
Filter on specified variables
iOperationalCompany and iWarehouse
"byCompany":
Filter on specified variable iOperationalCompany
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
Optional: Specific query to be used in session.
iOperationalCompany
Optional: Filter on Operational Company with filled
iStartFilter
iWarehouse
Optional: Filter on Warehouse with filled iStartFilter
iEnterpriseUnit
Optional: Filter on Enterprise Unit
iPlanningCluster
Optional: Filter on Planning Cluster with filled
iStartFilter
iSite
Optional: Filter on Site
iInEnterprisePlanningOnly
Optional: Filter on Include in EP when iInEpOnly is True
Output: oWarehouse              - for iStartMode MODAL: Selected
Warehouse
oExceptionMessage       - The last message if any message is
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
