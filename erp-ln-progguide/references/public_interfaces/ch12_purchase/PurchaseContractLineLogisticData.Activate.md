# PurchaseContractLineLogisticData.Activate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContractLineLogisticData
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 435-436

```baan
DLL:   tdextpurapi
This function is available from 2020.12 (KB2160844).
Syntax: long PurchaseContractLineLogisticData.Activate(
domain  tccono           iPurchaseContract,
domain  tcpono           iContractLine,
domain  tccwoc           iContractPurchaseOffice,
domain  tcpono           iContractSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to activate a purchase contract logistic
data record.
This function cannot be used if Change Requests are applicable
for the given purchase contract. Activation of a contract
logistic data record is not applicable in that case.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseContract       - Purchase Contract; Mandatory
iContractLine           - Purchase Contract Line; Mandatory
iContractPurchaseOffice - Purchase Office
iContractSequence       - Contract Sequence
Note: If the given sequence refers to
a total-line, then also the related
detail-lines will be updated with the
new status.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Contract Logistic Data is activated
<> 0                    - An error occurred
```
