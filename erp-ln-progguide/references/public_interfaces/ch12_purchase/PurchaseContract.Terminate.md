# PurchaseContract.Terminate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 430-430

```baan
DLL:   tdextpurapi
This function is available from 2020.12 (KB2160844).
Syntax: long PurchaseContract.Terminate(
domain  tccono           iPurchaseContract,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to terminate a purchase contract.
If ION Workflow Document Approval is used, then the following
applies:
* if the contract is waiting for Approval in ION, then
updating the status is not allowed.
* Termination does not require Workflow Document Approval
If Change Requests are applicable for the given purchase
contract, then the following applies:
* A change request will be created for the status change.
* Depending on the input argument
'iApproveAndProcessChangeRequestAutomatically',
Approving and Processing of the Change Request will be
done automatically or not.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract       - Purchase Contract or Contract Change
Request; Mandatory.
iApproveAndProcessChangeRequestAutomatically
- Yes:  The created change request
will be approved and
processed automatically.
No:   Approval and processing
of the change request
(if any) are not done
automatically.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The contract is terminated
<> 0                    - An error occurred
```
