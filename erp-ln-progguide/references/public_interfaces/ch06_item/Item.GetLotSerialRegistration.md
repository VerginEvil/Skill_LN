# Item.GetLotSerialRegistration

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 172-172

```baan
DLL:   whextwmdapi
This function is available from     2021.10 (KB2210123  ).
Syntax: long Item.GetLotSerialRegistration(
domain  tcitem           iItem,
domain  whkorg           iKindOfOrigin,
domain  whinh.oorg       iOrderOrigin,
domain  whinh.ittp       iTransactionType,
ref             boolean          oLotRegistration,
ref             boolean          oSerialRegistration,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface determines if Lot and Serial registration
is required for the given Item, Kind of Origin, Order Origin
and Transaction Type.
Pre:    N.A.
Post:   N.A.
Input:  iItem                                 - Item (Mandatory)
iKindOfOrigin                                 - Kind of Origin (Mandatory)
iOrderOrigin                                  - Order Origin (Mandatory)
iTransactionType                              - TransactionType (Mandatory)
Output: oLotRegistration                      - Lot registration required
oSerialRegistration                           - Serial registration required
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success
<> 0                                          - Error
```
