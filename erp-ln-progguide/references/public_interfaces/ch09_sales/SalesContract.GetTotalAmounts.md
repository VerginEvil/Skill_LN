# SalesContract.GetTotalAmounts

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 298-299

```baan
DLL:   tdextslsapi
This function is available from     2022.07 (KB2251744  ).
Syntax: long SalesContract.GetTotalAmounts(
domain  tccono           iSalesContract,
ref     domain  tcccur           oContractCurrency,
ref     domain  tcamnt           oContractOpenAmount,
ref     domain  tcamnt           oContractTotalAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function calculates total contract net amounts in contract
currency.
Pre:    N.A.
Post:   N.A.
Input:  iSalesContract                        - Sales Contract; Mandatory.
Output: oContractCurrency                     - Contract Currency.
oContractOpenAmount                           - Contract Open Amount: Sum of amounts
of all non                                                -terminated contract lines.
oContractTotalAmount                          - Contract Total Amount: Sum of amounts
of all contract lines.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Amount could be determined.
<> 0                                          - Error occurred.
```
