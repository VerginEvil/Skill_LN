# PlannedPeggingRelations.RetrieveSalesRelated

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedPeggingRelations
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 573-574

```baan
DLL:   cpextrrpapi
This function is available from     2025.10 (KB3605562  ).
Syntax: long PlannedPeggingRelations.RetrieveSalesRelated(
const           string           iScenario(),
domain  tcitem           iItem,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tctrns.date      iTransactionDateFrom,
domain  tctrns.date      iTransactionDateTo,
ref     domain  tccom.long       oParentTransactionArray(),
ref     domain  tcncmp           oParentCompanyArray(),
ref     domain  cpcom.plnc       oParentScenarioArray() fixed,
ref     domain  tccom.long       oChildTransactionArray(),
ref     domain  tcncmp           oChildCompanyArray(),
ref     domain  cpcom.plnc       oChildScenarioArray() fixed,
ref             long             oArraySize,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface retrieves planned pegging relation
information related to item sales.
If the Item is provided, the selection of Planned Pegging
Relations will be based on the Item and the
Sold To Business Partner.
If the Item is not provided (left empty), then the selection of
the planned pegging relations is based on the
Sold To Business Partner and the Ship To Business Partner.
The extender function must declare all array output variables
as based.
Pre     : N.A.
Post    : N.A.
Input:  iScenario               Scenario. Mandatory.
iItem                   Item.
iSoldToBusinessPartner
Sold To Business Partner. Mandatory.
iShipToBusinessPartner
Ship To Business Partner. Mandatory if
item is empty.
iTransactionDateFrom    Planned inventory transactions Date
From. Mandatory.
iTransactionDateTo      Planned inventory transactions Date To.
Mandatory.
Output: oParentTransactionArray
Parent transaction numbers, as used in
table Pegging Transactions (cprrp041).
oParentCompanyArray     Parent companies (relevant in multi                      -
company scenarios).
oParentScenarioArray    Parent scenarios (relevant in multi                      -
company scenarios).
oChildTransactionArray  Child transaction numbers, as used in
table Pegging Transactions (cprrp041).
oChildCompanyArray      Child companies (relevant in multi                      -
company scenarios).
oChildScenarioArray     Child scenarios (relevant in multi                      -
company scenarios).
oArraySize              Size of allocated Output arrays.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Sales related pegging relationships
retrieved successfully.
<> 0                    Otherwise.
```

## Public Interfaces for ProductAvailability

The following functions are available: ProductAvailability.GetDeliveryDate ProductAvailability.GetWhenAvailableSchedule
