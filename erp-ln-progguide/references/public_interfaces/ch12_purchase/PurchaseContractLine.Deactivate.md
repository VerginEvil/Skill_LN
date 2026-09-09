# PurchaseContractLine.Deactivate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContractLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 432-433

```baan
DLL:   tdextpurapi
This function is available from 2020.12 (KB2160844).
Syntax: long PurchaseContractLine.Deactivate(
domain  tccono           iPurchaseContract,
domain  tcpono           iContractLine,
domain  tccwoc           iContractPurchaseOffice,
domain  tcpono           iContractSequence,
boolean          iUpdateLogisticDataStatus,
boolean          iUpdatePriceStatus,
boolean          iUpdateTerminatedLines,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to deactivate a purchase contract line.
This function cannot be used if:
* ION Workflow Document Approval is used. Status changes
of the contract must be triggered on contract header
level in that case.
* Change Requests are applicable for the given purchase
contract. Deactivation of a contract line is not
applicable in that case.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract               - Purchase Contract; Mandatory
iContractLine                   - Purchase Contract Line; Mandatory
iContractPurchaseOffice         - Purchase Office
iContractSequence               - Contract Sequence (Must be 0.
The status change will be applied
to its contract detail lines
as well.)
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
Return: 0                       - Contract line is deactivated
<> 0                    - An error occurred
```
