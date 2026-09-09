# ProjectContract.GetTotalAmountContractLines

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContract
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1700-1701

```baan
DLL:   tpextctmapi
This function is available from 2025.10 (KB3559609).
Syntax: long ProjectContract.GetTotalAmountContractLines(
domain  tccono           iContract,
domain  tcccur           iCurrency,
boolean          iUseTransactionPrice,
ref     domain  tcamnt           oTotalContractAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionId )
Usage:        Expl:   This Public Interface determines total contract amount of
all the contract lines with status On hold, Active and Closed.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iContract               - Contract. Mandatory
iCurrency               - Currency. Mandatory
Currency in which oTotalContractAmount is returned
iUseTransactionPrice    - Use Transaction Price
if iUseTransactionPrice is True, then the transaction
price of each contract line is considered when
determining the contract amount.
if iUseTransactionPrice is False, then the contract line
amount of each contract line is considered when
determining the contract amount.
Output: oTotalContractAmount    - Total Contract Amount
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: N.A
```
