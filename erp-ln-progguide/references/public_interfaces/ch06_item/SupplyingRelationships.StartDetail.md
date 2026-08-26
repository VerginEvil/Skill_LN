# SupplyingRelationships.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for SupplyingRelationship
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 224-225

```baan
DLL:   cpextrpdapi
This function is available from     2024.07 (KB2329978  ).
Syntax: long SupplyingRelationships.StartDetail(
long             iStartMode,
domain  cpcom.plvl       iPlanLevel,
domain  tcemm.clus       iReceivingCluster,
domain  tccitg           iReceivingItemGroup,
domain  tcitem           iReceivingItem,
domain  cpcom.sern       iSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supplying Relationships
(cprpd7130m000) in detail mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iPlanLevel              Plan Level                       - Mandatory
iReceivingCluster       Receiving Cluster                       - Mandatory
iReceivingItemGroup     Receiving Item Group                       - Mandatory
iReceivingItem          Receiving Item                       - Mandatory
iSequenceNumber         Sequence Number                       - Mandatory
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
