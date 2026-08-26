# SalesOrderInstallments.Close

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderInstallment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 370-370

```baan
DLL:   tdextslsapi
This function is available from     2024.08 (KB3515640  ).
Syntax: long SalesOrderInstallments.Close(
domain  tcorno           iSalesOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function closes sales order installments. Invoicing by
installments must be 'Direct Settlement' or 'Indirect Settlement'.
Correction installment lines will be added if required.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -> No error
<> 0                          -> Error occurred
```
