# PriceBookLines.StartOverview

> Chapter: Chapter 13 Public Interfaces for Pricing
>
> Group: Public Interfaces for PriceBookLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 527-529

```baan
DLL:   tdextpcgapi
This function is available from     2022.08 (KB2255812  ).
Syntax: long PriceBookLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
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
ref     domain  tdpcg.prbk       oPriceBook,
ref     domain  tcitem           oItem,
ref     domain  tccom.bpid       oBuyFromBusinessPartner,
ref     domain  tccom.bpid       oShipFromBusinessPartner,
ref     domain  tcccur           oCurrency,
ref     domain  tccuni           oQuantityUnit,
ref     domain  tcqsl1           oBreakQuantityValue,
ref     domain  tdpcg.prit       oPriceType,
ref     domain  tcefex.date      oEffectiveDate,
ref     domain  tcmcs.long       oPriceBookLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Price Book Lines Overview
(tdpcg0131m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byPriceBook":
Data is displayed by price book.
The session will be started on table                                      -index 1
view fields: Price Book
"byItem":
Data is displayed by item.
The session will be started on table                                      -index 2
view fields: Item
iSessionIndex
Specifies the table                              -index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iPriceBook
Price Book
Mandatory if iStartMode is MODELESS and session                              -index 1
or 3 is used. (Note that session index 1 will
automatically be used if iStartFilter equals "byPriceBook")
iItem
Item
Mandatory if iStartMode is MODELESS and session                              -index 2
is used. (Note that session index 2 will automatically
be used if iStartFilter equals "byItem")
iBuyFromBusinessPartner
Buy                              -From Business Partner
Not mandatory.
iShipFromBusinessPartner
Ship                              -From Business Partner
Not mandatory.
iCurrency
The price book currency
Not mandatory.
iQuantityUnit
The unit in which the item's quantity is expressed.
Not mandatory.
iBreakQuantityValue
The minimum or maximum order quantity or value, in
inventory units, to which the price book applies.
Not mandatory.
iPriceType
The price type for which the price book line is applicable.
Allowed values
* empty
* Not Applicable
* Buying
Used for all non                                      -subcontracting purchasing scenarios
* Item Subcontracting
Used for item subcontracting
* Operation Subcontracting
Used for operation subcontracting
* Service Subcontracting
Used for service subcontracting
Not mandatory.
iEffectiveDate
The date and time from which the price book is valid.
Not mandatory.
iPriceBookLine
Price Book Line
Not mandatory.
Output: for iStartMode MODAL:
oPriceBook      The selected Price Book
oItem           Item of the selected Price Book Line
oBuyFromBusinessPartner
Buy                                              -From Business Partner of the selected
Price Book Line
oShipFromBusinessPartner
Ship                                              -From Business Partner of the selected
Price Book Line
oCurrency       Currency of the selected Price Book Line
oQuantityUnit   Quantity Unit of the selected
Price Book Line
oBreakQuantityValue
Break Quantity/Value of the selected
Price Book Line
oPriceType      Price Type of the selected Price Book Line
oEffectiveDate  Effective Date of the selected
Price Book Line
oPriceBookLine  Price Book Line number of the selected
Price Book Line
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```

## Public Interfaces for SalesPriceMatrices

The following functions are available: SalesPriceMatrices.StartOverview
