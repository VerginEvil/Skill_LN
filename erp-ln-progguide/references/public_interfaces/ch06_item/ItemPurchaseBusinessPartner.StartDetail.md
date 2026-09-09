# ItemPurchaseBusinessPartner.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemPurchaseBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 204-205

```baan
DLL:   tdextipuapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemPurchaseBusinessPartner.StartDetail(
long             iStartMode,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcefex.date      iEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Items - Purchase Business
Partner (tdipu0110m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
Following input variables form the primary key.
If the primary key cannot be found in the table, an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iItemGroup      Item Group
iItem           Item
iBuyFromBusinessPartner
Buy-from Business Partner
iShipFromBusinessPartner
Ship-from Business Partner
iEffectiveDate
Effective Date
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
