# ItemSupplyingRelationships.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSupplyingRelationship
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 227-228

```baan
DLL:   cpextrpdapi
This function is available from     2024.07 (KB2329978  ).
Syntax: long ItemSupplyingRelationships.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemm.clus       iReceivingCluster,
domain  tcitem           iReceivingItem,
domain  tcncmp           iSupplyingCompany,
domain  tcemm.clus       iSupplyingCluster,
domain  tcdate           iEffectiveDate,
domain  tcitem           iSupplyingItem,
ref     domain  tcemm.clus       oReceivingCluster,
ref     domain  tcitem           oReceivingItem,
ref     domain  tcncmp           oSupplyingCompany,
ref     domain  tcemm.clus       oSupplyingCluster,
ref     domain  tcdate           oEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supplying Relationships
(cprpd7131m000) in overview mode. Resources by Site should be
active for operations.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table                      -index that is to be
used. Optional.
Standard supported values:
1: sort by Receiving Item, Receiving
Cluster (default)
iQueryExtend            A specific query to be used when zooming
to this session.
iReceivingCluster       Receiving Cluster
iReceivingItem          Receiving Item
iSupplyingCompany       Supplying Company
iSupplyingCluster       Supplying Cluster
iEffectiveDate          Effective Date
iSupplyingItem          Supplying Item
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oReceivingCluster       Receiving Cluster
oReceivingItem          Receiving Item
oSupplyingCompany       Supplying Company
oSupplyingCluster       Supplying Cluster
oEffectiveDate          Effective Date
oExceptionMessage       The last message if any message is
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

## Public Interfaces for LotAndSerialSet

The following functions are available: LotAndSerialSet.StartOverview
