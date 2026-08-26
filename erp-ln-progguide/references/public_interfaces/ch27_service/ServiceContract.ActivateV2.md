# ServiceContract.ActivateV2

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1384-1387

```baan
DLL:   tsextctmapi
This function is available from     2023.11 (KB2309534  ).
Syntax: long ServiceContract.ActivateV2(
domain  tcorno           iServiceContract,
domain  tsctm.cchn       iServiceContractChange,
domain  tcyesno          iContinueWhenNoSalesAmountOnLines,
domain  tcyesno          iContinueWhenInvoicingByChanges,
domain  tcyesno
iContinueActivatingChangeWithExpiredContractLines,
domain  tsctm.upt.cntr   iActionOnOrdersCallsWhenExpired,
domain  tsctm.link
iLinkOrApplyCoverageOrIgnoreWhenOpenOrdersOrCalls,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function makes the passed Service Contract, and/or Service
Contract Change, active.
Note:
-                       Public Interface ServiceContract.Activate has transaction
management.
-                       Public Interface ServiceContract.ActivateV2 does not
have transaction management.
First general checks are executed whether activation is
allowed or not.
Next, for contract renewal, or an incidental change, possible
prepared changes in the Installation Group and Physical
Breakdowns of the configuration lines are processed.
Then the Contract Change is made active.
Finally, the table Totals (tsctm100) is filled based on the
aggregation process, and the contract installments are handled.
Based on the provided input arguments this process can
be controlled. It can be indicated to continue the activation
process or to stop. These are situations for which in LN UI
questions are asked whether the process should continue
or stop.
When only iServiceContract is passed, the Service Contract, and
the Service Contract Change of type Original Contract, is
activated.
When iServiceContract, and iServiceContractChange are passed,
and the Service Contract Change is of type Original Contract,
both Service Contract and Service Contract Change are activated.
When the Service Contract Change is not of type Original
Contract, then the Service Contract Change is activated.
Pre:    a db.retry.point() must have been specified.
Post:   an abort.transaction() or commit.transaction() must be
executed.
Input:  iServiceContract
Service Contract: Mandatory
iServiceContractChange
Service Contract Change. When the Service Contract must
be activated, pass zero (0). Otherwise, pass a valid
Service Contract Change number.
(Not mandatory)
iContinueWhenNoSalesAmountOnLines
Continue activation when sales amount has not been
filled on all contract configuration lines that are
used for contract coverage.
(mandatory Yes/No)
iContinueWhenInvoicingByChanges
Continue when there are Calls, Service Orders and/or
Maintenance Sales Orders present for configurations
covered by this contract with Invoicing By Project.
Invoicing By will be changed to Service.
(mandatory Yes/No)
iContinueActivatingChangeWithExpiredContractLines
Continue when there are Calls, Service Orders and/or
Maintenance Sales Orders present for configurations
that are expired by this contract change.
(mandatory Yes/No)
iActionOnOrdersCallsWhenExpired
When there are open Calls, Service Orders and/or
Maintenance Sales Orders and the effective or expiry
date of the contract line will result in an invalid
contract on the order/call, then there are the following
options:
-                               Unlink Contract
Unlinking is done by updating the orders/calls
by setting the coverage time to 0. The contract
will be unlinked and coverage is recalculated
for the cost lines.
-                               Relink Contract
Relinking is done by setting the coverage time
on the orders/calls to the contract line expiry
date, which will redetermine the applicable
service contract.
(mandatory unlink/relink)
iLinkOrApplyCoverageOrIgnoreWhenOpenOrdersOrCalls
When there are Calls, Service Orders and/or
Maintenance Sales Orders present for configurations
covered by this contract, then there are the following
options:
-                               Establish Link
For each contract configuration line which is
present on a Call, Service Order (Activities),
or Maintenance Sales Order Line, the Service
Contract is filled.
-                               Apply Coverage
Contract coverage is applied to orders and
calls present for contract configurations.
First the Service Contract is updated on each
of these Calls and Orders.
Next the contract coverage calculation is
performed.
-                               Ignore
Nothing is updated on open Calls, Service Order
(Activities), or Maintenance Sales Order Lines.
(mandatory Link/Cover/Ignore)
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Activation successful
<> 0                          - Error during Activation occurred
```
