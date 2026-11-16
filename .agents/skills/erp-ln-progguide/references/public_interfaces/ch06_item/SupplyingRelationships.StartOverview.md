# SupplyingRelationships.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SupplyingRelationship
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 226-227

```baan
DLL:   cpextrpdapi
This function is available from 2024.07 (KB2329978).
Syntax: long SupplyingRelationships.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plvl       iPlanLevel,
domain  tcemm.clus       iReceivingCluster,
domain  tccitg           iReceivingItemGroup,
domain  tcitem           iReceivingItem,
domain  cpcom.sern       iSequenceNumber,
domain  tcncmp           iSupplyingCompany,
domain  tcemm.clus       iSupplyingCluster,
domain  tcitem           iSupplyingItem,
ref     domain  cpcom.plvl       oPlanLevel,
ref     domain  tcemm.clus       oReceivingCluster,
ref     domain  tccitg           oReceivingItemGroup,
ref     domain  tcitem           oReceivingItem,
ref     domain  cpcom.sern       oSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supplying Relationships
(cprpd7130m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table-index that is to be
used. Optional.
Standard supported values:
1: sort by Plan Level, Receiving Item,
Supplying Item (default)
2: sort by Supplying Item , Plan Level
Receiving Item
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanLevel              Plan Level
iReceivingCluster       Receiving Cluster
iReceivingItemGroup     Receiving Item Group
iReceivingItem          Receiving Item
iSequenceNumber         Sequence Number
iSupplyingCompany       Supplying Company
iSupplyingCluster       Supplying Cluster
iSupplyingItem          Supplying Item
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanLevel              Plan Level
oReceivingCluster       Receiving Cluster
oReceivingItemGroup     Receiving Item Group
oReceivingItem          Receiving Item
oSequenceNumber         Sequence Number
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
