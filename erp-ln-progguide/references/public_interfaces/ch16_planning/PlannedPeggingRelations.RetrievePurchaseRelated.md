# PlannedPeggingRelations.RetrievePurchaseRelated

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedPeggingRelations
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 575-576

```baan
DLL:   cpextrrpapi
This function is available from 2025.10 (KB3605562).
Syntax: long PlannedPeggingRelations.RetrievePurchaseRelated(
const           string           iScenario(),
domain  tcitem           iItem,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
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
information related to item purchasing.
If the Item is provided, the selection of Planned Pegging
Relations will be based on the Item and the
Buy From Business Partner.
If the Item is not provided (left empty), then the selection of
the planned pegging relations is based on the
Buy From Business Partner and the Ship From Business Partner.
The extender function must declare all array output variables
as based.
Pre:    N.A.
Post:   N.A.
Input:  iScenario               Scenario. Mandatory.
iItem                   Item.
iBuyFromBusinessPartner
Buy From Business Partner. Mandatory.
iShipFromBusinessPartner
Ship From Business Partner. Mandatory if
item is empty.
iTransactionDateFrom    Planned inventory transaction Date From.
Mandatory.
iTransactionDateTo      Planned inventory transaction Date To.
Mandatory.
Output: oParentTransactionArray
Parent transaction numbers, as used in
table Pegging Transactions (cprrp041).
oParentCompanyArray     Parent companies (relevant in multi-
company scenarios).
oParentScenarioArray    Parent scenarios (relevant in multi-
company scenarios).
oChildTransactionArray  Child transaction numbers, as used in
table Pegging Transactions (cprrp041).
oChildCompanyArray      Child companies (relevant in multi-
company scenarios).
oChildScenarioArray     Child scenarios (relevant in multi-
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
Return: 0                       Purchase related pegging relationships
retrieved successfully.
<> 0                    Otherwise.
```
