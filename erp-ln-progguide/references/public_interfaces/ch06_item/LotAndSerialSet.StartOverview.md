# LotAndSerialSet.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for LotAndSerialSet
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 228-230

```baan
DLL:   tcextibdapi
This function is available from     2023.05 (KB2274414  ).
Syntax: long LotAndSerialSet.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcguid           iLotAndSerialSet,
domain  tcitem           iItem,
boolean          iDisplayOnly,
ref     domain  tcguid           oLotAndSerialSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Lot and Serial Set (tcibd4111m000) in
overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Not used.
iQueryExtend
Not used.
iLotAndSerialSet
Optional when iDisplayOnly is false.
iItem
Mandatory, must exist.
iDisplayOnly
Mandatory.
Output: oLotAndSerialSet                      - The newly created set in the case that
iDisplayOnly = false and
iLotAndSerialSet was empty. Only has a
value if iStartMode = MODAL.
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

## Public Interfaces for AlternativeItem

The following functions are available: AlternativeItem.StartDetail AlternativeItem.StartOverview
