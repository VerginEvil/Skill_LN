# Item.InsertSerialNumber

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 184-184

```baan
DLL:   tcextibdapi
This function is available from     2023.01 (KB2259343  ).
Syntax: long Item.InsertSerialNumber(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Insert a Serial Number for a given Item. The combination of
the Serial Number and the Item must not exist.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iItem
Item (Mandatory)
iSerialNumber
The Serial Number to insert (Mandatory)
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - The Serial Number has been inserted
<> 0                          - Error. The Serial Number could not been created
```
