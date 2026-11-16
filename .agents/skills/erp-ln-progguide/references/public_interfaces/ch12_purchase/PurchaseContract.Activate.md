# PurchaseContract.Activate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 426-427

```baan
DLL:   tdextpurapi
This function is available from 2020.12 (KB2160844).
Syntax: long PurchaseContract.Activate(
domain  tccono           iPurchaseContract,
boolean          iUpdateLineStatus,
boolean          iUpdateLogisticDataStatus,
boolean          iUpdatePriceStatus,
boolean          iUpdateTerminatedLines,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to activate a purchase contract.
If ION Workflow Document Approval is used, then the following
applies:
* if the contract is waiting for Approval in ION, then
updating the status is not allowed.
* After executing this Public Interface, the status
update must be approved in ION Workflow Document Approval.
* Activation/Deactivation cannot be initiated for individual
lines, but should be triggered on contract header
level.
If Change Requests are applicable for the given purchase
contract, then the following applies:
* Activation of the purchase contract can only be done
once. No change request is required for that.
After that, the change request procedure is required
to perform changes
Note: * This function does not trigger the generation of retro-billed
price change advices. A separate Public Interface can be
used to trigger that if necessary:
'Purchase.GenerateRetrobilledPriceChangeAdvicesForContracts'
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract               - Purchase Contract; Mandatory
iUpdateLineStatus               - True: will update the status
of the contract lines
as well.
False: Contract lines will not
be updated.
iUpdateLogisticDataStatus       - True: will update the status
of the logistic data
records as well.
False: Logistic Data is not
updated.
iUpdatePriceStatus              - True: will update the status
of the contract price
records as well.
False: Price records are not
updated.
iUpdateTerminatedLines          - True: will also update the
status of terminated
contract lines.
False: Terminated contract
lines are not updated.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Contract is activated
<> 0                    - An error occurred
```
