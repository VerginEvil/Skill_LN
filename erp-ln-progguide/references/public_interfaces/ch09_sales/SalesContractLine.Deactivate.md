# SalesContractLine.Deactivate

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesContractLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 303-303

```baan
DLL:   tdextslsapi
This function is available from     2026.08 (KB3679093  ).
Syntax: long SalesContractLine.Deactivate(
domain  tccono           iSalesContract,
domain  tcpono           iSalesContractLine,
domain  tccwoc           iSalesOffice,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function deactivates a sales contract line.
The given sales contract line must exist, but the sales office can
be empty.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesContract                                - Sales Contract (Mandatory)
iSalesContractLine                                    - Sales Contract Line (Mandatory)
iSalesOffice                                          - Sales Office (Optional)
Output: oExceptionMessage                             - The last message, if any message is
found. If more than one message is
given, these can be retrieved using
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the Exception
functions to get all relevant
information.
Return: 0                                             - The sales contract line is deactivated.
<> 0                                                  - An error has occurred.
```
