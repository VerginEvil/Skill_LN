# ActiveSupplySources.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ActiveSupplySource
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 238-240

```baan
DLL:   cpextrpdapi
This function is available from     2024.10 (KB3501630  ).
Syntax: long ActiveSupplySources.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpitem           iPlanItem,
domain  tcdate           iEffectiveDate,
domain  tccom.bpid       iBuyfromBusinessPartner,
domain  tccom.bpid       iShipfromBusinessPartner,
domain  tcncmp           iSupplyingCompany,
domain  cpitem           iSupplyingItem,
domain  tccwar           iSupplyingWarehouse,
ref     domain  cpitem           oPlanItem,
ref     domain  tcdate           oEffectiveDate,
ref     domain  tccom.bpid       oBuyfromBusinessPartner,
ref     domain  tccom.bpid       oShipfromBusinessPartner,
ref     domain  tcncmp           oSupplyingCompany,
ref     domain  cpitem           oSupplyingItem,
ref     domain  tccwar           oSupplyingWarehouse,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Active Supply Sources Overview
in overview mode (cprpd7150m000).
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
iSessionIndex           Specifies the table                      -index that is to
be used.
Standard supported values:
1: Sort by Item (default).
2: Sort by Business Partner.
3. Sort by Item, effective date.
4. Sort by Supplying Company, Supplying
Item.
iQueryExtend            A specific query to be used when zooming
to this session.
iPlanItem               Plan Item
iEffectiveDate          Effective Date
iBuyfromBusinessPartner
Buy from Business Partner
iShipfromBusinessPartner
Ship from Business Partner
iSupplyingCompany       Supplying Company
iSupplyingItem          Supplying Item
iSupplyingWarehouse     Supplying Warehouse
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oPlanItem               Plan Item
oEffectiveDate          Effective Date
oBuyfromBusinessPartner
Buy from Business Partner
oShipfromBusinessPartner
Ship from Business Partner
oSupplyingCompany       Supplying Company
oSupplyingItem          Supplying Item
oSupplyingWarehouse     Supplying Warehouse
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for PlanningBillOfCriticalMaterial

The following functions are available: PlanningBillOfCriticalMaterial.Generate
