# Item.CreateSerialNumber

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for Item
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 168-169

```baan
DLL:   tcextibdapi
This function is available from     2021.05 (KB2168640  ).
Syntax: long Item.CreateSerialNumber(
domain  tcsite           iSite,
domain  tcitem           iItem,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcuef.mask       iMask,
ref     domain  tcibd.sern       oSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Create a Serial Number for a given Item.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite
Site (Mandatory when the Site concept is Active)
iItem
Item (Mandatory)
iOrderOrigin
Order Origin (Optional)
iOrder
Order (Optional).
iOrderSet
Order Set (Optional)
iMask
Mask (Optional)
Output: oSerialNumber
The created Serial Number
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - Serial Number has been created
<> 0                       - Error. A new Serial Number could not been created
```
