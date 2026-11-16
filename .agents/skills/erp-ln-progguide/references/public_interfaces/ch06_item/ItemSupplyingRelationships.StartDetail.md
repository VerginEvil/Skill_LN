# ItemSupplyingRelationships.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSupplyingRelationship
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 228-228

```baan
DLL:   cpextrpdapi
This function is available from 2024.07 (KB2329978).
Syntax: long ItemSupplyingRelationships.StartDetail(
long             iStartMode,
domain  tcemm.clus       iReceivingCluster,
domain  tcitem           iReceivingItem,
domain  tcncmp           iSupplyingCompany,
domain  tcemm.clus       iSupplyingCluster,
domain  tcdate           iEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supplying Relationships
(cprpd7131m000) in detail mode. Resources by Site should be
active for operations.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iReceivingCluster       Receiving Cluster - Mandatory
iReceivingItem          Receiving Item - Mandatory
iSupplyingCompany       Supplying Company - Mandatory
iSupplyingCluster       Supplying Cluster - Mandatory
iEffectiveDate          Effective Date - Mandatory
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
