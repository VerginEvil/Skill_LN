# PriceBookLines.StartDetail

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for PriceBookLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 528-529

```baan
DLL:   tdextpcgapi
This function is available from 2023.10 (KB2308375).
Syntax: long PriceBookLines.StartDetail(
long             iStartMode,
domain  tdpcg.prbk       iPriceBook,
domain  tcitem           iItem,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcccur           iCurrency,
domain  tccuni           iQuantityUnit,
domain  tcqsl1           iBreakQuantityValue,
domain  tdpcg.prit       iPriceType,
domain  tcefex.date      iEffectiveDate,
domain  tcmcs.long       iPriceBookLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Price Book Lines Details
(tdpcg0131m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel
sessions that can be manipulated
simultaneously.
iPriceBook              Price Book (Mandatory)
iItem                   Item (Mandatory)
iBuyFromBusinessPartner Buy-From Business Partner (Optional)
iShipFromBusinessPartner
Ship-From Business Partner (Optional)
iCurrency               Currency
The price book currency (Mandatory)
iQuantityUnit           Quantity Unit
The unit in which the item's quantity is
expressed (Mandatory)
iBreakQuantityValue     Break Quantity/Value
The minimum or maximum order quantity or
value, in inventory unit, to which the
price book applies (Optional)
iPriceType              Price Type
The price type for which the price book
line is applicable (Mandatory).
iEffectiveDate          Effective Date
The date and time from which the price
book is valid (Mandatory)
iPriceBookLine          Price Book Line (Optional)
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
