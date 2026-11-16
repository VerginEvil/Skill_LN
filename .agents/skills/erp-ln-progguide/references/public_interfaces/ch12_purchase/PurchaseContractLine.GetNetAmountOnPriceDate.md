# PurchaseContractLine.GetNetAmountOnPriceDate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContractLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 433-434

```baan
DLL:   tdextpurapi
This function is available from 2020.07 (KB2129097).
Syntax: long PurchaseContractLine.GetNetAmountOnPriceDate(
domain  tccono           iPurchaseContract,
domain  tcpono           iContractLine,
domain  tccwoc           iContractPurchaseOffice,
domain  tcpono           iContractSequence,
domain  tcdate           iPriceSearchDate,
ref     domain  tcccur           oContractCurrency,
ref     domain  tcamnt           oContractLineNetAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to retrieve the contract line net amount,
based on the price on the given date.
Note that inactive price revisions are considered as well.
Pre:    NA
Post:   NA
Input:  iPurchaseContract       - Purchase Contract (Mandatory)
iContractLine           - Contract Line (Mandatory)
iContractPurchaseOffice - Purchase Office
iContractSequence       - Contract Sequence
iPriceSearchDate        - The date that is used to search the
price revision. (Mandatory)
Note that inactive price revisions
are considered as well.
Output: oContractCurrency
oContractLineNetAmount  - Net Amount, expressed in contract currency
oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function was executed successfull.
<> 0                    - An error occurred during the execution
of the function.
```
