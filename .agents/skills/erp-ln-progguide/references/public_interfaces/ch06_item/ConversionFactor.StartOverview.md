# ConversionFactor.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ConversionFactor
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 233-234

```baan
DLL:   tcextibdapi
This function is available from 2024.01 (KB2307652).
Syntax: long ConversionFactor.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tccitg           iItemGroup,
domain  tccuni           iBaseUnit,
domain  tccuni           iUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Conversion Factor
(tcibd0103m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used
iSessionIndex
Value:  1:  Item, Item Group, Base Unit
2:  Base Unit, Unit
For Session Index 1, Item and Item Group can be
empty, even if Base Unit is given.
iQueryExtend
Not used
iItem
Item (Optional)
iItemGroup
Item Group (Optional)
iBaseUnit
Base Unit (Mandatory if Item or Item Group or Unit is
provided)
iUnit
Unit (Mandatory if Base unit is provided and
Session Index = 2. Not used when Session Index = 1)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
