# ItemSalesBusinessPartner.StartDetail

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemSalesBusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 207-208

```baan
DLL:   tdextisaapi
This function is available from     2023.08 (KB2300144  ).
Syntax: long ItemSalesBusinessPartner.StartDetail(
long             iStartMode,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
domain  tccom.bpid       iSoldToBusinessPartner,
domain  tccom.bpid       iShipToBusinessPartner,
domain  tcefex.date      iEffectiveDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Items - Sales Business Partner
Details (tdisa0510m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItemGroup              Item Group (Mandatory if argument iItem
is not specified).
iItem                   Item (Mandatory if argument iItemGroup
is not specified).
iSoldToBusinessPartner  Sold                      -to Business Partner (Mandatory)
iShipToBusinessPartner  Ship                      -to Business Partner (Optional).
iEffectiveDate          Effective date (Mandatory).
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
