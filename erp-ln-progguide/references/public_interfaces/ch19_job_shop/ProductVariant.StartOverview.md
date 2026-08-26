# ProductVariant.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariant
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 686-687

```baan
DLL:   tiextpcfapi
This function is available from     2024.04 (KB2327962  ).
Syntax: long ProductVariant.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccpva           iProductVariant,
domain  tcitem           iItem,
domain  tcreft           iReferenceType,
domain  tccprj           iReferenceOrder,
domain  tcpono           iReferencePosition,
domain  tcpono           iAlternativeSalesQuotation,
domain  tccom.bpid       iBusinessPartner,
domain  tcmcs.st40m      iConfigurationUID mb,
domain  tcolid           iOptionListID,
domain  tiutcs           iConfigurationDate,
ref     domain  tccpva           oProductVariant,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Product Variants in overview
mode (tipcf5501m000).
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
Not Used.
iSessionIndex
Specifies the table                              -index that is to be used.
Standard supported values:
1: sort by Product Variant (default)
2: sort by Item, Product Variant
3: sort by Reference Type, Reference Order,
Reference  Position , Alternative Sales
Quotation, Product Variant
4: sort by Sold To Business Partner, Product
Variant
iQueryExtend
A specific query to be used when zooming to this
session.
iProductVariant
The Product Variant for which the session will be
started.
iItem
Item.
iReferenceType
Reference Type.
iReferenceOrder
Reference Order.
iReferencePosition
Reference Position.
iAlternativeSalesQuotation
Alternative Sales Quotation.
iBusinessPartner
Business Partner.
iConfigurationUID
Configuration UID.
iOptionListID
Option List ID.
iConfigurationDate
Configuration Date.
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductVariant                               - Product Variant
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started.
<> 0                                          - Otherwise.
```
