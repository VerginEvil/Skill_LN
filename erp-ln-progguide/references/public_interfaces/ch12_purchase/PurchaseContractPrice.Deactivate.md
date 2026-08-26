# PurchaseContractPrice.Deactivate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContractPrice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 436-437

```baan
DLL:   tdextpurapi
This function is available from     2020.12 (KB2160844  ).
Syntax: long PurchaseContractPrice.Deactivate(
domain  tccono           iPurchaseContract,
domain  tcpono           iContractLine,
domain  tccwoc           iContractPurchaseOffice,
domain  tcpono           iContractSequence,
domain  tcdate           iEffectiveDate,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to deactivate a purchase contract price line.
If ION Workflow Document Approval is used, then the following
applies:
* if the contract is waiting for Approval in ION, then
updating the status is not allowed.
* Activation/Deactivation of a price does not require
Workflow Document Approval
If Change Requests are applicable for the given purchase
contract, then the following applies:
* A change request will be created for the status change.
* Depending on the input argument
'iApproveAndProcessChangeRequestAutomatically',
Approving and Processing of the Change Request will be
done automatically or not.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract                     - Purchase Contract or Contract Change
Request; Mandatory.
iContractLine                                 - Purchase Contract Line; Mandatory
iContractPurchaseOffice                       - Purchase Office
iContractSequence                             - Contract Sequence
Note: If the given sequence refers to
a total                                                -line, then also the related
detail                                                -lines will be updated with the
new status.
iEffectiveDate                                - Effective Date; Mandatory
iApproveAndProcessChangeRequestAutomatically
-                                               Yes:  The created change request
will be approved and
processed automatically.
No:   Approval and processing
of the change request
(if any) are not done
automatically.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Contract price line is deactivated
<> 0                                          - An error occurred
```

## Public Interfaces for PurchaseSchedule

The following functions are available: PurchaseSchedule.GenerateReleaseForPushAndPullForecast PurchaseSchedule.Regenerate PurchaseSchedule.StartMultiMain PurchaseSchedule.Terminate
