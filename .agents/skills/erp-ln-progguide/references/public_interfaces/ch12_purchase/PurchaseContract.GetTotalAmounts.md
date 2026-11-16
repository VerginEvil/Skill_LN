# PurchaseContract.GetTotalAmounts

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 428-428

```baan
DLL:   tdextpurapi
This function is available from 2019.04 (KB2042557).
Syntax: long PurchaseContract.GetTotalAmounts(
domain  tccono           iPurchaseContract,
ref     domain  tcccur           oContractCurrency,
ref     domain  tcamnt           oContractOpenAmount,
ref     domain  tcamnt           oContractTotalAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function calculates total contract net amounts in contract
currency.
Contract is selected in the current company.
Pre:    N.A.
Post:   N.A.
Input:  iPurchaseContract       - Purchase Contract; Mandatory.
Output: oContractCurrency       - Contract Currency.
oContractOpenAmount     - Contract Open Amount: Sum of amounts
of all non terminated contract lines.
oContractTotalAmount - Contract Total Amount: Sum of amounts
of all contract lines.
oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Amount could be determined.
<> 0                    - Error occurred.
```
