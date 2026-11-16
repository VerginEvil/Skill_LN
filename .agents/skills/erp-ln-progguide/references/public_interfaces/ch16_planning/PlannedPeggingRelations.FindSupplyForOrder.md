# PlannedPeggingRelations.FindSupplyForOrder

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedPeggingRelations
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 571-573

```baan
DLL:   cpextrrpapi
This function is available from 2020.10 (KB2151080).
Syntax: long PlannedPeggingRelations.FindSupplyForOrder(
domain  cpcom.plnc       iPlanningScenario,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iSequence,
domain  tcpono           iMaterialPosition,
ref     domain  tccom.long       oParentTransactionArray(),
ref     domain  tcncmp           oParentCompanyArray(),
ref     domain  cpcom.plnc       oParentScenarioArray() fixed,
ref     domain  tccom.long       oChildTransactionArray(),
ref     domain  tcncmp           oChildCompanyArray(),
ref     domain  cpcom.plnc       oChildScenarioArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface returns the chain of planned supply
for a specified demand order, line / position, sequence.
The returned chain of planned supply is the same as
the information that is shown in the Upstream view of the
Order Pegging session (cprrp0740m200).
Limitations:
Pegging Relations are volatile, they can change substantially
with each new planning run, even if there are no changes for
the plan item.
Only Items having Order System = Planned can have (planned)
orders with planned supply.
Distribution Lines are not supported as input
Pre:    functional: Generate order planning (cprrp1210m000) must have
been executed for the plan item of the specified order
and its child items, with the option 'Update Pegging
Relations'.
technical: Output arrays must be defined as based arrays.
Post:   technical: Execute free.mem() for the output arrays (after
usage of the data).
Input:  iPlanningScenario       Mandatory. The planning scenario that
is used for creating the pegging relations
(generate order planning).
iOrderType              Mandatory. Type of the demand order
(E.g. tckoor.act.sls or tckoor.act.sfc)
iOrderNumber            Mandatory. The order number holding a
demand.
iOrderLine              Order Line or Position.
iSequence               Sequence number.
iMaterialPosition       The material position number (for
Job Shop orders).
iOrderLine or iMaterialPosition cannot
be filled both.
Output: oParentTransactionArray Parent transaction numbers, as used in
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
Example:
A sales order for item A is supplied by 2 production
orders. Both production orders are supplied for a
component by one purchase order.
Pegging Browser:
sls order for item A (10)
prod order for item  A (11)
pur order for component B (12)
prod order for item A (13)
pur order for component B (12)
(N) = transaction number
Resulting Parent and Child Transaction arrays
when executing the public interface for the sls order:
oParentTransactionArray oChildTransactionArray
0                       10
10                      11
11                      12
10                      13
13                      12
The transaction id's in the arrays refer to
table cprrp041 (Pegging Transactions), where
the details (order type, number, position, sequence,
demand or supply) of each transaction are stored.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Public Interface succesfully completed
<> 0                    Otherwise.
```
