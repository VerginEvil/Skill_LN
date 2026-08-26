# Load.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Load
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1135-1136

```baan
DLL:   whextinhapi
This function is available from     2022.07 (KB2243668  ).
Syntax: long Load.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.load       iLoad,
domain  tccfrw           iCarrier,
domain  tccrte           iRoute,
domain  tcdate           iPlannedDeliveryDate,
domain  tcncmp           iShipToCompany,
domain  tctyps           iShipToType,
domain  tccshp           iShipToCode,
ref     domain  whinh.load       oLoad,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Loads
(whinh4140m000).
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
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byLoad":
data is displayed by Load
session will be started on index 1
view field: None
"byCarrier":
data is displayed by Carrier
session will be started on index 2
view field: Carrier
"byShipTo":
data is displayed by Ship                                      -To
session will be started on index 3
view field: None
iSessionIndex
Specifies the table index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iLoad
The Load to be started
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1 (or iStartFilter = "byLoad")
iCarrier
Optional
iRoute
Optional
iPlannedDeliveryDate
Optional
iShipToCompany
Optional
iShipToType
Optional
iShipToCode
Optional
Output: for iStartMode MODAL:
oLoad                                         - selected load
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```

## Public Interfaces for DeliveryNote

The following functions are available: DeliveryNote.Print DeliveryNote.StartMultiMain
