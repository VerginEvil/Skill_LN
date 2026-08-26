# ServiceContract.GetTotalSalesAmount

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1391-1392

```baan
DLL:   tsextctmapi
This function is available from     2023.11 (KB2303875  ).
Syntax: long ServiceContract.GetTotalSalesAmount(
domain  tcorno           iServiceContract,
ref     domain  tcamnt           oContractTotalSalesAmount,
ref     domain  tcccur           oContractCurrency,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function calculates the net sales amount in contract
currency for the passed contract.
Pre:                  -
Post:                 -
Input:  iServiceContract
Service Contract
Mandatory
Output: oContractTotalSalesAmount
Contract Total Sales Amount
oContractCurrency
Service Contract Currency
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Amount could be determined.
<> 0                          - Error occurred.
```
